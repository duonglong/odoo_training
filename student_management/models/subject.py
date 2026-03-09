from odoo import models, fields


class Subject(models.Model):
    _name = 'subject.subject'

    name = fields.Char(string='Name')

