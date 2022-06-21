odoo.define('pos_delete_validation', function (require) {
    "use strict";
    
    const { useState } = owl;
    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const { useListener } = require('web.custom_hooks');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const NumberBuffer = require('point_of_sale.NumberBuffer');
    const Registries = require ('point_of_sale.Registries');
    const models = require('point_of_sale.models');   

    models.load_fields('res.company', ['code_pos', 'delete_pass_dev']);
    let debounce = 0;

    const UpdatedProductScreen = ProductScreen =>
        class extends ProductScreen {
            async _setValue(val) {
                var old_qty = this.env.pos.get_order().get_selected_orderline().quantity
                if (this.env.pos.company.delete_pass_dev && this.state.numpadMode === 'quantity' && debounce == 0){
                    const {confirmed,payload} = await this.showPopup('CodeAdminPopup',{
                        title: 'Ingrese Clave de Administrador',
                    })
                    if (confirmed && this.env.pos.company.code_pos == payload){
                        debounce = 1
                        setTimeout(() => { debounce = 0 }, 6500);
                        super._setValue(val);
                    } else if (confirmed && this.env.pos.company.code_pos != payload) {
                        this.showPopup('ErrorPopup', {
                            title: 'Alerta: Clave Inválida',
                            body: 'Disculpe, ingresó una clave nula o inválida'
                        })
                        NumberBuffer.set(old_qty)
                    }
                     else {
                        NumberBuffer.reset()              
                    }                    
                } else {
                    super._setValue(val)
                }
            }
        }
    Registries.Component.extend(ProductScreen, UpdatedProductScreen); 

    class CodeAdminPopup extends AbstractAwaitablePopup {
        /**
         * @param {Object} props
         * @param {Boolean} props.isPassword Show password popup.
         * @param {number|null} props.startingValue Starting value of the popup.
         *
         * Resolve to { confirmed, payload } when used with showPopup method.
         * @confirmed {Boolean}
         * @payload {String}
         */
        constructor() {
            super(...arguments);
            useListener('accept-input', this.confirm);
            useListener('close-this-popup', this.cancel);
            let startingBuffer = '';
            if (typeof this.props.startingValue === 'number' && this.props.startingValue > 0) {
                startingBuffer = this.props.startingValue.toString();
            }
            this.state = useState({ buffer: startingBuffer });
            NumberBuffer.use({
                nonKeyboardInputEvent: 'numpad-click-input',
                triggerAtEnter: 'accept-input',
                triggerAtEscape: 'close-this-popup',
                state: this.state,
            });
        }
        get inputBuffer() {
            if (this.state.buffer === null) {
                return '';
            }
            if (this.props.isPassword) {
                return this.state.buffer.replace(/./g, '•');
            } else {
                return this.state.buffer;

            }
        }
        confirm(event) {
            const bufferState = event.detail;
            if (bufferState.buffer !== '') {
                super.confirm();
            }
        }
        sendInput(key) {
            this.trigger('numpad-click-input', { key });
        }
        getPayload() {
            return NumberBuffer.get();
        }
    }
    CodeAdminPopup.template = 'CodeAdminPopup';
    CodeAdminPopup.defaultProps = {
        confirmText: 'Ok',
        cancelText: 'Cancel',
        title: 'Confirm ?',
        body: '',
        cheap: false,
        startingValue: null,
        isPassword: true,
    };

    Registries.Component.add(CodeAdminPopup);

    return CodeAdminPopup;
});  
