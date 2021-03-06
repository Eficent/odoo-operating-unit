# -*- coding: utf-8 -*-
# © 2015 Eficent Business and IT Consulting Services S.L. -
# Jordi Ballester Alomar
# © 2015 Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp.osv import orm, fields


class account_invoice(orm.Model):
    _inherit = "account.invoice"
    _columns = {
        'operating_unit_id': fields.many2one('operating.unit',
                                             'Operating Unit'),
    }

    def finalize_invoice_move_lines(self, cr, uid, invoice_browse, move_lines):
        move_lines = super(account_invoice, self).finalize_invoice_move_lines(
            cr, uid, invoice_browse, move_lines)
        new_move_lines = []
        for line_tuple in move_lines:
            if invoice_browse.operating_unit_id:
                line_tuple[2]['operating_unit_id'] = \
                    invoice_browse.operating_unit_id.id
            new_move_lines.append(line_tuple)
        return new_move_lines

    def _check_company_operating_unit(self, cr, uid, ids, context=None):
        for pr in self.browse(cr, uid, ids, context=context):
            if (
                pr.company_id and
                pr.operating_unit_id and
                pr.company_id != pr.operating_unit_id.company_id
            ):
                return False
        return True

    _constraints = [
        (_check_company_operating_unit,
         'The Company in the Invoice and in the Operating '
         'Unit must be the same.', ['operating_unit_id',
                                    'company_id'])]

    _defaults = {
        'operating_unit_id': lambda self, cr, uid, c: self.pool.get(
            'res.users').operating_unit_default_get(cr, uid, uid, context=c),
    }


class account_invoice_line(orm.Model):
    _inherit = 'account.invoice.line'

    _columns = {
        'operating_unit_id': fields.related(
            'invoice_id', 'operating_unit_id', type='many2one',
            relation='operating.unit', string='Operating Unit',
            store=True, readonly=True),
    }
