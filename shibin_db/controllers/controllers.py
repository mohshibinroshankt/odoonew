# -*- coding: utf-8 -*-
# from odoo import http


# class ShibinDb(http.Controller):
#     @http.route('/shibin_db/shibin_db', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shibin_db/shibin_db/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('shibin_db.listing', {
#             'root': '/shibin_db/shibin_db',
#             'objects': http.request.env['shibin_db.shibin_db'].search([]),
#         })

#     @http.route('/shibin_db/shibin_db/objects/<model("shibin_db.shibin_db"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shibin_db.object', {
#             'object': obj
#         })
