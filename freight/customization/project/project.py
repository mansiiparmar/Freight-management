from frappe import _
import frappe
def get_data(data=None):
    # Fetch tasks where is_group is not ticked (False)
    tasks = frappe.get_all("Task", filters={"is_group": False}, fields=["name", "project"])
    

    return {
        
        "heatmap": True,
        "heatmap_message": _("This is based on the Time Sheets created against this project"),
        "fieldname": "project",
        "transactions": [
            {
                "label": _("Project"),
                "items": ["Task", "Timesheet", "Issue", "Project Update"],
            },
            {"label": _("Material"), "items": ["Material Request", "BOM", "Stock Entry"]},
            {"label": _("Sales"), "items": ["Sales Order", "Delivery Note", "Sales Invoice"]},
            {"label": _("Purchase"), "items": ["Purchase Order", "Purchase Receipt", "Purchase Invoice"]},
        ],
        "tasks": tasks 
    }
