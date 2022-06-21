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
    "name": "Libros Fiscales para Venezuela",
    "version": "14.0.1",
    "depends": ['base',
                'account',
                'base_vat',
                'account_accountant',
                'withholding_iva',
                'account_fiscal_requirements',
                'validation_res_partner',
                'validation_facturacion',
                'grupo_localizacion',
    
                ],
    "author": "Localizacion Venezolana",
    "license": "AGPL-3",
    "category": "Libros Fiscales-Accounting",
    "data": [
        "wizard/fiscal_book_wizard_view.xml",
        "view/adjustment_book.xml",
        "view/fiscal_book.xml",
        "report/fiscal_purchase_book_report.xml",
        "report/fiscal_book_report.xml",
        "wizard/change_invoice_sin_cred_view.xml",
        "view/account_invoice_view.xml",
        "security/ir.model.access.csv"
    ],
    "test": [

    ],
    "installable": True,
}





