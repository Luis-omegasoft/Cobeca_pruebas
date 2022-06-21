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

from odoo import fields, models, api
from odoo.exceptions import UserError
from odoo.tools.translate import _


class ProductTemplate(models.Model):

    _inherit = "product.template"


    concept_id= fields.Many2one(
            'islr.wh.concept', 'Withhold  Concept', required=False,
            help="Concept Income Withholding to apply to the service")



class ProductProduct(models.Model):

    _inherit = "product.product"

    @api.onchange('product_type', 'prd_type')
    def onchange_product_type(self):
        """ Add a default concept for products that are not service type,
        Returns false if the product type is not a service, and if the
        product is service, returns the first concept except 'No apply
        withholding'
        @param prd_type: product type new
        """
        concept_id = False
        if self.prd_type != 'service':
            concept_obj = self.env['islr.wh.concept']

            concept_id = concept_obj.search([('withholdable', '=', False)])
            concept_id = concept_id and concept_id[0] or False
            if not concept_id:
                raise UserError("Invalid action! \nDebe crear el concepto de retención de ingresos")

        return {'value': {'concept_id': concept_id or False}}
