# -*- coding: utf-8 -*-

# from odoo import models, fields, api


from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_open_chatter(self):
        return {
            'name': "New CHatter",
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'views': [(False, 'form')],
            'res_model': "new.chatter.wizard",
            'target': 'new',
        }

    #     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
