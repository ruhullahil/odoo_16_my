from odoo import fields, models, api


class NomineeInfo(models.Model):
    _name = 'nominee.info'
    _description = 'NomineeInfo'

    name = fields.Char()
    age = fields.Float()
    relation = fields.Char()
    ratio = fields.Float()
    sign = fields.Binary()
    partner_id = fields.Many2one('res.partner')
