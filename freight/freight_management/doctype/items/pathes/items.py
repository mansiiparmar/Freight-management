
import frappe
def set_quantity():
    a = frappe.db.get_all("Items",fields=["name","quantity"])
    for i in a:
        if i.quantity == 0:
            frappe.db.set_value("Items",i.name,"quantity",1,update_modified=False)
        else:
            frappe.db.set_value("Items",i.name,"quantity",0,update_modified=False)
        