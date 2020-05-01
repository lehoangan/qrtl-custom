from odoo import fields, models


class Invite(models.TransientModel):
    _inherit = "mail.wizard.invite"

    send_mail = fields.Boolean(
        "Send Email",
        default=False,
        help="If checked, the partners will receive an \
            email warning they have been added in the document's followers.",
    )