// Copyright (c) 2025, admin and contributors
// For license information, please see license.txt


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



frappe.ui.form.on('Direct Shipment', {
    refresh:function(frm) {
        frm.add_custom_button(__("Shipment"),function(){
            frappe.msgprint(__("webcome"));

        });
    }
});

frappe.ui.form.on('Direct Shipment',{
    refresh:function(frm){
        frm.call({
            method:"show",
            args:{
                document:frm.doc.name,
            },
            callback: function(r){
                if(!r.exc){
                    frappe.msgprint(r.message)
                }
            }
        })
    }
})

// frappe.ui.form.on('Direct Shipment',{
//     refresh:function(frm){
//         frm.call({
//             method:'show',
//             args:{
//                 document:frm.doc.name,
//             },
//         })
//     }
// })
// frm.call({     //self
//     method:,
//     doc:frm.doc
// })


// frm.call({    //self,method 
//     method:,
//     args:{
//         document: frm.doc.name
//     },
//     doc:frm.doc
// })

// frappe.ui.form.on('Direct Shipment',{
//     refresh:function(frm){
//         frappe.call({
//             method:"display",
//             args:{
//                 document:frm.doc.name,
//             },
//             callback: function(r){
//                 if(!r.exc){
//                     frappe.msgprint(r.message)
//                 }
//             }
//         })
//     }
// })