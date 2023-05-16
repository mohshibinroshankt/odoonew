# -*- coding: utf-8 -*-
# from odoo import http


# class SaleDiscountApproval(http.Controller):
#     @http.route('/sale_discount_approval/sale_discount_approval', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_discount_approval/sale_discount_approval/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_discount_approval.listing', {
#             'root': '/sale_discount_approval/sale_discount_approval',
#             'objects': http.request.env['sale_discount_approval.sale_discount_approval'].search([]),
#         })

#     @http.route('/sale_discount_approval/sale_discount_approval/objects/<model("sale_discount_approval.sale_discount_approval"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_discount_approval.object', {
#             'object': obj
#         })
