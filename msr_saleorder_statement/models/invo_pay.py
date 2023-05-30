from odoo import models, fields, api


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    sale_order_id = fields.Many2one('sale.order')

    @api.onchange('amount', 'sale_order_id')
    def _onchange_amount(self):
        if self.sale_order_id:
            self.sale_order_id._compute_paid()
            self.sale_order_id._compute_balance()

    @api.onchange('sale_order_id')
    def _onchange_sale_order_id(self):
        if self.sale_order_id:
            # Update the form fields based on the selected sale order
            self.partner_id = self.sale_order_id.partner_id.id
            # Add other field assignments as needed
            self.amount = self.sale_order_id.amount_total

    def action_post(self):
        res = super(AccountPayment, self).action_post()
        if self.sale_order_id:
            self.sale_order_id.paid = self.amount
        return res

