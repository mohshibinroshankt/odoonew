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


    # @api.onchange('delivery_charges')
    # def onchange_delivery_charges(self):
    #     if self.delivery_charges:
    #         last_order_line = self.order_line.sorted(key=lambda l: l.sequence, reverse=True)[0]
    #
    #         delivery_product = self.env['product.product'].create({
    #             'name': 'Delivery Charges',
    #             'list_price': 10.00,
    #             'type': 'service',  # set product type to service to avoid stock management
    #         })
    #
    #

    #         order_line_vals = {
    #             'order_id': self.id,
    #             'name': 'Delivery Charges',
    #             # 'product_template_id': self.product_new.id,
    #             'product_id': delivery_product.id,
    #             'product_uom_qty': 1.0,
    #             'price_unit': self.delivery_charges,
    #             'sequence': last_order_line.sequence + 1,
    #
    #         }
    #
    #         new_order_line = self.env['sale.order.line'].create(order_line_vals)
    #         self.order_line += new_order_line

    # @api.onchange('delivery_charges')
    # def onchange_delivery_charges(self):
    #     if self.delivery_charges:
    #         last_order_line = self.order_line.sorted(key=lambda l: l.sequence, reverse=True)[0]
    #
    #         # Create a dictionary to hold the values for the new order line
    #         order_line_vals = {
    #             'order_id': self.id,
    #             'name': 'Delivery Charges',
    #             'price_unit': self.delivery_charges,
    #             'product_uom_qty': 1.0,
    #             'sequence': last_order_line.sequence + 1,
    #             # Set the required fields for the sale order line
    #             'product_id': False,
    #             'product_uom': False,
    #         }

    # Create a new sale order line using the values dictionary
    # order_line = self.env['sale.order.line'].new(order_line_vals)

    # Call the _onchange_product_id method to set the remaining fields

    # @api.onchange('delivery_charges')
    # def onchange_delivery_charges(self):
    #     if self.delivery_charges:
    #         last_order_line = self.order_line.sorted(key=lambda l: l.sequence, reverse=True)[0]
    #
    #         order_line = self.env['sale.order.line'].new({
    #             'order_id': self.id,
    #             'name': 'Delivery Charges',
    #             'product_template_id': False,
    #             'price_unit': self.delivery_charges,
    #             'product_uom_qty': 1.0,
    #             'tax_id': False,
    #             'sequence': last_order_line.sequence + 1,
    #
    #         })
