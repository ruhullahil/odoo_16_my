from odoo import fields, models, api


class InheritResUsers(models.Model):
    _inherit = 'res.users'


    signature_hand = fields.Image(
        string="Signature",
        copy=False, attachment=True, max_width=1024, max_height=1024)
