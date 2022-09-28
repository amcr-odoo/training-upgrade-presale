# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Presale",
    'version': '1.0',
    'author': 'Odoo PS',
    'summary': 'Presale application',
    'description':"""
         Presale order on a product
    """,
    'category': 'Customization',
    'depends': [
        'base',
        'base_automation',
        'product',
    ],
    'data': [
        'models/presale_order_line.xml',
        'models/presale_order.xml',
        'security/ir.model.access.csv',
        'views/presale_order.xml',
        'views/presale_menus.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}
