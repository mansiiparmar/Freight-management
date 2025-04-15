
# import frappe
# from erpnext.selling.doctype.quotation.quotation import Quotation as ERPQuotation

# class Quotation(ERPQuotation):
#     def calculate_custom_total(self):
#         total = 0

#         for item in self.items:
#             # Most specific condition first
#             if item.qty and item.custom_freight_weight and item.custom_distancekm and item.rate:
#                 total += item.qty * item.custom_freight_weight * item.custom_distancekm * item.rate
#             elif item.custom_freight_weight and item.rate:
#                 total += item.custom_freight_weight * item.rate
#             elif item.custom_distancekm and item.rate:
#                 total += item.custom_distancekm * item.rate
#             elif item.qty and item.rate:
#                 total += (item.qty * item.rate) + 2  # Only this condition includes "+2"

#         self.total = total  # 'total' must be a custom field on the Quotation doctype