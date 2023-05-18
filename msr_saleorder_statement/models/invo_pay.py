from odoo import models, fields, api


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    sale_order_id = fields.Many2one('sale.order')

    @api.onchange('amount')
    def _onchange_amount(self):
        if self.sale_order_id:
            self.sale_order_id.paid += self.amount
