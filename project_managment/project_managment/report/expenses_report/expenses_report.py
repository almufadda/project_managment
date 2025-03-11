import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data()
    return columns, data

def get_columns():
    return [
        {"label": "Parent Name", "fieldname": "parent", "fieldtype": "Data", "width": 200},
        {"label": "Expense Amount", "fieldname": "amount", "fieldtype": "Float", "width": 150}
    ]

def get_data():
    return frappe.db.sql("""
        SELECT 
            e.name AS parent, 
            ei.amount AS amount
        FROM `tabExpenses` e
        JOIN `tabExpenses Item` ei ON ei.parent = e.name
        ORDER BY e.name ASC
    """, as_dict=True)
