from odoo import models, fields


class CRMLead(models.Model):
    _inherit = 'crm.lead'

    x_full_name = fields.Char(string='Full Name')