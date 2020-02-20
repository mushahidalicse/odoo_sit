# -*- coding: utf-8 -*-

from odoo import models, fields, api

class sit_recruitment_agency(models.Model):
    _name = 'sit_recruitment_agency.sit_recruitment_agency'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100

class Vendor(models.Model):
	_inherit = 'res.partner'
	
	test_type = fields.Char()
	id_number = fields.Char(string="Id Number", readonly=True,copy=False, default='New')
	date_of_birth = fields.Date(string="Date of Birth")
	num_dependencies = fields.Integer(string="No of Dependencies")
	job_position = fields.Many2one('hr.job', 'Job Position')
	rec_attachment_ids = fields.Many2many('ir.attachment', string='Attachments')

	@api.model
	def create(self, vals):
		if vals.get('id_number', 'New') == 'New':
			vals['id_number'] = self.env['ir.sequence'].next_by_code('self.service') or 'New'

		result = super(Vendor, self).create(vals)
		return result


class sit_recruitment_agencies_customers(models.Model):
	_name = 'sit_recruitment_agencies.customers'
	_inherit = 'res.partner'

	name = fields.Char()
	value = fields.Integer()
	value2 = fields.Float()
	description = fields.Text()


class sit_recruitment_agencies_agencies(models.Model):
	_name = 'sit_recruitment_agencies.agencies'

	name = fields.Char()
	value = fields.Integer()
	value2 = fields.Float()
	description = fields.Text()


class sit_recruitment_agencies_recruit(models.Model):
	_name = "sit_recruitment_agencies.recruit"

	name = fields.Char()
	value = fields.Integer()
	value2 = fields.Float()
	description = fields.Text()



class sit_recruitment_agencies_mission(models.Model):
	_name = "sit_recruitment_agencies.mission"

	name = fields.Char()
	value = fields.Integer()
	value2 = fields.Float()
	description = fields.Text()

class sit_recruitment_agencies_traceability(models.Model):
	_name = "sit_recruitment_agencies.traceability"

	name = fields.Char()
	value = fields.Integer()
	value2 = fields.Float()
	description = fields.Text()


class RequestRecruit(models.Model):
	_name = "sit_recruitment_agencies.request_recruit"

	name = fields.Char()
	value = fields.Integer()
	value2 = fields.Float()
	description = fields.Text()
	id_code = fields.Char(string="Code",readonly=True,default='New')
	customer_id = fields.Many2one('res.partner', 'Customer')
	cus_id = fields.Char(string="Customer ID",readonly=True)
	cus_dob = fields.Char(string="Customer DOB",readonly=True)
	cus_mobile = fields.Char(string="Customer Mobile",readonly=True)
	cus_email = fields.Char(string="Customer Email",readonly=True)
	cus_job = fields.Char(string="Customer Job",readonly=True)

	req_template = fields.Selection([
            ('template1', 'Template1'),
            ('template2', 'Template2'),
           	('template3', 'Template3'),
           	   
        ], string='Recruit Template', default='template1') 
	release_date = fields.Date(string="Release Date")
	job_type = fields.Selection([
            ('job1', 'Job1'),
            ('job2', 'Job2'),
           	('job3', 'Job3'),
           	   
        ], string='Job Type', default='job1') 
	company_id = fields.Many2one('res.partner', 'Company')
	visa_number = fields.Char()

	state = fields.Selection([
            ('draft', 'Draft'),
            ('sent', 'Sent'),
           	('confirmed', 'Confirmed'),
           	   
        ], string='Status', default='draft', readonly=True, required=True, copy=False,
        help="If event is created, the status is 'Draft'. If event is confirmed for the particular dates the status is set to 'Confirmed'. If the event is over, the status is set to 'Done'. If event is cancelled the status is set to 'Cancelled'.")


	@api.onchange('customer_id')
	def _set_customer_value(self):
		print("asdfasdfasdfasdfasdfasdfasdfasdfasdf")

		
	@api.model
	def create(self, vals):
		if vals.get('id_code', 'New') == 'New':
			vals['id_code'] = self.env['ir.sequence'].next_by_code('request.recruit') or 'New'

		result = super(RequestRecruit, self).create(vals)
		return result