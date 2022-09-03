# -*- coding: utf-8 -*-
# from odoo import http


# class JulebTask(http.Controller):
#     @http.route('/juleb_task/juleb_task/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/juleb_task/juleb_task/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('juleb_task.listing', {
#             'root': '/juleb_task/juleb_task',
#             'objects': http.request.env['juleb_task.juleb_task'].search([]),
#         })

#     @http.route('/juleb_task/juleb_task/objects/<model("juleb_task.juleb_task"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('juleb_task.object', {
#             'object': obj
#         })
