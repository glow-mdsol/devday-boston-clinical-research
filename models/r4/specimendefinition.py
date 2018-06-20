#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 (http://hl7.org/fhir/StructureDefinition/SpecimenDefinition) on 2018-05-12.
#  2018, SMART Health IT.


from . import domainresource

class SpecimenDefinition(domainresource.DomainResource):
    """ Kind of specimen.
    
    A kind of specimen with associated set of requirements.
    """
    
    resource_type = "SpecimenDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.collection = None
        """ Specimen collection procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifier of a kind of specimen.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.patientPreparation = None
        """ Patient preparation for collection.
        Type `str`. """
        
        self.specimenToLab = None
        """ Specimen in container intended for testing by lab.
        List of `SpecimenDefinitionSpecimenToLab` items (represented as `dict` in JSON). """
        
        self.timeAspect = None
        """ Time aspect for collection.
        Type `str`. """
        
        self.typeCollected = None
        """ Kind of material to collect.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SpecimenDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenDefinition, self).elementProperties()
        js.extend([
            ("collection", "collection", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("patientPreparation", "patientPreparation", str, False, None, False),
            ("specimenToLab", "specimenToLab", SpecimenDefinitionSpecimenToLab, True, None, False),
            ("timeAspect", "timeAspect", str, False, None, False),
            ("typeCollected", "typeCollected", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class SpecimenDefinitionSpecimenToLab(backboneelement.BackboneElement):
    """ Specimen in container intended for testing by lab.
    
    Specimen conditioned in a container as expected by the testing laboratory.
    """
    
    resource_type = "SpecimenDefinitionSpecimenToLab"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.containerAdditive = None
        """ Additive associated with container.
        List of `SpecimenDefinitionSpecimenToLabContainerAdditive` items (represented as `dict` in JSON). """
        
        self.containerCap = None
        """ Color of container cap.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.containerCapacity = None
        """ Container capacity.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.containerDescription = None
        """ Container description.
        Type `str`. """
        
        self.containerMaterial = None
        """ Container material.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.containerMinimumVolume = None
        """ Minimum volume.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.containerPreparation = None
        """ Specimen container preparation.
        Type `str`. """
        
        self.containerType = None
        """ Kind of container associated with the kind of specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.handling = None
        """ Specimen handling before testing.
        List of `SpecimenDefinitionSpecimenToLabHandling` items (represented as `dict` in JSON). """
        
        self.isDerived = None
        """ Primary or secondary specimen.
        Type `bool`. """
        
        self.preference = None
        """ preferred | alternate.
        Type `str`. """
        
        self.rejectionCriterion = None
        """ Rejection criterion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.requirement = None
        """ Specimen requirements.
        Type `str`. """
        
        self.retentionTime = None
        """ Specimen retention time.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of intended specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SpecimenDefinitionSpecimenToLab, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenDefinitionSpecimenToLab, self).elementProperties()
        js.extend([
            ("containerAdditive", "containerAdditive", SpecimenDefinitionSpecimenToLabContainerAdditive, True, None, False),
            ("containerCap", "containerCap", codeableconcept.CodeableConcept, False, None, False),
            ("containerCapacity", "containerCapacity", quantity.Quantity, False, None, False),
            ("containerDescription", "containerDescription", str, False, None, False),
            ("containerMaterial", "containerMaterial", codeableconcept.CodeableConcept, False, None, False),
            ("containerMinimumVolume", "containerMinimumVolume", quantity.Quantity, False, None, False),
            ("containerPreparation", "containerPreparation", str, False, None, False),
            ("containerType", "containerType", codeableconcept.CodeableConcept, False, None, False),
            ("handling", "handling", SpecimenDefinitionSpecimenToLabHandling, True, None, False),
            ("isDerived", "isDerived", bool, False, None, True),
            ("preference", "preference", str, False, None, True),
            ("rejectionCriterion", "rejectionCriterion", codeableconcept.CodeableConcept, True, None, False),
            ("requirement", "requirement", str, False, None, False),
            ("retentionTime", "retentionTime", duration.Duration, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SpecimenDefinitionSpecimenToLabContainerAdditive(backboneelement.BackboneElement):
    """ Additive associated with container.
    
    Substance introduced in the kind of container to preserve, maintain or
    enhance the specimen. Examples: Formalin, Citrate, EDTA.
    """
    
    resource_type = "SpecimenDefinitionSpecimenToLabContainerAdditive"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additiveCodeableConcept = None
        """ Additive associated with container.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.additiveReference = None
        """ Additive associated with container.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(SpecimenDefinitionSpecimenToLabContainerAdditive, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenDefinitionSpecimenToLabContainerAdditive, self).elementProperties()
        js.extend([
            ("additiveCodeableConcept", "additiveCodeableConcept", codeableconcept.CodeableConcept, False, "additive", True),
            ("additiveReference", "additiveReference", fhirreference.FHIRReference, False, "additive", True),
        ])
        return js


class SpecimenDefinitionSpecimenToLabHandling(backboneelement.BackboneElement):
    """ Specimen handling before testing.
    
    Set of instructions for conservation/transport of the specimen at a defined
    temperature interval, prior the testing process.
    """
    
    resource_type = "SpecimenDefinitionSpecimenToLabHandling"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.conditionSet = None
        """ Conservation condition set.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.instruction = None
        """ Conservation instruction.
        Type `str`. """
        
        self.lightExposure = None
        """ Light exposure.
        Type `str`. """
        
        self.maxDuration = None
        """ Maximum conservation time.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.tempRange = None
        """ Temperature range.
        Type `Range` (represented as `dict` in JSON). """
        
        super(SpecimenDefinitionSpecimenToLabHandling, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenDefinitionSpecimenToLabHandling, self).elementProperties()
        js.extend([
            ("conditionSet", "conditionSet", codeableconcept.CodeableConcept, False, None, False),
            ("instruction", "instruction", str, False, None, False),
            ("lightExposure", "lightExposure", str, False, None, False),
            ("maxDuration", "maxDuration", duration.Duration, False, None, False),
            ("tempRange", "tempRange", range.Range, False, None, False),
        ])
        return js


from . import codeableconcept
from . import duration
from . import fhirreference
from . import identifier
from . import quantity
from . import range
