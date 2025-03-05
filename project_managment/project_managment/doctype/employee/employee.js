// Copyright (c) 2025, almufadda and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Employee", {
// 	refresh(frm) {

// 	},
// });
// Client-side script (e.g., in Frappe/ERPNext)

frappe.ui.form.on('Employee', {
    before_save: function(frm) {
        // Combine First Name and Last Name, trim extra spaces
        const firstName = frm.doc.first_name || '';
        const lastName = frm.doc.last_name || '';
        frm.set_value('full_name', `${firstName} ${lastName}`.trim());
    }
});
