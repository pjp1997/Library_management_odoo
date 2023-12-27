from odoo import models, fields, api


class LibrarySales(models.Model):
    _name = "library.sales"
    _description = "library sales"
    _rec_name = "book_id"
    _inherit = ["mail.thread", "mail.activity.mixin", "image.mixin"]

    # transaction_id = fields.Char(string='Transaction ID', required=True, copy=False, readonly=True, index=True, default=lambda self: ('New'))
    transaction_id = fields.Char(
        string="Transation Id",
        readonly=True,
        default=lambda self: self.env["ir.sequence"].next_by_code(
            "library_sales_transaction_id"
        ),
    )
    member_id = fields.Many2one("library.member", string="Member", required=True)
    book_id = fields.Many2one(
        string="Book Name",
        comodel_name="library.book",
    )
    genre_id = fields.Char(string="Genre", related="book_id.genre", store=True)
    transaction_type = fields.Selection(
        [("borrow", "Borrow"), ("buy", "Buy")], string="Transaction Type", required=True
    )
    transaction_date = fields.Date(string="Transaction Date", default=fields.Date.today)
    # due_date = fields.Date(string="Due Date")
    return_date = fields.Date(string="Return Date", store=True)
    total_amount = fields.Float(
        string="Total Amount", compute="_compute_total_amount", store=True
    )
    member_address = fields.Char(
        string="Member Address", related="member_id.new_address", readonly=True
    )
    member_mail = fields.Char(string="Mail Id", related="member_id.e_mail")
    status = fields.Selection(
        [("draft", "Draft"), ("confirm", "Confirm"), ("paid", "Paid")],
        string="Status",
        default="draft",
    )
    payment_status= fields.Selection([("done","Done"),("unpaid","Unpaid")] , string="Payment Status" , compute="_compute_payment")
    # partner_id = fields.Many2one(
    #     comodel_name="res.partner", string="Contact", ondelete="restrict"
    # )
    books_quantity = fields.Integer(string="Books Quantity")


    sale_ids = fields.Many2many("library.book", string="buy book"
          
      )
    
    sale_order_number = fields.Char(string="Sale Order Number" , readonly=True , default=lambda self: self.env["ir.sequence"].next_by_code("library_sales_order_number"
        ))
    
    @api.depends("payment_status", "status")
    def _compute_payment(self):
        for record in self:
            if record.status == 'paid':
                record.payment_status = 'done'
            else:
                record.payment_status = 'unpaid'
    
                
    def button_done(self):
        self.status = "confirm"
        print("confirmed")

    def button_paid(self):
        self.status = "paid"
        print("paid")

    @api.depends("return_date", "transaction_date", "books_quantity")
    def _compute_total_amount(self):
        for record in self:
            if record.return_date and record.transaction_date:
                date_difference = (record.return_date - record.transaction_date).days
                record.total_amount = date_difference * 20 * record.books_quantity
            else:
                record.total_amount = 0

    @api.model
    def create(self, values):
        res = super(LibrarySales, self).create(values)
        res.book_id.total_amount = res.total_amount
        # self.env['res.partner'].create({"name": res.author})
        return res

    def write(self, values):
        res = super(LibrarySales, self).write(values)
        if 'total_amount' in values:
            for sales in self:
                sales.book_id.total_amount = values['total_amount']
                
        return res

    def action_draft(self):
        self.write({'status':'draft'})     


    # def search_button(self):
    #     partner_ids = self.env['library.sales'].search([('genre_id','=','Fiction'),('genre_id','=','Romance')])
    #     for rec in partner_ids:
    #         print(rec.genre_id)

    # def search_counter_button(self):
    #     partner_counter_ids = self.env['library.sales'].search_count(['|',('genre_id','=','Fiction'),('genre_id','=','Romance')])
    #     print(partner_counter_ids)

    # def search_browse_botton(self):
    #     partner_browser_ids = self.env['library.sales'].browse(3)
    #     for rec in partner_browser_ids:
    #         print(rec.books_quantity)

    # def copy_botton(self):
    #     partner_browser_ids = self.env['library.sales'].browse(32)
    #     partner_browser_ids.copy()

    # def unlink_botton(self):
    #     partner_browser_ids = self.env['library.sales'].browse(33)
    #     partner_browser_ids.unlink()  

    




      


  

       
        





# class BooksSaleOrderLine (model.Model):
#     _name="books.sale.order.line" 
#     _description = "Order Details"

#     book_name_id = fields.Many2one(
#         string="Book Name",
#         comodel_name="library.book",
#         store=True
#     )
#     book_author_name = fields.Char(
#         string="Product Brand Name",
#         related="book_name_id.author",
#         store=True,
#     )
#     books_quantity = fields.Integer(string="Books Quantity", required=True)

#     tax = fields.Float()
#     total_amount = fields.Float(
#         string="Total Amount", compute="_compute_total_amount", store=True
#     )
#     product_sale_management_id = fields.Many2one(
#         "my.product.sale.management", "Sale Management Id"
#     )
#     last_selling_price = fields.Float(string='Last Selling Price')












