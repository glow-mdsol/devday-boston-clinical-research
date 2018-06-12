#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 on 2018-05-12.
#  2018, SMART Health IT.


import os
import io
import unittest
import json
from . import verificationresult
from .fhirdate import FHIRDate


class VerificationResultTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("VerificationResult", js["resourceType"])
        return verificationresult.VerificationResult(js)
    
    def testVerificationResult1(self):
        inst = self.instantiate_from("verificationresult-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a VerificationResult instance")
        self.implVerificationResult1(inst)
        
        js = inst.as_json()
        self.assertEqual("VerificationResult", js["resourceType"])
        inst2 = verificationresult.VerificationResult(js)
        self.implVerificationResult1(inst2)
    
    def implVerificationResult1(self, inst):
        self.assertEqual(inst.failureAction, "none")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.need, "initial")
        self.assertEqual(inst.status, "attested")
        self.assertEqual(inst.statusDate.date, FHIRDate("2017-12-18").date)
        self.assertEqual(inst.statusDate.as_json(), "2017-12-18")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.validationProcess[0].text, "primary")
        self.assertEqual(inst.validationType, "primary")

