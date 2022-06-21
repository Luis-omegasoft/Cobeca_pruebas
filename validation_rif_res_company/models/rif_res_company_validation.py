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
from odoo import models, fields, api
from odoo.exceptions import UserError
import re


class CompanyRif(models.Model):
    _inherit = 'res.company'

    rif = fields.Char(string='RIF')

    @api.model_create_multi
    def create(self, vals):
        res = super(CompanyRif, self).create(vals)
        if vals[0].get('rif'):
            if not self.validate_rif_er(vals[0].get('rif')):
                raise UserError('El rif tiene el formato incorrecto. Ej: V-012345678, E-012345678, J-012345678 o '
                                'G-012345678. Por favor intente de nuevo.')
            if self.validate_rif_duplicate(vals[0].get('rif'), res):
                raise UserError('El cliente o proveedor ya se encuentra registrado con el rif: %s y se encuentra activo'
                                % vals[0].get('rif'))
        if vals[0].get('email'):
            if not self.validate_email_addrs(vals[0].get('email'), 'email'):
                raise UserError('El email es incorrecto. Ej: cuenta@dominio.xxx. Por favor intente de nuevo')
        return res

    def write(self, vals):
        res = super(CompanyRif, self).write(vals)
        if vals.get('rif'):
            res = self.validate_rif_er(vals.get('rif'))
            if not res:
                raise UserError('El rif tiene el formato incorrecto. Ej: V-012345678, E-012345678, J-012345678 o '
                                'G-012345678. Por favor intente de nuevo')
            if self.validate_rif_duplicate(vals.get('rif'), False):
                raise UserError('El cliente o proveedor ya se encuentra registrado con el rif: %s y se encuentra activo'
                                % vals.get('rif'))
        if vals.get('email'):
            res = self.validate_email_addrs(vals.get('email'), 'email')
            if not res:
                raise UserError('El email es incorrecto. Ej: cuenta@dominio.xxx. Por favor intente de nuevo')
        return res

    @staticmethod
    def validate_rif_er(field_value):
        res = {}
        rif_obj = re.compile(r"^[J]+[-][\d]{9}", re.X)
        if rif_obj.search(field_value.upper()):
            res = {
                'rif': field_value
            }
        return res

    def validate_rif_duplicate(self, valor, res):
        if self:
            aux_ids = self.ids
            aux_item = self
        else:
            aux_ids = res.ids
            aux_item = res
        for _ in aux_item:
            company = self.env['res.company'].search([('rif', '=', valor), ('id', 'not in', aux_ids)])
            if company:
                return True
            else:
                return False

    @staticmethod
    def validate_email_addrs(email, field):
        res = {}
        mail_obj = re.compile(r"""
                \b             # comienzo de delimitador de palabra
                [\w.%+-]       # usuario: Cualquier caracter alfanumerico mas los signos (.%+-)
                +@             # seguido de @
                [\w.-]         # dominio: Cualquier caracter alfanumerico mas los signos (.-)
                +\.            # seguido de .
                [a-zA-Z]{2,3}  # dominio de alto nivel: 2 a 6 letras en minúsculas o mayúsculas.
                \b             # fin de delimitador de palabra
                """, re.X)     # bandera de compilacion X: habilita la modo verborrágico, el cual permite organizar
        # el patrón de búsqueda de una forma que sea más sencilla de entender y leer.
        if mail_obj.search(email):
            res = {
                field: email
            }
        return res
