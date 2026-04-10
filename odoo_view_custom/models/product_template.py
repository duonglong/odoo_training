from odoo import fields, models, api
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    _sql_constraints = [
        (
            "rating_range",
            "CHECK(rating BETWEEN 0 AND 5)",
            "Rating must be between 0 and 5.",
        ),
    ]

    rating = fields.Integer(
        string="Rating",
        default=0,
        help="Product star rating from 0 (unrated) to 5 stars.",
    )

    @api.constrains("rating")
    def _check_rating_range(self):
        for rec in self:
            if not (0 <= rec.rating <= 5):
                raise ValidationError(
                    f"Rating must be between 0 and 5 (got {rec.rating})."
                )
