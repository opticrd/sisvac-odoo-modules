import json
from odoo.http import request
from odoo.addons.component.core import Component


class AppointmentsService(Component):
    _inherit = "base.rest.service"
    _name = "appointments.service"
    _usage = "appointments"
    _collection = "sisvac.services"
    _description = """
        Appointments Related models API Services
    """

    def search(self):
        appointments = self.env["calendar.event"].search(
            [("vaccination_appointment", "=", True)]
        )
        return request.make_response(
            json.dumps([apt._get_appointment_data() for apt in appointments]),
            headers=[("Content-Type", "application/json")],
        )
