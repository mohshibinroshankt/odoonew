from odoo import api, fields, models


class NewChatterWizard(models.TransientModel):
    _name = "new.chatter.wizard"
    _description = "New chatter msg"

    new_msg = fields.Text(string="New Msg")

    def add_msg_to_chatter(self):
        self.ensure_one()
        active_model = self._context.get('active_model')
        active_id = self._context.get('active_id')

        sale_order = self.env[active_model].browse(active_id)

        sale_order.message_post(body=self.new_msg)
