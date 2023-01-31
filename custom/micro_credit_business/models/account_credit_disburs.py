from odoo import fields, models, api


class AccountCreditLoan(models.Model):
    _name = 'account.credit.loan'
    _description = 'Description'
    _rec_name = 'account_id'

    account_id = fields.Many2one('partner.credit.account', required=True)
    duration_type_id = fields.Many2one('partner.account.duration.type', required=True)
    collection_type_id = fields.Many2one('partner.collection.duration.type', required=True)
    default_interest_rate = fields.Float(store=True,
                                         string='Interest Rate After Not Paid in in Time', required=True)
    interest_rate = fields.Float(store=True, required=True)
    amount_loan = fields.Float(string='Loan Amount', required=True)
    amount_payable = fields.Float(string='Payable amount', compute='_get_account_payable', store=True)
    date = fields.Date(required=True)
    is_full_paid = fields.Boolean(default=False)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('posted', 'Posted')
    ], default='draft')
    payment_ids = fields.One2many('account.credit.payment', 'loan_id')
    installment_count = fields.Integer(required=True)
    installment_amount = fields.Float(compute='_get_installment_amount', store=True)

    @api.onchange('duration_type_id', 'collection_type_id')
    def _set_interest_rate(self):
        if self.duration_type_id and self.collection_type_id:
            interestrate = self.env['interest.instalment.conf'].sudo().search(
                [('duration_type_id', '=', self.duration_type_id.id),
                 ('collection_type_id', '=', self.collection_type_id.id)], limit=1)
            if interestrate:
                self.interest_rate = interestrate.interest_rate
                self.installment_count = interestrate.installment_count
                self.default_interest_rate = interestrate.interest_rate_after_default
        else:
            self.interest_rate = None
            self.installment_count = None
            self.default_interest_rate = None

    @api.depends('amount_loan', 'duration_type_id', 'interest_rate')
    def _get_account_payable(self):
        for rec in self:
            rec.amount_payable = 0
            if rec.amount_loan and rec.duration_type_id and rec.interest_rate:
                rec.amount_payable = rec.amount_loan * (1 + rec.interest_rate / 100)

    @api.depends('amount_loan', 'installment_count', 'amount_payable')
    def _get_installment_amount(self):
        for rec in self:
            if rec.amount_loan and rec.installment_count and rec.amount_payable:
                rec.installment_amount = rec.amount_payable / rec.installment_count if rec.amount_payable and rec.installment_count else 0.0

    def _prepare_balance_move(self):
        self.ensure_one()
        val = {
            'date': self.date,
            'amount': self.amount_loan * -1,

        }
        return val

    def btn_posted(self):
        for rec in self:
            if rec.state not in ('posted'):
                rec.account_id.last_disbust_id = rec.id
                rec.state = 'posted'
                balance_move = self.env['credit.balance.move'].sudo().create(rec._prepare_balance_move())
                if balance_move:
                    balance_move.loan_id = rec.id
                    balance_move.btn_set_post()
