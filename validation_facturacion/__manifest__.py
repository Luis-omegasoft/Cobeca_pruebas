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
    "name": "Validaciones facturación",
    "version": "1.1",
    "author": "MoviTrack",
    "license": "AGPL-3",
    "category": "Accounting",
    'summary': """
        Añade números de control automáticos en la factura a clientes-proveedores.""",
    'description': """
        * Realiza validaciones y correciones en la facturación.
        * Añade números de control automáticos para:
            * Clientes.
            * Proveedores.""",
    "depends": [
        "account",
        "base",
        "base_vat",
        "validation_res_partner",
        "validation_rif_res_company"
    ],
    "data": [
        'security/ir.model.access.csv',
        'view/invoice_view.xml',
    ],
    'installable': True,
}
