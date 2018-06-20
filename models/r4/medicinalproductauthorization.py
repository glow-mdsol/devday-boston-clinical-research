#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 (http://hl7.org/fhir/StructureDefinition/MedicinalProductAuthorization) on 2018-05-12.
#  2018, SMART Health IT.


from . import domainresource

class MedicinalProductAuthorization(domainresource.DomainResource):
    """ The regulatory authorization of a medicinal product.
    """
    
    resource_type = "MedicinalProductAuthorization"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.country = None
        """ The country in which the marketing authorization has been granted.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.dataExclusivityPeriod = None
        """ A period of time after authorization before generic product
        applicatiosn can be submitted.
        Type `Period` (represented as `dict` in JSON). """
        
        self.dateOfFirstAuthorization = None
        """ The date when the first authorization was granted by a Medicines
        Regulatory Agency.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.holder = None
        """ Marketing Authorization Holder.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifier for the marketing authorization, as assigned by
        a regulator.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.internationalBirthDate = None
        """ Date of first marketing authorization for a company's new medicinal
        product in any country in the World.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.jurisdictionalAuthorization = None
        """ Authorization in areas within a country.
        List of `MedicinalProductAuthorizationJurisdictionalAuthorization` items (represented as `dict` in JSON). """
        
        self.legalStatusOfSupply = None
        """ The legal status of supply of the medicinal product as classified
        by the regulator.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.marketingStatus = None
        """ Marketing status of the medicinal product, in contrast to marketing
        authorizaton.
        List of `MarketingStatus` items (represented as `dict` in JSON). """
        
        self.procedure = None
        """ The regulatory procedure for granting or amending a marketing
        authorization.
        Type `MedicinalProductAuthorizationProcedure` (represented as `dict` in JSON). """
        
        self.regulator = None
        """ Medicines Regulatory Agency.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.restoreDate = None
        """ The date when a suspended the marketing or the marketing
        authorization of the product is anticipated to be restored.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.status = None
        """ The status of the marketing authorization.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.statusDate = None
        """ The date at which the given status has become applicable.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.validityPeriod = None
        """ The beginning of the time period in which the marketing
        authorization is in the specific status shall be specified A
        complete date consisting of day, month and year shall be specified
        using the ISO 8601 date format.
        Type `Period` (represented as `dict` in JSON). """
        
        super(MedicinalProductAuthorization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductAuthorization, self).elementProperties()
        js.extend([
            ("country", "country", codeableconcept.CodeableConcept, True, None, True),
            ("dataExclusivityPeriod", "dataExclusivityPeriod", period.Period, False, None, False),
            ("dateOfFirstAuthorization", "dateOfFirstAuthorization", fhirdate.FHIRDate, False, None, False),
            ("holder", "holder", fhirreference.FHIRReference, False, None, True),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("internationalBirthDate", "internationalBirthDate", fhirdate.FHIRDate, False, None, True),
            ("jurisdictionalAuthorization", "jurisdictionalAuthorization", MedicinalProductAuthorizationJurisdictionalAuthorization, True, None, False),
            ("legalStatusOfSupply", "legalStatusOfSupply", codeableconcept.CodeableConcept, False, None, True),
            ("marketingStatus", "marketingStatus", marketingstatus.MarketingStatus, True, None, False),
            ("procedure", "procedure", MedicinalProductAuthorizationProcedure, False, None, True),
            ("regulator", "regulator", fhirreference.FHIRReference, False, None, True),
            ("restoreDate", "restoreDate", fhirdate.FHIRDate, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, True),
            ("statusDate", "statusDate", fhirdate.FHIRDate, False, None, True),
            ("validityPeriod", "validityPeriod", period.Period, False, None, True),
        ])
        return js


from . import backboneelement

class MedicinalProductAuthorizationJurisdictionalAuthorization(backboneelement.BackboneElement):
    """ Authorization in areas within a country.
    """
    
    resource_type = "MedicinalProductAuthorizationJurisdictionalAuthorization"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.country = None
        """ Country of authorization.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Jurisdiction within a country.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.legalStatusOfSupply = None
        """ The legal status of supply in a jurisdiction or region.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.number = None
        """ The assigned number for the marketing authorization.
        Type `Identifier` (represented as `dict` in JSON). """
        
        super(MedicinalProductAuthorizationJurisdictionalAuthorization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductAuthorizationJurisdictionalAuthorization, self).elementProperties()
        js.extend([
            ("country", "country", codeableconcept.CodeableConcept, False, None, True),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, False, None, False),
            ("legalStatusOfSupply", "legalStatusOfSupply", codeableconcept.CodeableConcept, False, None, False),
            ("number", "number", identifier.Identifier, False, None, False),
        ])
        return js


class MedicinalProductAuthorizationProcedure(backboneelement.BackboneElement):
    """ The regulatory procedure for granting or amending a marketing authorization.
    """
    
    resource_type = "MedicinalProductAuthorizationProcedure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.application = None
        """ Applcations submitted to obtain a marketing authorization.
        List of `MedicinalProductAuthorizationProcedureApplication` items (represented as `dict` in JSON). """
        
        self.date = None
        """ Date of procedure.
        Type `Period` (represented as `dict` in JSON). """
        
        self.number = None
        """ Identifier for this procedure.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductAuthorizationProcedure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductAuthorizationProcedure, self).elementProperties()
        js.extend([
            ("application", "application", MedicinalProductAuthorizationProcedureApplication, True, None, False),
            ("date", "date", period.Period, False, None, False),
            ("number", "number", identifier.Identifier, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class MedicinalProductAuthorizationProcedureApplication(backboneelement.BackboneElement):
    """ Applcations submitted to obtain a marketing authorization.
    """
    
    resource_type = "MedicinalProductAuthorizationProcedureApplication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ Date that the application was made.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.number = None
        """ A unique identifier for the specific instance of an application
        shall be provided in text. The application identifier/number is
        usually assigned by a Medicines Regulatory Agency.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.type = None
        """ The type of the application.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductAuthorizationProcedureApplication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductAuthorizationProcedureApplication, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("number", "number", identifier.Identifier, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import marketingstatus
from . import period
