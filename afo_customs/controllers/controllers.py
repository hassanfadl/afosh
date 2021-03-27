# -*- coding: utf-8 -*-
# from odoo import http


# class AfoCustoms(http.Controller):
#     @http.route('/afo_customs/afo_customs/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/afo_customs/afo_customs/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('afo_customs.listing', {
#             'root': '/afo_customs/afo_customs',
#             'objects': http.request.env['afo_customs.afo_customs'].search([]),
#         })

#     @http.route('/afo_customs/afo_customs/objects/<model("afo_customs.afo_customs"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('afo_customs.object', {
#             'object': obj
#         })
