from odoo import models, fields

class ClassRoom(models.Model):
    _name = 'student.classroom'

    name = fields.Char(string='Name')
    student_ids = fields.One2many(string="Students", comodel_name='student.student', inverse_name='class_room_id')
    student_m2m_ids = fields.Many2many(string="Students", comodel_name='student.student')
