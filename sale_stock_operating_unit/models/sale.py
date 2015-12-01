# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Eficent (<http://www.eficent.com/>)
#              <contact@eficent.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import fields, orm
from openerp.tools.translate import _


class SaleShop(orm.Model):
    _inherit = 'sale.shop'

    def _check_warehouse_operating_unit(self, cr, uid, ids, context=None):
        for r in self.browse(cr, uid, ids, context=context):
            if r.warehouse_id and \
                    r.warehouse_id.operating_unit_id != r.operating_unit_id:
                return False
        return True

    _constraints = [
        (_check_warehouse_operating_unit,
         'The Operating Unit in the Warehouse must be the same as in the '
         'Sale Shop.', ['operating_unit_id', 'warehouse_id'])]


class SaleOrder(orm.Model):
    _inherit = 'sale.order'

    def _prepare_order_picking(self, cr, uid, order, context=None):
        res = super(SaleOrder, self)._prepare_order_picking(cr, uid, order,
                                                            context=context)
        if order.operating_unit_id:
            res.update({
                'operating_unit_id': order.operating_unit_id.id
            })

        return res
