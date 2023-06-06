{
    'name': 'msr saleorder statement',
    'author': 'shibin',
    'website': 'machinser.com',
    'summary': 'new tree view fields',
    'depends': ['mail', 'sale', 'account', ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/create_pay_in_so_view.xml',
        'views/views.xml',
        'views/account_payment_view.xml',

    ]

}
