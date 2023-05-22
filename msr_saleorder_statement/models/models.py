from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    paid = fields.Monetary(string='Paid', compute='_compute_paid', store=True)
    balance_pay = fields.Monetary(string='Balance', compute='_compute_balance', store=True)

    def _compute_paid(self):
        for order in self:
            payment_idss = self.env['account.payment'].search(
                [('sale_order_id', '=', order.id), ('state', 'in', ['draft', 'posted'])])
            amounty = sum(payment_idss.mapped('amount'))
            order.paid = amounty

    @api.depends('amount_total', 'paid')
    def _compute_balance(self):
        for order in self:
            order.balance_pay = order.amount_total - order.paid

    def action_open_rp(self):
        return {
            'name': "Create Payment",
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'views': [(False, 'form')],
            'res_model': "create.payment.wizard",
            'target': 'new'
        }

        # return {
        #     'name': _('Register Payment'),
        #     'res_model': 'account.payment.register',
        #     'view_mode': 'form',
        #     'context': {
        #         'active_model': 'sale.order',
        #         'active_id': self.id,
        #     },
        #     'target': 'new',
        #     'type': 'ir.actions.act_window',
        # }
