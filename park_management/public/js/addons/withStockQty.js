export default function withStockQty(Pos) {
    return class PosExtended extends Pos {
        submit_invoice() {
            super.submit_invoice();
            this._update_stock_qty();
        }
        _update_stock_qty() {
            const me = this;
            $.each(this.frm.doc.items || [], function(i, item) {
               const bin_qty = me.bin_data[item.item_code][item.warehouse];
               const qty = item.qty * item.conversion_factor;
               me.bin_data[item.item_code][item.warehouse] = bin_qty - qty;
            });
            this.items = this.get_items();
            this.make_item_list();
        }
    };
}