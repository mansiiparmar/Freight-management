import frappe
from erpnext.crm.doctype.lead.lead import Lead
from frappe import _

class CustomLead(Lead):
    def validate_email_id(self):
            if self.email_id:
                # if not self.flags.ignore_email_validation:
                #     validate_email_address(self.email_id, throw=True)

                if self.email_id == self.lead_owner:
                    frappe.throw(_("Lead Owner cannot be same as the Lead Email Address"))

                # if self.is_new() or not self.image:
                #     self.image = has_gravatar(self.email_id)
    def set_full_name(self):
        if self.first_name:
            self.lead_name = " ".join(filter(None, [self.salutation, self.first_name,self.last_name]))
