# import frappe
# from frappe import _
# def execute(filters=None):
#     columns,data=[],[]
#     columns = get_columns()
#     data = get_data(filters) if filters else []
#     return columns, data

# def get_columns():
#     columns= [
      
#         {
#           "fieldname":"shipper",
# 			"fieldtype":"Link",
# 			"options":"Shipper",
# 			"label":"Shipper",
# 			"width":120
#         }
#     ]
#     return columns

# def get_data(filters):
#     item = frappe.qb.DocType("Direct Shipment")
#     query = (
#         frappe.qb.from_(item)
#         .select(item.shipper)
#     )
#     data = query.run(as_dict=True)

#     return data
import frappe
from frappe.query_builder import DocType

def execute(filters=None):
    if not filters:
        filters = {}
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {
            "label": "Customer", 
            "fieldname": "user", 
            "fieldtype": "Data",
            # "options": "Direct Shipment", 
            "width": 150
            },
        {
        "label": "Shipper",
         "fieldname": "shipper",
         "fieldtype": "Link",
         "options": "Shipper", 
         "width": 200
         },
          {
            "label": "Customer", 
            "fieldname": "user", 
            "fieldtype": "Data",
            # "options": "Direct Shipment", 
            "width": 150
            },
          {
            "label": "Customer", 
            "fieldname": "user", 
            "fieldtype": "Data",
            # "options": "Direct Shipment", 
            "width": 150
            },
           {
            "label": "Transport Medium", 
            "fieldname": "transport_medium", 
            "fieldtype": "Link",
            "options": "Transportation Medium", 
            "width": 150
            }
    ]

def get_data(filters):
    DirectShipment = DocType("Direct Shipment")

    query = (
        frappe.qb.from_(DirectShipment)
        .select(DirectShipment.user, DirectShipment.shipper,DirectShipment.transport_medium)
    )

    if filters.get("shipper"):
        query = query.where(DirectShipment.shipper == filters["shipper"])

    return query.run(as_dict=True)
