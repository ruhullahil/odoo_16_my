from odoo import fields, models, api


class AccountDurationType(models.Model):
    _name = 'partner.account.duration.type'
    _description = 'AccountDurationType'
    _order = 'sequence , id'

    name = fields.Char(required=True)
    description = fields.Text()
    duration_in_days = fields.Integer(required=True)
    interest_rate_after_default = fields.Float( required=True)
    interest_rate = fields.Float(required=True)
    sequence = fields.Integer()

