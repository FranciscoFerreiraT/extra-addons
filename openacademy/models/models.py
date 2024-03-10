# -*- coding: utf-8 -*-


from odoo import models, fields

class TestModel(models.Model):
    _name = 'model_test_model'
    _description = 'OpenAcademy Course'

    name = fields.Char(string='Name', required=True)
    description = fields.Text()
