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


class ResCompany(models.Model):
    _inherit = 'res.company'


    automatic_income_wh= fields.Boolean(
            'Retención Automática de Ingresos', default=False,
            help='Cuando sea cierto, la retención de ingresos del proveedor se'
                 'validara automáticamente')
    propagate_invoice_date_to_income_withholding= fields.Boolean(
            'Propague la fecha de la factura a la retención de ingresos', default = False,
            help='Propague la fecha de la factura a la retención de ingresos. Por defecto es'
                 'en falso')

