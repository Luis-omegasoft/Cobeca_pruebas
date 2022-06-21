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

from odoo import fields, models, api, _
from odoo.exceptions import UserError

class ChangeInvoiceSinCredwizard(models.TransientModel):

    """
    Wizard that changes the invoice sin_cred field.
    """
    _name = 'change.invoice.sin.cred'
    _description = 'Change Invoice Tax Exempt'

    sin_cred = fields.Boolean('Exento de impuestos',default=lambda s: s._context.get('invoice_sin_cred'),
            help='Exento de impuestos')
    sure = fields.Boolean('¿Estas Seguro?')


    def set_sin_cred(self):
        """
        Change the sin cred field in the invoice
        @return
        """
        context = self._context or {}
        ids = isinstance(self.ids, (int, int)) and [self.ids] or self.ids
        inv_obj = self.env['account.move']
        inv_ids = context.get('active_ids', [])
        data = self.browse(ids[0])
        invoice = inv_obj.browse(self._context['active_id'])

        if not data.sure:

            raise UserError("Error! \n Confirme que desea realizar esta accion marcando la opción")
        if inv_ids:
            invoice.write({'sin_cred': self.sin_cred})
        return {}
