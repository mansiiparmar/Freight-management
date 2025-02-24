// Copyright (c) 2025, admin and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Direct Shipment", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Direct Shipment', {
    refresh: function(frm) {
        frm.fields_dict['transport_medium'].get_query = function(doc) {
            if (doc.type_of_shipment == "Intra City") {
                return {
                    filters: {
                        name: "Road"
                    }
                };
            }
        };
    }
});