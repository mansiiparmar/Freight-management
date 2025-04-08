import frappe
from frappe.query_builder import DocType, functions as fn

def execute(filters=None):
    columns = get_column() 
    data = get_data()     
    return columns, data   

def get_column():
    return [
        {
            "label": "Items",
            "fieldname": "Items_name",
            "fieldtype": "Data",
            "width": 150
        },
           {
            "label": "Item Packages",
            "fieldname": "Items_Packages",
            "fieldtype": "Data",
            "width": 150
        },
        #    {
        #     "label": "Item Name",
        #     "fieldname": "Names",
        #     "fieldtype": "Data",
        #     "width": 150
        # },
        {
            "label": "Item Description",
            "fieldname": "Item_Description",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Item Quantity",
            "fieldname": "Items_Quantity",
            "fieldtype": "Int",
            "width": 150
        },
        {
            "label": "Package Quantity",
            "fieldname": "Package_Quantity",
            "fieldtype": "Int",
            "width": 150
        }
         
    ]

def get_data():
    Items = DocType("Items")  
    Packages = DocType("Packages")

    query = (
        frappe.qb.from_(Items)  
        .left_join(Packages)
        .on(Items.packages == Packages.name) 
        .select(
            fn.Count(Items.name).as_("Items_name"), 
         
            Items.description.as_("Item_Description"),
            Items.quantity.as_("Items_Quantity"),
            Packages.quantity.as_("Package_Quantity"),
            Items.packages.as_("Items_Packages")
        )
        .groupby(Items.packages) 
    )

    data = query.run(as_dict=True)  
    return data  
