#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 (http://hl7.org/fhir/StructureDefinition/MedicinalProductDeviceSpec) on 2018-05-12.
#  2018, SMART Health IT.


from . import domainresource

class MedicinalProductDeviceSpec(domainresource.DomainResource):
    """ A detailed description of a device, typically as part of a regulated
    medicinal product. It is not intended to relace the Device resource, which
    covers use of device instances.
    """
    
    resource_type = "MedicinalProductDeviceSpec"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.batchIdentifier = None
        """ Batch number or expiry date of a device.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.listingNumber = None
        """ Device listing number.
        Type `str`. """
        
        self.manufacturer = None
        """ Manufacturer of this Device.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.material = None
        """ A substance used to create the material(s) of which the device is
        made.
        List of `MedicinalProductDeviceSpecMaterial` items (represented as `dict` in JSON). """
        
        self.modelNumber = None
        """ Device model or reference number.
        Type `str`. """
        
        self.nomenclature = None
        """ A nomenclature term for the device.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.otherCharacteristics = None
        """ Other codeable characteristics.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.physicalCharacteristics = None
        """ Dimensions, color etc..
        Type `ProdCharacteristic` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ The quantity of the device present in the packaging of a medicinal
        product.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.shelfLife = None
        """ Shelf Life and storage information.
        List of `ProductShelfLife` items (represented as `dict` in JSON). """
        
        self.sterilisationRequirement = None
        """ Whether the device must be sterilised before use.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sterilityIndicator = None
        """ Whether the device is supplied as sterile.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.tradeName = None
        """ Trade name of the device, where applicable.
        Type `str`. """
        
        self.type = None
        """ The type of device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.usage = None
        """ Usage pattern including the number of times that the device may be
        used.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductDeviceSpec, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductDeviceSpec, self).elementProperties()
        js.extend([
            ("batchIdentifier", "batchIdentifier", identifier.Identifier, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("listingNumber", "listingNumber", str, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("material", "material", MedicinalProductDeviceSpecMaterial, True, None, False),
            ("modelNumber", "modelNumber", str, False, None, False),
            ("nomenclature", "nomenclature", codeableconcept.CodeableConcept, True, None, False),
            ("otherCharacteristics", "otherCharacteristics", codeableconcept.CodeableConcept, True, None, False),
            ("physicalCharacteristics", "physicalCharacteristics", prodcharacteristic.ProdCharacteristic, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("shelfLife", "shelfLife", productshelflife.ProductShelfLife, True, None, False),
            ("sterilisationRequirement", "sterilisationRequirement", codeableconcept.CodeableConcept, False, None, False),
            ("sterilityIndicator", "sterilityIndicator", codeableconcept.CodeableConcept, False, None, False),
            ("tradeName", "tradeName", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("usage", "usage", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class MedicinalProductDeviceSpecMaterial(backboneelement.BackboneElement):
    """ A substance used to create the material(s) of which the device is made.
    """
    
    resource_type = "MedicinalProductDeviceSpecMaterial"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allergenicIndicator = None
        """ Whether the substance is a known or suspected allergen.
        Type `bool`. """
        
        self.alternate = None
        """ Indicates an alternative material of the device.
        Type `bool`. """
        
        self.substance = None
        """ The substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductDeviceSpecMaterial, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductDeviceSpecMaterial, self).elementProperties()
        js.extend([
            ("allergenicIndicator", "allergenicIndicator", bool, False, None, False),
            ("alternate", "alternate", bool, False, None, False),
            ("substance", "substance", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


from . import codeableconcept
from . import fhirreference
from . import identifier
from . import prodcharacteristic
from . import productshelflife
from . import quantity
