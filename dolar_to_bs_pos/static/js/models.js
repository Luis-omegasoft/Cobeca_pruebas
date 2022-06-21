odoo.define('pos_product_list.models', function (require) {
    'use strict';
  
    var pos_model = require('point_of_sale.models');
  
    pos_model.load_fields('product.product', [
      'qty_available',
      'default_code',
      'list_price',
      'aux_price',
    ]);
    pos_model.load_fields('pos.payment.method', ['bs_active']);
  
    var models = require('point_of_sale.models');
    var _super_order = models.Order.prototype;
    var _super_paymentline = models.Paymentline.prototype;
  
    models.Order = models.Order.extend({
      initialize: function (attributes, options) {
        _super_order.initialize.call(this, attributes, options);
        this.printNumber = 0;
        this.discount_total = 0;
        //this.monto_total_dolar = 0;
        this.tasa_bs = 1;
        //this.multi = 1;
      },
  
      /* obtener_subtotal: function () {
        return this.get_total_without_tax();
      }, */
  
      //   MODIFICACIONES PARA GESTIONAR PAGOS EN $
  
      add_paymentline: function (payment_method) {
        var new_paymentline = _super_order.add_paymentline.call(this, payment_method);
        if (payment_method.bs_active) {
          new_paymentline.set_amount(0);
        }
        /* if(!payment_method.is_cash_count || this.pos.config.iface_precompute_cash){
            newPaymentline.set_amount( this.get_due() );
        }; */
      },
    });

    models.Paymentline = models.Paymentline.extend({
      set_amount: function(value){
        this.order.assert_editable();
        this.amount = parseFloat(value) || 0;
        if (this.pos.config.iface_customer_facing_display) this.pos.send_current_order_to_customer_facing_display();
        this.trigger('change',this);
      },
    })
  });