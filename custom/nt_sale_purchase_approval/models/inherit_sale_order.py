from odoo import fields, models, api


class InheritSaleOrder(models.Model):
    _inherit = 'sale.order'

    is_submit_button_show = fields.Boolean(compute='_get_show_button',store=False)
    state = fields.Selection(
        selection=[
            ('draft', "Quotation"),
            ('sent', "Quotation Sent"),
            ('waiting_for_approval', 'Waiting for Approval'),
            ('sale', "Sales Order"),
            ('done', "Locked"),
            ('cancel', "Cancelled"),
        ],
        string="Status",
        readonly=True, copy=False, index=True,
        tracking=3,
        default='draft')
    approve_user_ids = fields.One2many('nt.sale.approve.user', 'order_id', string='Approver Users')

    @api.depends('partner_id')
    def _get_show_button(self):
        for rec in self:
            rec.is_submit_button_show = self.env['ir.config_parameter'].sudo().get_param('sale.enable_approval') or False


    def _get_sale_approver(self):
        if not self.env['ir.config_parameter'].sudo().get_param('sale.enable_approval'):
            return
        configuration = self.env['nt.approval.configuration'].sudo().search(
            [('approval_type', '=', 'sale'), ('company_id', '=', self.env.company.id)], order='id desc', limit=1)
        list_val = list()
        for user in configuration.user_line:
            temp = {
                'name': user.name,
                'user_id': user.user_id.id,
                'is_approved': False
            }
            list_val.append((0, 0, temp))
        return list_val

    def prepare_approval_value(self, order):
        val_dict = dict()
        lines = list()
        for line in order.order_line:
            temp = {
                'name': line.product_id.name,
                'quantity': line.product_uom_qty,
                'unit_price': line.price_unit,
            }
            lines.append((0, 0, temp))
        val_dict['type'] = 'sale'
        val_dict['partner_id'] = order.partner_id.id
        val_dict['amount'] = order.amount_total
        val_dict['order_line'] = lines
        val_dict['rel_id'] = order.id
        return val_dict

    def btn_submit_for_approval(self):
        approver = self._get_sale_approver()
        for rec in self:
            rec.approve_user_ids = approver
            val_dict = self.prepare_approval_value(rec)
            val_dict['approval_users'] = approver
            self.env['nt.approval.orders'].sudo().create(val_dict)
            rec.state = 'waiting_for_approval'


class ApproveUsers(models.Model):
    _name = 'nt.sale.approve.user'
    _description = 'SaleApproveUser'

    name = fields.Char('Title')
    user_id = fields.Many2one('res.users', string='User')
    is_approved = fields.Boolean(string='Approved')
    order_id = fields.Many2one('sale.order')
