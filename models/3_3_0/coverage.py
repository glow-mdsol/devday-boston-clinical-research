#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 (http://hl7.org/fhir/StructureDefinition/Coverage) on 2018-05-12.
#  2018, SMART Health IT.


from . import domainresource

class Coverage(domainresource.DomainResource):
    """ Insurance or medical plan or a payment agreement.
    
    Financial instrument which may be used to reimburse or pay for health care
    products and services.
    """
    
    resource_type = "Coverage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.beneficiary = None
        """ Plan Beneficiary.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.class_fhir = None
        """ Additional coverage classifications.
        List of `CoverageClass` items (represented as `dict` in JSON). """
        
        self.contract = None
        """ Contract details.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.copay = None
        """ Patient payments for services/products.
        List of `CoverageCopay` items (represented as `dict` in JSON). """
        
        self.dependent = None
        """ Dependent number.
        Type `str`. """
        
        self.identifier = None
        """ The primary coverage ID.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.network = None
        """ Insurer network.
        Type `str`. """
        
        self.order = None
        """ Relative order of the coverage.
        Type `int`. """
        
        self.payor = None
        """ Identifier for the plan or agreement issuer.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.period = None
        """ Coverage start and end dates.
        Type `Period` (represented as `dict` in JSON). """
        
        self.policyHolder = None
        """ Owner of the policy.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.relationship = None
        """ Beneficiary relationship to the Subscriber.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        self.subscriber = None
        """ Subscriber to the policy.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.subscriberId = None
        """ ID assigned to the Subscriber.
        Type `str`. """
        
        self.type = None
        """ Type of coverage such as medical or accident.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Coverage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Coverage, self).elementProperties()
        js.extend([
            ("beneficiary", "beneficiary", fhirreference.FHIRReference, False, None, False),
            ("class_fhir", "class", CoverageClass, True, None, False),
            ("contract", "contract", fhirreference.FHIRReference, True, None, False),
            ("copay", "copay", CoverageCopay, True, None, False),
            ("dependent", "dependent", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("network", "network", str, False, None, False),
            ("order", "order", int, False, None, False),
            ("payor", "payor", fhirreference.FHIRReference, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("policyHolder", "policyHolder", fhirreference.FHIRReference, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, False),
            ("subscriber", "subscriber", fhirreference.FHIRReference, False, None, False),
            ("subscriberId", "subscriberId", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class CoverageClass(backboneelement.BackboneElement):
    """ Additional coverage classifications.
    
    A suite of underwrite specific classifiers, for example may be used to
    identify a class of coverage or employer group, Policy, Plan.
    """
    
    resource_type = "CoverageClass"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Display text for an identifier for the group.
        Type `str`. """
        
        self.type = None
        """ Type of class such as 'group' or 'plan'.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ The tag or value under the classification.
        Type `str`. """
        
        super(CoverageClass, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageClass, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("type", "type", coding.Coding, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


class CoverageCopay(backboneelement.BackboneElement):
    """ Patient payments for services/products.
    
    A suite of underwrite specific classifiers, for example may be used to
    identify a class of coverage or employer group, Policy, Plan.
    """
    
    resource_type = "CoverageCopay"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ The type of service or product.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ The amount or percentage of the copayment.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(CoverageCopay, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageCopay, self).elementProperties()
        js.extend([
            ("type", "type", coding.Coding, False, None, False),
            ("value", "value", quantity.Quantity, False, None, True),
        ])
        return js


from . import codeableconcept
from . import coding
from . import fhirreference
from . import identifier
from . import period
from . import quantity
