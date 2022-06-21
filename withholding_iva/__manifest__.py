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
    "name": "Retención IVA las leyes basicas en Venezuela",
    "version": "14.0.4.0",
    "author": 'Localizacion Venezolana',
    "category": 'Contabilidad',
    "depends": ['base_vat','base','account','base_withholdings','web','grupo_localizacion', 'account_debit_note'],
    'description' : """
Administración de las retenciones de IVA.
===================================================
    """,
    'data': [
        'security/ir.model.access.csv',
        'wizard/record_retention_view.xml',
        'wizard/record_retention_suppliers.xml',
        'view/generate_txt_view.xml',
        'view/account_invoice_view.xml',
        'view/account_view.xml',
        'view/partner_view.xml',
        'view/res_company_view.xml',
        'view/wh_iva_view.xml',
        'report/withholding_vat_report.xml',
        'view/account_move_reversal_inherit.xml'
    ],
    'installable': True,
    'application': True,
}
