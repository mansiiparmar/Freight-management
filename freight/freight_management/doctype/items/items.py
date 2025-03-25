# Copyright (c) 2025, admin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Items(Document):
	def before_rename(self,old_name,new_name,merge=False):
		frappe.msgprint(f"Document about before rename from {old_name} to {new_name}")
	# def after_rename(self,old_name,new_name,merge=False):
	# 	frappe.msgprint(f"Document about after rename from {old_name} to {new_name}")
