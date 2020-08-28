import { load_filters_on_load } from './utils';

export default function () {
  return {
    onload: load_filters_on_load('Sales Register', (filters) => [
      ...filters,
      {
        fieldname: 'sales_employee',
        label: __('Sales Employee'),
        fieldtype: 'Link',
        options: 'Employee',
      },
    ]),
    filters: [],
  };
}
