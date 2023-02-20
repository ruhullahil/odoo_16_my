from odoo import fields, models, api


class CreditPaymentType(models.Model):
    _name = 'credit.payment.type'
    _description = 'CreditPaymentType'

    name = fields.Char()
