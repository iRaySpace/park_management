// Copyright (c) 2018, 	9t9it and contributors
// For license information, please see license.txt

frappe.ui.form.off('Stock Entry Detail', 'item_code');
frappe.ui.form.on(
  'Stock Entry Detail',
  'item_code',
  pos_bahrain.scripts.extensions.stock_entry_item_code
);
