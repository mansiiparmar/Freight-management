
# import frappe
# from frappe.model.document import Document
# import random
# import string


# def after_insert(self,method=None):
#     back_jobb(self)
# def back_jobb(self,method=None):
#     frappe.enqueue(create_task,doc=self)

# def create_task(doc,method=None):
#     for i in range(5):
#         x = frappe.new_doc("Packages")
#         x.packages = "abc"
#         x.insert()