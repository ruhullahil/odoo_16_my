from odoo import fields, models, api


class ResTerritory(models.Model):
    _name = 'res.territory'
    _description = 'Res Territory'

    name = fields.Char()
    area_size = fields.Float()
    manager_id = fields.Many2one('res.user')
    description = fields.Text()
