# -*- coding: utf-8 -*-
{
    'name': "cash_transfer",

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
    'depends': ['base','account','point_of_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/seq.xml',
        'data/closing_pos_session.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/cash_transfer.xml',
        'wizard/date_range_wizard.xml',
        'wizard/product_wise_sale_purchase_stock_report.xml',
        'report/cash_transfer_report.xml',
        'report/p_w_sale_purchase_stock_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
