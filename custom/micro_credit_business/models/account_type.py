from odoo import fields, models, api


class AccountType(models.Model):
    _name = 'partner.account.type'
    _description = 'AccountType'
    _order = 'sequence,id '

    name = fields.Char()
    validity = fields.Integer()
    description = fields.Text()
    sequence = fields.Integer()
