#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 on 2018-05-12.
#  2018, SMART Health IT.


import os
import io
import unittest
import json
from . import medicinalproduct
from .fhirdate import FHIRDate


class MedicinalProductTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProduct", js["resourceType"])
        return medicinalproduct.MedicinalProduct(js)
    
    def testMedicinalProduct1(self):
        inst = self.instantiate_from("medicinalproduct-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicinalProduct instance")
        self.implMedicinalProduct1(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicinalProduct", js["resourceType"])
        inst2 = medicinalproduct.MedicinalProduct(js)
        self.implMedicinalProduct1(inst2)
    
    def implMedicinalProduct1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier.value, "example")
        self.assertEqual(inst.name[0].countryLanguage[0].country.coding[0].code, "code")
        self.assertEqual(inst.name[0].countryLanguage[0].language.coding[0].code, "code")
        self.assertEqual(inst.name[0].fullName, "name")
        self.assertEqual(inst.text.status, "generated")

