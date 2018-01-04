# -*- coding: utf-8 -*-
# Copyright (c) 2017, RSS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

from frappe.utils import getdate, nowdate
from frappe import _
from frappe.model.document import Document
from erpnext.hr.utils import set_employee_name

class Cuti(Document):
	pass
