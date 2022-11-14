# -*- coding: utf-8 -*-
# from odoo import http


# class CashTransfer(http.Controller):
#     @http.route('/cash_transfer/cash_transfer', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cash_transfer/cash_transfer/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cash_transfer.listing', {
#             'root': '/cash_transfer/cash_transfer',
#             'objects': http.request.env['cash_transfer.cash_transfer'].search([]),
#         })

#     @http.route('/cash_transfer/cash_transfer/objects/<model("cash_transfer.cash_transfer"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cash_transfer.object', {
#             'object': obj
#         })
