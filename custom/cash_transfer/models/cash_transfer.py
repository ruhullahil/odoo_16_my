from odoo import api, fields, models
from odoo.exceptions import ValidationError


class CashTransfer(models.Model):
    _name = 'cash.transfer'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin', 'sequence.mixin']
    _description = 'CashTransfer'

    def _default_currency_id(self):
        return self.env.company.currency_id.id

    def _default_journal_id(self):
        return self.env['account.journal'].sudo().search(
            [('name', 'ilike', 'Cash'), ('company_id', '=', self.env.company.id)], limit=1).id

    name = fields.Char(
        'Name', copy=False, required=True, readonly=True,
        default=lambda self: self.env['ir.sequence'].next_by_code('cash.transfer.seq'))
    state = fields.Selection([('pending', 'Pending'), ('approve', 'Approve')], string='State', tracking=True,
                             default='pending')
    transaction_type = fields.Selection([('send_money', 'Send Money'), ('received_money', 'Received Money')],
                                        string='Transaction Type')
    partner_id = fields.Many2one('res.partner', string='Partner Name', tracking=True)
    journal_name = fields.Many2one('account.journal', string='Journal Name', tracking=True,
                                   default=lambda self: self._default_journal_id())
    account_name = fields.Many2one('account.account')
    label = fields.Text()
    currency_id = fields.Many2one('res.currency', string='Currency', required=True,
                                  default=lambda self: self._default_currency_id())
    amount = fields.Monetary(string='Amount', tracking=True)
    date = fields.Date(default=fields.date.today())
    account_move_id = fields.Many2one('account.move', string='Journal')

    def action_view_journal(self):
        self.ensure_one()
        return {'type': 'ir.actions.act_window',
                'res_model': 'account.move',
                'view_mode': 'form',
                'res_id': self.account_move_id.id,
                'target': 'current',
                }

    def _prepare_account_move_line(self, partner_id, account_name, tran_type, amount, label=None):
        data = []
        if tran_type == 'received_money':
            dict_val = {
                'account_id': account_name.id,
                'partner_id': partner_id.id,
                'name': label,
                'credit': amount,
                'debit': 0,
                'company_id': self.env.company.id

            }
        else:
            dict_val = {
                'account_id': account_name.id,
                'partner_id': partner_id.id,
                'name': label,
                'credit': 0,
                'debit': amount,
                'company_id': self.env.company.id

            }
        data.append((0, 0, dict_val))
        return data

    def button_approve(self):
        for rec in self:
            lines = self._prepare_account_move_line(rec.partner_id, rec.account_name, rec.transaction_type, rec.amount,
                                                    rec.label)
            move_dict = {
                'move_type': 'entry',
                'date': rec.date,
                'journal_id': rec.journal_name.id,
                'line_ids': lines,
                'company_id': self.env.company.id

            }
            account_move_id = self.env['account.move'].sudo().create(move_dict)
            if account_move_id:
                account_move_id.action_post()
                rec.account_move_id = account_move_id.id
                rec.state = 'approve'
    def unlink(self):
        for rec in self:
            if rec.state =='approve':
                raise ValidationError('{} is already approved!!So,Not possible To Unlink'.format(rec.name))

        return super(CashTransfer, self).unlink()


