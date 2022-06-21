odoo.define("pos_product_list.models", function (require) {
  "use strict";

  var pos_model = require("point_of_sale.models");

  pos_model.load_fields("product.product", [
    "qty_available",
    "default_code",
    "list_price",
    "aux_price",
  ]);
  pos_model.load_fields("pos.payment.method", ["dolar_active"]);

  var models = require("point_of_sale.models");
  var _pos_model = models.PosModel.prototype;
  var _super_order = models.Order.prototype;
  var rpc = require("web.rpc");

  models.PosModel = models.PosModel.extend({
    after_load_server_data: function () {
      this.conversion_rate = 1;

      //TODO: Tomar la moneda alterna desde algún parámetro de configuración
      var convert_to = "USD";
      // se obtiene el factor de conversión y luego se continúa con la inicialización de los componentes
      return rpc
        .query({
          model: "res.currency",
          method: "get_conversion_rate",
          args: [posmodel.company_currency.name, convert_to],
        })
        .then((rs) => {
          console.log("conversion_rate", rs);
          this.conversion_rate = rs;
          return;
        })
        .catch((err) => {
          console.log("conversion_rate Error:", err);
        })
        .then((rs) => {
          return _pos_model.after_load_server_data.call(this);
        });
    },
  });

  models.Order = models.Order.extend({
    initialize: function (attributes, options) {
      _super_order.initialize.call(this, attributes, options);
      this.printNumber = 0;
      this.discount_total = 0;
      this.monto_total_dolar = 0;
      this.tasa_dolar = 1;
      this.multi = 1;
    },

    //   MODIFICACIONES PARA GESTIONAR PAGOS EN $

    add_paymentline: function (payment_method) {
      var new_paymentline = _super_order.add_paymentline.call(
        this,
        payment_method
      );
      if (payment_method.dolar_active) {
        new_paymentline.set_amount(0);
      }
    },
  });
});
