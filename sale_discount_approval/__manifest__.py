# -*- coding: utf-8 -*-
{
    'name': "sale_discount_approval",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'base', 'account'],

    # always loaded
    'data': [
        'wizard/tandc_wizard_view.xml',
        'views/sale_order_approval.xml',
        'security/security_access.xml',
        'security/ir.model.access.csv',

    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
