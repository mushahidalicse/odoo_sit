# -*- coding: utf-8 -*-
from odoo import http

# class SitRecruitmentAgency(http.Controller):
#     @http.route('/sit_recruitment_agency/sit_recruitment_agency/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sit_recruitment_agency/sit_recruitment_agency/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sit_recruitment_agency.listing', {
#             'root': '/sit_recruitment_agency/sit_recruitment_agency',
#             'objects': http.request.env['sit_recruitment_agency.sit_recruitment_agency'].search([]),
#         })

#     @http.route('/sit_recruitment_agency/sit_recruitment_agency/objects/<model("sit_recruitment_agency.sit_recruitment_agency"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sit_recruitment_agency.object', {
#             'object': obj
#         })