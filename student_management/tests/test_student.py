from odoo.tests.common import TransactionCase, HttpCase, tagged

from odoo import fields


@tagged('at_install', 'standard')
class TestStudentRecordUnit(TransactionCase):

    def setUp(self):
        super().setUp()
        self.student = self.env['student.student'].create({
            'name': 'Nguyen Van A',
            'date_of_birth': fields.Date.today()
        })

    def test_fields_stored_correctly(self):
        self.assertRecordValues(self.student, [{
            'name': 'Nguyen Van B',
            'date_of_birth': fields.Date.today()
        }])


@tagged('post_install', '-at_install', 'student_record_tour')
class TestStudentRecordTour(HttpCase):
    def test_student_tour_full_workflow(self):
        action = self.env.ref('student_management.student_action')
        url = f"/odoo/action-{action.id}"
        self.start_tour(
            url,  # URL to open in the browser
            'student_record_tour',  # must match registry name in JS
            login='admin',  # log in as this user before starting
        )
