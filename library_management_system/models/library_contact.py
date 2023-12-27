
from odoo import models, fields, api


class LibraryContact(models.Model):

    _inherit = 'res.partner'

    library_mail = fields.Char(copy=False , string="Library Mail")



