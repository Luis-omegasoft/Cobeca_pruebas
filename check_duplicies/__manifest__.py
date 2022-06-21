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
    'name': "Action duplicar de factura proveedor",

    'summary': """
        Modifica el botón de duplicar para las facturas del proveedor
        """,
    'description': """
        Realiza modificaciones al botón de duplicar factura:\n
            * Modifica el status de la factura duplicada.
            * Evita generar documento de retención de ingresos.
            * Evita generar el número de control por default.
            * Evita que se cree el número de factura de proveedor por default.
    """,

    "author": "MoviTrack",
    'category': 'Account',
    'version': '14.0.0.1',
    'depends': ['base', 'account', 'withholding_islr'],
    'data': [
    ],
    'demo': [

    ],
}
