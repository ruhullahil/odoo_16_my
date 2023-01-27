from odoo import fields, models, api


class ResTerritory(models.Model):
    _name = 'res.territory'
    _description = 'Res Territory'

    name = fields.Char(required=True)
    area_size = fields.Float()
    manager_id = fields.Many2one('res.users',required=True)
    description = fields.Text()
