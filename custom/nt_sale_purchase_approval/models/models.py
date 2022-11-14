# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class nt_sale_purchase_approval(models.Model):
#     _name = 'nt_sale_purchase_approval.nt_sale_purchase_approval'
#     _description = 'nt_sale_purchase_approval.nt_sale_purchase_approval'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
