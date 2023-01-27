from odoo import fields, models, api


class AccountCreditLoan(models.Model):
    _name = 'account.credit.loan'
    _description = 'Description'
    _rec_name = 'account_id'

    account_id = fields.Many2one('partner.credit.account',required=True)
    duration_type_id = fields.Many2one('partner.account.duration.type', required=True)
    collection_type_id = fields.Many2one('partner.collection.duration.type', required=True)
    default_interest_rate = fields.Float(related='duration_type_id.interest_rate_after_default')
    interest_rate = fields.Float(related='duration_type_id.interest_rate')
    amount_disbust = fields.Float(string='Loan Amount' ,required=True)
    amount_payable = fields.Float(string='Payable amount',compute='_get_account_payable',store=True)
    date = fields.Date(required=True)

    @api.depends('amount_disbust','duration_type_id','duration_type_id.interest_rate')
    def _get_account_payable(self):
        for rec in self:
            rec.amount_payable = 0
            if rec.amount_disbust and rec.duration_type_id and rec.duration_type_id.interest_rate:
                rec.amount_payable = rec.amount_disbust * (1+rec.duration_type_id.interest_rate/100)
