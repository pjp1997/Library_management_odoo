from odoo import models, fields,api


class LibraryBooks(models.Model):
    _name = "library.book"
    _description = "Library Book"
    _rec_name = "title"

    title = fields.Char(string="Title", required=True )
    author = fields.Char(string="Author")
    isbn = fields.Char(string='ISBN', readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('library_books_isbn'))
    genre = fields.Char(string="Genre")
    publication_year = fields.Integer(string="Publication Year")
    available_copies = fields.Integer(string="Available Copies")
    total_copies = fields.Integer(string="Total Copies")
    image = fields.Binary(string='Product Image')
    book_pdf = fields.Binary(string='Books Pdf')
    total_amount = fields.Float(string="Total Amount")

    @api.model
    def create(self, values):
        
        res = super(LibraryBooks, self).create(values)
        print(":rrrrrrrrrrrrrrr", res)
        self.env['res.partner'].create({"name": res.author})
        return res

    def write(self, values):

        res = super(LibraryBooks, self).write(values)
        print(":rrrrrrrrrrrrrrr", res)
        for rec in self:
            if rec.author:
                partner_ids = self.env['res.partner'].search([("name", "=", rec.author)], limit=1)
                partner_ids.write({"name": "pavan"})
        return res
    
    @api.constrains('title')
    def _constrains(self):
        for tit in self:
            if len(tit.name)<3:
                raise ValueError(_("Validation Error"))






