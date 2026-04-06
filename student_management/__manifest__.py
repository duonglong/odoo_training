# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Student Management',
    'version': '1.0',
    'summary': 'Student Management',
    'sequence': 10,
    'description': """
    Student Management:
        - Classroom management
        - Subject management
        - Student enrollment management
    """,
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_management.xml',
        'views/class_room.xml',
        'views/menus.xml',
    ],
    'demo': [
    ],
    'assets': {
        'web.assets_tests': [
            'student_management/static/src/js/tours/student_test_tour.js',
        ],
    },
    'installable': True,
    'application': False,
    'author': 'LongDT',
    'license': 'LGPL-3',
}
