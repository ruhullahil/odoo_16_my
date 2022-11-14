from odoo import fields, models, api


class CashTransferReport(models.TransientModel):
    _name = 'cash.transfer.report'
    _description = 'Description'

    start_date = fields.Date(string='Start Date', default=fields.date.today(), required=1)
    end_date = fields.Date(default=fields.date.today(), required=1)
    transaction_type = fields.Selection([('send_money', 'Send Money'), ('received_money', 'Received Money')],
                                        string='Transaction Type', required=1)
    entry_type = fields.Selection([('pending', 'Pending'), ('approve', 'Approve'), ('all', 'All')], default='approve')

    def get_report(self):
        data = self.read()[0]
        # print(data)
        return self.env.ref('cash_transfer.report_cash_transfer').report_action(self, data=data)


class CashTransferReportReportView(models.AbstractModel):
    """
        Abstract Model specially for report template.
        _name = Use prefix `report.` along with `module_name.report_name`
    """
    _name = 'report.cash_transfer.report_cash_transfer_report_view'

    def _get_report_values(self, docids, data=None):
        start_date = data.get('start_date', fields.date.today())
        end_date = data.get('end_date', fields.date.today())
        transiction_type = data.get('transaction_type', False)
        entry_type = data.get('entry_type', False)
        domain = list()
        if start_date:
            domain.append(('date', '>=', start_date))
        if end_date:
            domain.append(('date', '<=', end_date))
        if transiction_type:
            domain.append(('transaction_type', '=', transiction_type))
        if entry_type and entry_type != 'all':
            domain.append(('state', '=', entry_type))
        cash_tr_data = self.env['cash.transfer'].sudo().search(domain, order='date desc')

        return {
            'report_name': 'Cash Transfer Report',
            'start_date': start_date,
            'end_date': end_date,
            'records': cash_tr_data,

        }
