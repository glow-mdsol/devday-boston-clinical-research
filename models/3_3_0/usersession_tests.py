#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 on 2018-05-12.
#  2018, SMART Health IT.


import os
import io
import unittest
import json
from . import usersession
from .fhirdate import FHIRDate


class UserSessionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("UserSession", js["resourceType"])
        return usersession.UserSession(js)
    
    def testUserSession1(self):
        inst = self.instantiate_from("usersession-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a UserSession instance")
        self.implUserSession1(inst)
        
        js = inst.as_json()
        self.assertEqual("UserSession", js["resourceType"])
        inst2 = usersession.UserSession(js)
        self.implUserSession1(inst2)
    
    def implUserSession1(self, inst):
        self.assertEqual(inst.context[0].type, "task")
        self.assertEqual(inst.context[0].valueCodeableConcept.text, "context-value")
        self.assertEqual(inst.created.date, FHIRDate("2017-11-15T17:31:00Z").date)
        self.assertEqual(inst.created.as_json(), "2017-11-15T17:31:00Z")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier.value, "usersession-1")
        self.assertEqual(inst.status.code, "active")
        self.assertEqual(inst.status.source, "system")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Example UserSession.</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.workstation.value, "computer-name")

