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


class IslrWhConcept(models.Model):

    """ Model to create the withholding concepts
    """
    _name = 'islr.wh.concept'
    _description = 'Concepto de retención de ingresos'


    name= fields.Char(
            'Concepto de retención', translate=True, size=256, required=True,
            help="Nombre del concepto de retención, ejemplo: Honorarios "
                 "Profesionales, Comisiones a ...")
    codigo = fields.Char(string="Código")
    withholdable= fields.Boolean(
            string=' A Retener', default=True,
            help="Compruebe si la retención del concepto se retiene o no ")
    property_retencion_islr_payable= fields.Many2one(
            'account.account',
            string="Cuenta de Compra para la Retención de Ingresos",
            company_dependet=True,
            required=False,
            #domain="[('internal_type','=','payable')]",
            help="Esta cuenta se usará como la cuenta donde se retuvo"
                 "los importes se cargarán en su totalidad (Compra) del impuesto sobre la renta"
                 "por este concepto")
    property_retencion_islr_receivable= fields.Many2one(
            'account.account',
            string="Cuenta de Venta para la Retención de Ingresos",
            company_dependet=True,
            required=False,
          #  domain="[('internal_type','=','receivable')]",
            help="Esta cuenta se usará como la cuenta donde se retuvo"
                 "los importes se cargarán en (Venta) del impuesto sobre la renta")
    rate_ids= fields.One2many(
            'islr.rates', 'concept_id', 'Tasas',
            help="Tasa de concepto de retención", required=False)

    user_id = fields.Many2one('res.users', 'Responsible', default=lambda self: self.env.user)


IslrWhConcept()
