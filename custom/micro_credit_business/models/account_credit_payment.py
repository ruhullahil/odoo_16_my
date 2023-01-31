from odoo import fields, models, api


class AccountCreditPayment(models.Model):
    _name = 'account.credit.payment'
    _description = 'AccountCreditPayment'
    _rec_name = 'account_id'

    account_id = fields.Many2one('partner.credit.account')
    loan_id = fields.Many2one('account.credit.loan')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('posted', 'posted'),

    ], default='draft')
    date = fields.Date(required=True)
    amount_to_pay = fields.Float()
    amount_paid = fields.Float()
    account_payable_ids = fields.Many2many('account.credit.payable')
    manager_id = fields.Many2one('res.user', required=True, default=lambda self: self.env.user.id)
    credit_move_id = fields.Many2one('credit.balance.move')

    def button_post(self):
        for rec in self:
            rec.state = 'posted'
