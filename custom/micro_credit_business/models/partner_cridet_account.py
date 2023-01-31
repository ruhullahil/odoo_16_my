from odoo import fields, models, api


class PartnerCreditAccount(models.Model):
    _name = 'partner.credit.account'
    _description = 'PartnerCreditAccount'

    name = fields.Char(string='Account Id', required=True)
    partner_id = fields.Many2one('res.partner', required=True)
    account_type_id = fields.Many2one('partner.account.type', required=True)
    territory_id = fields.Many2one('res.territory', related='partner_id.territory_id')
    account_manager = fields.Many2one('res.users', related='partner_id.user_id',string='Account Manager')
    total_payed = fields.Float(compute='_get_total_amount')
    total_received = fields.Float(compute='_get_total_amount')
    book_no = fields.Char()
    remarks = fields.Text()
    description = fields.Text()
    risk_factor = fields.Float()
    last_disbust_id = fields.Many2one('account.credit.loan')
    last_disbust_date = fields.Date(related='last_disbust_id.date')
    last_disbursed_amount = fields.Float(related='last_disbust_id.amount_loan')
    last_disbursed_paid = fields.Float(compute='get_last_disbursed_info',string='Last Loan Paid')
    last_disbursed_remain = fields.Float(compute='get_last_disbursed_info',string='Last Loan Remain')
    last_collection_date = fields.Date()
    last_collection_user = fields.Many2one('res.users')
    payment_ids = fields.One2many('account.credit.payment', 'account_id')
    loan_ids = fields.One2many('account.credit.loan', 'account_id')

    @api.depends('partner_id')
    def _get_total_amount(self):
        for rec in self:
            rec.total_payed = sum(rec.loan_ids.mapped('amount_loan')) or 0.0
            rec.total_received = sum(
                rec.payment_ids.filtered(lambda l: l.state == 'posted').mapped('amount_paid')) or 0.0

    @api.depends('last_disbust_id')
    def get_last_disbursed_info(self):
        for rec in self:
            rec.last_disbursed_paid = sum(
                rec.payment_ids.filtered(lambda l: l.loan_id == rec.last_disbust_id.id and l.state == 'posted').mapped(
                    'amount_paid')) if rec.last_disbust_id else 0.0
            rec.last_disbursed_remain = (rec.last_disbust_id.amount_payable - sum(
                rec.payment_ids.filtered(lambda l: l.loan_id == rec.last_disbust_id.id and l.state == 'posted').mapped(
                    'amount_paid'))) if rec.last_disbust_id else 0.0
    def name_get(self):
        res = []
        for partner in self:
            name = "%s (%s-%s)" % (partner.name, partner.partner_id.name,partner.partner_id.partner_code)
            res += [(partner.id, name)]
        return res

