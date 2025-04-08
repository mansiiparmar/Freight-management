// Copyright (c) 2025, admin and contributors
// For license information, please see license.txt

// frappe.ui.form.on("test", {
// 	refresh(frm) {
//         frappe.call({
//             method: 'freight.freight_management.doctype.test.test.get_password',
//             args: {
//                 docname: frm.doc.name
//             },
//             callback: function(r) {
//                 if (r.message) {
//                     frappe.msgprint(__('Password: {0}', [r.message]));
//                 }
//             }
//         });

// 	},
// });
// frappe.ui.form.on("Test", {
//     refresh: function (frm) {
//         if (frm.doc.country) {
//             frappe.msgprint(frm.doc.country);
//         }
//     }
// });

frappe.ui.form.on('test', {
    refresh: function(frm) {
        frappe.call({
            method: 'freight.freight_management.doctype.test.test.get_password',
            args: {
                docname: frm.doc.name
            },
            callback: function(r) {
                if (r.message) {
                    frappe.msgprint(__('Password: {0}', [r.message]));
                }
            }
        });
    }
});