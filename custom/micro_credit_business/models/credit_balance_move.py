from odoo import fields, models, api


class CreditBalanceMove(models.Model):
    _name = 'credit.balance.move'
    _description = 'CreditBalanceMove'

    name = fields.Char()
    date = fields.Date(required=True)
    active = fields.Boolean()
    state = fields.Selection([
        ('draft','Draft'),
        ('posted','Posted')
    ])
    payment_id = fields.Many2one('account.credit.payment')
    entry_id = fields.Many2one('account.credit.entry')
    amount = fields.Float(required=True)



