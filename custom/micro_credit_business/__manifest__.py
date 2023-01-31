# -*- coding: utf-8 -*-
{
    'name': "micro_credit_business",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/seq.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/inherit_res_partner.xml',
        'views/credit_account_view.xml',
        'views/territory_view.xml',
        'views/credit_entry_type.xml',
        'views/duration_type.xml',
        'views/collection_duration_type.xml',
        'views/account_type.xml',
        'views/account_credit_loan.xml',
        'views/credit_balance_move.xml',
        'views/installment_configuration.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
