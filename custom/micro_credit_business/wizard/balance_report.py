from odoo import fields, models, api


class AccountBalanceReport(models.TransientModel):
    _name = 'account.balance.report'
    _description = 'AccountBalanceReport'

    date_from = fields.Date('Date From',default = fields.date.today(),required=True)
    date_to = fields.Date('Date To',default = fields.date.today(),required=True)

    def print_report(self):
        pass

