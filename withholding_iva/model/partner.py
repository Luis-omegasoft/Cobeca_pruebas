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

import logging

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'
    logger = logging.getLogger('res.partner')

    consolidate_vat_wh = fields.Boolean(
        string='Consolidar Semana de Retencion de IVA',
        help='Si se establece, las retenciones en IVA generadas en una misma'
        ' noche se agruparán en un recibo de retención')

    wh_iva_agent = fields.Boolean(
        '¿Es Agente de Retención (IVA)?',
        help="Indique si el socio es un agente de retención de IVA")

    wh_iva_rate = fields.Float(
        string='Tasa de retención de IVA',
        help="Se coloca el porcentaje de la Tasa de retención de IVA")

    vat_subjected = fields.Boolean('Declaración legal de IVA',
    help="Marque esta casilla si el socio está sujeto al IVA. Se utilizará para la declaración legal del IVA.")

    purchase_journal_id = fields.Many2one('account.journal','Diario de Compra para IVA')
    purchase_sales_id = fields.Many2one('account.journal', 'Diario de Venta para IVA')
