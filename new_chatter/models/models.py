# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class new_chatter(models.Model):
#     _name = 'new_chatter.new_chatter'
#     _description = 'new_chatter.new_chatter'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
