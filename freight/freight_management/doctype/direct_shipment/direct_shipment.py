# Copyright (c) 2025, admin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

# class DirectShipment(Document):
#     def generate_tracking_number(prefix, length=8):
#         random_digits = ''.join(random.choices(string.digits, k=length))
#         tracking_number = f"{self.destination}-{random_digits}"
#         return tracking_number
#     def autoname(self):
#         if self.direction == Import:
#         self.name = "I" + tracking_number
import random
import string

class DirectShipment(Document):
	
	# Method to generate tracking number
	def generate_tracking_number(self, length=8):
		# Generate a random string of digits with the specified length
		random_digits = ''.join(random.choices(string.digits, k=length))
		
		# Combine the destination and random digits for the tracking number
		tracking_number = f"{self.destination_location}-{random_digits}"
		return tracking_number

	# Method to set the name with tracking number
	def autoname(self):
		if self.direction == "Import":
			# Generate the tracking number
			tracking_number = self.generate_tracking_number()
			
			# Set the name with "I" prefix and the tracking number
			self.name = "I" + tracking_number
		else:
			tracking_number = self.generate_tracking_number()
			self.name = "E" + tracking_number
			
	# def after_insert(self):
	#     self.back_jobb()
	# def back_jobb(self,method=None):
	#     frappe.enqueue(self.create_task)

	# def create_task(self,method=None):
	#     for i in range(5):
	#         x = frappe.new_doc("Task")
	#         x.subject = "abc"
	#         x.insert()
	# def after_insert(self):
	# 	self.enqueue_example()
	# def enqueue_example(self,method=None):
	# 	frappe.enqueue(self.set_status)
	# def set_status(self,method=None):
	# 	frappe.msgprint("Done")
	# 	doc = frappe.get_doc("Direct Shipment","I[]-11116942")
	# 	doc.status = "Done"
	# 	doc.save()

  