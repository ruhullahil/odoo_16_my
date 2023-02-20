# -*- coding: utf-8 -*-
# from odoo import http


# class NewMicroCredit(http.Controller):
#     @http.route('/new_micro_credit/new_micro_credit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_micro_credit/new_micro_credit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_micro_credit.listing', {
#             'root': '/new_micro_credit/new_micro_credit',
#             'objects': http.request.env['new_micro_credit.new_micro_credit'].search([]),
#         })

#     @http.route('/new_micro_credit/new_micro_credit/objects/<model("new_micro_credit.new_micro_credit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_micro_credit.object', {
#             'object': obj
#         })
