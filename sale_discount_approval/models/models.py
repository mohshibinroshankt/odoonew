from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_confirmable = fields.Boolean(string='Is Confirmable', compute='_compute_is_confirmable')
    my_custom_field = fields.Char(string='My Custom Field')

    login_id = fields.Char(string='Login Id')

    def action_open_tc(self):
        return {
            'name': "T&C Wizard",
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'views': [(False, 'form')],
            'res_model': "terms.condition.wizard",
            'target': 'new',
            'context': {'default_sale_order_id': self.id}
        }

    # _sql_constraints = [
    #     ('sale_order_conditional_reequired',
    #      "CHECK(login_id IS NOT NULL)",
    #      "login id cannot be zero"),
    # ]

    # _sql_constraints = [
    #     ('check_login_id_field', "CHECK(login_id != abc )", "This Field cannot be abc")
    # ]

    @api.depends('amount_total', 'partner_id')
    def _compute_is_confirmable(self):
        for order in self:
            if order.amount_total > 100 and not order.env.user.has_group(
                    'sale_order_discount_approval_odoo.approval_user_user'):
                order.is_confirmable = True
            else:
                order.is_confirmable = False

    def _prepare_invoice(self, ):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals.update({
            'my_custom_field': self.my_custom_field,
        })
        return invoice_vals

    # def action_new_tandc(self):
    #     return

    #     {
    #     'name': 'New T&C',
    #     'type': 'ir.actions.act_window',
    #     'view_mode': 'form',
    #     'res_model': 'terms.condition.wizard',
    #     'target': 'new',
    #
    # }


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    custom_field = fields.Char(string='Custom Field')

    def _prepare_invoice_line(self, **optional_values):
        res = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
        res.update({'custom_field': self.custom_field})
        return res
