from odoo import fields, models, api


class AccountCreditPayment(models.Model):
    _name = 'account.credit.payment'
    _description = 'AccountCreditPayment'
    _rec_name = 'name'

    name = fields.Char(
        'Name', copy=False, required=True, readonly=True,
        default=lambda self: self.env['ir.sequence'].next_by_code('account.credit.payment'))
    account_id = fields.Many2one('partner.credit.account')
    loan_id = fields.Many2one('account.credit.loan')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('posted', 'posted'),

    ], default='draft')
    date = fields.Date(required=True,default=fields.date.today())
    amount_to_pay = fields.Float()
    amount_paid = fields.Float()
    account_payable_ids = fields.Many2many('account.credit.payable')
    manager_id = fields.Many2one('res.users', related='account_id.partner_id.user_id',store=True)
    credit_move_id = fields.Many2one('credit.balance.move')

    @api.onchange('account_id')
    def onchange_set_loan_id(self):
        if self.account_id:
            self.loan_id = self.account_id.last_disbust_id.id



    def _prepare_balance_move(self):
        self.ensure_one()
        val = {
            'date': self.date,
            'amount': self.amount_paid,
        }
        return val

    def btn_posted(self):
        for rec in self:
            if rec.state not in ('posted'):
                balance = rec.credit_move_id
                if not rec.credit_move_id:
                    balance = self.env['credit.balance.move'].sudo().create(rec._prepare_balance_move())
                    balance.payment_id = rec.id
                    rec.credit_move_id = balance.id
                balance.btn_set_post()
                if rec.loan_id:
                    rec.loan_id.account_id.last_collection_date = rec.date
                    rec.loan_id.account_id.last_collection_user = rec.manager_id or self.env.user.id
                rec.state = 'posted'

    def button_reset_draft(self):
        for rec in self:
            if rec.state not in ('draft'):
                rec.credit_move_id.btn_rest_draft()
                rec.state = 'draft'
