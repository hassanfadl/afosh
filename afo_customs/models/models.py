# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools


class product_extend(models.Model):
    _name = 'afo_customs.product_extend'
    _description = 'afo_customs.product_extend'
    _inherit = 'product.product'

class contact_extend(models.Model):
    _inherit = ['res.partner']
    frontnamecard_image = fields.Image(string="Business Card", max_width='500',max_height='400', verify_resolution=True) 
    backnamecard_image = fields.Image(string="Back Business Card", max_width='500', max_height='400', verify_resolution=True)



#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
