import frappe
from frappe.model.document import Document

class Quotation(Document):
    def validate(self):
        super(Quotation, self).validate()

        total = 0
        # Loop through all the items in the quotation and calculate total based on qty or custom_freight_weight
        for item in self.items:
            if item.custom_freight_weight and item.rate:
                item.total = item.custom_freight_weight * item.rate
            elif item.qty and item.rate:
                item.total = item.qty * item.rate
            total += item.total

        # Update the total field in the Quotation doc
        self.total = total
