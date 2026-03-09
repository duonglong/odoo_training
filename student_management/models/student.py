from odoo import fields, models


class Student(models.Model):
    _name = 'student.student'

    name = fields.Char(string='Name')
    class_room_id = fields.Many2one(string='Class Room', comodel_name='student.classroom')
    subject_ids = fields.Many2many('subject.subject', string='Subjects')
