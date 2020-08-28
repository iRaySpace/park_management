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
      {
        fieldtype: 'Select',
        fieldname: 'vat_type',
        label: 'VAT Type',
        reqd: 1,
        options: [
          'Standard Rated',
          'Zero Rated',
          'Exempted',
          'Imported',
          'Out of Scope',
        ],
        default: 'Standard Rated',
      },
    ],
  };
}
