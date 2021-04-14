# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools


class calendar_reminder(models.Model):
    _name = 'calendar.reminder'
    _description = 'afo_customs.calendar.reminder'
    _inherit = ['calendar.event']
    _order = "start desc"
    
    product_moq = fields.Float(string="MOQ", help="Internal Use MOQ")



#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
