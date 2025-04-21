frappe.ui.form.on('Sales Order', {
    refresh: function(frm) {
        frm.fields_dict['custom_transportation_medium'].get_query = function(doc) {
            if (doc.custom_type_of_shipment == "Intra City" ) {
                return {
                    filters: [
                        ['name','in',['Road','Drone']]
                    ]
                };
           
            }
            if(doc.custom_type_of_shipment=="International" ) { 
                return {
                    filters: [
                        ['name','in',['Road','Sea','Air']]
                    ]
                };
            }
       
        };

        frm.fields_dict['custom_shipment_type'].get_query = function(doc) {
            if (doc.custom_transportation_medium == "Sea" ) {
                return {
                    filters: [
                        ['name','in',['FCL','LCL']]
                    ]
                };
           
            }
        };
    }
});
