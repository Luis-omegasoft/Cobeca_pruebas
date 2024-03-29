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
import ast
import datetime, time

from odoo.tools.translate import _
from odoo import models, fields, api
from odoo.exceptions import UserError

class SaleOrderInnherit(models.Model):
    _inherit = 'sale.order'

    # partner_id = fields.Many2one(
    #     'res.partner', string='Customer', readonly=True,
    #     states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
    #     required=True, change_default=True, index=True, tracking=1,
    #     domain="['|',('customer_rank', '>=', 0),('supplier_rank', '>=', 0)]")

    partner_id = fields.Many2one('res.partner', readonly=True,
                                 #                                 states={'draft': [('readonly', False)]},
                                 domain="['|',('customer_rank', '>=', 0),('supplier_rank', '>=', 0)]",
                                 string='Partner')

    rif = fields.Char(string="RIF", related='partner_id.rif', store=True, states={'draft': [('readonly', True)]})

    identification_id = fields.Char('Documento de Identidad', related='partner_id.identification_id', size=20,
                                     store=True, states={'draft': [('readonly', True)]})

    nationality = fields.Selection([
        ('V', 'Venezolano'),
        ('E', 'Extranjero'),
        ('P', 'Pasaporte')], string="Tipo Documento", related='partner_id.nationality', store=True,
        states={'draft': [('readonly', True)]})

    people_type_company = fields.Selection([
        ('pjdo', 'PJDO    Persona Jurídica Domiciliada'),
        ('pjnd', 'PJND    Persona Jurídica No Domiciliada')
    ], 'Tipo de Persona', related='partner_id.people_type_company')


    people_type_individual = fields.Selection([
        ('pnre', 'PNRE    Persona Natural Residente'),
        ('pnnr', 'PNNR    Persona Natural No Residente')], 'Tipo de Persona', related='partner_id.people_type_individual')

    company_type = fields.Selection(string='Company Type',
                                     selection=[('person', 'Individual'), ('company', 'Company')], related='partner_id.company_type')

    def write(self, vals):
        res = {}
        if vals.get('partner_id'):
                partner_id = vals.get('partner_id')
                partner_obj =self.env['res.partner'].search([('id', '=', partner_id)])
                if (partner_obj.company_type == 'person' and not partner_obj.identification_id):
                    raise UserError('El Cliente no posee Documento Fiscal, por favor diríjase a la configuación de %s, y realice el registro correctamente para poder continuar' % str(partner_obj.name))
                if (partner_obj.company_type == 'company'):
                    if (partner_obj.people_type_company == 'pjdo' and not partner_obj.rif):
                        raise UserError('El Cliente no posee Documento Fiscal, por favor diríjase a la configuación de %s, y realice el registro correctamente para poder continuar' % str(partner_obj.name))

        res = super(SaleOrderInnherit, self).write(vals)
        return res

    @api.model
    def create(self, vals):
        res = {}
        if vals.get('partner_id'):
            partner_id = vals.get('partner_id')
            partner_obj =self.env['res.partner'].search([('id', '=', partner_id)])
            if (partner_obj.company_type == 'person' and not partner_obj.identification_id):
                raise UserError('El Cliente no posee Documento Fiscal, por favor diríjase a la configuación de %s, y realice el registro correctamente para poder continuar' % str(partner_obj.name))

            if (partner_obj.company_type == 'company'):
                if (partner_obj.people_type_company == 'pjdo' and not partner_obj.rif):
                    raise UserError('El Cliente no posee Documento Fiscal, por favor diríjase a la configuación de %s, y realice el registro correctamente para poder continuar' % str(partner_obj.name))

        res = super(SaleOrderInnherit, self).create(vals)
        return res