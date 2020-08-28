import frappe
from frappe import _
from toolz import first


@frappe.whitelist()
def get_customer_info(customer):
    customer = frappe.get_all(
        'Customer',
        filters={'name': customer},
        fields=['pb_lease_validity', 'pb_adults_allowed', 'pb_children_allowed']
    )
    if not customer:
        frappe.throw(_('Unable to find the customer'))
    return first(customer)
