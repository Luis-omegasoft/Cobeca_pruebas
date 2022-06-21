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


class ResPartner(models.Model):
    _inherit = 'res.partner'


    islr_withholding_agent = fields.Boolean(
            '¿Agente de retención de ingresos?', default=True,
            help="Verifique si el partner es un agente de retención de ingresos")
    spn = fields.Boolean(
            '¿Es una sociedad de personas físicas?',
            help='Indica si se refiere a una sociedad de personas físicas.')
    islr_exempt = fields.Boolean(
            '¿Está exento de retención de ingresos?',
            help='Si el individuo está exento de retención de ingresos')
 #   islr_wh_historical_data_ids = fields.One2many(
 #         'islr.wh.historical.data', 'partner_id', 'Datos históricos de ISLR',
  #        help='Valores a utilizar al calcular las tasas')
    purchase_islr_journal_id = fields.Many2one('account.journal', 'Diario de Compra para ISLR')
    sale_islr_journal_id = fields.Many2one('account.journal', 'Diario de Venta para ISLR')




    def copy(self, default=None):
        """ Initialized id by duplicating
        """
        # NOTE: use ids argument instead of id for fix the pylint error W0622.
        # Redefining built-in 'id'
        if default is None:
            default = {}
        default = default.copy()
        default.update({
            'islr_withholding_agent': 1,
            'spn': 0,
            'islr_exempt': 0,
            'islr_wh_historical_data_ids': [],
        })

        return super(ResPartner, self).copy(default)
