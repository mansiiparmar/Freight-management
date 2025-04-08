frappe.ui.form.on("Sales Invoice", {
	refresh: function(frm) {
		// if (frm.doc.customer_name === "Ganapat  University") {
			frm.add_custom_button("Shipment Order", function () {
				frappe.model.open_mapped_doc({
                    method:"freight.customization.sales_invoice.sales_invoice.create_shipment_order",
                    frm:frm,
                })
			});
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
		
	},
	onchange: function(frm) {
		alert("on change");
		frappe.throw("kumel")

	}
});



       

// frappe.ui.form.on("Sales Invoice", {
// 	onchange: function(frm) {
// 		alert("on change");
// 		frappe.throw("kumel")

// 	}
// })


