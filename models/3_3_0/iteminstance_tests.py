#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 on 2018-05-12.
#  2018, SMART Health IT.


import os
import io
import unittest
import json
from . import iteminstance
from .fhirdate import FHIRDate


class ItemInstanceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ItemInstance", js["resourceType"])
        return iteminstance.ItemInstance(js)
    
    def testItemInstance1(self):
        inst = self.instantiate_from("iteminstance-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ItemInstance instance")
        self.implItemInstance1(inst)
        
        js = inst.as_json()
        self.assertEqual("ItemInstance", js["resourceType"])
        inst2 = iteminstance.ItemInstance(js)
        self.implItemInstance1(inst2)
    
    def implItemInstance1(self, inst):
        self.assertEqual(inst.count, 1)
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")

