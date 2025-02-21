// frappe.ui.form.on('Sales Invoice', {
//     refresh:function(frm) {
//         frm.add_custom_button("Shipment Order",function(){
//             frappe.msgprint(__("welcome"));

//         });
//     }
// });


frappe.ui.form.on('Sales Invoice', {
    refresh: function(frm) {
        frm.add_custom_button("Shipment Order", function() {
            // Create a dialog for the user to select transportation status
            var d = new frappe.ui.Dialog({
                title: __('Shipment Status'),
                fields: [
                    {
                        fieldtype: 'Select',
                        label: __('Select Status'),
                        fieldname: 'status',
                        options: ['Order Pending','Sent to Transporter','In Transit', 'Delivered'],
                        default: 'In Transit',
                        reqd: 1
                    }
                ],
                primary_action_label: __('Submit'),
                primary_action: function() {
                    var status = d.get_value('status');
                    frappe.msgprint(__('You selected: ') + status);
                    d.hide();
                }
            });
            d.show();
        });
    }
});
