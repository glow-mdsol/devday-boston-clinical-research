#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 (http://hl7.org/fhir/StructureDefinition/DeviceComponent) on 2018-05-12.
#  2018, SMART Health IT.


from . import domainresource

class DeviceComponent(domainresource.DomainResource):
    """ An instance of a medical-related component of a medical device.
    
    The characteristics, operational status and capabilities of a medical-
    related component of a medical device.
    """
    
    resource_type = "DeviceComponent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Instance identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.languageCode = None
        """ Language code for the human-readable text strings produced by the
        device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.lastSystemChange = None
        """ Recent system change timestamp.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.measurementPrinciple = None
        """ other | chemical | electrical | impedance | nuclear | optical |
        thermal | biological | mechanical | acoustical | manual+.
        Type `str`. """
        
        self.operationalStatus = None
        """ Current operational status of the component, for example On, Off or
        Standby.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.parameterGroup = None
        """ Current supported parameter group.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.parent = None
        """ Parent resource link.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.productionSpecification = None
        """ Specification details such as Component Revisions, or Serial
        Numbers.
        List of `DeviceComponentProductionSpecification` items (represented as `dict` in JSON). """
        
        self.property = None
        """ Other Attributes.
        List of `DeviceComponentProperty` items (represented as `dict` in JSON). """
        
        self.source = None
        """ Top-level device resource link.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ What kind of component it is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DeviceComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceComponent, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("languageCode", "languageCode", codeableconcept.CodeableConcept, False, None, False),
            ("lastSystemChange", "lastSystemChange", fhirdate.FHIRDate, False, None, False),
            ("measurementPrinciple", "measurementPrinciple", str, False, None, False),
            ("operationalStatus", "operationalStatus", codeableconcept.CodeableConcept, True, None, False),
            ("parameterGroup", "parameterGroup", codeableconcept.CodeableConcept, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, False, None, False),
            ("productionSpecification", "productionSpecification", DeviceComponentProductionSpecification, True, None, False),
            ("property", "property", DeviceComponentProperty, True, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


from . import backboneelement

class DeviceComponentProductionSpecification(backboneelement.BackboneElement):
    """ Specification details such as Component Revisions, or Serial Numbers.
    
    The production specification such as component revision, serial number,
    etc.
    """
    
    resource_type = "DeviceComponentProductionSpecification"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.componentId = None
        """ Internal component unique identification.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.productionSpec = None
        """ A printable string defining the component.
        Type `str`. """
        
        self.specType = None
        """ Type or kind of production specification, for example serial number
        or software revision.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DeviceComponentProductionSpecification, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceComponentProductionSpecification, self).elementProperties()
        js.extend([
            ("componentId", "componentId", identifier.Identifier, False, None, False),
            ("productionSpec", "productionSpec", str, False, None, False),
            ("specType", "specType", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class DeviceComponentProperty(backboneelement.BackboneElement):
    """ Other Attributes.
    
    Other device properties expressed as a `type` which identifies the property
    and a value(s) either as a quantity or a code.
    """
    
    resource_type = "DeviceComponentProperty"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Code that specifies the property.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCode = None
        """ Property value as a code.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Property value as a quantity.
        List of `Quantity` items (represented as `dict` in JSON). """
        
        super(DeviceComponentProperty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceComponentProperty, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueCode", "valueCode", codeableconcept.CodeableConcept, True, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, True, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
