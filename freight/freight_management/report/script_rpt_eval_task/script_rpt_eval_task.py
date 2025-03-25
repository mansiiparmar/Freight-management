import frappe

def execute(filters=None):
    
    columns = get_columns()
    data = get_data()
    return columns, data

def get_columns():
    return [
            {
            "label": "Item List",
            "fieldname": "Item_name",
            "fieldtype": "Data",
            "width": 150
        },
         {
            "label": "Items Name",
            "fieldname": "Names",
            "fieldtype": "Data",
            "width": 150
        },
      
        # {
        #     "label": "Item Quantity",
        #     "fieldname": "Item_Quantity",
        #     "fieldtype": "Int",
        #     "width": 150
        # },
        {
            "label": "Item Description",
            "fieldname": "Item_Description",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Item Packages",
            "fieldname": "Item_Packages",
            "fieldtype": "Link",
            "options": "Packages",
            "width": 150
        },
     
        #   {
        #     "label": "Total Volume CBM",
        #     "fieldname": "Total_Volume_CBM",
        #     "fieldtype": "Data",
        #     "width": 150
        # },
        # {
        #     "label": "Total Item weight",
        #     "fieldname": "Total_gross_weight",
        #     "fieldtype": "Float",
        #     "width": 150
        # },
        {
            "label": "Packages Packages",
            "fieldname": "Package_Packages",
            "fieldtype": "Data",
            "width": 150
        },
           {
            "label": "Total Gross Weight",
            "fieldname": "Total_gross_weight",
            "fieldtype": "Foat",
            "width": 150
        }
    ]

def get_data():
    data = frappe.db.sql("""
        select 
        count(Items.name) as Item_name,
        Items.name as Names,
        Items.description AS Item_Description,
        Items.packages AS Item_Packages,
        Items.quantity AS Item_Quantity,
        Items.volume_cbm AS Total_Volume_CBM,
        Packages.quantity AS Package_Quantity,
        Packages.packages as Package_Packages,
        Items.gross_weight_kg * Items.quantity as Total_gross_weight
        FROM `tabItems` AS Items
        
        right join `tabPackages` AS Packages
            ON Items.packages = Packages.packages
        GROUP BY Items.packages
    """, as_dict=True)
    
    return data

# import frappe
# from frappe.query_builder import DocType
# def execute(filters=None):
#     if not filters:
#         filters={}
#     columns = get_columns()
#     data = get_data(filters)
#     return columns, data

# def get_columns():
#     return [
#           {
#             "label": "Item Name",
#             "fieldname": "Item_name",
#             "fieldtype": "Data",
#             "width": 150
#         },
#         {
#             "label": "Item Quantity",
#             "fieldname": "Item_Quantity",
#             "fieldtype": "Int",
#             "width": 150
#         },
#         {
#             "label": "Item Description",
#             "fieldname": "Item_Description",
#             "fieldtype": "Data",
#             "width": 150
#         },
#         {
#             "label": "Item Packages",
#             "fieldname": "Item_Packages",
#             "fieldtype": "Link",
#             "options": "Packages",
#             "width": 150
#         },
#         {
#             "label": "Package Quantity",
#             "fieldname": "Package_Quantity",
#             "fieldtype": "Int",
#             "width": 150
#         },
#           {
#             "label": "Total Volume CBM",
#             "fieldname": "Total_Volume_CBM",
#             "fieldtype": "Data",
#             "width": 150
#         },
#         {
#             "label": "Total Item weight",
#             "fieldname": "Total_gross_weight",
#             "fieldtype": "Float",
#             "width": 150
#         }
#         # {
#         #     "label": "Volume CBM",
#         #     "fieldname": "volum_cbm",
#         #     "fieldtype": "Float",
#         #     "width": 150
#         # }
#     ]

# def get_data(filters):
#     select_query = """
#         select 
#         # count(Items.name) as Item_name,
#         Items.description AS Item_Description,
#         Items.packages AS Item_Packages,
#         Items.quantity AS Item_Quantity,
#         Items.volume_cbm AS Total_Volume_CBM,
#         Packages.quantity AS Package_Quantity,
#         Items.gross_weight_kg * Items.quantity as Total_gross_weight
#         FROM `tabItems` AS Items
#         left join `tabPackages` AS Packages
#             ON Items.packages = Packages.packages
#         # GROUP BY Items.packages
#     """
#     if filters.get("Item_Packages"):
#         select_query+= "Where Items.packages = %(Item_Packages)s"
#     data=frappe.db.sql(select_query,filters,as_dict=True)
#     return data
