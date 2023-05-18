from odoo import api, fields, models


class TermsConditionWizard(models.TransientModel):
    _name = "terms.condition.wizard"
    _description = "New T & C"

    my_field = fields.Char(string='My Field')
    sale_order_id = fields.Many2one('sale.order')

    def action_write(self):
        self.sale_order_id.note = self.my_field
