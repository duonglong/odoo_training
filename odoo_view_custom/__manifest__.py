{
    'name': 'Gallery View & Star Rating',
    'version': '19.0.1.0.0',
    'category': 'Custom',
    'summary': '',
    'description': """
       
    """,
    'author': 'LongDT',
    'depends': ['base', 'web', 'product'],
    'data': [
        'views/product_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'odoo_view_custom/static/src/fields/star_rating_field.js',
            'odoo_view_custom/static/src/fields/star_rating_field.xml',
            'odoo_view_custom/static/src/fields/star_rating_field.scss',

            'odoo_view_custom/static/src/views/card_gallery_view.js',
            'odoo_view_custom/static/src/views/card_gallery_view.xml',
            'odoo_view_custom/static/src/views/card_gallery_view.scss',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
