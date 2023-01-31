from odoo import fields, models, api


class CreditBalanceMove(models.Model):
    _name = 'credit.balance.move'
    _description = 'CreditBalanceMove'

    name = fields.Char(
        'Name', copy=False, required=True, readonly=True,
        default=lambda self: self.env['ir.sequence'].next_by_code('credit.balance.move'))
    date = fields.Date(required=True,default=fields.date.today())
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('posted', 'Posted')
    ], default='draft', required=True)
    payment_id = fields.Many2one('account.credit.payment')
    entry_id = fields.Many2one('account.credit.entry')
    loan_id = fields.Many2one('account.credit.loan')
    amount = fields.Float(required=True)

    def btn_set_post(self):
        for rec in self:
            rec.state = 'posted'
