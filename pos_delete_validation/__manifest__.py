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
    'name': "pos_delete_validation",

    'summary': """
        Desarrollo para borrar y/o modificar productos en POS
    """,
    'description': """
        Desarrollo para borrar y/o modificar productos en POS
    """,
    "author": "MoviTrack",
    'category': 'Uncategorized',
    'version': '14.0.1',
    'depends': ['base', 'point_of_sale'],
    'data': [
        'views/templates.xml',
        'static/src/xml/pos_code_admin_pos.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': ['static/src/xml/pos_delete_validation.xml']
}
