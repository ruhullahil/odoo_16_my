# -*- coding: utf-8 -*-
# from odoo import http


# class MimeTask(http.Controller):
#     @http.route('/mime_task/mime_task', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mime_task/mime_task/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mime_task.listing', {
#             'root': '/mime_task/mime_task',
#             'objects': http.request.env['mime_task.mime_task'].search([]),
#         })

#     @http.route('/mime_task/mime_task/objects/<model("mime_task.mime_task"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mime_task.object', {
#             'object': obj
#         })
