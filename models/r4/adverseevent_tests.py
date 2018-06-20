#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 on 2018-05-12.
#  2018, SMART Health IT.


import os
import io
import unittest
import json
from . import adverseevent
from .fhirdate import FHIRDate


class AdverseEventTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("AdverseEvent", js["resourceType"])
        return adverseevent.AdverseEvent(js)
    
    def testAdverseEvent1(self):
        inst = self.instantiate_from("adverseevent-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a AdverseEvent instance")
        self.implAdverseEvent1(inst)
        
        js = inst.as_json()
        self.assertEqual("AdverseEvent", js["resourceType"])
        inst2 = adverseevent.AdverseEvent(js)
        self.implAdverseEvent1(inst2)
    
    def implAdverseEvent1(self, inst):
        self.assertEqual(inst.actuality, "actual")
        self.assertEqual(inst.category[0].coding[0].code, "ProductUseError")
        self.assertEqual(inst.category[0].coding[0].display, "Product Use Error")
        self.assertEqual(inst.category[0].coding[0].system, "http://hl7.org/fhir/adverse-event-category")
        self.assertEqual(inst.date.date, FHIRDate("2017-01-29T12:34:56+00:00").date)
        self.assertEqual(inst.date.as_json(), "2017-01-29T12:34:56+00:00")
        self.assertEqual(inst.event.coding[0].code, "304386008")
        self.assertEqual(inst.event.coding[0].display, "O/E - itchy rash")
        self.assertEqual(inst.event.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.event.text, "This was a mild rash on the left forearm")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier.system, "http://acme.com/ids/patients/risks")
        self.assertEqual(inst.identifier.value, "49476534")
        self.assertEqual(inst.seriousness.coding[0].code, "Non-serious")
        self.assertEqual(inst.seriousness.coding[0].display, "Non-serious")
        self.assertEqual(inst.seriousness.coding[0].system, "http://hl7.org/fhir/adverse-event-seriousness")
        self.assertEqual(inst.severity.coding[0].code, "Mild")
        self.assertEqual(inst.severity.coding[0].display, "Mild")
        self.assertEqual(inst.severity.coding[0].system, "http://hl7.org/fhir/adverse-event-severity")
        self.assertEqual(inst.text.status, "generated")
    
    def testAdverseEvent2(self):
        inst = self.instantiate_from("medicinalproductauthorization-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a AdverseEvent instance")
        self.implAdverseEvent2(inst)
        
        js = inst.as_json()
        self.assertEqual("AdverseEvent", js["resourceType"])
        inst2 = adverseevent.AdverseEvent(js)
        self.implAdverseEvent2(inst2)
    
    def implAdverseEvent2(self, inst):
        self.assertEqual(inst.actuality, "actual")
        self.assertEqual(inst.date.date, FHIRDate("2017-01-29T12:34:56+00:00").date)
        self.assertEqual(inst.date.as_json(), "2017-01-29T12:34:56+00:00")
        self.assertEqual(inst.event.coding[0].code, "304386008")
        self.assertEqual(inst.event.coding[0].display, "O/E - itchy rash")
        self.assertEqual(inst.event.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.event.text, "This was a mild rash on the left forearm")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier.system, "http://acme.com/ids/patients/risks")
        self.assertEqual(inst.identifier.value, "49476534")
        self.assertEqual(inst.seriousness.coding[0].code, "Non-serious")
        self.assertEqual(inst.seriousness.coding[0].display, "Non-serious")
        self.assertEqual(inst.seriousness.coding[0].system, "http://hl7.org/fhir/adverse-event-seriousness")
        self.assertEqual(inst.severity.coding[0].code, "Mild")
        self.assertEqual(inst.severity.coding[0].display, "Mild")
        self.assertEqual(inst.severity.coding[0].system, "http://hl7.org/fhir/adverse-event-severity")
        self.assertEqual(inst.text.status, "generated")
    
    def testAdverseEvent3(self):
        inst = self.instantiate_from("medicinalproductclinicals-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a AdverseEvent instance")
        self.implAdverseEvent3(inst)
        
        js = inst.as_json()
        self.assertEqual("AdverseEvent", js["resourceType"])
        inst2 = adverseevent.AdverseEvent(js)
        self.implAdverseEvent3(inst2)
    
    def implAdverseEvent3(self, inst):
        self.assertEqual(inst.actuality, "actual")
        self.assertEqual(inst.date.date, FHIRDate("2017-01-29T12:34:56+00:00").date)
        self.assertEqual(inst.date.as_json(), "2017-01-29T12:34:56+00:00")
        self.assertEqual(inst.event.coding[0].code, "304386008")
        self.assertEqual(inst.event.coding[0].display, "O/E - itchy rash")
        self.assertEqual(inst.event.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.event.text, "This was a mild rash on the left forearm")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier.system, "http://acme.com/ids/patients/risks")
        self.assertEqual(inst.identifier.value, "49476534")
        self.assertEqual(inst.seriousness.coding[0].code, "Non-serious")
        self.assertEqual(inst.seriousness.coding[0].display, "Non-serious")
        self.assertEqual(inst.seriousness.coding[0].system, "http://hl7.org/fhir/adverse-event-seriousness")
        self.assertEqual(inst.severity.coding[0].code, "Mild")
        self.assertEqual(inst.severity.coding[0].display, "Mild")
        self.assertEqual(inst.severity.coding[0].system, "http://hl7.org/fhir/adverse-event-severity")
        self.assertEqual(inst.text.status, "generated")
    
    def testAdverseEvent4(self):
        inst = self.instantiate_from("medicinalproductdevicespec-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a AdverseEvent instance")
        self.implAdverseEvent4(inst)
        
        js = inst.as_json()
        self.assertEqual("AdverseEvent", js["resourceType"])
        inst2 = adverseevent.AdverseEvent(js)
        self.implAdverseEvent4(inst2)
    
    def implAdverseEvent4(self, inst):
        self.assertEqual(inst.actuality, "actual")
        self.assertEqual(inst.date.date, FHIRDate("2017-01-29T12:34:56+00:00").date)
        self.assertEqual(inst.date.as_json(), "2017-01-29T12:34:56+00:00")
        self.assertEqual(inst.event.coding[0].code, "304386008")
        self.assertEqual(inst.event.coding[0].display, "O/E - itchy rash")
        self.assertEqual(inst.event.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.event.text, "This was a mild rash on the left forearm")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier.system, "http://acme.com/ids/patients/risks")
        self.assertEqual(inst.identifier.value, "49476534")
        self.assertEqual(inst.seriousness.coding[0].code, "Non-serious")
        self.assertEqual(inst.seriousness.coding[0].display, "Non-serious")
        self.assertEqual(inst.seriousness.coding[0].system, "http://hl7.org/fhir/adverse-event-seriousness")
        self.assertEqual(inst.severity.coding[0].code, "Mild")
        self.assertEqual(inst.severity.coding[0].display, "Mild")
        self.assertEqual(inst.severity.coding[0].system, "http://hl7.org/fhir/adverse-event-severity")
        self.assertEqual(inst.text.status, "generated")
    
    def testAdverseEvent5(self):
        inst = self.instantiate_from("medicinalproductingredient-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a AdverseEvent instance")
        self.implAdverseEvent5(inst)
        
        js = inst.as_json()
        self.assertEqual("AdverseEvent", js["resourceType"])
        inst2 = adverseevent.AdverseEvent(js)
        self.implAdverseEvent5(inst2)
    
    def implAdverseEvent5(self, inst):
        self.assertEqual(inst.actuality, "actual")
        self.assertEqual(inst.date.date, FHIRDate("2017-01-29T12:34:56+00:00").date)
        self.assertEqual(inst.date.as_json(), "2017-01-29T12:34:56+00:00")
        self.assertEqual(inst.event.coding[0].code, "304386008")
        self.assertEqual(inst.event.coding[0].display, "O/E - itchy rash")
        self.assertEqual(inst.event.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.event.text, "This was a mild rash on the left forearm")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier.system, "http://acme.com/ids/patients/risks")
        self.assertEqual(inst.identifier.value, "49476534")
        self.assertEqual(inst.seriousness.coding[0].code, "Non-serious")
        self.assertEqual(inst.seriousness.coding[0].display, "Non-serious")
        self.assertEqual(inst.seriousness.coding[0].system, "http://hl7.org/fhir/adverse-event-seriousness")
        self.assertEqual(inst.severity.coding[0].code, "Mild")
        self.assertEqual(inst.severity.coding[0].display, "Mild")
        self.assertEqual(inst.severity.coding[0].system, "http://hl7.org/fhir/adverse-event-severity")
        self.assertEqual(inst.text.status, "generated")
    
    def testAdverseEvent6(self):
        inst = self.instantiate_from("medicinalproductpackaged-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a AdverseEvent instance")
        self.implAdverseEvent6(inst)
        
        js = inst.as_json()
        self.assertEqual("AdverseEvent", js["resourceType"])
        inst2 = adverseevent.AdverseEvent(js)
        self.implAdverseEvent6(inst2)
    
    def implAdverseEvent6(self, inst):
        self.assertEqual(inst.actuality, "actual")
        self.assertEqual(inst.date.date, FHIRDate("2017-01-29T12:34:56+00:00").date)
        self.assertEqual(inst.date.as_json(), "2017-01-29T12:34:56+00:00")
        self.assertEqual(inst.event.coding[0].code, "304386008")
        self.assertEqual(inst.event.coding[0].display, "O/E - itchy rash")
        self.assertEqual(inst.event.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.event.text, "This was a mild rash on the left forearm")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier.system, "http://acme.com/ids/patients/risks")
        self.assertEqual(inst.identifier.value, "49476534")
        self.assertEqual(inst.seriousness.coding[0].code, "Non-serious")
        self.assertEqual(inst.seriousness.coding[0].display, "Non-serious")
        self.assertEqual(inst.seriousness.coding[0].system, "http://hl7.org/fhir/adverse-event-seriousness")
        self.assertEqual(inst.severity.coding[0].code, "Mild")
        self.assertEqual(inst.severity.coding[0].display, "Mild")
        self.assertEqual(inst.severity.coding[0].system, "http://hl7.org/fhir/adverse-event-severity")
        self.assertEqual(inst.text.status, "generated")
    
    def testAdverseEvent7(self):
        inst = self.instantiate_from("medicinalproductpharmaceutical-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a AdverseEvent instance")
        self.implAdverseEvent7(inst)
        
        js = inst.as_json()
        self.assertEqual("AdverseEvent", js["resourceType"])
        inst2 = adverseevent.AdverseEvent(js)
        self.implAdverseEvent7(inst2)
    
    def implAdverseEvent7(self, inst):
        self.assertEqual(inst.actuality, "actual")
        self.assertEqual(inst.date.date, FHIRDate("2017-01-29T12:34:56+00:00").date)
        self.assertEqual(inst.date.as_json(), "2017-01-29T12:34:56+00:00")
        self.assertEqual(inst.event.coding[0].code, "304386008")
        self.assertEqual(inst.event.coding[0].display, "O/E - itchy rash")
        self.assertEqual(inst.event.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.event.text, "This was a mild rash on the left forearm")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier.system, "http://acme.com/ids/patients/risks")
        self.assertEqual(inst.identifier.value, "49476534")
        self.assertEqual(inst.seriousness.coding[0].code, "Non-serious")
        self.assertEqual(inst.seriousness.coding[0].display, "Non-serious")
        self.assertEqual(inst.seriousness.coding[0].system, "http://hl7.org/fhir/adverse-event-seriousness")
        self.assertEqual(inst.severity.coding[0].code, "Mild")
        self.assertEqual(inst.severity.coding[0].display, "Mild")
        self.assertEqual(inst.severity.coding[0].system, "http://hl7.org/fhir/adverse-event-severity")
        self.assertEqual(inst.text.status, "generated")

