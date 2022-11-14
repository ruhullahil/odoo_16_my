from odoo import fields, models, api


class ResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'

    enable_sale_approval = fields.Boolean(string='Sale Approval', config_parameter='sale.enable_approval')
    enable_purchase_approval = fields.Boolean(string='Purchase Approval', config_parameter='purchase.enable_approval')
    enable_accounting_approval = fields.Boolean(string='Accounting Approval',
                                                config_parameter='accounting.enable_approval')
