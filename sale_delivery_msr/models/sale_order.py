from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    delivery_charges = fields.Float(string='Delivery Charges')

    @api.onchange('delivery_charges')
    def onchange_delivery_charges(self):
        if self.delivery_charges:
            last_order_line = self.order_line.sorted(key=lambda l: l.sequence, reverse=True)[0]

            delivery_charges_product = self.env['product.product'].create({
                'name': 'Delivery Charges',
                'list_price': self.delivery_charges,
            })

            # dictionary to hold the values
            order_line_vals = {
                'order_id': self.id,
                'name': 'Delivery Charges',
                'product_id': delivery_charges_product.id,
                'product_uom_qty': 1.0,
                'price_unit': delivery_charges_product.list_price,
                'sequence': last_order_line.sequence + 1,
            }

            new_order_line = self.env['sale.order.line'].new(order_line_vals)


    
