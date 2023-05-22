from odoo import api, fields, models


class CreatePayInSo(models.TransientModel):
    _name = "create.payment.wizard"

    journal_id = fields.Many2one('account.journal')
    payment_method_line_id = fields.Many2one('account.payment.method.line', readonly=False, store=True)
    date = fields.Date(string='Payment Date', required=True,  default=fields.Date.context_today)
    currency_id = fields.Many2one('res.currency', string='Currency')
    # amount = fields.Float(string='Amount')
    amount = fields.Monetary(currency_field='currency_id', store=True, readonly=False)

    def action_create_pay_so(self):
        active_ids = self._context.get('active_ids', [])
        sale_orders = self.env['sale.order'].browse(active_ids)

        for order in sale_orders:
            payment_vals = {
                'payment_type': 'inbound',
                'partner_type': 'customer',
                'partner_id': order.partner_id.id,
                'amount': order.amount_total,
                'date': self.date,
            }
            payment = self.env['account.payment'].create(payment_vals)
            payment.action_post()

        return {'type': 'ir.actions.act_window_close'}
