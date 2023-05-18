from odoo import api, fields, models


# class SaleOrderLine(models.Model):
#     # _name = 'table.inherited'
#     _inherit = 'sale.order.line'
#     serial_number = fields.Integer(string='Serial No', readonly=True, default=1)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    serial_number = fields.Integer(string='Serial No', store=True, required=True, compute='_compute_serial_number')

    #
    # @api.model
    # def create(self, vals):
    #     vals['serial_number'] = self.search_count([]) + 1
    #     return super(SaleOrderLine, self).create(vals)

    # def create(self, vals):
    #     vals['serial_number'] = self.env['ir.sequence'].next_by_code('sale.order.line') or 0
    #     return super(SaleOrderLine, self).create(vals)
    # @api.depends('order_id.order_line')
    # def _compute_line_number(self):
    #     for line in self:
    #         line.serial_number = str(line.order_id.order_line.ids.index(line.id) + 1)
    @api.depends('sequence', 'order_id')
    def _compute_serial_number(self):
        for order_line in self:
            if not order_line.serial_number:
                serial_no = 1
                for line in order_line.mapped('order_id').order_line:
                    line.serial_number = serial_no
                    serial_no += 1



