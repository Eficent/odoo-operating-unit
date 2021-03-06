# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Eficent (<http://www.eficent.com/>)
#               <contact@eficent.com>
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

{
    "name": "Operating Unit in Sales Stock",
    "version": "1.0",
    "author": "Eficent",
    "website": "http://www.eficent.com",
    "category": "Purchase Management",
    "depends": ["sale_stock",
                "sale_operating_unit",
                "stock_operating_unit"],
    "description": """
Operating Unit in Sales Stock
=============================
This module prevents a user from selecting a Warehouse in the Sale Shop
that does not belong to the same operating unit.


Credits
=======

Contributors
------------

* Jordi Ballester <jordi.ballester@eficent.com>

    """,
    "data": [],
    'installable': True,
    'active': False,
}
