{
    'name': 'new product wizard',
    'website': 'machinser.com',
    'summary': 'This will add new product from a wizard',
    'author': 'msrkt',
    'depends': ['sale', 'base', 'account'],
    'data': [
        'views/sale_order_view_pdt.xml',
        'views/new_invoice_line_view.xml',
        'wizard/new_pdt_wizard_view.xml',
        'security/ir.model.access.csv',

    ],
    'demo': []
}
