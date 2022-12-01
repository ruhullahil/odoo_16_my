from odoo import fields, models, api, _


class InheritPurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    _description = 'InheritPurchaseOrder'

    # state = fields.Selection([
    #     ('draft', 'RFQ'),
    #     ('sent', 'RFQ Sent'),
    #     ('to approve', 'To Approve'),
    #     ('purchase', 'Purchase Order'),
    #     ('done', 'Locked'),
    #     ('cancel', 'Cancelled')
    # ], string='Status', readonly=True, index=True, copy=False, default='draft', tracking=True)
    #
    # is_approve_invisible = fields.Boolean(compute='get_i')
    def _approval_allowed(self):
        """Returns whether the order qualifies to be approved by the current user"""
        self.ensure_one()
        return (
                self.company_id.po_double_validation == 'one_step'
                or (self.company_id.po_double_validation == 'two_step'
                    and self.amount_total < self.env.company.currency_id._convert(
                    self.company_id.po_double_validation_amount, self.currency_id, self.company_id,
                    self.date_order or fields.Date.today()))
                or self.user_has_groups('mime_task.group_md'))

    can_edit = fields.Boolean(compute='_set_read_only')


    @api.depends('state')
    def _set_read_only(self):
        for rec in self:
            rec.can_edit = self.env.user.has_group('mime_task.group_purchase_approval_procurement_team')


    def mail_send(self):
        '''
        This function opens a window to compose an email, with the edi purchase template message loaded by default
        '''
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            if self.env.context.get('send_rfq', False):
                template_id = ir_model_data._xmlid_lookup('purchase.email_template_edi_purchase')[2]
            else:
                template_id = ir_model_data._xmlid_lookup('purchase.email_template_edi_purchase_done')[2]
        except ValueError:
            template_id = False
        self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)

    def create(self, values):
        res = super(InheritPurchaseOrder, self).create(values)
        res.mail_send()
        return res
