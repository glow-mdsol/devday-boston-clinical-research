#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 on 2018-05-12.
#  2018, SMART Health IT.


import os
import io
import unittest
import json
from . import organizationrole
from .fhirdate import FHIRDate


class OrganizationRoleTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("OrganizationRole", js["resourceType"])
        return organizationrole.OrganizationRole(js)
    
    def testOrganizationRole1(self):
        inst = self.instantiate_from("organizationrole-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a OrganizationRole instance")
        self.implOrganizationRole1(inst)
        
        js = inst.as_json()
        self.assertEqual("OrganizationRole", js["resourceType"])
        inst2 = organizationrole.OrganizationRole(js)
        self.implOrganizationRole1(inst2)
    
    def implOrganizationRole1(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.availabilityExceptions, "Reduced Services on public holidays and during the Christmas/New Year break")
        self.assertEqual(inst.availableTime[0].availableEndTime.date, FHIRDate("16:30:00").date)
        self.assertEqual(inst.availableTime[0].availableEndTime.as_json(), "16:30:00")
        self.assertEqual(inst.availableTime[0].availableStartTime.date, FHIRDate("09:00:00").date)
        self.assertEqual(inst.availableTime[0].availableStartTime.as_json(), "09:00:00")
        self.assertEqual(inst.availableTime[0].daysOfWeek[0], "mon")
        self.assertEqual(inst.availableTime[0].daysOfWeek[1], "tue")
        self.assertEqual(inst.availableTime[0].daysOfWeek[2], "wed")
        self.assertEqual(inst.availableTime[1].availableEndTime.date, FHIRDate("12:00:00").date)
        self.assertEqual(inst.availableTime[1].availableEndTime.as_json(), "12:00:00")
        self.assertEqual(inst.availableTime[1].availableStartTime.date, FHIRDate("09:00:00").date)
        self.assertEqual(inst.availableTime[1].availableStartTime.as_json(), "09:00:00")
        self.assertEqual(inst.availableTime[1].daysOfWeek[0], "thu")
        self.assertEqual(inst.availableTime[1].daysOfWeek[1], "fri")
        self.assertEqual(inst.code[0].coding[0].code, "provider")
        self.assertEqual(inst.code[0].coding[0].system, "http://hl7.org/fhir/organization-role")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://www.acme.org/practitioners")
        self.assertEqual(inst.identifier[0].value, "23")
        self.assertEqual(inst.period.end.date, FHIRDate("2012-03-31").date)
        self.assertEqual(inst.period.end.as_json(), "2012-03-31")
        self.assertEqual(inst.period.start.date, FHIRDate("2012-01-01").date)
        self.assertEqual(inst.period.start.as_json(), "2012-01-01")
        self.assertEqual(inst.specialty[0].coding[0].code, "408443003")
        self.assertEqual(inst.specialty[0].coding[0].display, "General medical practice")
        self.assertEqual(inst.specialty[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.telecom[0].system, "email")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "general.practice@example.org")
        self.assertEqual(inst.text.status, "generated")

