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
    _inherit = 'sale.order'

    currency_bs_rate = fields.Float(string='Tasa($)', store=True, compute="calculate_last_rate")
    currency_bs_date = fields.Datetime(string="Fecha")

    @api.depends('date_order')
    def calculate_last_rate(self):
        for i in self:
            fecha = None
            if i.date_order:
                fecha = i.date_order.date()
            else:
                fecha = date.today()
            currency_id = self.env['res.currency'].search([('name', '=', 'USD')], limit=1)
            rate = self.env['res.currency.rate'].search([
                ('currency_id', '=', currency_id.id),
                ('name', '<=', fecha),
            ], limit=1)
            i.currency_bs_rate = rate.rate
            i.currency_bs_date = rate.name

class res_partner(models.Model):
    _inherit = 'res.partner'

    # currency_bs_rate = fields.Float(string='Tasa($)', digits=(12, 10), default=1.0)
    # currency_bs_date = fields.Datetime(string="Fecha tasa")
    #
    # @api.onchange('currency_bs_rate')
    # def update_date(self):
    #     if self.currency_bs_rate:
    #         self.currency_bs_date = date.today()
    #     else:
    #         self.currency_bs_date = None

class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    # currency_bs_rate = fields.Float(string='Tasa($)', related='partner_id.currency_bs_rate', digits=(12, 10), default=1.0)
    # currency_bs_date = fields.Datetime(string="Fecha", related='partner_id.currency_bs_date')
    currency_bs_rate = fields.Float(string='Tasa($)', store=True, compute="calculate_last_rate")
    currency_bs_date = fields.Datetime(string="Fecha")

    @api.depends('date_order')
    def calculate_last_rate(self):
        for i in self:
            fecha = None
            if i.date_order:
                fecha = i.date_order.date()
            else:
                fecha = date.today()
            currency_id = self.env['res.currency'].search([('name', '=', 'USD')], limit=1)
            rate = self.env['res.currency.rate'].search([
                ('currency_id', '=', currency_id.id),
                ('name', '<=', fecha),
            ], limit=1)
            i.currency_bs_rate = rate.rate
            i.currency_bs_date = rate.name



