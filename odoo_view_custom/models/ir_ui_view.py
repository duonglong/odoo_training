from odoo import models, fields


class IrUiView(models.Model):
    _inherit = "ir.ui.view"

    type = fields.Selection(
        selection_add=[("card_gallery", "Card Gallery")],
    )

    def _get_view_info(self):
        return {
            **super()._get_view_info(),
            'card_gallery': {'icon': 'oi oi-view-kanban'},
        }


class IrActionsAct_WindowView(models.Model):
    _inherit = 'ir.actions.act_window.view'

    view_mode = fields.Selection(selection_add=[
        ('card_gallery', 'Card Gallery')
    ], ondelete={'card_gallery': 'cascade'})

