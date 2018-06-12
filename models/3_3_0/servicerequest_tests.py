#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 on 2018-05-12.
#  2018, SMART Health IT.


import os
import io
import unittest
import json
from . import servicerequest
from .fhirdate import FHIRDate


class ServiceRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ServiceRequest", js["resourceType"])
        return servicerequest.ServiceRequest(js)
    
    def testServiceRequest1(self):
        inst = self.instantiate_from("servicerequest-example-ambulation.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest1(inst2)
    
    def implServiceRequest1(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2017-03-05").date)
        self.assertEqual(inst.authoredOn.as_json(), "2017-03-05")
        self.assertEqual(inst.code.coding[0].code, "62013009")
        self.assertEqual(inst.code.coding[0].display, "Ambulating patient (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Ambulation")
        self.assertEqual(inst.id, "ambulation")
        self.assertEqual(inst.identifier[0].value, "45678")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testServiceRequest2(self):
        inst = self.instantiate_from("servicerequest-example-appendectomy.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest2(inst)
        
        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest2(inst2)
    
    def implServiceRequest2(self, inst):
        self.assertEqual(inst.code.text, "Appendectomy")
        self.assertEqual(inst.id, "appendectomy-narrative")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "additional")
    
    def testServiceRequest3(self):
        inst = self.instantiate_from("servicerequest-example-colonoscopy-bx.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest3(inst)
        
        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest3(inst2)
    
    def implServiceRequest3(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2017-03-05").date)
        self.assertEqual(inst.authoredOn.as_json(), "2017-03-05")
        self.assertEqual(inst.code.coding[0].code, "76164006")
        self.assertEqual(inst.code.coding[0].display, "Biopsy of colon (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Biopsy of colon")
        self.assertEqual(inst.id, "colon-biopsy")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.requisition.system, "http://bumc.org/requisitions")
        self.assertEqual(inst.requisition.value, "req12345")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testServiceRequest4(self):
        inst = self.instantiate_from("servicerequest-example-colonoscopy.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest4(inst)
        
        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest4(inst2)
    
    def implServiceRequest4(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2017-03-05").date)
        self.assertEqual(inst.authoredOn.as_json(), "2017-03-05")
        self.assertEqual(inst.code.coding[0].code, "73761001")
        self.assertEqual(inst.code.coding[0].display, "Colonoscopy (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Colonoscopy")
        self.assertEqual(inst.id, "colonoscopy")
        self.assertEqual(inst.identifier[0].value, "45678")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.requisition.system, "http://bumc.org/requisitions")
        self.assertEqual(inst.requisition.value, "req12345")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testServiceRequest5(self):
        inst = self.instantiate_from("servicerequest-example-di.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest5(inst)
        
        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest5(inst2)
    
    def implServiceRequest5(self, inst):
        self.assertEqual(inst.code.coding[0].code, "24627-2")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Chest CT")
        self.assertEqual(inst.id, "di")
        self.assertEqual(inst.intent, "original-order")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2013-05-08T09:33:27+07:00").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2013-05-08T09:33:27+07:00")
        self.assertEqual(inst.reasonCode[0].text, "Check for metastatic disease")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testServiceRequest6(self):
        inst = self.instantiate_from("servicerequest-example-edu.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest6(inst)
        
        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest6(inst2)
    
    def implServiceRequest6(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2016-08-16").date)
        self.assertEqual(inst.authoredOn.as_json(), "2016-08-16")
        self.assertEqual(inst.category[0].coding[0].code, "311401005")
        self.assertEqual(inst.category[0].coding[0].display, "Patient education (procedure)")
        self.assertEqual(inst.category[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.category[0].text, "Education")
        self.assertEqual(inst.code.coding[0].code, "48023004")
        self.assertEqual(inst.code.coding[0].display, "Breast self-examination technique education (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Health education - breast examination")
        self.assertEqual(inst.id, "education")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2014-08-16")
        self.assertEqual(inst.reasonCode[0].text, "early detection of breast mass")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testServiceRequest7(self):
        inst = self.instantiate_from("servicerequest-example-ft4.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest7(inst)
        
        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest7(inst2)
    
    def implServiceRequest7(self, inst):
        self.assertEqual(inst.code.coding[0].code, "3024-7")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Free T4")
        self.assertEqual(inst.id, "ft4")
        self.assertEqual(inst.intent, "reflex-order")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2015-08-27T09:33:27+07:00").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2015-08-27T09:33:27+07:00")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testServiceRequest8(self):
        inst = self.instantiate_from("servicerequest-example-implant.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest8(inst)
        
        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest8(inst2)
    
    def implServiceRequest8(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2015-03-30").date)
        self.assertEqual(inst.authoredOn.as_json(), "2015-03-30")
        self.assertEqual(inst.code.coding[0].code, "25267002")
        self.assertEqual(inst.code.coding[0].display, "Insertion of intracardiac pacemaker (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Implant Pacemaker")
        self.assertEqual(inst.id, "example-implant")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.reasonCode[0].text, "Bradycardia")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testServiceRequest9(self):
        inst = self.instantiate_from("servicerequest-example-lipid.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest9(inst)
        
        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest9(inst2)
    
    def implServiceRequest9(self, inst):
        self.assertEqual(inst.code.coding[0].code, "LIPID")
        self.assertEqual(inst.code.coding[0].system, "http://acme.org/tests")
        self.assertEqual(inst.code.text, "Lipid Panel")
        self.assertEqual(inst.contained[0].id, "fasting")
        self.assertEqual(inst.contained[1].id, "serum")
        self.assertEqual(inst.id, "lipid")
        self.assertEqual(inst.identifier[0].system, "urn:oid:1.3.4.5.6.7")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "PLAC")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://hl7.org/fhir/identifier-type")
        self.assertEqual(inst.identifier[0].type.text, "Placer")
        self.assertEqual(inst.identifier[0].value, "2345234234234")
        self.assertEqual(inst.intent, "original-order")
        self.assertEqual(inst.note[0].text, "patient is afraid of needles")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2013-05-02T16:16:00-07:00").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2013-05-02T16:16:00-07:00")
        self.assertEqual(inst.reasonCode[0].coding[0].code, "V173")
        self.assertEqual(inst.reasonCode[0].coding[0].display, "Fam hx-ischem heart dis")
        self.assertEqual(inst.reasonCode[0].coding[0].system, "http://hl7.org/fhir/sid/icd-9")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testServiceRequest10(self):
        inst = self.instantiate_from("servicerequest-example-myringotomy.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest10(inst)
        
        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest10(inst2)
    
    def implServiceRequest10(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2014-02-14").date)
        self.assertEqual(inst.authoredOn.as_json(), "2014-02-14")
        self.assertEqual(inst.category[0].coding[0].code, "103696004")
        self.assertEqual(inst.category[0].coding[0].display, "Patient referral to specialist")
        self.assertEqual(inst.category[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.coding[0].code, "172676009")
        self.assertEqual(inst.code.coding[0].display, "Myringotomy and insertion of tympanic ventilation tube")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Insertion of grommets")
        self.assertEqual(inst.id, "myringotomy")
        self.assertEqual(inst.identifier[0].system, "http://orionhealth.com/fhir/apps/referralids")
        self.assertEqual(inst.identifier[0].value, "ret4421")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.note[0].authorString, "Serena Shrink")
        self.assertEqual(inst.note[0].text, "In the past 2 years Beverly has had 6 instances of rt-sided Otitis media. She is     falling behind her peers at school, and displaying some learning difficulties.")
        self.assertEqual(inst.note[0].time.date, FHIRDate("2014-02-14").date)
        self.assertEqual(inst.note[0].time.as_json(), "2014-02-14")
        self.assertEqual(inst.occurrencePeriod.end.date, FHIRDate("2014-03-14").date)
        self.assertEqual(inst.occurrencePeriod.end.as_json(), "2014-03-14")
        self.assertEqual(inst.performerType.coding[0].code, "ent")
        self.assertEqual(inst.performerType.coding[0].display, "ENT")
        self.assertEqual(inst.performerType.coding[0].system, "http://orionhealth.com/fhir/apps/specialties")
        self.assertEqual(inst.priority, "routine")
        self.assertEqual(inst.reasonCode[0].text, "For consideration of Grommets")
        self.assertEqual(inst.requisition.value, "1234")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

