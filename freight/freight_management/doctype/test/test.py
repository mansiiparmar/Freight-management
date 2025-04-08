# Copyright (c) 2025, admin and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

import frappe
from frappe.utils.password import get_decrypted_password
class test(Document):
	pass


@frappe.whitelist()
def get_password(docname):
    password = get_decrypted_password('test', docname, 'password')
    return password
