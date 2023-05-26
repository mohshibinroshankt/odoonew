from odoo import api, fields, models


class CreatePayInSo(models.TransientModel):
    _name = "create.payment.wizard"

    journal_id = fields.Many2one('account.journal')
    payment_method_line_id = fields.Many2one('account.payment.method.line', readonly=False, store=True)
    date = fields.Date(string='Payment Date', required=True, default=fields.Date.context_today)
    currency_id = fields.Many2one('res.currency', string='Currency')
    amount = fields.Monetary(currency_field='currency_id', store=True, readonly=False)
    sale_order_id = fields.Many2one('sale.order')

    def action_create_pay_so(self):
        active_ids = self._context.get('active_ids', [])
        sale_orders = self.env['sale.order'].browse(active_ids)

        for order in sale_orders:
            payment_vals = {
                'payment_type': 'inbound',
                'partner_type': 'customer',
                'partner_id': order.partner_id.id,
                'amount': self.amount,
                'date': self.date,
            }
            payment = self.env['account.payment'].create(payment_vals)
            payment.action_post()

            order.paid = self.amount

        return {'type': 'ir.actions.act_window_close'}

    # @api.depends('sale_order_id')
    # def _compute_paid(self):
    #     for wizard in self:
    #         wizard.paid = wizard.sale_order_id.paid
    #
    # @api.depends('amount', 'sale_order_id')
    # def _compute_balance(self):
    #     for wizard in self:
    #         wizard.balance_pay = wizard.sale_order_id.amount_total - wizard.paid
