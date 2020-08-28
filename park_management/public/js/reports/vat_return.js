export default function () {
  return {
    filters: [
      {
        fieldtype: 'DateRange',
        fieldname: 'date_range',
        label: 'Date Range',
        reqd: 1,
        default: [frappe.datetime.month_start(), frappe.datetime.month_end()],
      },
    ],
    formatter: function (value, row, column, data, default_formatter) {
      const formatted = default_formatter(value, row, column, data);
      if (data.bold) {
        return $(`<span>${formatted}</span>`)
          .css('font-weight', 'bold')
          .wrap('<p />')
          .parent()
          .html();
      }
      return formatted;
    },
  };
}
