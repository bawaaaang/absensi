# -*- coding: utf-8 -*-
# Copyright (c) 2018, RSS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class HakCuti(Document):

	def fill_employee_details(employees):
		return frappe.db.sql('''
			select
				t1.name as employee, t1.employee_name
			from
				`tabEmployee` t1, `tabSalary Structure Employee` t2
			where
				t1.docstatus!=2
				and t1.name = t2.employee
			'''({"employee": employee, "employee_name":employee_name}), as_dict=1)
