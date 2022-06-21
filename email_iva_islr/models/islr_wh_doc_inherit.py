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
from odoo import models, fields
from odoo.exceptions import UserError


class IslrWhDocInherit(models.Model):
    _inherit = 'islr.wh.doc'

    res_partner_email = fields.Char(string="Email de la compañía", related="partner_id.email")
    user_id = fields.Many2one('res.users', 'Responsable', default=lambda self: self.env.user)

    def action_done(self):
        res = super(IslrWhDocInherit, self).action_done()
        if self.res_partner_email:
            self.state = 'done'
            email_template_id = self.env.ref('email_iva_islr.ret_islr_template').id
            template = self.env['mail.template'].browse(email_template_id)
            template.send_mail(self.id, force_send=True)
            return res
        else:
            raise UserError('La compañía no tiene email asociado. Por favor, añada uno para continuar')

    def action_confirm(self):
        if not self.res_partner_email:
            raise UserError('La compañía no tiene email asociado. Por favor, añada uno para continuar')
        else:
            return super(IslrWhDocInherit, self).action_confirm()
