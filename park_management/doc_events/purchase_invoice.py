# -*- coding: utf-8 -*-
# Copyright (c) 2019, 	9t9it and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

from park_management.doc_events.purchase_receipt import set_or_create_batch
from park_management.doc_events.sales_invoice import set_cost_center


def before_validate(doc, method):
    set_or_create_batch(doc, method)


def before_save(doc, method):
    set_cost_center(doc)
