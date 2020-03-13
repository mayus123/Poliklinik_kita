# -*- coding: utf-8 -*-
from odoo import http

# class Mqpoliklinik(http.Controller):
#     @http.route('/mqpoliklinik/mqpoliklinik/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mqpoliklinik/mqpoliklinik/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mqpoliklinik.listing', {
#             'root': '/mqpoliklinik/mqpoliklinik',
#             'objects': http.request.env['mqpoliklinik.mqpoliklinik'].search([]),
#         })

#     @http.route('/mqpoliklinik/mqpoliklinik/objects/<model("mqpoliklinik.mqpoliklinik"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mqpoliklinik.object', {
#             'object': obj
#         })