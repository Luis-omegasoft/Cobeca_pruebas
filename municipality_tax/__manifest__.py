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
    'name': 'Impuestos municipales para la Localización venezolana',

    'summary': """
        Módulo que contiene los impuestos auxiliares para la localización de Venezuela.""",

    'description': """
        * Menú action en Contabilidad.
        * Vistas form y tree para registro de impuestos municipales.
    """,
    'version': '14.2.1',
    "author": "MoviTrack",
    'description': 'Municipal Taxes',
    'category': 'Accounting',
    'depends': ['account_accountant', 'base', 'withholding_iva', 've_dpt'],
    'data': [
        'security/ir.model.access.csv',
        'data/muni.wh.concept.csv',
        'data/seq_muni_tax_data.xml',
        'data/period.month.csv',
        'data/period.year.csv',
        'views/account_move_views.xml',
        'views/res_partner_views.xml',
        'views/municipality_tax_views.xml',
        'report/report_municipal_tax.xml',
        'views/res_company_views.xml',
        ],
    'installable': True,
    'application': True,
}
