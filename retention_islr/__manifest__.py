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
    'name': "Retention ISLR",

    'summary': """Module_Retention_ISLR""",
    'description': """
      Generación de reportes por concepto de retención del ISLR, 
	reportes pdf y xls
    """,
    'version': '14.0.4.0',
    'author': 'Localizacion Venezolana',
    'category': 'Tools',
    'depends': ['base', 'account', 'withholding_islr', 'grupo_localizacion'],
    'data': [
         'security/ir.model.access.csv',
        'wizard/wizard_retention_islr.xml',
        'report/report_retention_islr_pdf.xml',
    ],
    'demo': [
    ],
    "installable": True,
    'application': True,

}
