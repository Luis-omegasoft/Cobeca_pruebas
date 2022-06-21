{
    "name": "Gestión de retenciones leyes venezolanas",
    "version": "1.0",
    "author": "Localizacion Venezolana",
    "category": 'Contabilidad',
    "depends": ['account', 'base_vat', 'account_accountant', 'base', 'account_fiscal_requirements','grupo_localizacion'],
    'data': [
        'view/base_withholding_view.xml', 'view/account_journal_view.xml'
    ],
    'installable': True,
    'active': True,
}
