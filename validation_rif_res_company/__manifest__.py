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
    "name": "Validaciones RIF res.company-res.partner",
    "version": "1.1",
    'category': 'Accounting',
    "author": "MoviTrack",
    
    'summary': """
        Modifica y realiza validaciones al nif-vat-rif.""",
    'description': """
        * Modifica campo y realiza validaciones al vat(nif) y al email:
            * De la compañia.
            * Del cliente-proveedor.""",
    'depends' : ["base","base_vat","validation_res_partner"],
    "data": [
        'security/ir.model.access.csv',
        'views/3mit_validation_res_company_rif.xml',
	    'views/3mit_validation_res_partner.xml',
             ],
    'installable': True,
}
