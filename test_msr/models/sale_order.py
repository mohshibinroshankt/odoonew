from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    vat_number = fields.Char(string='Vat Number', copy=False, size=None)
    confirmed_user_id = fields.Many2one('res.users', string='Confirmed User')
    partner_name = fields.Text(string='Partners')
    serial_number = fields.Integer(string='Serial No', default=0, required=True)

    delivery_charges = fields.Float(string='Delivery Charges')
    order_line = fields.One2many('sale.order.line', 'order_id', string='Order Lines', copy=True, readonly=False)

    @api.onchange('delivery_charges')
    def onchange_delivery_charges(self):
        if self.delivery_charges:
            last_order_line = self.order_line.sorted(key=lambda l: l.sequence, reverse=True)[0]

            order_line = self.env['sale.order.line'].new({
                'order_id': self.id,
                'name': 'Delivery Charges',
                'product_template_id': False,
                'price_unit': self.delivery_charges,
                'product_uom_qty': 1.0,
                'tax_id': False,
                'sequence': last_order_line.sequence + 1,

            })

# @api.onchange('delivery_charges')
# def onchange_delivery_charges(self):
#     if self.delivery_charges:
#         order_line = self.env['sale.order.line'].new({
#             'order_id': self.id,
#             'product_template_id': 'Delivery Charges',
#             'name': 'Delivery Charges',
#             'product_id': False,
#             'price_unit': self.delivery_charges,
#             'product_uom_qty': 1.0,
#             'tax_id': False,
#         })

# class SaleOrderLine(models.Model):
#     # _name = 'table.inherited'
#     _inherit = 'sale.order.line'
#     serial_number = fields.Integer(string='Serial No', readonly=True, default=1)
#
#
# class SaleOrderLineView(models.Model):
#     _inherit = 'sale.order.line'
#
#
# # @api.model
# def create(self, vals):
#     vals['serial_number'] = self.search_count([]) + 1
#     return super(SaleOrderLineView, self).create(vals)
