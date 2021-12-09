# -*- coding: utf-8 -*-
{
    'name' : 'School Management',
    'version' : '1.0',
    'summary': 'School Management Software',
    'sequence': 10,
    'description': """School Management Software""",
    'category': 'Sales/Sales',
    'website': 'https://www.samatashikshyaniketan.com',
    'depends' : ['base','web','report_xlsx','nepali_datepicker'],
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        # 'views/access.xml',
        'views/student_view.xml',
        'views/section_view.xml',
        'report/report.xml',
        'report/student_card.xml'
        
    ],
    "assets": {
        "web.assets_backend": [
            "samata_school/static/src/js/students.js"
        ]
    },
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
