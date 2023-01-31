from odoo import fields, models, api


class InterestAndInstallment(models.Model):
    _name = 'interest.instalment.conf'
    _description = 'InterestAndInstallment'
    _rec_name = 'duration_type_id'
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (duration_type_id,collection_type_id)', 'combination  must be unique')
    ]

    duration_type_id = fields.Many2one('partner.account.duration.type',required=True)
    collection_type_id = fields.Many2one('partner.collection.duration.type',required=True)
    interest_rate = fields.Float(required=True)
    interest_rate_after_default = fields.Float(required=True)
    installment_count = fields.Integer(required=True)
    # installment_amount = fields.Float(required=True)
