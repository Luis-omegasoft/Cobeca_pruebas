# coding: utf-8

{
    'name': 'Requerimientos Fiscales Venezuela',
    'version': '14.0.2',
    'category': 'Accounting',
    "author": "MoviTrack",
    'summary': """
        Requerimientos fiscales exigidos por las leyes venezolanas.""",
    'description': """
        Agrega los requerimientos fiscales exigidos por las leyes venezolanas.""",
    'depends': ['account','base_vat','account_accountant','grupo_localizacion'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/l10n_ut_data.xml',
        'wizard/search_info_partner_seniat.xml',
        'wizard/wizard_nro_ctrl_view.xml',
        'view/res_company_view.xml',
        'view/l10n_ut_view.xml',
        'view/account_tax_view.xml',
        'view/account_invoice_view.xml',
        'view/nro_ctrl_secuencial_customer.xml',
    ],
    'installable': True,
}
