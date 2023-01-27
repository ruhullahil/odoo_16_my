# -*- coding: utf-8 -*-
# from odoo import http


# class MicroCreditBusiness(http.Controller):
#     @http.route('/micro_credit_business/micro_credit_business', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/micro_credit_business/micro_credit_business/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('micro_credit_business.listing', {
#             'root': '/micro_credit_business/micro_credit_business',
#             'objects': http.request.env['micro_credit_business.micro_credit_business'].search([]),
#         })

#     @http.route('/micro_credit_business/micro_credit_business/objects/<model("micro_credit_business.micro_credit_business"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('micro_credit_business.object', {
#             'object': obj
#         })
