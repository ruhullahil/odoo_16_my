from odoo import fields, models, api


class InheritResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Description'

    partner_code = fields.Char(string='Customer Code', required=True)
    territory_id = fields.Many2one('res.territory')


    @api.onchange('territory_id')
    def onchange_territory_id_to_account_user(self):
        for rec in self:
            if rec.territory_id:
                rec.user_id = rec.territory_id.manager_id.id or self.env.user.id




    def name_get(self):
        res = []
        for partner in self:
            name = "%s (%s)" % (partner.name, partner.partner_code)
            res += [(partner.id, name)]
        return res
