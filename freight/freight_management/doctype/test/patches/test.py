import frappe
def execute():
    a = frappe.db.get_all("test",fields=["name","status"])
    for i in a:
        if i.status == 1:
            frappe.db.set_value("test",i.name,"test","a",update_modified=False)
        else:
            frappe.db.set_value("test",i.name,"test","b",update_modified=False)
        
