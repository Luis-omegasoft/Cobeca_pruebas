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
    'name': "Email: Información I.V.A. e I.S.L.R.",
    'summary': """
        Envía un email automático al partner al momento de confirmar el documento 
        de I.V.A. o I.S.L.R. según sea el caso.""",
    'description': """
        * Verifica si existe un email asociado al partner y lo setea como obligatorio.
        * Crea un template para enviar el Comprobante del I.V.A.
        * Envía automáticamente por correo el Comprobante de I.V.A. una vez confirmado.
        * Crea un template para enviar el Detalle de Retenciones de I.S.L.R.
        * Envía automáticamente por correo el Detalle de Retenciones de I.S.L.R. una vez confirmado.
    """,
    "author": "MoviTrack",
    'category': 'Accounting',
    'version': '14.0.1',
    'depends': ['base', 'account', 'account_fiscal_requirements',
                'base_withholdings', 'withholding_iva', 'withholding_islr', 'retention_islr'],
    'data': [
        'views/islr_wh_doc_suppliers_inherit_view.xml',
        'views/islr_wh_doc_inherit_view.xml',
        'views/email_template_islr.xml',
        'views/account_wh_iva_inherit_view.xml',
        'views/email_template_iva.xml',
    ],
    'installable': True,
    'active': True,
}
