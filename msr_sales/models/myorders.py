from odoo import api, fields, models


class MyownOrders(models.Model):
    _name = "myown.orders"
    _inherit = 'mail.thread'
    _description = "My orders"

    order_item = fields.Many2one('myown.sales', string='Order Item')
    gender = fields.Selection(related='order_item.gender')
    order_time = fields.Datetime(string='Order time')
    order_date = fields.Date(string='Order Date')


