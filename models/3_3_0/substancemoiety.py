#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 (http://hl7.org/fhir/StructureDefinition/SubstanceMoiety) on 2018-05-12.
#  2018, SMART Health IT.


from . import backboneelement

class SubstanceMoiety(backboneelement.BackboneElement):
    """ Chemical substances are a single substance type whose primary defining
    element is the molecular structure. Chemical substances shall be defined on
    the basis of their complete covalent molecular structure; the presence of a
    salt (counter-ion) and/or solvates (water, alcohols) is also captured.
    Purity, grade, physical form or particle size are not taken into account in
    the definition of a chemical substance or in the assignment of a Substance
    ID.
    """
    
    resource_type = "SubstanceMoiety"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Used to capture quantitative values for a variety of elements. If
        only limits are given, the arithmetic mean would be the average. If
        only a single definite value for a given element is given, it would
        be captured in this field.
        Type `SubstanceAmount` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ The unique identifier assigned to the substance representing the
        moiety based on the ISO 11238 substance controlled vocabulary.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.molecularFormula = None
        """ Molecular formula shall be captured as described in 4.7.3.
        Type `str`. """
        
        self.name = None
        """ The name of the moiety shall be provided.
        Type `str`. """
        
        self.opticalActivity = None
        """ Optical activity shall be captured as described in 4.7.2.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.role = None
        """ The role of the moiety should be specified if there is a specific
        role the moiety is playing.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.stereochemistry = None
        """ Stereochemistry shall be captured as described in 4.7.1.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceMoiety, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceMoiety, self).elementProperties()
        js.extend([
            ("amount", "amount", substanceamount.SubstanceAmount, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("molecularFormula", "molecularFormula", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("opticalActivity", "opticalActivity", codeableconcept.CodeableConcept, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("stereochemistry", "stereochemistry", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import codeableconcept
from . import identifier
from . import substanceamount
