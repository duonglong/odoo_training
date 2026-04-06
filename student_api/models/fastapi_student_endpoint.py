from odoo import fields, models
from ..routers.student_router import router as student_router


class FastapiEndpoint(models.Model):
    _inherit = "fastapi.endpoint"

    app: str = fields.Selection(
        selection_add=[
            ("student", "Student Endpoint"),
        ], ondelete={"student": "cascade"}
    )

    def _get_fastapi_routers(self):
        if self.app == "student":
            return [student_router]
        return super()._get_fastapi_routers()
