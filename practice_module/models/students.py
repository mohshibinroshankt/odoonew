from odoo import api, fields, models


class CollegeStudents(models.Model):
    _name = 'college.students'
    _description = "class 001"

    name = fields.Char(string='Name', required=True )
    branch = fields.Char(string='Branch')
    age = fields.Integer(string='age' )
    address = fields.Text(string='Address')
    date_of_birth = fields.Date(string='Date of birth')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender")
