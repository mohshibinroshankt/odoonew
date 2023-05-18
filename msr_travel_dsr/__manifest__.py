

{
    'name': 'MSR TRAVEL',
    'summary': 'Adds a new menu item to the Sales module',
    'description': 'This module extends the Sales module and adds a new menu item',
    'version': '1.0',
    'author': 'Shibin',
    'depends': ['sale', 'base'],
    'data': [
        'views/new_menu.xml',
        'views/dsr_view.xml',
        'security/ir.model.access.csv'

    ],

}
