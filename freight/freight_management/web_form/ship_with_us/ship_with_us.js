frappe.ready(function() {
	// bind events here
})

frappe.ready(function() {
    
    fetchDataFromOtherDocType();
});

function fetchDataFromOtherDocType() {
    frappe.call({
        method: "frappe.client.get_value",
        args: {
            doctype: "Customer", 
            fieldname: ["customer_name"],
            filters: { customer_name: "Mr kumel gandhi" } 
        },
        callback: function(response) {
            if (response.message) {
          frappe.web_form.set_value("first_name", response.message.customer_name);

                frappe.msgprint("/////");
            }
        }
    });
}