odoo.define("point_of_sale.pos_campos", function (require) {
  "use strict";

  const Registries = require("point_of_sale.Registries");
  const PaymentScreen = require("point_of_sale.PaymentScreen");
  const models = require('point_of_sale.models');

  models.load_fields("res.partner",['people_type_individual','nationality','identification_id','company_type']);


  const CamposPaymentScreen = (PaymentScreen) =>
    class extends PaymentScreen {
      async validateOrder(isForceValidate) {
        if (!this.env.pos.get_order().attributes.client) {
          this.showPopup("ErrorPopup", {
            title: "Alerta: Verificar",
            body: "El Cliente debe estar Seleccionado.",
          });
        } else {
          super.validateOrder(isForceValidate);
        }
      }
    };
  Registries.Component.extend(PaymentScreen, CamposPaymentScreen);
});
