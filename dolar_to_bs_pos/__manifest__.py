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
    "name": "Agrega precio y Pagos en Bs en punto de venta",
    "version": "1.0",
    "author": "MoviTrack",
    "license": "AGPL-3",
    "category": "ventas",
    'depends': ['stock_account', 'web_editor', 'digest', 'point_of_sale','aux_product'],
    'demo': [
    ],
    "data": [
        'views/point_of_sale.xml',
        'views/bool_metodopagos_view.xml',
    ],
    'installable': True,
    'active': True,
    'qweb': ['static/src/xml/pos.xml'],

}
