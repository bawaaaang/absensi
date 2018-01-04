// Copyright (c) 2018, RSS and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Hak Cuti', {
//	refresh: function(frm) {

//	}
// });

frappe.ui.form.on('Hak Cuti', {
	refresh: function(frm) {
	},
});

cur_frm.cscript.get_employees = function (doc) {
	var callback = function (r) {
		if (r.docs[0].employees){
			cur_frm.refresh_field('employees');
		}
	};
	return $c('runserverobj', { 'method': 'fill_employee_details', 'docs': doc }, callback);
};
