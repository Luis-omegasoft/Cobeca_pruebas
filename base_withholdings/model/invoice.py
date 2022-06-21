# -*- coding: utf-8 -*-
##############################################################################
#
#    MoviTrack
#    Copyright (C) 2020-TODAY MoviTrack.
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import time
from odoo import api,fields,models
from odoo.exceptions import UserError
from odoo.fields import _

class AccountInvoice(models.Model):
    _inherit = 'account.move'

    def ret_and_reconcile(self, pay_amount, pay_account_id,
                          pay_journal_id, writeoff_acc_id,
                          writeoff_journal_id, date,
                          name, to_wh,type_retencion):
        """ Make the payment of the invoice
        """

        rp_obj = self.env['res.partner']
        hola = self.ids
        carro = hola
        if self.ids :
            assert len(self.ids) == 1, "Solo puede pagar una factura a la vez"
        else:
            assert len(to_wh) == 1, "Solo puede pagar una factura a la vez"
        invoice = self.browse(self.ids)
        src_account_id = pay_account_id.id

        # Take the seq as name for move
        types = {'out_invoice': -1,
                 'in_invoice': 1,
                 'out_refund': 1, 'in_refund': -1}
        direction = types[invoice.move_type]
        l1 = {
            'debit': direction * pay_amount > 0 and direction * pay_amount,
            'credit': direction * pay_amount < 0 and - direction * pay_amount,
            'account_id': src_account_id,
            'partner_id': rp_obj._find_accounting_partner(
                invoice.partner_id).id,
            'ref': invoice.name,
             'date': date,
            'currency_id': False,
            'name': name
             }
        lines = [(0, 0, l1)]

        if type_retencion == 'wh_iva':
            l2 = self._get_move_lines1(to_wh, pay_journal_id, writeoff_acc_id,
                                      writeoff_journal_id, date, name)
        if type_retencion == 'wh_islr':
            l2 = self._get_move_lines2(to_wh, pay_journal_id, writeoff_acc_id,
                                      writeoff_journal_id, date, name)
        if type_retencion == 'wh_muni':
            l2 = self._get_move_lines3(to_wh, pay_journal_id, writeoff_acc_id,
                                      writeoff_journal_id, date, name)

        if not l2:
            raise UserError("Advertencia! \nNo se crearon movimientos contables.\n Por favor, verifique si hay impuestos / conceptos para retener en las facturas!")

        deb = l2[0][2]['debit']
        cred = l2[0][2]['credit']
        if deb < 0: l2[0][2].update({'debit': deb * direction})
        if cred < 0: l2[0][2].update({'credit': cred * direction})
        lines += l2

        move = {'ref': name + 'de '+ str(invoice.name),
                'line_ids': lines,
                'journal_id': pay_journal_id,
                'date': date,
                'state': 'draft',
                'type_name': 'entry'
                }
       # self.env['account.move'].create(move_vals_list)
        move_obj = self.env['account.move']
        move_id = move_obj.create(move)

        return move_id

        line_ids = []
        total = 0.0
        line = self.env['account.move.line']
        self._cr.execute(
            'select id'
            ' from account_move_line'
            ' where move_id in (' + str(move_id.id) + ',' +
            str(invoice.move_id.id) + ')')
        lines = line.browse( [item[0] for item in self._cr.fetchall()])
        for aml_brw in lines:
            if aml_brw.account_id.id == src_account_id:
                line_ids.append(aml_brw.id)
                total += (aml_brw.debit or 0.0) - (aml_brw.credit or 0.0)
        for aml_brw in invoice.payment_ids:
            if aml_brw.account_id.id == src_account_id:
                line_ids.append(aml_brw.id)
                total += (aml_brw.debit or 0.0) - (aml_brw.credit or 0.0)
        if (not round(total, self.env['decimal.precision'].precision_get(
                 'Withhold'))) or writeoff_acc_id:
            self.env['account.move.line'].reconcile(
                 line_ids, 'manual', writeoff_acc_id,
                writeoff_period_id, writeoff_journal_id)

        self.env['account.move'].write({})
        self.move_id = move_id


    def _get_move_lines(self, to_wh,
                        pay_journal_id, writeoff_acc_id,
                        writeoff_journal_id, date, name
                        ):
        """ Function openerp is rewritten for adaptation in
        the ovl
        """
        return []

    def ret_payment_get(self,*args):
        """ Return payments associated with this bill
        """
        # /!\ This method need revision and I (hbto) have come to believe it is
        # useless at worst, at best it needs to be refactored, to get payments
        # from invoice one just need to look at the payment_ids field
        lines = []
        return lines

class AccountInvoiceTax(models.Model):
    _inherit = 'account.tax'

    tax_id = fields.Many2one(
            'account.tax', 'Tax', required=False, ondelete='set null',
            help="Tax relation to original tax, to be able to take off all"
                 " data from invoices.")

    @api.model
    def compute(self, invoice):
        """ Calculate the amount, base, tax amount,
        base amount of the invoice
        """
        tax_grouped = {}
        if isinstance(invoice, (int)):
            inv = self.env['account.move'].browse(invoice)
        else:
            inv = invoice
        currency = inv.currency_id.with_context(
            date=inv.date_invoice or time.strftime('%Y-%m-%d'))
        company_currency = inv.company_id.currency_id
        for line in inv.invoice_line:
            for tax in line.invoice_line_tax_id.compute_all(
                    (line.price_unit * (1 - (line.discount or 0.0) / 100.0)),
                    line.quantity, line.product_id, inv.partner_id)['taxes']:
                val = {}
                val['invoice_id'] = inv.id
                val['name'] = tax['name']
                val['amount'] = tax['amount']
                val['manual'] = False
                val['sequence'] = tax['sequence']
                val['base'] = tax['price_unit'] * line['quantity']
                # add tax id #
                val['tax_id'] = tax['id']

                if inv.type_name in ('out_invoice', 'in_invoice'):
                    val['base_code_id'] = tax['base_code_id']
                    val['tax_code_id'] = tax['tax_code_id']
                    val['base_amount'] = currency.compute(
                        val['base'] * tax['base_sign'], company_currency,
                        round=False)
                    val['tax_amount'] = currency.compute(
                        val['amount'] * tax['tax_sign'], company_currency,
                        round=False)
                    val['account_id'] = tax['account_collected_id'] or \
                                        line.account_id.id
                else:
                    val['base_code_id'] = tax['ref_base_code_id']
                    val['tax_code_id'] = tax['ref_tax_code_id']
                    val['base_amount'] = currency.compute(
                        val['base'] * tax['ref_base_sign'], company_currency,
                        round=False)
                    val['tax_amount'] = currency.compute(
                        val['amount'] * tax['ref_tax_sign'], company_currency,
                        round=False)
                    val['account_id'] = tax['account_paid_id'] or \
                                        line.account_id.id

                key = (val['tax_id'])
                if key not in tax_grouped:
                    tax_grouped[key] = val
                else:
                    tax_grouped[key]['amount'] += val['amount']
                    tax_grouped[key]['base'] += val['base']
                    tax_grouped[key]['base_amount'] += val['base_amount']
                    tax_grouped[key]['tax_amount'] += val['tax_amount']

        for tax in tax_grouped.values():
            tax['base'] = currency.round(tax['base'])
            tax['amount'] = currency.round(tax['amount'])
            tax['base_amount'] = currency.round(tax['base_amount'])
            tax['tax_amount'] = currency.round(tax['tax_amount'])
        return tax_grouped