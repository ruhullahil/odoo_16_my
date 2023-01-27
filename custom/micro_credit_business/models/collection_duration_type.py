from odoo import fields, models, api


class CollectionDurationType(models.Model):
    _name = 'partner.collection.duration.type'
    _description = 'CollectionDurationType'

    name = fields.Char()
    description = fields.Text()
    duration_in_days = fields.Integer()
