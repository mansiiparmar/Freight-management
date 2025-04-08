
frappe.query_reports["scripe test"] = {
    filters: [
        {
            fieldname: "shipper",
            label: __("Shipper"),
            fieldtype: "Link",
            options: "Shipper"
        }
    ]
};