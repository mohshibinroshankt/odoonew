from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    paid_amount = fields.Monetary(string='Paid', compute='_compute_paid', store=True)
    balance_pay_amount = fields.Monetary(string='Balance', compute='_compute_balance', store=True)

    def _compute_paid(self):
        for order in self:
            payment_idss = self.env['account.payment'].search(
                [('sale_order_id', '=', order.id), ('state', 'in', ['draft', 'posted'])])
            amount_paid = sum(payment_idss.mapped('amount'))
            order.paid_amount = amount_paid

    @api.depends('amount_total', 'paid_amount')
    def _compute_balance(self):
        for order in self:
            order.balance_pay_amount = order.amount_total - order.paid_amount

    def action_open_rp(self):
        if self.state == 'sale':
            return {
                'name': "Create Payment",
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'views': [(False, 'form')],
                'res_model': "create.payment.wizard",
                'target': 'new'
            }

