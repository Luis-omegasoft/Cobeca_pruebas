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
from odoo import fields, models


class Partners(models.Model):
    _inherit = 'res.partner'

    muni_wh_agent = fields.Boolean(string='Agente de retención', help='Verdadero si el partner es agente de retención'
                                                                      ' municipal.')
    purchase_jrl_id = fields.Many2one('account.journal', string='Diario de compras')
    sale_jrl_id = fields.Many2one('account.journal', string='Diario de ventas')
    account_ret_muni_receivable_id = fields.Many2one('account.account', string='Cuenta de retención clientes')
    account_ret_muni_payable_id = fields.Many2one('account.account', string='Cuenta de retención proveedores')
    nit = fields.Char(string='NIT', help='Número antiguo de identificación del impuesto reemplazado por el RIF actual.')
    econ_act_license = fields.Char(string='License number', help='Número de licencia para la actividad económica.',
                                   required=True)
    nifg = fields.Char(string='NIFG', help='Número asignado por el Satrin.', required=True)
