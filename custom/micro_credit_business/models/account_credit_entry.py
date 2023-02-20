from odoo import fields, models, api


class AccountCreditEntry(models.Model):
    _name = 'account.credit.entry'
    _description = 'AccountCreditEntry'

    name = fields.Char(
        'Name', copy=False, required=True, readonly=True,
        default=lambda self: self.env['ir.sequence'].next_by_code('account.credit.entry'))
    entry_type_id = fields.Many2one('credit.entry.type', domain="[('active','=',True)]", required=True,string='Entry For')
    account_id = fields.Many2one('partner.credit.account')
    date = fields.Date(required=True, default=fields.date.today())
    amount = fields.Float(required=True)
    balance_move_id = fields.Many2one('credit.balance.move')
    remarks = fields.Text()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('posted', 'Posted')
    ], default='draft')

    def _prepare_balance_move(self):
        self.ensure_one()
        val = {
            'date':self.date,
            'amount':self.amount if self.entry_type_id.type == 'income' else self.amount * -1,
        }
        return val

    def btn_posted(self):
        for rec in self:
            if rec.state not in ('posted'):
                balance = rec.balance_move_id
                if not rec.balance_move_id:
                    balance = self.env['credit.balance.move'].sudo().create(rec._prepare_balance_move())
                    balance.entry_id = rec.id
                    rec.balance_move_id = balance.id
                balance.btn_set_post()
                rec.state = 'posted'

    def button_reset_draft(self):
        for rec in self:
            if rec.state not in ('draft'):
                rec.balance_move_id.btn_rest_draft()
                rec.state = 'draft'
