from odoo import fields, models, api


class InheritPosSession(models.Model):
    _inherit = 'pos.session'

    def close_pos_all_session_close(self):
        open_sessions = self.sudo().search([('state','not in',['closed'])])
        for session in open_sessions:
            session.action_pos_session_closing_control()
            session.action_pos_session_close()
