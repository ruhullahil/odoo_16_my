# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class micro_credit_business(models.Model):
#     _name = 'micro_credit_business.micro_credit_business'
#     _description = 'micro_credit_business.micro_credit_business'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
