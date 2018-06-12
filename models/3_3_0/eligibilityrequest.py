#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 (http://hl7.org/fhir/StructureDefinition/EligibilityRequest) on 2018-05-12.
#  2018, SMART Health IT.


from . import domainresource

class EligibilityRequest(domainresource.DomainResource):
    """ Determine insurance validity and scope of coverage.
    
    The EligibilityRequest provides patient and insurance coverage information
    to an insurer for them to respond, in the form of an EligibilityResponse,
    with information regarding whether the stated coverage is valid and in-
    force and optionally to provide the insurance details of the policy.
    """
    
    resource_type = "EligibilityRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authorization = None
        """ Services which may require prior authorization.
        List of `EligibilityRequestAuthorization` items (represented as `dict` in JSON). """
        
        self.benefitCategory = None
        """ Type of services covered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.benefitSubCategory = None
        """ Detailed services covered within the type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.businessArrangement = None
        """ Business agreement.
        Type `str`. """
        
        self.coverage = None
        """ Insurance or medical plan.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.enterer = None
        """ Author.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.facility = None
        """ Servicing Facility.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.insurer = None
        """ Target.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.patient = None
        """ The subject of the Products and Services.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.priority = None
        """ Desired processing priority.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.provider = None
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.servicedDate = None
        """ Estimated date or dates of Service.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.servicedPeriod = None
        """ Estimated date or dates of Service.
        Type `Period` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        super(EligibilityRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EligibilityRequest, self).elementProperties()
        js.extend([
            ("authorization", "authorization", EligibilityRequestAuthorization, True, None, False),
            ("benefitCategory", "benefitCategory", codeableconcept.CodeableConcept, False, None, False),
            ("benefitSubCategory", "benefitSubCategory", codeableconcept.CodeableConcept, False, None, False),
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("status", "status", str, False, None, False),
        ])
        return js


from . import backboneelement

class EligibilityRequestAuthorization(backboneelement.BackboneElement):
    """ Services which may require prior authorization.
    
    A list of billable services for which an authorization prior to service
    delivery may be required by the payor.
    """
    
    resource_type = "EligibilityRequestAuthorization"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.diagnosis = None
        """ List of Diagnosis.
        List of `EligibilityRequestAuthorizationDiagnosis` items (represented as `dict` in JSON). """
        
        self.facility = None
        """ Servicing Facility.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.modifier = None
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Procedure sequence for reference.
        Type `int`. """
        
        self.service = None
        """ Billing Code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(EligibilityRequestAuthorization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EligibilityRequestAuthorization, self).elementProperties()
        js.extend([
            ("diagnosis", "diagnosis", EligibilityRequestAuthorizationDiagnosis, True, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("service", "service", codeableconcept.CodeableConcept, False, None, True),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class EligibilityRequestAuthorizationDiagnosis(backboneelement.BackboneElement):
    """ List of Diagnosis.
    
    List of patient diagnosis for which care is sought.
    """
    
    resource_type = "EligibilityRequestAuthorizationDiagnosis"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.diagnosisCodeableConcept = None
        """ Patient's diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.diagnosisReference = None
        """ Patient's diagnosis.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(EligibilityRequestAuthorizationDiagnosis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EligibilityRequestAuthorizationDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosisCodeableConcept", "diagnosisCodeableConcept", codeableconcept.CodeableConcept, False, "diagnosis", False),
            ("diagnosisReference", "diagnosisReference", fhirreference.FHIRReference, False, "diagnosis", False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity
