# -*- coding: utf-8 -*-
##############################################################################
#
#    MoviTrack
#    Copyright (C) 2020-TODAY MoviTrack.
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import time
from odoo import api, fields, models, exceptions
from odoo.fields import _

class AccountJournal(models.Model):
    _inherit = 'account.journal'

    default_iva_account = fields.Many2one('account.account', string='Cuenta retención IVA')
    default_islr_account = fields.Many2one('account.account', string='Cuenta retención ISLR')
    is_iva_journal = fields.Boolean(default=False)
    is_islr_journal = fields.Boolean(default=False)




