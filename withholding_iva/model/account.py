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
from odoo import models, fields


class AccountTax(models.Model):
    _inherit = 'account.tax'

    ret = fields.Boolean(
        string='Retenido?',
        help="Indique si el impuesto debe ser retenido")

    wh_vat_collected_account_id = fields.Many2one(
        'account.account',
        string="Cuenta de retención de IVA de factura",
        help="Esta cuenta se utilizará al aplicar una retención a una Factura")

    wh_vat_paid_account_id = fields.Many2one(
        'account.account',
        string="Cuenta de Devolucion de la retención de IVA",
        help="Esta cuenta se utilizará al aplicar una retención a un Reembolso")

    type_tax = fields.Selection([('iva', 'IVA'),
        						('islr', 'ISLR'),
        						('responsability','Responsabilidad social'),
        						('municipal', 'Municipal'),
        						('fiscal', 'Timbre fiscal')],required=True,help="Selecione el Tipo de Impuesto",string="Tipo de Impuesto")