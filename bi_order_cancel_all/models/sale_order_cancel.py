# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, api

class sale(models.Model):
    _inherit = 'sale.order'

    @api.one
    def action_cancel(self):
        """
        Cancel order,invoice and picking
        """
        if self.picking_ids:
            self.picking_ids.action_cancel()
        if self.invoice_ids:
            self.invoice_ids.action_cancel()
        return super(sale, self).action_cancel()

