from odoo import fields, models, api


class SalePurchaseStock(models.TransientModel):
    _name = 'sale.purchase.stock.report'

    start_date = fields.Date(string='Start Date', default=fields.date.today(), required=1)
    end_date = fields.Date(default=fields.date.today(), required=1)

    def get_report(self):
        data = self.read()[0]
        # print(data)
        return self.env.ref('cash_transfer.report_p_w_sale_purchase_stock').report_action(self, data=data)


class CashTransferReportReportView(models.AbstractModel):
    """
        Abstract Model specially for report template.
        _name = Use prefix `report.` along with `module_name.report_name`
    """
    _name = 'report.cash_transfer.report_p_w_sale_purchase_stock_view'

    def _get_rel_product(self, start_date, end_date):
        sql = "select product_id from purchase_order_line where create_date::date between '{}'::date and '{}'::date and company_id = {}".format(
            start_date,
            end_date, self.env.company.id)
        self._cr.execute(sql)
        product_ids = self._cr.fetchall()
        return product_ids

    def _get_report_values(self, docids, data=None):
        start_date = data.get('start_date', fields.date.today())
        end_date = data.get('end_date', fields.date.today())
        product_ids = self._get_rel_product(start_date, end_date)
        final_data = list()
        for product in product_ids:
            temp = dict()
            temp['product_name'] = self.env['product.product'].sudo().search(
                [('id', '=', product)]).product_tmpl_id.name
            temp['purchase'] = sum(self.env['purchase.order.line'].sudo().search(
                [('product_id', '=', product), ('create_date', '>=', start_date), ('create_date', '<=', end_date),
                 ('company_id', '=', self.env.company.id), ('state', 'in', ['purchase', 'done'])]).mapped(
                'product_qty'))
            temp['sale'] = sum(self.env['sale.order.line'].sudo().search(
                [('product_id', '=', product), ('create_date', '>=', start_date), ('create_date', '<=', end_date),
                 ('company_id', '=', self.env.company.id), ('state', 'in', ['sale', 'done'])]).mapped(
                'qty_delivered'))
            temp['pos'] = sum(self.env['pos.order.line'].sudo().search(
                [('product_id', '=', product), ('create_date', '>=', start_date), ('create_date', '<=', end_date),
                 ('company_id', '=', self.env.company.id)]).mapped(
                'qty'))
            temp['stock'] = sum(self.env['stock.quant'].sudo().search(
                [('product_id', '=', product), ('create_date', '>=', start_date), ('create_date', '<=', end_date),
                 ('company_id', '=', self.env.company.id), ('location_id.usage', '=', 'internal')]).mapped(
                'quantity'))
            final_data.append(temp)

        return {
            'report_name': 'Product Wise Sale Purchase Report',
            'start_date': start_date,
            'end_date': end_date,
            'records': final_data
        }
