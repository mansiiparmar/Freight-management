frappe.ui.form.on('Task', {
    refresh(frm) {
        frm.add_custom_button(__('Start'), function() {
            frappe.msgprint("Button clicked!");
        });
    }
});