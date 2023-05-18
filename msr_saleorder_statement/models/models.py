from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    paid = fields.Monetary(string='Paid', compute='_compute_paid', store=True)
    balance_pay = fields.Monetary(string='Balance', compute='_compute_balance', store=True)

    def _compute_paid(self):
        for order in self:
            payment_ids = self.env['account.payment'].search(
                [('sale_order_id', '=', order.id), ('state', '=', 'posted')])
            amount = sum(payment_ids.mapped('amount'))
            order.paid = amount






    def _compute_balance(self):
        pass

    #     for order in self:
    #         order.balance_pay = order.amount_total - order.paid

    def action_open_rp(self):
        return {
            'name': _('Register Payment'),
            'res_model': 'account.payment.register',
            'view_mode': 'form',
            'context': {
                'active_model': 'account.move',
                'active_ids': self.ids,
            },
            'target': 'new',
            'type': 'ir.actions.act_window',
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
