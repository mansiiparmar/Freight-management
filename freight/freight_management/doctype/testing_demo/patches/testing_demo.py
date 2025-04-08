import frappe
from frappe.utils import getdate,today
def execute():
	doc=frappe.db.get_all("Testing Demo",fields=['name','due_date'])
	for i in doc:
		if i.due_date:
			due_date=getdate(i.due_date)
			to_date=getdate(today())
			if due_date>to_date:
				frappe.db.set_value("Testing Demo",i.name,"priority","High",update_modified=False)
			else:
				frappe.db.set_value("Testing Demo",i.name,"priority","Medium",update_modified=False)