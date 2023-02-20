# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class new_micro_credit(models.Model):
#     _name = 'new_micro_credit.new_micro_credit'
#     _description = 'new_micro_credit.new_micro_credit'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
