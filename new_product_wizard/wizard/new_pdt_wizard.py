from odoo import api, fields, models


class NewProductWizard(models.TransientModel):
    _name = "new.product.wizard"
    _description = "New Product"

    product_id = fields.Many2one('product.product', string='Product')
    quantity = fields.Float(string='Quantity', default=1.0)
    unit_price = fields.Float(string='Unit Price')

    def add_product_to_order(self):
        sale_order_id = self.env.context.get('active_id')
        sale_order = self.env['sale.order'].browse(sale_order_id)
        selected_product = self.product_id

        sale_order.write({
            'order_line': [(0, 0, {
                'product_id': selected_product.id,
                'name': selected_product.name,
                'product_uom_qty': self.quantity,
                'price_unit': self.unit_price or selected_product.list_price,
            })]
        })

        return {'type': 'ir.actions.act_window_close'}
