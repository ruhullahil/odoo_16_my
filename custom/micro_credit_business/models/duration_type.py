from odoo import fields, models, api


class AccountDurationType(models.Model):
    _name = 'partner.account.duration.type'
    _description = 'AccountDurationType'

    name = fields.Char()
    description = fields.Text()
    duration_in_days = fields.Integer()
    interest_rate_after_default = fields.Float()
    interest_rate = fields.Float()

