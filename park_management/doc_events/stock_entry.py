# -*- coding: utf-8 -*-
# Copyright (c) 2019, 	9t9it and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

from park_management.doc_events.purchase_receipt import set_or_create_batch


def before_validate(doc, method):
    if doc.purpose == "Material Receipt":
        set_or_create_batch(doc, method)
