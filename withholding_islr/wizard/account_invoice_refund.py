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

from odoo import models


class AccountInvoiceRefund(models.TransientModel):

    """Refunds invoice"""

    _inherit = 'account.invoice.refund'

    def validate_wh(self):
        """ Method that validate if invoice has non-yet processed INCOME
        withholds.
        return: True: if invoice is does not have wh's or it does have and
                      those ones are validated.
                False: if invoice is does have and those wh's are not yet
                       validated.
        """
        if self._context is None:
            context = {}
        res = []
        inv_obj = self.env['account.invoice']

        res.append(super(AccountInvoiceRefund, self).validate_wh())
        res.append(inv_obj.validate_wh_income_done())
        return all(res)

AccountInvoiceRefund()
