from odoo import fields, models, api


class CollectionDurationType(models.Model):
    _name = 'partner.collection.duration.type'
    _description = 'CollectionDurationType'
    _order = 'sequence, id '

    name = fields.Char()
    description = fields.Text()
    duration_in_days = fields.Integer()
    sequence = fields.Integer()
