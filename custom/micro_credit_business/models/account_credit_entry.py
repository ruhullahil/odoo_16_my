from odoo import fields, models, api


class AccountCreditEntry(models.Model):
    _name = 'account.credit.entry'
    _description = 'AccountCreditEntry'

    name = fields.Char()
    entry_type_id = fields.Char('credit.entry.type', domain="[('active','=',True)]", required=True)
    date = fields.Date(required=True, default=fields.date.today())
    amount = fields.Float(required=True)
    balance_move_id = fields.Many2one('credit.balance.move')
