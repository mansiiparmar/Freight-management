# import frappe
# from frappe.model.utils.rename_field import rename_field





# import frappe

# def execute():
#     doctype = "test"
#     fieldname = "test1"

#     if frappe.db.has_column(doctype, fieldname):
#         field_type = frappe.db.get_value("Custom Field", 
#                                          {"dt": doctype, "fieldname": fieldname}, 
#                                          "fieldtype")

#         if field_type == "Select":
#             # Convert 'Yes' to 1 and 'No' to 0 using parameterized queries
#             frappe.db.sql("""
#                 UPDATE `tabtest`
#                 SET test1 = 1 WHERE test1 = %s
#             """, ("Check",))

#             frappe.db.sql("""
#                 UPDATE `tabtest`
#                 SET test1 = 0 WHERE test1 = %s
#             """, ("UnCheck",))

#             # Update field type to Check (Checkbox)
#             frappe.db.set_value("Custom Field", 
#                                 {"dt": doctype, "fieldname": fieldname}, 
#                                 "fieldtype", 
#                                 "Check")

#     frappe.db.commit()



import frappe

def execute():
    doctype = "test"
    fieldname = "test1"

    if frappe.db.has_column(doctype, fieldname):
        # Get field type from tabDocField (for standard fields)
        field_type = frappe.db.get_value("DocField", 
                                         {"parent": doctype, "fieldname": fieldname}, 
                                         "fieldtype")

        if field_type == "Select":
            # Convert 'Yes' to 1 and 'No' to 0 using parameterized queries
            frappe.db.sql("""
                UPDATE `tab{doctype}`
                SET `{fieldname}` = 1 WHERE `{fieldname}` = %s
            """.format(doctype=doctype, fieldname=fieldname), ("Check",))

            frappe.db.sql("""
                UPDATE `tab{doctype}`
                SET `{fieldname}` = 0 WHERE `{fieldname}` = %s
            """.format(doctype=doctype, fieldname=fieldname), ("UnCheck",))

            # Update field type to Check (Checkbox) in DocField
            frappe.db.set_value("DocField", 
                                {"parent": doctype, "fieldname": fieldname}, 
                                "fieldtype", 
                                "Check")

            # Update in database schema
            frappe.db.sql_ddl(f"""
                ALTER TABLE `tab{doctype}`
                MODIFY `{fieldname}` TINYINT(1)
            """)

    frappe.db.commit()
