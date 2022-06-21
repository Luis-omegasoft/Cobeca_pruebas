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

from odoo import api
from odoo import fields, models
from datetime import datetime

class AccountInvoice(models.Model):
    _inherit = 'account.move'
    # Esta clase es para crear en la factura el saldo de anticipo del cliente o proveedor.

    account_advance_ids = fields.One2many('account.advanced.payment','invoice_id')
    partner_id = fields.Many2one('res.partner')
    sum_amount_available = fields.Monetary('Anticipo Disponible', currency_field='company_currency')
    currency_id = fields.Many2one('res.currency', string='Currency')
    company_currency = fields.Many2one('res.currency', string='Bs currency',default=lambda self: self.env['res.currency'].search([('symbol', '=', 'Bs.')]))
    sum_amount_available_dolares = fields.Monetary('Monto moneda extranjera', currency_field='foreign_currency')
    currency_company = fields.Many2one('res.currency', string='Currency')
    foreign_currency = fields.Many2one('res.currency', string='Currency')
    anticipo_check = fields.Boolean('Ya esta atado a un anticipo')
    anticipo_ref = fields.Many2one('account.advanced.payment', string="N° referencia de anticipo")

    @api.onchange('partner_id')
    def _onchange_amount_available(self):
        '''Muestra el saldo disponible en los anticipos para clientes y proveedores'''
        self.currency_company = self.env.company.currency_id
        self.foreign_currency = self.env['res.currency'].search([
            ('name', '=', 'USD')
        ])
        self.sum_amount_available = 0
        bolivares = 0
        dolares = 0
        sum_bolivares = 0
        advance_obj = self.env['account.advanced.payment']

        if self.move_type == 'out_invoice' or self.move_type == 'out_refund':
            advance_bw = advance_obj.search([('partner_id', '=', self.partner_id.id),
                                         ('state', '=', 'available'),
                                         ('is_customer','=',True)])

            for advance in advance_bw:
                if advance.currency_id.id == self.env.company.currency_id.id:
                    bolivares += advance.amount_available
                else:
                    dolares += advance.amount_available
                    sum_bolivares += advance.amount_available * advance.rate
            fecha = datetime.now().strftime('%Y-%m-%d')
            currency_rate = self.env['res.currency.rate'].search([
                ('currency_id', '=', self.env.company.currency_id.id),
                ('name', '=', fecha),
            ]).rate
            self.sum_amount_available = bolivares + sum_bolivares
            if not currency_rate:
                self.sum_amount_available_dolares = dolares
            else:
                self.sum_amount_available_dolares = dolares + bolivares / currency_rate
        else:
            advance_bw = advance_obj.search([('partner_id', '=', self.partner_id.id),
                                             ('state', '=', 'available'),
                                             ('is_supplier', '=', True)])
            for advance in advance_bw:
                if advance.currency_id.id == self.env.company.currency_id.id:
                    bolivares += advance.amount_available
                else:
                    dolares += advance.amount_available
                    sum_bolivares += advance.amount_available * advance.rate
            fecha = datetime.now().strftime('%Y-%m-%d')
            currency_rate = self.env['res.currency.rate'].search([
                ('currency_id', '=', self.env.company.currency_id.id),
                ('name', '=', fecha),
            ]).rate
            self.sum_amount_available = bolivares + sum_bolivares
            if not currency_rate:
                self.sum_amount_available_dolares = dolares
            else:
                self.sum_amount_available_dolares = dolares + bolivares / currency_rate
        return

    @api.onchange('invoice_date')
    def onchange_invoice_date(self):
        self.sum_amount_available = 0
        bolivares = 0
        dolares = 0
        sum_bolivares = 0
        advance_obj = self.env['account.advanced.payment']

        if self.move_type == 'out_invoice' or self.move_type == 'out_refund':
            advance_bw = advance_obj.search([('partner_id', '=', self.partner_id.id),
                                             ('state', '=', 'available'),
                                             ('is_customer', '=', True)])

            for advance in advance_bw:
                if advance.currency_id.id == self.env.company.currency_id.id:
                    bolivares += advance.amount_available
                else:
                    dolares += advance.amount_available
                    sum_bolivares += advance.amount_available * advance.rate
            currency_rate = self.env['res.currency.rate'].search([
                ('currency_id', '=', self.env.company.currency_id.id),
                ('name', '=', self.invoice_date),
            ]).rate
            self.sum_amount_available = bolivares + sum_bolivares
            if not currency_rate:
                self.sum_amount_available_dolares = dolares
            else:
                self.sum_amount_available_dolares = dolares + bolivares / currency_rate
        else:
            advance_bw = advance_obj.search([('partner_id', '=', self.partner_id.id),
                                             ('state', '=', 'available'),
                                             ('is_supplier', '=', True)])
            for advance in advance_bw:
                if advance.currency_id.id == self.env.company.currency_id.id:
                    bolivares += advance.amount_available
                else:
                    dolares += advance.amount_available
                    sum_bolivares += advance.amount_available * advance.rate
            currency_rate = self.env['res.currency.rate'].search([
                ('currency_id', '=', self.env.company.currency_id.id),
                ('name', '=', self.invoice_date),
            ]).rate
            self.sum_amount_available = bolivares + sum_bolivares
            if not currency_rate:
                self.sum_amount_available_dolares = dolares
            else:
                self.sum_amount_available_dolares = dolares + bolivares / currency_rate
        return
