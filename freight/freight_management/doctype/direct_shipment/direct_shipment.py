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
        tracking_number = f"{self.destination}-{random_digits}"
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
            
# @frappe.whitelist()
# def display(document):
#     doc=frappe.get_doc("Direct Shipment",document)
#     return "done"
@frappe.whitelist()
def show(document):
    doc=frappe.get_doc("Direct Shipment",document)
    return "done"
        # doc=frappe.get_doc("Direct Shipment",document)
