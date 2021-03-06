# -*- coding: utf-8 -*-
# © 2015 Eficent - Jordi Ballester Alomar
# © 2015 Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp.osv import fields, orm


class res_users(orm.Model):

    _inherit = 'res.users'

    _columns = {
        'operating_unit_ids': fields.many2many(
            'operating.unit', 'operating_unit_users_rel',
            'user_id', 'poid',
            'Operating Units'),
        'default_operating_unit_id': fields.many2one(
            'operating.unit', 'Default Operating Unit')
    }

    def operating_unit_default_get(self, cr, uid, uid2, context=None):
        if not uid2:
            uid2 = uid
        user = self.pool.get('res.users').browse(cr, uid, uid2, context)
        return user.default_operating_unit_id and \
            user.default_operating_unit_id.id or False

    def _operating_unit_default_get(self, cr, uid, context=None):
        return self.operating_unit_default_get(cr, uid, uid, context=context)

    def _get_operating_units(self, cr, uid, context=None):
        op_unit = self.operating_unit_default_get(cr, uid, uid,
                                                  context=context)
        if op_unit:
            return [op_unit]
        return False

    _defaults = {
         'default_operating_unit_id': _operating_unit_default_get,
         'operating_unit_ids': _get_operating_units,
     }
