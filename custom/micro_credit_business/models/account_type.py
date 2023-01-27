from odoo import fields, models, api


class AccountType(models.Model):
    _name = 'partner.Account.type'
    _description = 'AccountType'

    name = fields.Char()
    validity = fields.Integer()
