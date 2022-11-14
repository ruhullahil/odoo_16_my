from odoo import fields, models, api


class NtApprovalOrders(models.Model):
    _name = 'nt.approval.orders'
    _description = 'NtApprovalOrders'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    state_selection = [
        ('draft', 'Draft'),
        ('waiting_for_approval', 'Waiting Approval'),
        ('approved', 'Approved')
    ]
    type_select = [
        ('sale', 'Sale'),
        ('purchase', 'Purchase'),
        ('invoice', 'Invoice'),
        ('bill', 'Bill'),
    ]

    name = fields.Char('Name', copy=False, required=True, readonly=True,
                       default=lambda self: self.env['ir.sequence'].next_by_code('nt.approval.order.seq'))
    state = fields.Selection(state_selection, string='State', default='waiting_for_approval', tracking=True)
    partner_id = fields.Many2one('res.partner', string='Partner')
    type = fields.Selection(type_select, string='Type')
    date = fields.Date(string='Date', default=fields.date.today())
    amount = fields.Float(string='Total Amount')
    is_visible_user = fields.Boolean(compute='set_is_visible_user')
    approval_users = fields.One2many('nt.approval.user', 'order_id', string='Approval Users')
    order_line = fields.One2many('nt.approval.orders.lines', 'order_id', string='Order Line')
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company.id)
    rel_id = fields.Integer()

    @api.depends('state', 'approval_users')
    def set_is_visible_user(self):
        user = self.env.user.id
        for rec in self:
            rec.is_visible_user = False
            enable_users = rec.approval_users.filtered(lambda c: c.is_approved == False)
            if user in enable_users.user_id.ids:
                rec.is_visible_user = True
            if rec.state != 'waiting_for_approval':
                rec.is_visible_user = False

    def button_approve(self):
        model_map_dict = {
            'sale': 'sale.order',
            'purchase': 'purchase.order',
            'invoice': 'account.move',
            'bill': 'account.move',
        }
        configuration = self.env['nt.approval.configuration'].sudo().search(
            [('approval_type', '=', 'sale'), ('company_id', '=', self.env.company.id)], order='id desc', limit=1)


class ApprovalOrderUser(models.Model):
    _name = 'nt.approval.user'
    _description = 'ApprovalOrderUser'

    name = fields.Char('Title')
    user_id = fields.Many2one('res.users', string='User')
    is_approved = fields.Boolean(string='Approved')
    order_id = fields.Many2one('nt.approval.orders')


class OrderLines(models.Model):
    _name = 'nt.approval.orders.lines'
    _description = 'OrderLines'

    name = fields.Char(string='Item')
    quantity = fields.Float(string='Quantity')
    unit_price = fields.Float(string='Unit Price')
    total_price = fields.Float(string='Total Price', compute='_get_total')
    order_id = fields.Many2one('nt.approval.orders')

    @api.depends('quantity', 'unit_price')
    def _get_total(self):
        for rec in self:
            rec.total_price = rec.unit_price * rec.quantity
