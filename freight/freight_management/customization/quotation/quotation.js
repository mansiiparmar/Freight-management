// // // frappe.ui.form.on('Quotation', {
// // //     refresh: function(frm) {
// // //         frm.fields_dict['custom_transportation_medium'].get_query = function(doc) {
// // //             if (doc.custom_type_of_shipment == "Intra City" ) {
// // //                 return {
// // //                     filters: [
// // //                         ['name','in',['Road','Drone']]
// // //                     ]
// // //                 };
           
// // //             }
// // //             if(doc.custom_type_of_shipment=="International" ) { 
// // //                 return {
// // //                     filters: [
// // //                         ['name','in',['Road','Sea','Air']]
// // //                     ]
// // //                 };
// // //             }
       
// // //         };

// // //         frm.fields_dict['custom_shipment_type'].get_query = function(doc) {
// // //             if (doc.custom_transportation_medium == "Sea" ) {
// // //                 return {
// // //                     filters: [
// // //                         ['name','in',['FCL','LCL']]
// // //                     ]
// // //                 };
           
// // //             }
// // //         };
// // //     }
// // // });
// // frappe.ui.form.on('Quotation', {
// //     // Trigger when the form is loaded
// //     onload: function(frm) {
// //         // Trigger calculations when qty or custom_freight_weight is updated in the item table
// //         frm.fields_dict['items'].grid.get_field('qty').get_query = function(doc) {
// //             return {
// //                 filters: { }
// //             };
// //         };
        
// //         frm.fields_dict['items'].grid.get_field('custom_freight_weight').get_query = function(doc) {
// //             return {
// //                 filters: { }
// //             };
// //         };
// //     },

// //     // Trigger calculation when any field in items table changes
// //     items_on_form_rendered: function(frm) {
// //         frm.fields_dict['items'].grid.get_field('qty').refresh();
// //         frm.fields_dict['items'].grid.get_field('custom_freight_weight').refresh();
// //     }
// // });

// // frappe.ui.form.on('Quotation Item', {
// //     qty: function(frm, cdt, cdn) {
// //         let item = locals[cdt][cdn];

// //         // Recalculate the total when qty changes
// //         if (!isNaN(item.qty) && !isNaN(item.rate)) {
// //             let total_amount = item.qty * item.rate;
// //             frappe.model.set_value(cdt, cdn, 'total', total_amount);
// //         }

// //         // Recalculate the parent Quotation total
// //         update_quotation_total(frm);
// //     },

// //     custom_freight_weight: function(frm, cdt, cdn) {
// //         let item = locals[cdt][cdn];

// //         // Recalculate the total when custom_freight_weight changes
// //         if (!isNaN(item.custom_freight_weight) && !isNaN(item.rate)) {
// //             let total_amount = item.custom_freight_weight * item.rate;
// //             frappe.model.set_value(cdt, cdn, 'total', total_amount);
// //         }

// //         // Recalculate the parent Quotation total
// //         update_quotation_total(frm);
// //     }
// // });

// // // Function to update the Quotation total by summing item totals
// // function update_quotation_total(frm) {
// //     let total = 0;

// //     // Loop through the items and calculate the total
// //     $.each(frm.doc.items || [], function(i, item) {
// //         total += item.total || 0;  // Add each item's total
// //     });

// //     // Update the total in the Quotation form
// //     frm.set_value('total', total);
// // }


// frappe.ui.form.on('Quotation', {
//     onload(frm) {
//         calculate_total_amount(frm);
//     },
//     custom_distancekm(frm) {
//         calculate_total_amount(frm);
//     },
//     custom_freight_weight(frm) {
//         calculate_total_amount(frm);
//     },
//     custom_type(frm) {
//         calculate_total_amount(frm);
//     }
// });


// function calculate_total_amount(frm) {
//     const distance = frm.doc.custom_distancekm * 2;
//     const weight = frm.doc.custom_freight_weight * 10;
//     const type =  2;

//     const total = distance * weight * type;

//     frm.set_value('total', total);
// }
// frappe.ui.form.on("Quatation Item",{
//     refresh(frm,cdt,cdn){
//         doc = locals[cdt][cdn]
//     }
// })


frappe.ui.form.on('Quotation Item', {
    custom_distancekm(frm, cdt, cdn) {
        frappe.throw("//////////")
        calculate_total_amount(frm);
    },
    custom_freight_weight(frm, cdt, cdn) {
        calculate_total_amount(frm);
        frappe.throw("//////////")
    },
    custom_type(frm, cdt, cdn) {
        calculate_total_amount(frm);
        frappe.throw("//////////")
    }
});

function calculate_total_amount(frm) {
    let total = 0;
    frappe.throw("//////////")

    frm.doc.items.forEach(row => {

        const distance = row.custom_distancekm ? row.custom_distancekm *2 : 1;
        const weight = row.custom_freight_weight ? row.custom_freight_weight * 10 : 1;
        const type = 2;

        total += distance * weight * type;
    });
    frm.doc.set_value('total', total);
}
