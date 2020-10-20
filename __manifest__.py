# -*- coding: utf-8 -*-
{
    'name': "Certificate Planer",

    'summary': """
        Certificate Planer Summary
    """,

    'description': """
        Certificate Planer Description
    """,

    'author': "Mint System GmbH",
    'website': "https://www.mint-system.ch",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/document_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
