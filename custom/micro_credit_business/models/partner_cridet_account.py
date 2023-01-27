from odoo import fields, models, api


class PartnerCreditAccount(models.Model):
    _name = 'partner.credit.account'
    _description = 'PartnerCreditAccount'

    name = fields.Char(string='Account Id', required=True)
    partner_id = fields.Many2one('res.partner', required=True)
    account_type_id = fields.Many2one('partner.Account.type', required=True)
    territory_id = fields.Many2one('res.territory', related='partner_id.territory_id')
    account_manager = fields.Many2one('res.users', related='partner_id.user_id')
    total_payed = fields.Float()
    total_received = fields.Float()
    book_no = fields.Char()
    remarks = fields.Text()
    description = fields.Text()
    risk_factor = fields.Float()
    last_disbust_date = fields.Date()
    last_disbursed_amount = fields.Float()
    last_disbursed_paid = fields.Float()
    last_disbursed_remain = fields.Float()
    last_collection_date = fields.Date()
    last_collection_user = fields.Many2one('res.users')
