# Copyright (c) 2025, admin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Packages(Document):
	# pass
	def after_insert(self):
		frappe.enqueue(self.set_status)
	def set_status(self,method=None):
		frappe.msgprint("Done")
		doc = frappe.new_doc("Items")
		doc.packages=self.packages	
		doc.operation=self.operation
		doc.save()

  
	def before_insert(self):
		if not self.quantity:
			frappe.throw("Quantity is required")
	def before_validate(self):
		if self.volumecbm:
			if self.volumecbm<=25:
				frappe.throw("Add Volume atlease 25, Validate")
		else:
			frappe.throw("Volume CBM is empty")
	def validate(self):
		if not self.description:
			frappe.throw("Description Required")	
		# self.gross_weightkg=200
	def after_insert(self):
		frappe.msgprint(f"Thank You {self.name}")
	def on_update(self):
		frappe.msgprint("update successfully")
	def before_submit(self):
		if not self.operation:
			frappe.throw("please enter opertaions")
	def on_submit(self):
		frappe.msgprint(f"After Submit {self.name}")
	def before_cancel(self):
		frappe.msgprint("before cancel document")
	def on_cancel(self):
		frappe.msgprint(f"After cancler {self.name}")
	def on_trash(self):
		frappe.msgprint("Before Delete Document")
	def after_delete(self):
		frappe.msgprint(f"{self.name}Deleted Successfully")
	# def on_update_after_submit(self):
	# 	frappe.throw("before update submited documents")
	def before_print(self,print_settings=None):
		frappe.msgprint("Preaper documents for print")
		if print_settings:
			frappe.msgprint(f"print settings {print_settings}")
	def before_rename(self,old_name,new_name,merge=False):
		frappe.msgprint(f"Document rename from {old_name} to {new_name}")
