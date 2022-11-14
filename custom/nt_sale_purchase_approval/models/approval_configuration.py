from odoo import fields, models, api


class ApprovalConfiguration(models.Model):
    _name = 'nt.approval.configuration'
    _description = 'SaleApprovalConfiguration'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    type_select = [
        ('sale', 'Sale'),
        ('purchase', 'Purchase'),
        ('invoice', 'Invoice'),
        ('bill', 'Bill'),
    ]
    name = fields.Char('Name', copy=False, required=True, readonly=True,
                       default=lambda self: self.env['ir.sequence'].next_by_code('nt.approval.seq'))
    image_1920 = fields.Binary(string='Image')

    company_id = fields.Many2one('res.company', string='Company', required=1, default=lambda self: self.env.company.id,
                                 tracking=True)
    minimum_count = fields.Integer('Minimum User')
    approval_type = fields.Selection(type_select, string='Approval For ', tracking=True, required=1)
    active = fields.Boolean('Active', compute='_get_active_value', tracking=True, store=True)
    user_line = fields.One2many('approval.config.user.line', 'approval_id', string='Users')
    pending_approval_count = fields.Integer(compute='get_pending_approval_count', store=False)

    @api.depends('approval_type', 'company_id')
    def _get_active_value(self):
        for rec in self:
            if rec.approval_type == 'sale':
                rec.active = self.env['ir.config_parameter'].sudo().get_param('sale.enable_approval') or False
            if rec.approval_type == 'purchase':
                rec.active = self.env['ir.config_parameter'].sudo().get_param('purchase.enable_approval') or False
            if rec.approval_type in ['bill', 'invoice']:
                rec.active = self.env['ir.config_parameter'].sudo().get_param('accounting.enable_approval') or False

    def get_pending_approvals(self):
        pass

    @api.depends('name', 'user_line', 'approval_type')
    def get_pending_approval_count(self):
        user_id = self.env.user.id
        for rec in self:
            # rec.pending_approval_count = 0
            # ,
            # ('approval_users.is_approved', '=', False), ('approval_users.user_id.id', '=', user_id)
            approval_count = self.env['nt.approval.orders'].sudo().search_count(
                [('type', '=', rec.approval_type), ('state', 'in', ['waiting_for_approval']),
                 ('approval_users.is_approved', '=', False), ('approval_users.user_id.id', '=', user_id)])
            rec.pending_approval_count = approval_count


class ApprovalConfigurationLine(models.Model):
    _name = 'approval.config.user.line'
    _description = 'SaleApprovalConfigurationLine'
    name = fields.Char('Title')
    user_id = fields.Many2one('res.users', string='User')
    is_required = fields.Boolean(string='Required')
    approval_id = fields.Many2one('nt.approval.configuration')
    company_id = fields.Many2one('res.company', string='Company', required=1, default=lambda self: self.env.company.id)
