{
    'name': 'Simple Sale Order PDF Report',
    'version': '19.0.1.0.0',
    'category': 'Sales',
    'summary': 'Batch PDF report for Sale Orders',
    'depends': ['sale'],
    'data': [
        'report/sale_order_report.xml',
        'report/sale_order_report_template.xml',
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}