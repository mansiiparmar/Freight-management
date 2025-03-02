import frappe
from frappe.model.mapper import get_mapped_doc

# # @frappe.whitelist()
# # def create_shipment_order(Sales Invoice, DIrect Shipment=None):
# #     def set_missing_values(source, target):
# #         customer = user  # Link Sales Invoice
#         # target.customer = source.customer
#         # target.customer_address = source.customer_address
#         # target.sales_order_ref = source.sales_order  # Map Sales Order to a different field
#         # target.status = "In Transportation"  # Default status

@frappe.whitelist()
def create_shipment_order(source,target=None,ignore_permissions= True):

	doclist= get_mapped_doc("Sales Invoice", source,{
		"Sales Invoice":{"doctype":"Direct Shipment",
		"field_map":{

			'customer':'user',
            'posting_date':'date',
            'custom_type_of_shipment':'type_of_shipment',
            'custom_transportation_medium':'transport_medium',
            'custom_origin_location':'origin_location',
            'custom_destination_location':'destination_location',
            'custom_freight_weight_expected':'freight_weight_expected',
            'custom_preferred_transporter':'preferred_transporter'
			
		},
		}
		})
	return doclist