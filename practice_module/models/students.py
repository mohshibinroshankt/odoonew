from odoo import api, fields, models


class CollegeStudents(models.Model):
    _name = 'college.students'
    _description = "class 001"

    name = fields.Char(string='Name', required=True, tracking=True)
    branch = fields.Char(string='Branch')
    age = fields.Integer(string='age', tracking=True)
    address = fields.Text(string='Address', tracking=True)
    date_of_birth = fields.Date(string='Date of birth', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender",
                              tracking=True)
