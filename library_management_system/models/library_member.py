from odoo import fields, models, api


class LibraryMember(models.Model):
    _name = "library.member"
    _description = "Library Member"

    name = fields.Char(string="Name", required=True)
    Date_of_birth = fields.Date(string="Date Of Birth")
    # age = fields.Integer(string="Age")
    mobile_number = fields.Char()
    e_mail = fields.Char(string="E-mail")
   
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("other", "Other")], string="Gender"
    )
    membership_type = fields.Selection(
        [("student", "Student"), ("faculty", "Faculty"), ("staff", "Staff")],
        string="Membership Type",
    )
    joining_date = fields.Date(string="Joining Date", default=fields.Date.today)
    image = fields.Binary()
    sales_order = fields.One2many("library.sales", "member_id", string="Sales Order")
    age = fields.Integer(
        string="Age",
    )
    street = fields.Char(string="Address")
    street2 = fields.Char()
    city = fields.Char(string='City')
    country_id = fields.Many2one(
        string='Country',
        comodel_name='res.country',
        ondelete='restrict',  # This line ensures that you cannot delete a country if it's used in your records
    )
    state_id = fields.Many2one(
        string='State',
        comodel_name='res.country.state',
        domain="[('country_id', '=', country_id)]",  # This ensures that only states of the selected country are available
    )
    zip = fields.Char(string='Zip')
    new_address = fields.Char(string="Member Adress" , compute="_compute_new_address" , store=True)


    @api.depends('street','street2','city','country_id','state_id','zip')
    def _compute_new_address(self):
        for address in self:
            address.new_address=f'{address.street},{address.street2},{address.city},{address.country_id.name},{address.state_id.name},{address.zip}'

    @api.onchange("Date_of_birth")
    def _onchange_vehicle(self):
        today = fields.Date.today()
        if self.Date_of_birth:
            birth_date = datetime.combine(self.Date_of_birth, datetime.min.time())
            delta = today - birth_date.date()
            self.age = delta.days // 365