# -*- coding: utf-8 -*-
{
    'name': "Estate",

    'summary': """
        Real Estate Advertisement""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Duong Hoang",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'application': True,
    'installable': True,
    'license': "LGPL-3",

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

}
