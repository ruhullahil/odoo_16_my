from odoo import fields, models, api


class InheritResPartner(models.Model):
    _inherit = 'res.partner'

    member_id = fields.Char(required=True)
    data_of_add = fields.Date(required=True,default=fields.date.today())
    husband_or_father_name = fields.Char(required=True)
    mother_name = fields.Char()
    current_address = fields.Text()
    permanent_address = fields.Text()
    nid_no = fields.Char( required=True)
    occupation = fields.Char(required=True)
    nomine_name = fields.Char(required=True)
    nomine_age = fields.Char(required=True)
    nomine_relation = fields.Char(required=True)
    nomine_sign = fields.binary()


