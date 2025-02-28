frappe.ui.form.on("Sales Invoice", {
	refresh: function(frm) {
		// if (frm.doc.customer_name === "Ganapat  University") {
			frm.add_custom_button("Shipment Order", function () {
				frappe.model.open_mapped_doc({
                    method:"freight.customization.sales_invoice.sales_invoice.create_shipment_order",
                    frm:frm,
                })
			});
		
	}
});