# -*- coding: utf-8 -*-
{
    'name': "mime_task",

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
    'depends': ['base', 'purchase'],
    # purchase.access_mime_task_mime_task,mime_task.mime_task,model_mime_task_mime_task,base.group_user,1,1,1,1

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/inherit_purchase_order.xml',
        'views/inherit_res_users.xml',
        'report/purchase_report.xml',
        'report/purchase_order_report_custom.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
