#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 (http://hl7.org/fhir/StructureDefinition/VisionPrescription) on 2018-05-12.
#  2018, SMART Health IT.


from . import domainresource

class VisionPrescription(domainresource.DomainResource):
    """ Prescription for vision correction products for a patient.
    
    An authorization for the supply of glasses and/or contact lenses to a
    patient.
    """
    
    resource_type = "VisionPrescription"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dateWritten = None
        """ When prescription was authorized.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.dispense = None
        """ Vision supply authorization.
        List of `VisionPrescriptionDispense` items (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Created during encounter / admission / stay.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who prescription is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.prescriber = None
        """ Who authorizes the vision product.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCodeableConcept = None
        """ Reason or indication for writing the prescription.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Reason or indication for writing the prescription.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        super(VisionPrescription, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(VisionPrescription, self).elementProperties()
        js.extend([
            ("dateWritten", "dateWritten", fhirdate.FHIRDate, False, None, False),
            ("dispense", "dispense", VisionPrescriptionDispense, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("prescriber", "prescriber", fhirreference.FHIRReference, False, None, False),
            ("reasonCodeableConcept", "reasonCodeableConcept", codeableconcept.CodeableConcept, False, "reason", False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False, "reason", False),
            ("status", "status", str, False, None, False),
        ])
        return js


from . import backboneelement

class VisionPrescriptionDispense(backboneelement.BackboneElement):
    """ Vision supply authorization.
    
    Deals with details of the dispense part of the supply specification.
    """
    
    resource_type = "VisionPrescriptionDispense"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.add = None
        """ Lens add.
        Type `float`. """
        
        self.axis = None
        """ Lens axis.
        Type `int`. """
        
        self.backCurve = None
        """ Contact lens back curvature.
        Type `float`. """
        
        self.brand = None
        """ Brand required.
        Type `str`. """
        
        self.color = None
        """ Color required.
        Type `str`. """
        
        self.cylinder = None
        """ Lens cylinder.
        Type `float`. """
        
        self.diameter = None
        """ Contact lens diameter.
        Type `float`. """
        
        self.duration = None
        """ Lens wear duration.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.eye = None
        """ right | left.
        Type `str`. """
        
        self.note = None
        """ Notes for coatings.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.power = None
        """ Contact lens power.
        Type `float`. """
        
        self.prism = None
        """ Lens prism.
        List of `VisionPrescriptionDispensePrism` items (represented as `dict` in JSON). """
        
        self.product = None
        """ Product to be supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sphere = None
        """ Lens sphere.
        Type `float`. """
        
        super(VisionPrescriptionDispense, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(VisionPrescriptionDispense, self).elementProperties()
        js.extend([
            ("add", "add", float, False, None, False),
            ("axis", "axis", int, False, None, False),
            ("backCurve", "backCurve", float, False, None, False),
            ("brand", "brand", str, False, None, False),
            ("color", "color", str, False, None, False),
            ("cylinder", "cylinder", float, False, None, False),
            ("diameter", "diameter", float, False, None, False),
            ("duration", "duration", quantity.Quantity, False, None, False),
            ("eye", "eye", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("power", "power", float, False, None, False),
            ("prism", "prism", VisionPrescriptionDispensePrism, True, None, False),
            ("product", "product", codeableconcept.CodeableConcept, False, None, False),
            ("sphere", "sphere", float, False, None, False),
        ])
        return js


class VisionPrescriptionDispensePrism(backboneelement.BackboneElement):
    """ Lens prism.
    
    Allows for adjustment on two axis.
    """
    
    resource_type = "VisionPrescriptionDispensePrism"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Amount of adjustment.
        Type `float`. """
        
        self.base = None
        """ up | down | in | out.
        Type `str`. """
        
        super(VisionPrescriptionDispensePrism, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(VisionPrescriptionDispensePrism, self).elementProperties()
        js.extend([
            ("amount", "amount", float, False, None, True),
            ("base", "base", str, False, None, True),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
