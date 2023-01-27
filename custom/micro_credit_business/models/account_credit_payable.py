from odoo import fields, models, api


class AccountCreditPayable(models.Model):
    _name = 'account.credit.payable'
    _description = 'AccountCreditPayable'

    account_id = fields.Many2one('partner.credit.account')
    loan_id = fields.Many2one('account.credit.loan')
    state = fields.Selection([
        ('not_mature', 'Not Matured'),
        ('mature', 'Matured'),
        ('paid', 'Paid'),
        ('due', 'Due'),
        ('partial', 'Partial'),

    ], default='not_mature')
    date = fields.Date(required=True)
    amount_to_pay = fields.Float()
    amount_paid = fields.Float()
    account_payment_ids = fields.Many2many('account.credit.payment')
    manager_id = fields.Many2one('res.user', required=True, default=lambda self: self.env.user.id)
