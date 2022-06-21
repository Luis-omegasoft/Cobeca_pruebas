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
    'name': "Chequeo documento ISLR",

    'summary': """
        Chequea si una una factura tiene retención de ISLR.
        """,
    'description': """
        Realiza el chequeo de factura y verifica si tiene un ISLR asociado.\n
        Si se le modifican los valores en el account.move.line, actualiza el documento de retención del ISLR asociado.
    """,
    "author": "MoviTrack",
    'category': 'Tax',
    'version': '14.0.1',
    'depends': ['base', 'account', 'withholding_islr'],
}
