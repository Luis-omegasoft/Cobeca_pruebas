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
    'name': 'Pos campos en registro clientes',
    'version': '14.0.1.0.0',
    'summary': """"Campos en Cliente""",
    'description': """Campos en Cliente""",
    'category': 'Point of Sale',
    'live_test_url': '',
    "author": "MoviTrack",
    'website': "",
    'depends': ['point_of_sale'],
    'data': [
        'views/templates.xml',
    ],
    'images': [],
    'qweb': [
        "static/src/xml/pos_cliente.xml",
    ],
    'license': 'LGPL-3',
    'installable': True,
    'active': True,
}
