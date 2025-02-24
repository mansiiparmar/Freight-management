import json
import os

import frappe


def after_migrate():
	create_custom_fields()
	create_property_setter()


def create_custom_fields():
	CUSTOM_FIELDS = {}
	print("Creating/Updating Custom Fields....")
	path = os.path.join(os.path.dirname(__file__), "freight_management/custom_fields")
	for file in os.listdir(path):
		with open(os.path.join(path, file), "r") as f:
			CUSTOM_FIELDS.update(json.load(f))
	from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

	create_custom_fields(CUSTOM_FIELDS)


def create_property_setter():
	from frappe import make_property_setter

	PPS = {}
	print("Creating/Updating Property Setter....")
	path = os.path.join(os.path.dirname(__file__), "freight_management/property_setter")
	for file in os.listdir(path):
		with open(os.path.join(path, file), "r") as f:
			args = json.load(f)
			PPS.update(args)

	for row in PPS:
		for field in PPS[row]:
			if isinstance(field.get("value"), list):
				field["value"] = json.dumps(field["value"])
			if field.get("field_name"):
				field["fieldname"] = field.get("field_name")
			make_property_setter(field, is_system_generated=False)
