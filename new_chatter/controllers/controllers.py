# -*- coding: utf-8 -*-
# from odoo import http


# class NewChatter(http.Controller):
#     @http.route('/new_chatter/new_chatter', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_chatter/new_chatter/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_chatter.listing', {
#             'root': '/new_chatter/new_chatter',
#             'objects': http.request.env['new_chatter.new_chatter'].search([]),
#         })

#     @http.route('/new_chatter/new_chatter/objects/<model("new_chatter.new_chatter"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_chatter.object', {
#             'object': obj
#         })
