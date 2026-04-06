{
    'name': 'Student API',
    'version': '1.0',
    'summary': 'Student API',
    'sequence': 10,
    'description': """
    Student API
    """,
    'category': 'Education',
    'depends': ['student_management', 'fastapi'],
    'data': [
        'data/jwt_validator.xml',
        'data/fastapi_endpoint.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
    'author': 'LongDT',
    'license': 'LGPL-3',
}
