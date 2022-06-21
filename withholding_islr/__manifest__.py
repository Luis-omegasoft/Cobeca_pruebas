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
    "name": "Calcula la Retención del ISLR",
    "version": "14.0.0.3",
    "author": "Localizacion Venezolana",
    "license": "AGPL-3",
    "category": "Contabilidad, facturacion",
    "depends": [
        "account",
        "account_fiscal_requirements",
        "base_withholdings",
        'grupo_localizacion',
    ],
    "data": [
        'security/ir.model.access.csv',
         "data/l10n_ve_islr_withholding_data.xml",
         "data/sequence_withholding_islr.xml",
         "view/invoice_view.xml",
         "view/partner_view.xml",
         "view/res_company_view.xml",
         "view/islr_wh_doc_view.xml",
         "view/islr_wh_concept_view.xml",
         "view/product_view.xml",
         "view/islr_xml_wh.xml",
         "report/wh_islr_report.xml",
    ],
    "installable": True,
    'application': True,
}
