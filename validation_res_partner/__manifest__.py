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

{
    "name": "Validaciones res.partner",
    "version": "1.1",
    'category' : 'Accounting',
    "author": "MoviTrack",
    'summary': """
        Validaciones y adición de campos sobre el partner cliente-proveedor.""",
    'description' : """
        Agrega el tipo de persona, y coloca el Documento de Identidad segun el tipo de persona y sus respectivos atributos.""",
    'depends' : [
                 "base","base_vat"],
    "data": [
        'security/ir.model.access.csv',
        'views/res_partner_people_type.xml',
        'views/docum_ident_res_partner.xml',
             ],
    'installable': True,
}
