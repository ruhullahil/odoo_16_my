from odoo import fields, models, api


class CreditEntryType(models.Model):
    _name = 'credit.entry.type'
    _description = 'CreditEntryType'
    _order = 'sequence'

    name = fields.Char(required=True)
    active = fields.Boolean()
    sequence = fields.Integer()
    type = fields.Selection([('income', 'Income'), ('expense', 'Expense')])
