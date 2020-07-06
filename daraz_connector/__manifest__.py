# -*- coding: utf-8 -*-
{
    'name': "Daraz Connector",

    'summary': """
        Daraz connector that integrate the Odoo and Daraz Store""",

    'description': """
       Daraz connector that integrate the Odoo and Daraz Store
    """,

    'author': "Telenoc",
    'website': "http://www.telenoc.org",

    
    'category': 'Tools',
    'version': '13.9',

    'depends': ['sale_stock','purchase','sale','account','stock','sale_management','contacts'],

    'data': [
        'security/ir.model.access.csv',
        'views/daraz_instance.xml',
        'views/sale.xml',
        'views/ir_cron.xml',
        'views/purchase.xml',
        'views/view_process_job.xml',
        'wizard/process_import_export_view.xml',
        'wizard/cancel_reason.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

    'images': ['static/description/icon.png'],
    # 'demo': [
    #     'demo/demo.xml',
    # ],
 	"price": 250,
    "currency": "EUR",
}
