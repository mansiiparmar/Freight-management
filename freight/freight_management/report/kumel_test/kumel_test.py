# Copyright (c) 2025, admin and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.query_builder import DocType


def execute(filters: dict | None = None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    return [
        {
            "label": _("Customer Name"),
            "fieldname": "customer_name",
            "fieldtype": "Data",
        },
        {
            "label": _("Lead"),
            "fieldname": "lead_name",
            "fieldtype": "Data",
			"width":"100px"
        },
    ]


def get_data(filters):
    Customer = DocType("Customer")
    Lead = DocType("Lead")

    query = (
        frappe.qb.from_(Customer)
        .inner_join(Lead)
        .on(Customer.lead_name == Lead.name)
        .select(Customer.customer_name, Lead.first_name.as_("lead_name"))
    )

    if filters and filters.get("customer_name"):
        query = query.where(Customer.customer_name.like(f"%{filters.get('customer_name')}%"))

    result = query.run(as_dict=True)
    return result


# def get_data(filters):
	

	# customer = frappe.db.get_all("Customer",fields=["customer_name","lead_name"])
	# return [{"customer_name":i.customer_name,"lead_name":i.lead_name} for i in customer ]

# def get_data(filters):
#     conditions = []

#     # Apply filter if provided
#     if filters and filters.get("customer_name"):
#         conditions.append(["customer_name", "like", f"%{filters.get('customer_name')}%"])

#     customer = frappe.get_all(
#         "Customer",
#         fields=["customer_name", "lead_name"],
#         filters=conditions
#     )

#     return [{"customer_name": i.customer_name, "lead_name": i.lead_name} for i in customer]


# def get_data(filters):
#     Customer = DocType("Customer")
	
#     query = (
#         frappe.qb.from_("Customer")
#         .select(Customer.customer_name, Customer.lead_name)
#     )

#     if filters and filters.get("customer_name"):
#         query = query.where(Customer.customer_name.like(f"%{filters.get('customer_name')}%"))

#     result = query.run(as_dict=True)

#     return result\\

