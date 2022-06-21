# -*- coding: utf-8 -*-
{
    'name': 'Install In10_ve_Location',
    'summary': 'Instala modulos de la localización',
    'description': '''
Instala de forma automatica todos los modulos de la
 localización personalizada Omegasoft.
''',
    "author": "Christopher",
    'version': '14.1.1',
    'category': 'Install',
    'depends': [
        'l10n_ve',     
        'account_advance_payment',     
        'account_fiscal_requirements', 
        'aux_product',                 
        'base_withholdings',           
        'check_duplicies',             
        'dolar_to_bs_pos',             
        'email_iva_islr',              
        'fiscal_book',                 
        'grupo_localizacion',          
        'islr_checking',               
        'multimoneda',                 
        'pos_client_camp',
        'pos_delete_validation',
        'precioaux_pos',
        'rates',
        'retention_islr',
        'sale_purchase_order_innherit',
        'validation_facturacion',
        'validation_res_partner',
        'validation_rif_res_company',
        've_dpt',
        'withholding_islr'
        ],
    'data': [
        ],
    'installable': True,
    'active': True,
}
