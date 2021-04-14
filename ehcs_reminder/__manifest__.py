# -*- coding: utf-8 -*-
{
    'name': 'Reminder',
    'author': 'ERP Harbor Consulting Services',
    'category': 'Reminder',
    'summary': 'Reminder',
    'website': 'http://www.erpharbor.com',
    'version': '14.0.1.0.0',
    'description': """
        Reminder
    """,
    'depends': [
        'calendar'
    ],
    'data': [
        'views/reminder_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
