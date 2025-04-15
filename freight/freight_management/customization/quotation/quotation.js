function calculateCustomTotal(frm) {
    let total = 0;

    (frm.doc.items || []).forEach(item => {
        if (item.qty && item.custom_freight_weight && item.custom_distancekm && item.rate && item.custom_transportation_type == "Air") {
            total += item.qty * item.custom_freight_weight * item.custom_distancekm * item.rate * 7;
        }
        else if (item.qty && item.custom_freight_weight && item.custom_distancekm && item.rate && item.custom_transportation_type == "Ocean(Sea)") {
            total += item.qty * item.custom_freight_weight * item.custom_distancekm * item.rate * 4;
        }
        else if (item.qty && item.custom_freight_weight && item.custom_distancekm && item.rate && item.custom_transportation_type == "Land") {
            total += item.qty * item.custom_freight_weight * item.custom_distancekm * item.rate * 2;
        }
        else if (item.qty && item.custom_freight_weight && item.custom_distancekm && item.rate) {
            total += item.qty * item.custom_freight_weight * item.custom_distancekm * item.rate;
        } else if (item.custom_freight_weight && item.rate) {
            total += item.custom_freight_weight * item.rate;
        } else if (item.custom_distancekm && item.rate) {
            total += item.custom_distancekm * item.rate;
        }else if (item.custom_freight_weight && item.rate) {
                total += item.custom_freight_weight * item.rate;
            }
         else if (item.qty && item.rate) {
            total += (item.qty * item.rate) ;
        }

    });
    
//     let t = 0
//     // (frm.doc.items || []).forEach(item => {
//     // if (item.custom_transportation_type =="Air"){
//     //     t = 7
//     // }else if (item.custom_transportation_type =="Ocean(sea)"){
//     //     t= 2
//     // }else if (item.custom_transportation_type =="Land"){
//     //     t= 4
//     // }
//     // total = t * total
// });
    frm.set_value("total", total);
    frm.refresh_field("total");
    // frm.fields_dict["items"].grid.refresh();

}

frappe.ui.form.on("Quotation", {
    onload(frm) {
        calculateCustomTotal(frm);
    },
    // validate(frm) {
    //     calculateCustomTotal(frm); 
    // }
});

frappe.ui.form.on("Quotation Item", {
    qty: calculateCustomTotal,
    custom_freight_weight: calculateCustomTotal,
    custom_distancekm: calculateCustomTotal,
    rate: calculateCustomTotal,
    custom_transportation_type: calculateCustomTotal
});
