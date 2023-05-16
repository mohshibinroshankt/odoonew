from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    paid = fields.Monetary(string='Paid')
    balance = fields.Monetary(string='Balance')
