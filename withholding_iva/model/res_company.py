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


class ResCompany(models.Model):
    _inherit = "res.company"

    consolidate_vat_wh = fields.Boolean(
        string="Consolidar Quincena de Retencion de IVA", default=False,
        help='Si se establece, las retenciones en IVA generadas en una misma'
        ' noche se agruparán en un recibo de retención')
    allow_vat_wh_outdated = fields.Boolean(
        string="Permitir retención de IVA",
        help="Permite confirmar comprobantes de retención para anteriores o futuras "
        " fechas.")
    propagate_invoice_date_to_vat_withholding = fields.Boolean(
        string='Propagar fecha de factura a retención de IVA', default=False,
        help='Propague la fecha de la factura a la retención de IVA. Por defecto está en '
        'Falso.')
