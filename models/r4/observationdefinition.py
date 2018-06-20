#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 (http://hl7.org/fhir/StructureDefinition/ObservationDefinition) on 2018-05-12.
#  2018, SMART Health IT.


from . import domainresource

class ObservationDefinition(domainresource.DomainResource):
    """ Definition of an observation.
    
    Set of definitional characteristics for a kind of observation or
    measurement produced or consumed by an orderable health care service.
    """
    
    resource_type = "ObservationDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.abnormalCodedValueSet = None
        """ Value set of abnormal coded values for the observation.
        Type `str`. """
        
        self.category = None
        """ Category of observation.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.code = None
        """ Type of observation (code / type).
        Type `Coding` (represented as `dict` in JSON). """
        
        self.criticalCodedValueSet = None
        """ Value set of critical coded values for the observation.
        Type `str`. """
        
        self.method = None
        """ The method or technique used to perform the observation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.multipleResultsAllowed = None
        """ Multiple results allowed.
        Type `bool`. """
        
        self.normalCodedValueSet = None
        """ Value set of normal coded values for the observation.
        Type `str`. """
        
        self.permittedDataType = None
        """ Permitted data type for observation value.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.preferredReportName = None
        """ Preferred report name.
        Type `str`. """
        
        self.qualifiedInterval = None
        """ Reference range for observation result.
        List of `ObservationDefinitionQualifiedInterval` items (represented as `dict` in JSON). """
        
        self.quantitativeDetails = None
        """ Characteristics of quantitative results.
        Type `ObservationDefinitionQuantitativeDetails` (represented as `dict` in JSON). """
        
        self.validCodedValueSet = None
        """ Value set of valid coded values for the observation.
        Type `str`. """
        
        super(ObservationDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ObservationDefinition, self).elementProperties()
        js.extend([
            ("abnormalCodedValueSet", "abnormalCodedValueSet", str, False, None, False),
            ("category", "category", coding.Coding, False, None, False),
            ("code", "code", coding.Coding, False, None, True),
            ("criticalCodedValueSet", "criticalCodedValueSet", str, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("multipleResultsAllowed", "multipleResultsAllowed", bool, False, None, False),
            ("normalCodedValueSet", "normalCodedValueSet", str, False, None, False),
            ("permittedDataType", "permittedDataType", coding.Coding, True, None, False),
            ("preferredReportName", "preferredReportName", str, False, None, False),
            ("qualifiedInterval", "qualifiedInterval", ObservationDefinitionQualifiedInterval, True, None, False),
            ("quantitativeDetails", "quantitativeDetails", ObservationDefinitionQuantitativeDetails, False, None, False),
            ("validCodedValueSet", "validCodedValueSet", str, False, None, False),
        ])
        return js


from . import backboneelement

class ObservationDefinitionQualifiedInterval(backboneelement.BackboneElement):
    """ Reference range for observation result.
    
    Reference range for ordinal and continuous observations.
    """
    
    resource_type = "ObservationDefinitionQualifiedInterval"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.age = None
        """ Applicable age range, if relevant.
        Type `Range` (represented as `dict` in JSON). """
        
        self.appliesTo = None
        """ Reference range population.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.category = None
        """ The category or type of interval.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.condition = None
        """ Condition associated with the reference range.
        Type `str`. """
        
        self.gestationalAge = None
        """ Applicable gestational age range, if relevant.
        Type `Range` (represented as `dict` in JSON). """
        
        self.range = None
        """ Low bound of reference range, if relevant.
        Type `Range` (represented as `dict` in JSON). """
        
        self.type = None
        """ Reference range qualifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ObservationDefinitionQualifiedInterval, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ObservationDefinitionQualifiedInterval, self).elementProperties()
        js.extend([
            ("age", "age", range.Range, False, None, False),
            ("appliesTo", "appliesTo", codeableconcept.CodeableConcept, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("condition", "condition", str, False, None, False),
            ("gestationalAge", "gestationalAge", range.Range, False, None, False),
            ("range", "range", range.Range, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ObservationDefinitionQuantitativeDetails(backboneelement.BackboneElement):
    """ Characteristics of quantitative results.
    
    Characteristics for quantitative results of this observation.
    """
    
    resource_type = "ObservationDefinitionQuantitativeDetails"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.conversionFactor = None
        """ SI to Customary unit conversion factor.
        Type `float`. """
        
        self.customaryUnit = None
        """ Customary unit for quantitative results.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.decimalPrecision = None
        """ Decimal precision of observation quantitative results.
        Type `int`. """
        
        self.unit = None
        """ SI unit for quantitative results.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ObservationDefinitionQuantitativeDetails, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ObservationDefinitionQuantitativeDetails, self).elementProperties()
        js.extend([
            ("conversionFactor", "conversionFactor", float, False, None, False),
            ("customaryUnit", "customaryUnit", coding.Coding, False, None, False),
            ("decimalPrecision", "decimalPrecision", int, False, None, False),
            ("unit", "unit", coding.Coding, False, None, False),
        ])
        return js


from . import codeableconcept
from . import coding
from . import range
