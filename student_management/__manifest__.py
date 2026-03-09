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
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
    'assets': {

    },
    'author': 'LongDT',
    'license': 'LGPL-3',
}
