from odoo import api, fields, models


class CancelOrdersWizard(models.TransientModel):
    _name = "cancel.orders.wizard"
    _description = "Cancel orders"

    order_id = fields.Many2one('myown.orders', string='Order Id')

    def action_cancel(self):
        return
