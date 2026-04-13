from odoo import fields, models, api
from uuid import uuid4
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Student(models.Model):
    _name = 'student.student'

    name = fields.Char(string='Name')
    date_of_birth = fields.Date(string='DoB')
    age = fields.Integer()
    class_room_id = fields.Many2one(string='Class Room', comodel_name='student.classroom')
    subject_ids = fields.Many2many('subject.subject', string='Subjects')

    @api.model_create_multi
    def create(self, vals_list):
        return super().create(vals_list)

    def create_random_student(self):
        self.create({
            'name': str(uuid4())
        })

    @api.onchange('date_of_birth')
    def _compute_age(self):
        self.age = 0
        if self.date_of_birth:
            self.age = relativedelta(datetime.now().date(), self.date_of_birth).years
