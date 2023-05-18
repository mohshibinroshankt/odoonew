from odoo import http
from odoo.http import request


class MySales(http.Controller):

    @http.route('/msr/sales/', website=True, auth='public')
    def msr_sales(self):
        # return "Hello, World"
        return request.render("msr_sales.shibsales", {})
