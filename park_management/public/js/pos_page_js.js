erpnext.pos.PointOfSale = erpnext.pos.PointOfSale.extend({
  onload: function() {
    this._super();
    this.setinterval_to_sync_master_data(600000);
  },
  init_master_data: async function(r, freeze = true) {
    this._super(r);
    try {
      const { message: pos_data = {} } = await frappe.call({
        method: 'park_management.api.item.get_more_pos_data',
        args: {
          profile: this.pos_profile_data.name,
          company: this.doc.company,
        },
        freeze,
        freeze_message: __('Syncing Item details'),
      });

      await this.set_opening_entry();
      return pos_data;
    } catch (e) {
      frappe.msgprint({
        indicator: 'orange',
        title: __('Warning'),
        message: __(
          'Unable to load extended Item details. Usage will be restricted.'
        ),
      });
    }
  },
  setinterval_to_sync_master_data: function(delay) {
    setInterval(async () => {
      const { message } = await frappe.call({ method: 'frappe.handler.ping' });
      if (message) {
        const r = await frappe.call({
          method: 'erpnext.accounts.doctype.sales_invoice.pos.get_pos_data',
        });
        localStorage.setItem('doc', JSON.stringify(r.message.doc));
        this.init_master_data(r, false);
        this.load_data(false);
        this.make_item_list();
        this.set_missing_values();
      }
    }, delay);
  },
  set_opening_entry: async function() {
    const { message: pos_voucher } = await frappe.call({
      method: 'park_management.api.pos_voucher.get_unclosed',
      args: {
        user: frappe.session.user,
        pos_profile: this.pos_profile_data.name,
        company: this.doc.company,
      },
    });
    if (pos_voucher) {
      this.pos_voucher = pos_voucher;
    } else {
      const dialog = new frappe.ui.Dialog({
        title: __('Enter Opening Cash'),
        fields: [
          {
            fieldtype: 'Datetime',
            fieldname: 'period_from',
            label: __('Start Date Time'),
            default: frappe.datetime.now_datetime(),
          },
          {
            fieldtype: 'Currency',
            fieldname: 'opening_amount',
            label: __('Amount'),
          },
        ],
      });
      dialog.show();
      dialog.get_close_btn().hide();
      dialog.set_primary_action('Enter', async () => {
        try {
          const { message: voucher_name } = await frappe.call({
            method: 'park_management.api.pos_voucher.create_opening',
            args: {
              posting: dialog.get_value('period_from'),
              opening_amount: dialog.get_value('opening_amount'),
              company: this.doc.company,
              pos_profile: this.pos_profile_data.name,
            },
          });
          if (!voucher_name) {
            throw Exception;
          }
          this.pos_voucher = voucher_name;
        } catch (e) {
          frappe.msgprint({
            message: __('Unable to create POS Closing Voucher opening entry.'),
            title: __('Warning'),
            indicator: 'orange',
          });
        } finally {
          dialog.hide();
          dialog.$wrapper.remove();
        }
      });
    }
  },
  show_items_in_item_cart: function() {
    this._super();
    this.wrapper
      .find('.items')
      .find('.pos-bill-item > .cell:nth-child(3)')
      .each((i, el) => {
        const value = el.innerText;
        if (value !== '0') {
          el.innerText = flt(value, this.precision);
        }
      });
  },
  make_menu_list: function() {
    this._super();
    this.page.menu
      .find('a.grey-link:contains("Cashier Closing")')
      .parent()
      .hide();
    this.page.add_menu_item('POS Closing Voucher', async () => {
      if (this.connection_status) {
        if (!this.pos_voucher) {
          await this.set_opening_entry();
        }
        frappe.dom.freeze('Syncing');
        this.sync_sales_invoice();
        await frappe.after_server_call();
        frappe.set_route('Form', 'POS Closing Voucher', this.pos_voucher, {
          period_to: frappe.datetime.now_datetime(),
        });
        frappe.dom.unfreeze();
        this.pos_voucher = null;
      } else {
        frappe.msgprint({
          message: __('Please perform this when online.'),
        });
      }
    });
  },
  refresh_fields: function(update_paid_amount) {
    this.apply_pricing_rule();
    this.discount_amount_applied = false;
    this._calculate_taxes_and_totals();
    this.calculate_discount_amount();
    this.show_items_in_item_cart();
    this.set_taxes();
    this.calculate_outstanding_amount(update_paid_amount);
    this.set_totals();
    this.update_total_qty();
  },
  update_total_qty: function() {
    var me = this;
    var qty_total = 0;
    $.each(this.frm.doc['items'] || [], function(i, d) {
      if (d.item_code) {
        qty_total += d.qty;
      }
    });
    this.frm.doc.qty_total = qty_total;
    this.wrapper.find('.qty-total').text(this.frm.doc.qty_total);
  },
  create_invoice: function() {
    var me = this;
    var invoice_data = {};
    function get_barcode_uri(text) {
      return JsBarcode(document.createElement('canvas'), text, {
        height: 40,
        displayValue: false,
      })._renderProperties.element.toDataURL();
    }
    this.si_docs = this.get_doc_from_localstorage();
    if (this.frm.doc.offline_pos_name) {
      this.update_invoice();
    } else {
      this.frm.doc.offline_pos_name = $.now();
      this.frm.doc.pos_name_barcode_uri = get_barcode_uri(
        this.frm.doc.offline_pos_name
      );
      this.frm.doc.posting_date = frappe.datetime.get_today();
      this.frm.doc.posting_time = frappe.datetime.now_time();
      this.frm.doc.pos_total_qty = this.frm.doc.qty_total;
      this.frm.doc.pos_profile = this.pos_profile_data['name'];
      invoice_data[this.frm.doc.offline_pos_name] = this.frm.doc;
      this.si_docs.push(invoice_data);
      this.update_localstorage();
      this.set_primary_action();
    }
    return invoice_data;
  },
  sync_sales_invoice: function() {
    const me = this;

    // instead of replacing instance variables
    const si_docs = this.get_submitted_invoice() || [];
    const email_queue_list = this.get_email_queue() || {};
    const customers_list = this.get_customers_details() || {};

    if (si_docs.length || email_queue_list || customers_list) {
      frappe.call({
        method: "erpnext.accounts.doctype.sales_invoice.pos.make_invoice",
        freeze: true,
        args: {
          doc_list: si_docs,
          email_queue_list: email_queue_list,
          customers_list: customers_list
        },
        callback: function (r) {
          if (r.message) {
            me.freeze = false;
            me.customers = r.message.synced_customers_list;
            me.address = r.message.synced_address;
            me.contacts = r.message.synced_contacts;
            me.removed_items = r.message.invoice;
            me.removed_email = r.message.email_queue;
            me.removed_customers = r.message.customers;
            me.remove_doc_from_localstorage();
            me.remove_email_queue_from_localstorage();
            me.remove_customer_from_localstorage();
            me.prepare_customer_mapper();
            me.autocomplete_customers();
            me.render_list_customers();
          }
        }
      });
    }
  },
  refresh: function() {
    this._super();
    if (!this.pos_voucher) {
      this.set_opening_entry();
    }
  },
  make_customer: function() {
    this._super();
    const me = this;
    me.party_field.$input.on('awesomplete-select', async function(e) {
      const customer = e.target.value;
      me.customer_info = await _get_customer_info(customer);
      _validate_customer_info(me.customer_info);
    });
  },
  validate_add_to_cart: function() {
    const me = this;
    const current_item = this.items[0];

    const children_allowed = me.customer_info.pb_children_allowed;
    const child_items_length = this.frm.doc.items
      .filter((item) => item.item_name.includes('Resident Child'))
      .reduce((total, item) => total + item.qty, 0);
    if (current_item['item_name'].includes('Resident Child') && me.customer_info.lease_expired) {
      frappe.throw(__('Lease is already expired. Please pay for the entrance fee'));
    } else if (current_item['item_name'].includes('Resident Child') && child_items_length + 1 > children_allowed) {
      frappe.throw(__(`Only ${children_allowed} children allowed`));
    }

    const adults_allowed = me.customer_info.pb_adults_allowed;
    const adult_items_length = this.frm.doc.items
      .filter((item) => item.item_name.includes('Resident Adult'))
      .reduce((total, item) => total + item.qty, 0);
    if (current_item['item_name'].includes('Resident Adult') && me.customer_info.lease_expired) {
      frappe.throw(__('Lease is already expired. Please pay for the entrance fee'));
    } else if (current_item['item_name'].includes('Resident Adult') && adult_items_length + 1 > adults_allowed) {
      frappe.throw(__(`Only ${adults_allowed} adults allowed`));
    }
  }
});


async function _get_customer_info(customer) {
  const { message: customer_info } = await frappe.call({
    method: "park_management.api.customer.get_customer_info",
    freeze: true,
    args: { customer },
  });
  return customer_info;
}


function _validate_customer_info(customer_info) {
  if (customer_info.lease_expired) {
    frappe.msgprint(__('Lease is expired. Customer has to Pay'));
  }
}


erpnext.pos.PointOfSale = pos_bahrain.addons.extend_pos(
  erpnext.pos.PointOfSale
);
