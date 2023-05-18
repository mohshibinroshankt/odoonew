from odoo import api, fields, models
from datetime import date
from datetime import datetime


class MyownSales(models.Model):
    _name = "myown.sales"
    _inherit = 'mail.thread'
    _description = "Sales Record"

    name = fields.Char(string='Name', required=True, tracking=True)
    product = fields.Char(string='Product')
    cost = fields.Integer(string='Cost', tracking=True)
    notes = fields.Text(string='Notes', tracking=True)
    bought_date = fields.Date(string='Bought Date', tracking=True)
    date_till_bought = fields.Integer(string='Days till bought', compute='_compute_date_till', readonly=False,
                                      tracking=True)
    affordable = fields.Boolean(string='Affordable')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender",
                              tracking=True)
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done'), ('cancel', 'Cancel')],
                             string='Status', tracking=True)
    seller_id = fields.Many2one('res.partner', string='Seller', tracking=True)
    image = fields.Image(string='Image')

    def msr_action_draft(self):
        self.state = 'draft'

    def msr_action_confirm(self):
        self.state = 'confirmed'

    def msr_action_done(self):
        self.state = 'done'

    def msr_action_cancel(self):
        self.state = 'cancel'

    @api.onchange('cost')
    def _onchange_cost(self):
        if self.cost <= 200:
            self.affordable = True
        else:
            self.affordable = False

    @api.model
    def create(self, vals):
        if not vals.get('notes'):
            vals['notes'] = 'New fruit or vegetable'
        res = super(MyownSales, self).create(vals)
        return res

    @api.depends('bought_date')
    def _compute_date_till(self):
        for rec in self:
            today = date.today()
            if rec.bought_date:
                delta = today - rec.bought_date
                rec.date_till_bought = abs(delta.days)
            # if rec.bought_date:
            #     rec.date_till_bought = today.day - rec.bought_date.day
            #     rec.date_till_bought = abs(delta.days)
                # error coming from substituting from greater value like 27 of last month minus 6th this month gives
                # negative value
            else:
                rec.date_till_bought = 0
