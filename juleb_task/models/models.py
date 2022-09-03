# -*- coding: utf-8 -*-

from odoo import models, fields, api
from googletrans import Translator, constants
from pprint import pprint

translator = Translator()


class TranslateName(models.Model):
    _name = 'translate.name'

    @api.model
    def translate_names(self, company_id):
        related_return_op = self.env['stock.picking.type'].search([('company_id', '=', company_id), ('code', '=', 'return')])
        if related_return_op:
            translation = translator.translate(str(related_return_op.name), self.env.user.lang)
            related_return_op.name = translation.text



class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    code = fields.Selection(selection_add=[('return', 'Return')])
    company_id = fields.Many2one(
        'res.company', 'Company', required=True, index=True)


class ResCompany(models.Model):
    _inherit = 'res.company'

    @api.model
    @api.returns('self', lambda value: value.id)
    def _company_default_get(self, object=False, field=False):
        """ Returns the user's company
            - Deprecated
        """
        print("weihfowudjn")
        return self.env.company


    @api.model
    def create(self, vals):
        stock_picking_type = self.env['stock.picking.type'].search([])
        company = super(ResCompany, self).create(vals)
        sequence_id = self.env.ref('juleb_task.sequence_return_type')
        sequence_id.company_id = company.id
        sequence_id = sequence_id.id
        vals = {
            'name': 'Return',
            'sequence_code':'RT',
            'code': 'return',
            'sequence_id': sequence_id,
            'company_id': company.id if company else False,
            'warehouse_id': False
        }
        if company:
            stock_picking_type.create(vals)
        return company

