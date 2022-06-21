odoo.define("precioaux_pos.payment", function (require) {
  "use strict";

  const PaymentScreenPaymentLines = require("point_of_sale.PaymentScreenPaymentLines");
  const PaymentScreen = require("point_of_sale.PaymentScreen");
  const PaymentScreenStatus = require("point_of_sale.PaymentScreenStatus");
  const ProductItem = require("point_of_sale.ProductItem");
  const OrderSummary = require("point_of_sale.OrderSummary");
  const Registries = require("point_of_sale.Registries");

  const NumberBuffer = require("point_of_sale.NumberBuffer");
  const utils = require("web.utils");

  const ExtendOrderSummary = (OrderSummary) =>
    class extends OrderSummary {
      getTotalDolarAmount() {
        var total = this.env.pos.get_order().get_total_with_tax();

        return this.env.pos.format_currency_no_symbol(
          total * this.env.pos.conversion_rate,
          2
        );
      }
    };
  Registries.Component.extend(OrderSummary, ExtendOrderSummary);

  const ExtendPaymentScreenPaymentLines = (PaymentScreenPaymentLines) =>
    class extends PaymentScreenPaymentLines {
      formatLineAmount(paymentline) {
        if (paymentline.payment_method.dolar_active) {
          return this.env.pos.format_currency_no_symbol(
            paymentline.get_amount() * this.env.pos.conversion_rate
          );
        } else {
          return this.env.pos.format_currency_no_symbol(
            paymentline.get_amount()
          );
        }
      }
    };

  Registries.Component.extend(
    PaymentScreenPaymentLines,
    ExtendPaymentScreenPaymentLines
  );

  const ExtendPaymentScreenStatus = (PaymentScreenStatus) =>
    class extends PaymentScreenStatus {
      get remainingDolarText() {
        return this.env.pos.format_currency_no_symbol(
          this.currentOrder.get_due() > 0
            ? this.currentOrder.get_due() * this.env.pos.conversion_rate
            : 0
        );
      }
    };
  Registries.Component.extend(PaymentScreenStatus, ExtendPaymentScreenStatus);

  const ExtendPaymentScreen = (PaymentScreen) =>
    class extends PaymentScreen {
      _updateSelectedPaymentline() {
        if (this.paymentLines.every((line) => line.paid)) {
          this.currentOrder.add_paymentline(this.env.pos.payment_methods[0]);
        }
        if (!this.selectedPaymentLine) return; // do nothing if no selected payment line
        // disable changing amount on paymentlines with running or done payments on a payment terminal
        if (
          this.payment_interface &&
          !["pending", "retry"].includes(
            this.selectedPaymentLine.get_payment_status()
          )
        ) {
          return;
        }
        if (NumberBuffer.get() === null) {
          this.deletePaymentLine({
            detail: { cid: this.selectedPaymentLine.cid },
          });
        } else {
          //this.selectedPaymentLine.set_amount(NumberBuffer.getFloat());
          var paymentline = this.selectedPaymentLine;

          var amount = NumberBuffer.getFloat();
          if (paymentline.payment_method.dolar_active) {
            var due_bs = this.env.pos.get_order().get_due(paymentline);
            var due_usd = utils.round_decimals(
              due_bs * this.env.pos.conversion_rate,
              2
            );
            if (due_usd == amount) {
              paymentline.set_amount(due_bs);
            } else {
              paymentline.set_amount(amount / this.env.pos.conversion_rate);
            }
          } else {
            paymentline.set_amount(amount);
          }
        }
      }
    };
  Registries.Component.extend(PaymentScreen, ExtendPaymentScreen);
  const ExtendProductItem = (ProductItem) =>
    class extends ProductItem {
      get price_dolar() {
        const formattedUnitPrice = this.env.pos.format_currency_no_symbol(
          this.props.product.get_price(this.pricelist, 1) *
            this.env.pos.conversion_rate,
          "Product Price"
        );
        if (this.props.product.to_weight) {
          return `${formattedUnitPrice}/${
            this.env.pos.units_by_id[this.props.product.uom_id[0]].name
          }`;
        } else {
          return formattedUnitPrice;
        }
      }
    };
  Registries.Component.extend(ProductItem, ExtendProductItem);
});
