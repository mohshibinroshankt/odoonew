from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    sale_order_line_quantity = fields.Float(
        string='Invo Quantity',
        compute='_compute_sale_order_line_quantity',
        readonly=True,
        store=True
    )

    @api.depends('sale_line_ids.product_uom_qty')
    def _compute_sale_order_line_quantity(self):
        for line in self:
            quantities = line.sale_line_ids.mapped('product_uom_qty')
            line.sale_order_line_quantity = sum(quantities)






            # line.sale_order_line_quantity = quantities[0] if quantities else 0.0
            # line.sale_order_line_quantity = sum(line.sale_line_ids.mapped('product_uom_qty'))

    # @api.depends('sale_line_ids')
    # def _compute_sale_order_line_quantity(self):
    #     for line in self:
    #
    #         for sale_line in line.sale_line_ids:
    #             sale_order_line_quantity += sale_line.product_uom_qty
    #         line.sale_order_line_quantity = sale_order_line_quantity

    # sale_order_line_quantity = fields.Float(
    #     string='Sale Order Line Quantity',
    #     compute='_compute_sale_order_line_quantity',
    #     readonly=True,
    #     store=True
    # )
    #
    # @api.depends('sale_line_ids')
    # def _compute_sale_order_line_quantity(self):
    #     for line in self:
    #         if line.sale_line_ids:
    #             line.sale_order_line_quantity = line.sale_line_ids.product_uom_qty

    # qty_sold = fields.Float(compute='_compute_qty_sold', store=True)
    #
    # def _compute_qty_sold(self):
    #     for line in self:
    #         sale_line = self.env['sale.order.line'].search([('id', '=', line.sale_line_id.id)])
    #         line.qty_sold = sale_line.quantity if sale_line else 0.0

    # sale_line_id = fields.Many2one('sale.order.line', string='Sale Order Line')
    # qty_sold = fields.Float(compute='_compute_qty_sold', store=True)
    #
    # def _compute_qty_sold(self):
    #     for line in self:
    #         sale_line = self.env['sale.order.line'].search([('id', '=', line.sale_line_id.id)])
    #         line.qty_sold = sale_line.quantity if sale_line else 0.0
