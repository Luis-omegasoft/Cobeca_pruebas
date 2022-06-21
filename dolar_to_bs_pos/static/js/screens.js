odoo.define('dolar_to_bs_pos.payment', function (require) {
    'use strict';

    const PaymentScreenPaymentLines = require('point_of_sale.PaymentScreenPaymentLines');
    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const PaymentScreenStatus = require('point_of_sale.PaymentScreenStatus');
    const ProductItem = require('point_of_sale.ProductItem');
    const OrderSummary = require('point_of_sale.OrderSummary');
    const Registries = require('point_of_sale.Registries');

    const NumberBuffer = require('point_of_sale.NumberBuffer');
    const utils = require('web.utils');

    const ExtendOrderSummary = OrderSummary => 
        class extends OrderSummary {
            getTotalBsAmount() {
                var total = this.props.total.slice(2)
                var tasa_bs = this.env.pos.company_currency.rate
                return parseFloat((total / tasa_bs).toFixed(2))
            }
        
    }
    
    Registries.Component.extend(OrderSummary, ExtendOrderSummary);

    const ExtendPaymentScreenPaymentLines = PaymentScreenPaymentLines => 
        class extends PaymentScreenPaymentLines {
            formatLineAmount(paymentline) {
                var tasa_bs = this.env.pos.company_currency.rate
                if(paymentline.payment_method.bs_active){
                    return this.env.pos.format_currency_no_symbol(paymentline.get_amount()/tasa_bs);
                } else {
                    return this.env.pos.format_currency_no_symbol(paymentline.get_amount());
                }                
            }
        
    }
    
    Registries.Component.extend(PaymentScreenPaymentLines, ExtendPaymentScreenPaymentLines);

    const ExtendPaymentScreenStatus = PaymentScreenStatus => 
        class extends PaymentScreenStatus {
            get remainingBsText() {
                var tasa_bs = this.env.pos.company_currency.rate
                return this.env.pos.format_currency_no_symbol(
                    this.currentOrder.get_due() > 0 ? this.currentOrder.get_due()/tasa_bs : 0
                );
            }
        
    }    
    Registries.Component.extend(PaymentScreenStatus, ExtendPaymentScreenStatus);

    const ExtendPaymentScreen = PaymentScreen => 
        class extends PaymentScreen {
            _updateSelectedPaymentline() {
                if (this.paymentLines.every((line) => line.paid)) {
                    this.currentOrder.add_paymentline(this.env.pos.payment_methods[0]);
                }
                if (!this.selectedPaymentLine) return; // do nothing if no selected payment line
                // disable changing amount on paymentlines with running or done payments on a payment terminal
                if (
                    this.payment_interface &&
                    !['pending', 'retry'].includes(this.selectedPaymentLine.get_payment_status())
                ) {
                    return;
                }
                if (NumberBuffer.get() === null) {
                    this.deletePaymentLine({ detail: { cid: this.selectedPaymentLine.cid } });
                } else {
                    //this.selectedPaymentLine.set_amount(NumberBuffer.getFloat());
                    var paymentline = this.selectedPaymentLine
                    var tasa_bs = this.env.pos.company_currency.rate
                    var amount = NumberBuffer.getFloat();
                    if (paymentline.payment_method.bs_active) {
                        var due_usd = this.env.pos.get_order().get_due(paymentline);
                        var due_bs = utils.round_decimals(due_usd / tasa_bs, 2);
                        if (due_bs == amount) {
                          paymentline.set_amount(due_usd);
                        } else {
                          paymentline.set_amount(amount * tasa_bs);
                        }
                    } else {
                        paymentline.set_amount(amount);
                    }
                      
                }
            }
        }
    Registries.Component.extend(PaymentScreen, ExtendPaymentScreen);
    const ExtendProductItem = ProductItem => 
        class extends ProductItem {
            get price_bs() {
                var tasa_bs = this.env.pos.company_currency.rate
                const formattedUnitPrice = this.env.pos.format_currency_no_symbol(
                    this.props.product.get_price(this.pricelist, 1)/tasa_bs,
                    'Product Price'
                );
                if (this.props.product.to_weight) {
                    return `${formattedUnitPrice}/${
                        this.env.pos.units_by_id[this.props.product.uom_id[0]].name
                    }`;
                } else {
                    return formattedUnitPrice;
                }
            }
        }
    Registries.Component.extend(ProductItem, ExtendProductItem);
    
});