# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Nicolas Bessi
#    Copyright 2013 Camptocamp SA
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
from openerp.osv import orm, fields


class product_product(orm.Model):
    """Add relation to framework agreement"""

    _inherit = "product.product"
    _columns = {'framework_agreement_ids': fields.one2many('framework.agreement',
                                                           'product_id',
                                                           'Framework Agreements (LTA)')
                }

    def copy(self, cr, uid, id, default=None, context=None):
        """Override of copy in order not to copy agreements"""
        if not default:
            default = {}
        default['framework_agreement_ids'] = False
        return super(product_product, self).copy(cr, uid, id,
                                                 default=default,
                                                 context=context)
