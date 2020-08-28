import frappe
from frappe import _
from frappe.utils import nowdate, date_diff
from toolz import first


@frappe.whitelist()
def get_customer_info(customer):
    def make_data(row):
        lease_validity = row.get('pb_lease_validity')
        row['lease_expired'] = date_diff(lease_validity, nowdate()) < 0
        return row
    customer = frappe.get_all(
        'Customer',
        filters={'name': customer},
        fields=['pb_lease_validity', 'pb_adults_allowed', 'pb_children_allowed']
    )
    if not customer:
        frappe.throw(_('Unable to find the customer'))
    return first(map(make_data, customer))
