# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 EMvolution CZ s.r.o. (<http://www.emvolution.cz>).
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
    'name': 'Czech Republic chart of accounts',
    'version': '2.0',
    'category': 'Localization/Account Charts',
    'description': """
This is the localisation package necessary to run Odoo accounting for Czech Republic:
=====================================================================================
    - CZ chart of accounts
    - CZ chart of taxes""",
    'author': 'EMvolution CZ s.r.o.',
    'website': 'http://www.emvolution.cz',
    'depends': ['base_iban', 'base_vat', 'account_chart'],
    'data': [
        'data/account.account.type.csv',
        'data/account.account.template.csv',
        'data/account.tax.code.template.csv',
        'data/account.chart.template.csv',
        'data/account.tax.template.csv',
        'l10n_cz_wizard.xml',
    ],
    'installable': 'True',
    'images': ['images/l10n_cz_chart.jpeg'],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
