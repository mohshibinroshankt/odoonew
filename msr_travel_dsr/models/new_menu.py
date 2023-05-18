from odoo import api, fields, models


class SaleOrder(models.Model):
    _name = 'msr.travel.dsr'

    name_of_customer = fields.Char(string='Name')
    contact_number = fields.Char(string='Contact Number')
    reference_by = fields.Selection([('sales person master', 'Sales person master')], string="Reference by")
    cost = fields.Integer(string='Cost')
    profit = fields.Float(string='Profit')
    supplier_name = fields.Selection([('vendor master', 'Vendor master')], string="Supplier Name")
    supplier_cost = fields.Integer(string='Supplier Cost')
