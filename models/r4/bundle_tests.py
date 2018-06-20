#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 on 2018-05-12.
#  2018, SMART Health IT.


import os
import io
import unittest
import json
from . import bundle
from .fhirdate import FHIRDate


class BundleTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Bundle", js["resourceType"])
        return bundle.Bundle(js)
    
    def testBundle1(self):
        inst = self.instantiate_from("bundle-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle1(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle1(inst2)
    
    def implBundle1(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "https://example.com/base/MedicationRequest/3123")
        self.assertEqual(inst.entry[0].resource.id, "3123")
        self.assertEqual(inst.entry[0].search.mode, "match")
        self.assertEqual(inst.entry[0].search.score, 1)
        self.assertEqual(inst.entry[1].fullUrl, "https://example.com/base/Medication/example")
        self.assertEqual(inst.entry[1].resource.id, "example")
        self.assertEqual(inst.entry[1].search.mode, "include")
        self.assertEqual(inst.id, "bundle-example")
        self.assertEqual(inst.link[0].relation, "self")
        self.assertEqual(inst.link[0].url, "https://example.com/base/MedicationRequest?patient=347&_include=MedicationRequest.medication")
        self.assertEqual(inst.link[1].relation, "next")
        self.assertEqual(inst.link[1].url, "https://example.com/base/MedicationRequest?patient=347&searchId=ff15fd40-ff71-4b48-b366-09c706bed9d0&page=2")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2014-08-18T01:43:30Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2014-08-18T01:43:30Z")
        self.assertEqual(inst.total, 3)
        self.assertEqual(inst.type, "searchset")
    
    def testBundle2(self):
        inst = self.instantiate_from("diagnosticreport-example-f001-bloodexam.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle2(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle2(inst2)
    
    def implBundle2(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "https://example.com/base/DiagnosticReport/f001")
        self.assertEqual(inst.entry[0].resource.id, "f001")
        self.assertEqual(inst.entry[1].fullUrl, "https://example.com/base/ServiceRequest/req")
        self.assertEqual(inst.entry[1].resource.id, "req")
        self.assertEqual(inst.id, "f001")
        self.assertEqual(inst.type, "collection")
    
    def testBundle3(self):
        inst = self.instantiate_from("diagnosticreport-example-f202-bloodculture.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle3(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle3(inst2)
    
    def implBundle3(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "https://example.com/base/DiagnosticReport/f202")
        self.assertEqual(inst.entry[0].resource.id, "f202")
        self.assertEqual(inst.entry[1].fullUrl, "https://example.com/base/ServiceRequest/req")
        self.assertEqual(inst.entry[1].resource.id, "req")
        self.assertEqual(inst.id, "f202")
        self.assertEqual(inst.type, "collection")
    
    def testBundle4(self):
        inst = self.instantiate_from("diagnosticreport-example-ghp.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle4(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle4(inst2)
    
    def implBundle4(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "https://example.com/base/DiagnosticReport/ghp")
        self.assertEqual(inst.entry[0].resource.id, "ghp")
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRDate("2015-08-16T10:35:23Z").date)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), "2015-08-16T10:35:23Z")
        self.assertEqual(inst.entry[1].fullUrl, "https://example.com/base/Specimen/rtt")
        self.assertEqual(inst.entry[1].resource.id, "rtt")
        self.assertEqual(inst.entry[2].fullUrl, "https://example.com/base/Specimen/ltt")
        self.assertEqual(inst.entry[2].resource.id, "ltt")
        self.assertEqual(inst.entry[3].fullUrl, "https://example.com/base/Specimen/urine")
        self.assertEqual(inst.entry[3].resource.id, "urine")
        self.assertEqual(inst.entry[4].fullUrl, "https://example.com/base/Observation/p2")
        self.assertEqual(inst.entry[4].resource.id, "p2")
        self.assertEqual(inst.entry[5].fullUrl, "https://example.com/base/Observation/r1")
        self.assertEqual(inst.entry[5].resource.id, "r1")
        self.assertEqual(inst.entry[6].fullUrl, "https://example.com/base/Observation/r2")
        self.assertEqual(inst.entry[6].resource.id, "r2")
        self.assertEqual(inst.entry[7].fullUrl, "https://example.com/base/Observation/r3")
        self.assertEqual(inst.entry[7].resource.id, "r3")
        self.assertEqual(inst.entry[8].fullUrl, "https://example.com/base/Observation/r4")
        self.assertEqual(inst.entry[8].resource.id, "r4")
        self.assertEqual(inst.entry[9].fullUrl, "https://example.com/base/Observation/r5")
        self.assertEqual(inst.entry[9].resource.id, "r5")
        self.assertEqual(inst.id, "ghp")
        self.assertEqual(inst.type, "collection")
    
    def testBundle5(self):
        inst = self.instantiate_from("diagnosticreport-example-lipids.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle5(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle5(inst2)
    
    def implBundle5(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "https://example.com/base/DiagnosticReport/lipids")
        self.assertEqual(inst.entry[0].resource.id, "lipids")
        self.assertEqual(inst.entry[1].fullUrl, "https://example.com/base/Observation/cholesterol")
        self.assertEqual(inst.entry[1].resource.id, "cholesterol")
        self.assertEqual(inst.entry[2].fullUrl, "https://example.com/base/Observation/triglyceride")
        self.assertEqual(inst.entry[2].resource.id, "triglyceride")
        self.assertEqual(inst.entry[3].fullUrl, "https://example.com/base/Observation/hdlcholesterol")
        self.assertEqual(inst.entry[3].resource.id, "hdlcholesterol")
        self.assertEqual(inst.entry[4].fullUrl, "https://example.com/base/Observation/ldlcholesterol")
        self.assertEqual(inst.entry[4].resource.id, "ldlcholesterol")
        self.assertEqual(inst.id, "lipids")
        self.assertEqual(inst.type, "collection")
    
    def testBundle6(self):
        inst = self.instantiate_from("diagnosticreport-example-lri.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle6(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle6(inst2)
    
    def implBundle6(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "http://test.fhir.org/r4/DiagnosticReport/lri-example")
        self.assertEqual(inst.entry[0].resource.id, "lri-example")
        self.assertEqual(inst.entry[1].fullUrl, "http://test.fhir.org/r4/Observation/lri-gramstain1")
        self.assertEqual(inst.entry[1].resource.id, "gramstain1")
        self.assertEqual(inst.entry[2].fullUrl, "http://test.fhir.org/r4/Observation/lri-gramstain2")
        self.assertEqual(inst.entry[2].resource.id, "gramstain2")
        self.assertEqual(inst.entry[3].fullUrl, "http://test.fhir.org/r4/Observation/lri-gramstain3")
        self.assertEqual(inst.entry[3].resource.id, "gramstain3")
        self.assertEqual(inst.entry[4].fullUrl, "http://test.fhir.org/r4/Observation/lri-gramstain4")
        self.assertEqual(inst.entry[4].resource.id, "gramstain4")
        self.assertEqual(inst.entry[5].fullUrl, "http://test.fhir.org/r4/Observation/lri-growth1")
        self.assertEqual(inst.entry[5].resource.id, "growth1")
        self.assertEqual(inst.entry[6].fullUrl, "http://test.fhir.org/r4/Observation/lri-growth2")
        self.assertEqual(inst.entry[6].resource.id, "growth2")
        self.assertEqual(inst.entry[7].fullUrl, "http://test.fhir.org/r4/Observation/lri-growth3")
        self.assertEqual(inst.entry[7].resource.id, "growth3")
        self.assertEqual(inst.entry[8].fullUrl, "http://test.fhir.org/r4/Observation/lri-org2-amp")
        self.assertEqual(inst.entry[8].resource.id, "org2-amp")
        self.assertEqual(inst.entry[9].fullUrl, "http://test.fhir.org/r4/Observation/lri-org2-cip")
        self.assertEqual(inst.entry[9].resource.id, "org2-cip")
        self.assertEqual(inst.id, "lri-example")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2017-06-27T00:52:51Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2017-06-27T00:52:51Z")
        self.assertEqual(inst.meta.versionId, "1")
        self.assertEqual(inst.type, "collection")
    
    def testBundle7(self):
        inst = self.instantiate_from("diagnosticreport-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle7(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle7(inst2)
    
    def implBundle7(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "https://example.com/base/DiagnosticReport/101")
        self.assertEqual(inst.entry[0].resource.id, "101")
        self.assertEqual(inst.entry[0].resource.meta.tag[0].code, "01")
        self.assertEqual(inst.entry[0].resource.meta.tag[0].display, "Needs Review")
        self.assertEqual(inst.entry[0].resource.meta.tag[0].system, "http://example.org/fhir/CodeSystem/workflow-codes")
        self.assertEqual(inst.entry[1].fullUrl, "https://example.com/base/Observation/r1")
        self.assertEqual(inst.entry[1].resource.id, "r1")
        self.assertEqual(inst.entry[2].fullUrl, "https://example.com/base/Observation/r2")
        self.assertEqual(inst.entry[2].resource.id, "r2")
        self.assertEqual(inst.entry[3].fullUrl, "https://example.com/base/Observation/r3")
        self.assertEqual(inst.entry[3].resource.id, "r3")
        self.assertEqual(inst.entry[4].fullUrl, "https://example.com/base/Observation/r4")
        self.assertEqual(inst.entry[4].resource.id, "r4")
        self.assertEqual(inst.entry[5].fullUrl, "https://example.com/base/Observation/r5")
        self.assertEqual(inst.entry[5].resource.id, "r5")
        self.assertEqual(inst.entry[6].fullUrl, "https://example.com/base/Observation/r6")
        self.assertEqual(inst.entry[6].resource.id, "r6")
        self.assertEqual(inst.entry[7].fullUrl, "https://example.com/base/Observation/r7")
        self.assertEqual(inst.entry[7].resource.id, "r7")
        self.assertEqual(inst.entry[8].fullUrl, "https://example.com/base/Observation/r8")
        self.assertEqual(inst.entry[8].resource.id, "r8")
        self.assertEqual(inst.entry[9].fullUrl, "https://example.com/base/Observation/r9")
        self.assertEqual(inst.entry[9].resource.id, "r9")
        self.assertEqual(inst.id, "101")
        self.assertEqual(inst.type, "collection")
    
    def testBundle8(self):
        inst = self.instantiate_from("diagnosticreport-examples-general.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle8(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle8(inst2)
    
    def implBundle8(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "http://hl7.org/fhir/Bundle/3")
        self.assertEqual(inst.entry[0].resource.id, "3")
        self.assertEqual(inst.entry[1].fullUrl, "http://hl7.org/fhir/Bundle/4")
        self.assertEqual(inst.entry[1].resource.id, "4")
        self.assertEqual(inst.entry[2].fullUrl, "http://hl7.org/fhir/Bundle/5")
        self.assertEqual(inst.entry[2].resource.id, "5")
        self.assertEqual(inst.entry[3].fullUrl, "http://hl7.org/fhir/Bundle/6")
        self.assertEqual(inst.entry[3].resource.id, "6")
        self.assertEqual(inst.entry[4].fullUrl, "http://hl7.org/fhir/Bundle/7")
        self.assertEqual(inst.entry[4].resource.id, "7")
        self.assertEqual(inst.entry[5].fullUrl, "http://hl7.org/fhir/Bundle/8")
        self.assertEqual(inst.entry[5].resource.id, "8")
        self.assertEqual(inst.entry[6].fullUrl, "http://hl7.org/fhir/Bundle/9")
        self.assertEqual(inst.entry[6].resource.id, "9")
        self.assertEqual(inst.entry[7].fullUrl, "http://hl7.org/fhir/Bundle/15")
        self.assertEqual(inst.entry[7].resource.id, "15")
        self.assertEqual(inst.entry[8].fullUrl, "http://hl7.org/fhir/Bundle/16")
        self.assertEqual(inst.entry[8].resource.id, "16")
        self.assertEqual(inst.entry[9].fullUrl, "http://hl7.org/fhir/Bundle/17")
        self.assertEqual(inst.entry[9].resource.id, "17")
        self.assertEqual(inst.id, "72ac8493-52ac-41bd-8d5d-7258c289b5ea")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2012-04-14T10:35:23Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2012-04-14T10:35:23Z")
        self.assertEqual(inst.type, "collection")
    
    def testBundle9(self):
        inst = self.instantiate_from("diagnosticreport-genetics-example-2-familyhistory.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle9(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle9(inst2)
    
    def implBundle9(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "https://example.com/base/DiagnosticReport/dg2")
        self.assertEqual(inst.entry[0].resource.id, "dg2")
        self.assertEqual(inst.entry[1].fullUrl, "https://example.com/base/FamilyMemberHistory/f1-genetics")
        self.assertEqual(inst.entry[1].resource.id, "f1-genetics")
        self.assertEqual(inst.id, "dg2")
        self.assertEqual(inst.type, "collection")
    
    def testBundle10(self):
        inst = self.instantiate_from("diagnosticreport-hla-genetics-results-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle10(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle10(inst2)
    
    def implBundle10(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "urn:uuid:b0a4b18e-94e7-4b1b-8031-c7ae4bdd8db9")
        self.assertEqual(inst.entry[0].request.method, "POST")
        self.assertEqual(inst.entry[0].request.url, "DiagnosticReport")
        self.assertEqual(inst.entry[1].fullUrl, "urn:uuid:8200dab6-18a2-4550-b913-a7db480c0804")
        self.assertEqual(inst.entry[1].request.method, "POST")
        self.assertEqual(inst.entry[1].request.url, "Sequence")
        self.assertEqual(inst.entry[2].fullUrl, "urn:uuid:7c393185-f15c-45bc-a714-c0fdbea32675")
        self.assertEqual(inst.entry[2].request.method, "POST")
        self.assertEqual(inst.entry[2].request.url, "Sequence")
        self.assertEqual(inst.entry[3].fullUrl, "urn:uuid:65c85f14-c3a0-4b72-818f-820e04fcc621")
        self.assertEqual(inst.entry[3].request.method, "POST")
        self.assertEqual(inst.entry[3].request.url, "Sequence")
        self.assertEqual(inst.entry[4].fullUrl, "urn:uuid:fbba9fe7-0ece-4ec1-9233-a437a8d242a0")
        self.assertEqual(inst.entry[4].request.method, "POST")
        self.assertEqual(inst.entry[4].request.url, "Sequence")
        self.assertEqual(inst.entry[5].fullUrl, "urn:uuid:cbabf93e-1b4b-46f2-ba1e-d84862670670")
        self.assertEqual(inst.entry[5].request.method, "POST")
        self.assertEqual(inst.entry[5].request.url, "Sequence")
        self.assertEqual(inst.entry[6].fullUrl, "urn:uuid:c233ad3d-1572-48d6-93da-0a583535e138")
        self.assertEqual(inst.entry[6].request.method, "POST")
        self.assertEqual(inst.entry[6].request.url, "Sequence")
        self.assertEqual(inst.entry[7].fullUrl, "urn:uuid:05fa52d7-5c67-460a-8722-d3460b24d6fe")
        self.assertEqual(inst.entry[7].request.method, "POST")
        self.assertEqual(inst.entry[7].request.url, "Sequence")
        self.assertEqual(inst.entry[8].fullUrl, "urn:uuid:db69e549-6267-4777-b4b9-8813f3329309")
        self.assertEqual(inst.entry[8].request.method, "POST")
        self.assertEqual(inst.entry[8].request.url, "Sequence")
        self.assertEqual(inst.entry[9].fullUrl, "urn:uuid:bb55c2bc-5ad2-4bc1-8ff3-c407d06b12d0")
        self.assertEqual(inst.entry[9].request.method, "POST")
        self.assertEqual(inst.entry[9].request.url, "Sequence")
        self.assertEqual(inst.id, "hla-1")
        self.assertEqual(inst.type, "transaction")

