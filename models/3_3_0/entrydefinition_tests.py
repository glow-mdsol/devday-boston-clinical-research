#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 on 2018-05-12.
#  2018, SMART Health IT.


import os
import io
import unittest
import json
from . import entrydefinition
from .fhirdate import FHIRDate


class EntryDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("EntryDefinition", js["resourceType"])
        return entrydefinition.EntryDefinition(js)
    
    def testEntryDefinition1(self):
        inst = self.instantiate_from("entrydefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a EntryDefinition instance")
        self.implEntryDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("EntryDefinition", js["resourceType"])
        inst2 = entrydefinition.EntryDefinition(js)
        self.implEntryDefinition1(inst2)
    
    def implEntryDefinition1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.purpose.text, "NoPurpose")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")

