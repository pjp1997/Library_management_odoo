
{
    'name': "library management system",
    'license': "LGPL-3",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",
       'category': 'Uncategorized',
    'version': '0.1',
     'depends': ['base','mail'],
     'data': [
        'security/ir.model.access.csv',
        'views/library_member_view.xml',
        'views/library_books_view.xml',
        'views/library_sales_view.xml',
        'data/library_books_sequence.xml',
        'data/library_sales_sequence.xml',
        'views/library_contact_view.xml',
        'data/library_sales_order_number.xml',
    ],
     'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,

}