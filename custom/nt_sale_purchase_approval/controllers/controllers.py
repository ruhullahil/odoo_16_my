# -*- coding: utf-8 -*-
from odoo import http


class NtSalePurchaseApproval(http.Controller):
    @http.route('/api/hellow_world/',auth='public', methods=['GET'])
    def hellow_world(self):
        return 'hellow world'
    # @http.route('/nt_sale_purchase_approval/nt_sale_purchase_approval', auth='public')
    # def index(self, **kw):
    #     return "Hello, world"
    #
    # @http.route('/nt_sale_purchase_approval/nt_sale_purchase_approval/objects', auth='public')
    # def list(self, **kw):
    #     return http.request.render('nt_sale_purchase_approval.listing', {
    #         'root': '/nt_sale_purchase_approval/nt_sale_purchase_approval',
    #         'objects': http.request.env['nt_sale_purchase_approval.nt_sale_purchase_approval'].search([]),
    #     })
    #
    # @http.route('/nt_sale_purchase_approval/nt_sale_purchase_approval/objects/<model("nt_sale_purchase_approval.nt_sale_purchase_approval"):obj>', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('nt_sale_purchase_approval.object', {
    #         'object': obj
    #     })
