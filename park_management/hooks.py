# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__

app_name = "park_management"
app_version = __version__
app_title = "Park Management"
app_publisher = "9t9it"
app_description = "Pos Customization"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@9t9it.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/css/pos_css.css"
# app_include_js = "/assets/park_management/js/park_management.js"
app_include_css = "/assets/css/jmi.min.css"
app_include_js = [
    "/assets/js/jmi.min.js",
    "/assets/js/park_management.min.js",
    "/assets/park_management/js/batch_quick_entry.js",
]

# include js, css files in header of web template
# web_include_css = "/assets/park_management/css/park_management.css"
# web_include_js = "/assets/park_management/js/park_management.js"

# include js in page
page_js = {
    "pos": "public/js/pos_page_js.js",
    "point-of-sale": "public/js/pos_page_js.js",
}

# include js in doctype views
doctype_js = {
    "Mode of Payment": "public/js/mode_of_payment.js",
    "Stock Entry": ["public/js/includes/scan_barcode.js", "public/js/stock_entry.js"],
    "Company": "public/js/company.js",
    "Sales Invoice": [
        "public/js/alternate_discount.js",
        "public/js/includes/scan_barcode.js",
    ],
    "Sales Order": "public/js/alternate_discount.js",
    "Purchase Invoice": [
        "public/js/set_retail_price.js",
        "public/js/includes/scan_barcode.js",
    ],
    "Purchase Order": "public/js/set_retail_price.js",
    "Purchase Receipt": "public/js/includes/scan_barcode.js",
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
                    "Sales Invoice-pos_total_qty",
                    "Mode of Payment-currency_section",
                    "Mode of Payment-in_alt_currency",
                    "Mode of Payment-alt_currency",
                    "Mode of Payment-pb_alt_col",
                    "Mode of Payment-pb_bank_method",
                    "POS Profile-pb_max_discount",
                    "Sales Invoice Payment-pos_section",
                    "Sales Invoice Payment-mop_currency",
                    "Sales Invoice Payment-cb11",
                    "Sales Invoice Payment-mop_conversion_rate",
                    "Sales Invoice Payment-mop_amount",
                    "Sales Invoice Payment-pb_ref_sec",
                    "Sales Invoice Payment-pb_reference_no",
                    "Sales Invoice Payment-pb_reference_date",
                    "Batch-naming_series",
                    "Company-default_warehouse",
                    "Sales Invoice-pb_set_cost_center",
                    "Sales Invoice-pb_sales_employee",
                    "Sales Invoice-pb_sales_employee_name",
                    "Sales Invoice-discount_on_retail_price",
                    "Sales Invoice Item-other_prices_section",
                    "Sales Invoice Item-retail_price",
                    "Sales Invoice Item-discount_percentage_on_retail",
                    "Sales Order-discount_on_retail_price",
                    "Sales Order Item-other_prices_section",
                    "Sales Order Item-retail_price",
                    "Sales Order Item-discount_percentage_on_retail",
                    "Purchase Receipt-pb_scan_barcode",
                    "Purchase Invoice-pb_set_cost_center",
                    "Purchase Invoice Item-retail_price",
                    "Purchase Invoice Item-pb_supplier_part_no",
                    "Purchase Receipt Item-pb_supplier_part_no",
                    "Purchase Order-pb_get_items_from_default_supplier",
                    "Purchase Order Item-pb_supplier_part_no",
                    "Purchase Order Item-retail_price",
                    "Purchase Order Item-pb_actual_qty",
                    "Batch-pb_price_sec",
                    "Batch-pb_price_based_on",
                    "Batch-pb_price_col",
                    "Batch-pb_rate",
                    "Batch-pb_discount",
                    "Sales Order Item-batch_no",
                    "Item Barcode-pb_uom",
                    "Purchase Receipt Item-pb_expiry_date",
                    "Purchase Invoice Item-pb_expiry_date",
                    "Stock Entry Detail-pb_expiry_date",
                    "Journal Entry-pb_is_cheque",
                    "Payment Entry Reference-pb_invoice_date",
                    "Item Price-pb_conversion_factor",
                    "Item Price-pb_customer_name",
                    "Payment Entry-pb_posting_time",
                    "Customer-pb_children_allowed",
                    "Customer-pb_adults_allowed",
                    "Customer-pb_lease_validity",
                    "Customer-pb_customer_cb",
                    "Customer-pb_city",
                    "Customer-pb_building_no",
                    "Customer-pb_building_name",
                    "Customer-pb_cpr_expiry_date",
                    "Customer-pb_country",
                    "Customer-pb_area_name",
                    "Customer-pb_road_name",
                    "Customer-pb_road_no",
                    "Customer-pb_flat_no",
                    "Customer-pb_property_card_no",
                    "Customer-pb_cpr_no",
                    "Customer-pb_customer_sb"
                ],
            ]
        ],
    },
    {
        "doctype": "Property Setter",
        "filters": [
            [
                "name",
                "in",
                [
                    "Batch-search_fields",
                    "Batch-batch_id-reqd",
                    "Batch-batch_id-bold",
                    "Batch-expiry_date-in_list_view",
                    "Batch-expiry_date-bold",
                    "Sales Invoice Item-discount_percentage-precision",
                    "Sales Invoice Item-discount_percentage-depends_on",
                    "Sales Order Item-discount_percentage-precision",
                    "Sales Order Item-discount_percentage-depends_on",
                    "Payment Entry Reference-total_amount-in_list_view",
                ],
            ]
        ],
    },
]

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "park_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "park_management.install.before_install"
# after_install = "park_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "park_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Sales Invoice": {
        "validate": "park_management.doc_events.sales_invoice.validate",
        "before_save": "park_management.doc_events.sales_invoice.before_save",
        "on_submit": "park_management.doc_events.sales_invoice.on_submit",
    },
    "Purchase Receipt": {
        "before_save": "park_management.doc_events.purchase_receipt.before_validate",
        "on_submit": "park_management.doc_events.purchase_receipt.set_batch_references",
    },
    "Purchase Invoice": {
        "before_save": [
            "park_management.doc_events.purchase_invoice.before_validate",
            "park_management.doc_events.purchase_invoice.before_save",
        ],
        "on_submit": "park_management.doc_events.purchase_receipt.set_batch_references",
    },
    "Payment Entry": {
        "before_save": "park_management.doc_events.payment_entry.before_save"
    },
    "Stock Entry": {
        "before_save": "park_management.doc_events.stock_entry.before_validate",
        "on_submit": "park_management.doc_events.purchase_receipt.set_batch_references",
    },
    "Item Price": {"before_save": "park_management.doc_events.item_price.before_save"},
    "Bin": {"on_update": "park_management.doc_events.bin.on_update"},
    "Bank Reconciliation": {
        "get_payment_entries": "park_management.doc_events.bank_reconciliation.get_payment_entries",
        "update_clearance_date": "park_management.doc_events.bank_reconciliation.update_clearance_date",
    },
}

boot_session = "park_management.doc_events.boot.boot_session"
on_session_creation = "park_management.doc_events.set_user_defaults"

# Scheduled Tasks
# ---------------

scheduler_events = {
    "daily": ["park_management.scheduler_events.daily.send_email_to_manager"]
}
# scheduler_events = {
# 	"all": [
# 		"park_management.tasks.all"
# 	],
# 	"daily": [
# 		"park_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"park_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"park_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"park_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "park_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
override_whitelisted_methods = {
    "erpnext.stock.get_item_details.get_item_details": "park_management.api.get_item_details.get_item_details",  # noqa
    "erpnext.accounts.doctype.sales_invoice.pos.get_pos_data": "park_management.api.item.get_pos_data",  # noqa
    "erpnext.accounts.doctype.sales_invoice.pos.make_invoice": "park_management.api.pos.make_invoice",  # noqa
    "erpnext.selling.page.point_of_sale.point_of_sale.search_serial_or_batch_or_barcode_number": "park_management.api.item.search_serial_or_batch_or_barcode_number",  # noqa
}
