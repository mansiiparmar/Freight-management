# your_app/api.py
import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_sales_invoice_data(invoice_name):
    """Custom API to fetch Sales Invoice data."""
    try:
        invoice = frappe.get_doc("Sales Invoice", invoice_name)
        if invoice:
            return {
                "customer": invoice.customer,
                "grand_total": invoice.grand_total,
                "items": [{"item_code": item.item_code, "qty": item.qty} for item in invoice.items]
            }
        else:
            return {"error": _("Sales Invoice not found")}
    except Exception as e:
        return {"error": str(e)}
