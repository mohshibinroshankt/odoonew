from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    quantity_total = fields.Float(string='Total Quantity', compute='_compute_product_quantity_total', readonly=False,
                                  store=True)

    @api.depends('order_line.product_uom_qty')
    def _compute_product_quantity_total(self):
        for order in self:
            order.quantity_total = sum(order.order_line.mapped('product_uom_qty'))

    def action_open_pdt(self):
        return {
            'name': "New Product",
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'views': [(False, 'form')],
            'res_model': "new.product.wizard",
            'target': 'new',
        }
