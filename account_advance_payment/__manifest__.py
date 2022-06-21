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
    'name': 'Account Advanced Payment',
    'summary': 'Registro de Anticipo para proveedores y clientes.',
    'description': '''
Registro de Anticipos para ser aplicados a las facturas de clientes y proveedores,
asi como los reversos de los mismos.
============================
''',
    "author": "MoviTrack",
    'version': '14.1.3',
    'category': 'Accounting',
    'depends': ['base', 'web', 'mail', 'account'],
    'data': [
            'security/ir.model.access.csv',
            'view/account_advance_payment.xml',
            'data/sequence_advance_data.xml',
            'view/res_partner_view.xml',
            'view/invoice_view.xml',
            'security/group.xml',
        ],
    'installable': True,
    'active': True,
}
