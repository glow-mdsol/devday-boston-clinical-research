#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 on 2018-05-12.
#  2018, SMART Health IT.


import os
import io
import unittest
import json
from . import productplan
from .fhirdate import FHIRDate


class ProductPlanTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ProductPlan", js["resourceType"])
        return productplan.ProductPlan(js)
    
    def testProductPlan1(self):
        inst = self.instantiate_from("productplan-example-onc.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProductPlan instance")
        self.implProductPlan1(inst)
        
        js = inst.as_json()
        self.assertEqual("ProductPlan", js["resourceType"])
        inst2 = productplan.ProductPlan(js)
        self.implProductPlan1(inst2)
    
    def implProductPlan1(self, inst):
        self.assertEqual(inst.address[0].city, "Washington")
        self.assertEqual(inst.address[0].country, "USA")
        self.assertEqual(inst.address[0].line[0], "123 Fake Street")
        self.assertEqual(inst.address[0].postalCode, "20005")
        self.assertEqual(inst.address[0].state, "DC")
        self.assertEqual(inst.alias[0], "PPO Sample Plan")
        self.assertEqual(inst.coverage[0].benefit[0].item[0].code.text, "primary care visit")
        self.assertEqual(inst.coverage[0].benefit[0].item[1].code.text, "specialty care visit")
        self.assertEqual(inst.coverage[0].benefit[0].type.text, "Diagnostic and treatment services")
        self.assertEqual(inst.coverage[0].type.text, "Medical")
        self.assertEqual(inst.id, "example-onc")
        self.assertEqual(inst.name, "Sample Plan")
        self.assertEqual(inst.period.start.date, FHIRDate("2017-01-01").date)
        self.assertEqual(inst.period.start.as_json(), "2017-01-01")
        self.assertEqual(inst.plan[0].category[0].benefit[0].cost[0].applicability[0].code, "preferred")
        self.assertEqual(inst.plan[0].category[0].benefit[0].cost[0].type.text, "copay")
        self.assertEqual(inst.plan[0].category[0].benefit[0].cost[0].value.code, "USD")
        self.assertEqual(inst.plan[0].category[0].benefit[0].cost[0].value.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.plan[0].category[0].benefit[0].cost[0].value.value, 25)
        self.assertEqual(inst.plan[0].category[0].benefit[0].cost[1].applicability[0].code, "participating")
        self.assertEqual(inst.plan[0].category[0].benefit[0].cost[1].type.text, "coinsurance")
        self.assertEqual(inst.plan[0].category[0].benefit[0].cost[1].value.unit, "%")
        self.assertEqual(inst.plan[0].category[0].benefit[0].cost[1].value.value, 35)
        self.assertEqual(inst.plan[0].category[0].benefit[0].cost[2].applicability[0].code, "non-participating")
        self.assertEqual(inst.plan[0].category[0].benefit[0].cost[2].type.text, "coinsurance")
        self.assertEqual(inst.plan[0].category[0].benefit[0].cost[2].value.unit, "%")
        self.assertEqual(inst.plan[0].category[0].benefit[0].cost[2].value.value, 35)
        self.assertEqual(inst.plan[0].category[0].benefit[0].type.text, "primary care office visit")
        self.assertEqual(inst.plan[0].category[0].benefit[1].cost[0].applicability[0].code, "preferred")
        self.assertEqual(inst.plan[0].category[0].benefit[1].cost[0].type.text, "copay")
        self.assertEqual(inst.plan[0].category[0].benefit[1].cost[0].value.code, "USD")
        self.assertEqual(inst.plan[0].category[0].benefit[1].cost[0].value.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.plan[0].category[0].benefit[1].cost[0].value.value, 35)
        self.assertEqual(inst.plan[0].category[0].benefit[1].cost[1].applicability[0].code, "participating")
        self.assertEqual(inst.plan[0].category[0].benefit[1].cost[1].type.text, "coinsurance")
        self.assertEqual(inst.plan[0].category[0].benefit[1].cost[1].value.unit, "%")
        self.assertEqual(inst.plan[0].category[0].benefit[1].cost[1].value.value, 35)
        self.assertEqual(inst.plan[0].category[0].benefit[1].cost[2].applicability[0].code, "non-participating")
        self.assertEqual(inst.plan[0].category[0].benefit[1].cost[2].type.text, "coinsurance")
        self.assertEqual(inst.plan[0].category[0].benefit[1].cost[2].value.unit, "%")
        self.assertEqual(inst.plan[0].category[0].benefit[1].cost[2].value.value, 35)
        self.assertEqual(inst.plan[0].category[0].benefit[1].type.text, "specialty care office visit")
        self.assertEqual(inst.plan[0].category[0].code.text, "Medical")
        self.assertEqual(inst.plan[0].premium.code, "USD")
        self.assertEqual(inst.plan[0].premium.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.plan[0].premium.value, 2000)
        self.assertEqual(inst.plan[0].type.text, "Standard")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testProductPlan2(self):
        inst = self.instantiate_from("productplan-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProductPlan instance")
        self.implProductPlan2(inst)
        
        js = inst.as_json()
        self.assertEqual("ProductPlan", js["resourceType"])
        inst2 = productplan.ProductPlan(js)
        self.implProductPlan2(inst2)
    
    def implProductPlan2(self, inst):
        self.assertEqual(inst.address[0].city, "Ann Arbor")
        self.assertEqual(inst.address[0].country, "USA")
        self.assertEqual(inst.address[0].line[0], "3300 Washtenaw Avenue, Suite 227")
        self.assertEqual(inst.address[0].postalCode, "48104")
        self.assertEqual(inst.address[0].state, "MI")
        self.assertEqual(inst.alias[0], "HL7 International")
        self.assertEqual(inst.coverage[0].benefit[0].item[0].benefitValue.code, "USD")
        self.assertEqual(inst.coverage[0].benefit[0].item[0].benefitValue.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.coverage[0].benefit[0].item[0].benefitValue.value, 450.23)
        self.assertEqual(inst.coverage[0].benefit[0].item[0].code.text, "day")
        self.assertEqual(inst.coverage[0].benefit[0].type.text, "Primary Care")
        self.assertEqual(inst.coverage[0].type.text, "Substance Abuse")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.name, "Health Level Seven International Staff Plan")
        self.assertEqual(inst.period.start.date, FHIRDate("2017-01-01").date)
        self.assertEqual(inst.period.start.as_json(), "2017-01-01")
        self.assertEqual(inst.plan[0].premium.code, "USD")
        self.assertEqual(inst.plan[0].premium.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.plan[0].premium.value, 2000)
        self.assertEqual(inst.plan[0].type.text, "Silver")
        self.assertEqual(inst.text.status, "generated")

