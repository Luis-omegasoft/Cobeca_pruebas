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


class ValidationDocument(models.Model):
    _inherit = 'res.partner'

    @api.model_create_multi
    def create(self, vals):
        if vals[0].get('identification_id') and vals[0].get('nationality'):
            valor = vals[0].get('identification_id')
            nationality = vals[0].get('nationality')
            self.validation_document_ident(valor, nationality)
        if vals[0].get('identification_id'):
            if not self.validate_ci_duplicate(vals[0].get('identification_id', False), True):
                raise UserError('El cliente o proveedor ya se encuentra registrado con el Documento: %s'
                                % (vals[0].get('identification_id', False)))
        res = super(ValidationDocument, self).create(vals)
        return res

    def write(self, vals):
        if vals.get('identification_id') and not vals.get('nationality'):
            valor = vals.get('identification_id')
            nationality = self.nationality
            self.validation_document_ident(valor, nationality)
        if vals.get('identification_id') and vals.get('nationality'):
            valor = vals.get('identification_id')
            nationality = vals.get('nationality')
            self.validation_document_ident(valor, nationality)
        if vals.get('nationality') and not vals.get('identification_id'):
            valor = self.identification_id
            nationality = vals.get('nationality')
            self.validation_document_ident(valor, nationality)
        if not self.validate_ci_duplicate(vals.get('identification_id', False)):
            raise UserError('El cliente o proveedor ya se encuentra registrado con el Documento: %s'
                            % (vals.get('identification_id', False)))
        res = super(ValidationDocument, self).write(vals)
        return res

    nationality = fields.Selection([
        ('V', 'Venezolano'),
        ('E', 'Extranjero'),
        ('P', 'Pasaporte')], string="Tipo Documento")
    identification_id = fields.Char(string='Documento de Identidad')
    value_parent = fields.Boolean(string='Valor parent_id', compute='compute_value_parent_id')

    @api.depends('company_type')
    def compute_value_parent_id(self):
        for rec in self:
            rec.value_parent = rec.parent_id.active

    @staticmethod
    def validation_document_ident(valor, nationality):
        if valor:
            if nationality == 'V' or nationality == 'E':
                if len(valor) == 7 or len(valor) == 8:
                    if not valor.isdigit():
                        raise UserError('La Cédula solo debe ser Numerico. Por favor corregir para proceder a Crear/Editar el registro')
                    return
                else:
                    raise UserError('La Cedula de Identidad no puede ser menor que 7 cifras ni mayor a 8.')
            if nationality == 'P':
                if(len(valor) > 20) or (len(valor) < 10):
                    raise UserError('El Pasaporte no puede ser menor que 10 cifras ni mayor a 20.')
                return

    def validate_ci_duplicate(self, valor, create=False):
        found = True
        partner_2 = self.search([('identification_id', '=', valor)])
        for cus_supp in partner_2:
            if create:
                if cus_supp and (cus_supp.customer_rank or cus_supp.supplier_rank):
                    found = False
                elif cus_supp and (cus_supp.customer_rank or cus_supp.supplier_rank):
                    found = False
        return found
