from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    my_custom_field = fields.Char(string='My Custom Field', readonly=True)

    # def _prepare_invoice_line(self, line):
    #     invoice_line = super(AccountMove, self)._prepare_invoice_line(line)
    #     invoice_line['custom_field'] = line.order_line.custom_field
    #     return invoice_line


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    custom_field = fields.Char(string='Custom Field')
