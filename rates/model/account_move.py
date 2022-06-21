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
from odoo import fields, models, api
from odoo.exceptions import UserError
from datetime import date, timedelta

class SaleOrderInherit(models.Model):
    _inherit = 'account.move'

    currency_bs_rate = fields.Float(string='Tasa($)', store=True, compute="calculate_last_rate")
    currency_bs_date = fields.Date(string="Fecha")

    @api.depends('invoice_date')
    def calculate_last_rate(self):
        for i in self:
            fecha = None
            if i.invoice_date:
                fecha = i.invoice_date
            else:
                fecha = date.today()
            currency_id = self.env['res.currency'].search([('name', '=', 'USD')], limit=1)
            rate = self.env['res.currency.rate'].search([
                ('currency_id', '=', currency_id.id),
                ('name', '<=', fecha),
            ], limit=1)
            if rate.rate != 0 or rate.rate:
                i.currency_bs_rate = 1/rate.rate
            else:
                i.currency_bs_rate = 0
            i.currency_bs_date = rate.name






