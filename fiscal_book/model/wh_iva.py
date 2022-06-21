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
from odoo import fields, models, api, exceptions, _

class AccountWhIvaLine(models.Model):
    _inherit = "account.wh.iva.line"

    fb_id = fields.Many2one('fiscal.book', 'Fiscal Book',
            help='Libro fiscal donde esta línea está relacionada')


    def _update_wh_iva_lines(self, inv_id, fb_id):
        """
        It relate the fiscal book id to the according withholding iva lines.
        """
        inv_obj = self.env['account.move']
        inv = inv_obj.browse(inv_id)
        if inv.wh_iva and inv.wh_iva_id:
            awil_ids = self.search([('invoice_id', '=', inv.id)])
            self.write({'fb_id': fb_id})
        return True
