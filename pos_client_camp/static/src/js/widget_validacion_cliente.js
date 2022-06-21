odoo.define('point_of_sale.validacion_cliente', function(require) {
"use strict";

    const ClientDetailsEdit = require("point_of_sale.ClientDetailsEdit");
    const Registries = require("point_of_sale.Registries");

    const ExtendClientDetailsEdit = (ClientDetailsEdit) =>
        class extends ClientDetailsEdit {
            saveChanges() {
                let processedChanges = {};
                for (let [key, value] of Object.entries(this.changes)) {
                    if (this.intFields.includes(key)) {
                        processedChanges[key] = parseInt(value) || false;
                    } else {
                        processedChanges[key] = value;
                    }
                }
                if ((!this.props.partner.name && !processedChanges.name) ||
                    processedChanges.name === '' ){
                    return this.showPopup('ErrorPopup', {
                      title: _('A Customer Name Is Required'),
                    });
                }
                if (this.props.partner.company_type == 'company' || processedChanges.company_type == 'company'){
                    if ((!this.props.partner.vat && !processedChanges.vat) ||
                        processedChanges.vat === '' ){
                        return this.showPopup('ErrorPopup', {
                        title: ('El RIF de la Compañia es requerido.'),
                        });
                    }
                    if ((!this.props.partner.street && !processedChanges.street) ||
                        processedChanges.street === '' ){
                        return this.showPopup('ErrorPopup', {
                        title: ('Debe llenar la dirección (Calle).'),
                        });
                    }
                    if ((!this.props.partner.city && !processedChanges.city) ||
                        processedChanges.city === '' ){
                        return this.showPopup('ErrorPopup', {
                        title: ('Debe llenar la dirección (Ciudad).'),
                        });
                    }
                    if ((!this.props.partner.country_id && !processedChanges.country_id) ||
                        processedChanges.country_id === '' ){
                        return this.showPopup('ErrorPopup', {
                        title: ('Debe llenar la dirección (País).'),
                        });
                    }
                    if ((!this.props.partner.state_id && !processedChanges.state_id) ||
                        processedChanges.state_id === '' ){
                        return this.showPopup('ErrorPopup', {
                        title: ('Debe llenar la dirección (Estado).'),
                        });
                    }
                    if ((!this.props.partner.zip && !processedChanges.zip) ||
                        processedChanges.zip === '' ){
                        return this.showPopup('ErrorPopup', {
                        title: ('Debe llenar la dirección (Código Postal).'),
                        });
                    }
                }
                if (processedChanges.vat){
                    var RegExPattern = /^(V|E|J|P|G){1}(-){1}([0-9]){9}$/;
                    if (!processedChanges.vat.match(RegExPattern)) {
                        return this.showPopup('ErrorPopup', {
                            title: ('Verificar'),
                            body: ('El RIF del cliente es Invalido. Debe tener el formato V-000000005 con un tamaño de 9 caracteres numericos, de poseer menos, rellenar con ceros luego del '-'.')
                        });
                    }
                    
                }
                if (this.props.partner.company_type == 'person' || processedChanges.company_type == 'person'){
                    if ((!this.props.partner.identification_id && !processedChanges.identification_id) ||
                        processedChanges.identification_id === '' ){
                        return this.showPopup('ErrorPopup', {
                        title: ('El Documento de Identidad del cliente es requerido.'),
                        });
                    }
                    if ((!this.props.partner.street && !processedChanges.street) ||
                        processedChanges.street === '' ){
                        return this.showPopup('ErrorPopup', {
                        title: ('Debe llenar la dirección (Calle).'),
                        });
                    }
                }
                if (processedChanges.identification_id){
                    var RegExPattern = /^([0-9]){6,8}$/;
                    if (!processedChanges.identification_id.match(RegExPattern)) {
                        return this.showPopup('ErrorPopup', {
                            title: ('Verificar'),
                            body: ('El Documento de Identidad del cliente es Invalido. Debe tener el formato 00000000 sin puntos.')
                        });
                    }
                    
                }
                if (processedChanges.email){
                    var RegExPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
                    if (!processedChanges.email.match(RegExPattern)) {
                        return this.showPopup('ErrorPopup', {
                            title: ('Verificar'),
                            body: ('El correo es invalido, por favor ingrese un correo valido.')
                        });
                    }
                    
                }
                processedChanges.id = this.props.partner.id || false;
                this.trigger('save-changes', { processedChanges });
            }
        };
    Registries.Component.extend(ClientDetailsEdit, ExtendClientDetailsEdit);

});
