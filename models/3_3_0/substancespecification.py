#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 (http://hl7.org/fhir/StructureDefinition/SubstanceSpecification) on 2018-05-12.
#  2018, SMART Health IT.


from . import domainresource

class SubstanceSpecification(domainresource.DomainResource):
    """ The detailed description of a substance, typically at a level beyond what
    is used for prescribing.
    """
    
    resource_type = "SubstanceSpecification"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment = None
        """ Textual comment.
        Type `str`. """
        
        self.identifier = None
        """ Identifier by which this substance is known.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.moiety = None
        """ Moiety, for structural modifications.
        List of `SubstanceSpecificationMoiety` items (represented as `dict` in JSON). """
        
        self.molecularWeight = None
        """ The molecular weight or weight range (for proteins, polymers or
        nucleic acids).
        List of `SubstanceSpecificationStructureIsotopeMolecularWeight` items (represented as `dict` in JSON). """
        
        self.polymer = None
        """ Data items specific to polymers.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.property = None
        """ General specifications for this substance, including how it is
        related to other substances.
        List of `SubstanceSpecificationProperty` items (represented as `dict` in JSON). """
        
        self.referenceInformation = None
        """ General information detailing this substance.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.referenceSource = None
        """ Supporting literature.
        List of `str` items. """
        
        self.stoichiometric = None
        """ Chemicals may be stoichiometric or non-stoichiometric.
        Type `bool`. """
        
        self.structure = None
        """ Structural information.
        Type `SubstanceSpecificationStructure` (represented as `dict` in JSON). """
        
        self.substanceCode = None
        """ Codes associated with the substance.
        List of `SubstanceSpecificationSubstanceCode` items (represented as `dict` in JSON). """
        
        self.substanceName = None
        """ Names applicable to this substence.
        List of `SubstanceSpecificationSubstanceName` items (represented as `dict` in JSON). """
        
        self.type = None
        """ High level categorization, e.g. polymer or nucleic acid.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecification, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecification, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("moiety", "moiety", SubstanceSpecificationMoiety, True, None, False),
            ("molecularWeight", "molecularWeight", SubstanceSpecificationStructureIsotopeMolecularWeight, True, None, False),
            ("polymer", "polymer", fhirreference.FHIRReference, False, None, False),
            ("property", "property", SubstanceSpecificationProperty, True, None, False),
            ("referenceInformation", "referenceInformation", fhirreference.FHIRReference, False, None, False),
            ("referenceSource", "referenceSource", str, True, None, False),
            ("stoichiometric", "stoichiometric", bool, False, None, False),
            ("structure", "structure", SubstanceSpecificationStructure, False, None, False),
            ("substanceCode", "substanceCode", SubstanceSpecificationSubstanceCode, True, None, False),
            ("substanceName", "substanceName", SubstanceSpecificationSubstanceName, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class SubstanceSpecificationMoiety(backboneelement.BackboneElement):
    """ Moiety, for structural modifications.
    """
    
    resource_type = "SubstanceSpecificationMoiety"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Quantitative value for this moiety.
        Type `str`. """
        
        self.identifier = None
        """ Identifier by which this moiety substance is known.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.molecularFormula = None
        """ Molecular formula.
        Type `str`. """
        
        self.name = None
        """ Textual name for this moiety substance.
        Type `str`. """
        
        self.opticalActivity = None
        """ Optical activity type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.role = None
        """ Role that the moiety is playing.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.stereochemistry = None
        """ Stereochemistry type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationMoiety, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationMoiety, self).elementProperties()
        js.extend([
            ("amount", "amount", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("molecularFormula", "molecularFormula", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("opticalActivity", "opticalActivity", codeableconcept.CodeableConcept, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("stereochemistry", "stereochemistry", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SubstanceSpecificationProperty(backboneelement.BackboneElement):
    """ General specifications for this substance, including how it is related to
    other substances.
    """
    
    resource_type = "SubstanceSpecificationProperty"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Quantitative value for this property.
        Type `str`. """
        
        self.name = None
        """ Description todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.parameters = None
        """ A field that should be used to capture parameters that were used in
        the measurement of a property.
        Type `str`. """
        
        self.substanceId = None
        """ Identifier for a substance upon which a defining property depends.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.substanceName = None
        """ Description todo.
        Type `str`. """
        
        self.type = None
        """ Description todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationProperty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationProperty, self).elementProperties()
        js.extend([
            ("amount", "amount", str, False, None, False),
            ("name", "name", codeableconcept.CodeableConcept, False, None, False),
            ("parameters", "parameters", str, False, None, False),
            ("substanceId", "substanceId", identifier.Identifier, False, None, False),
            ("substanceName", "substanceName", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SubstanceSpecificationStructure(backboneelement.BackboneElement):
    """ Structural information.
    """
    
    resource_type = "SubstanceSpecificationStructure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.isotope = None
        """ Applicable for single substances that contain a radionuclide or a
        non-natural isotopic ratio.
        List of `SubstanceSpecificationStructureIsotope` items (represented as `dict` in JSON). """
        
        self.molecularFormula = None
        """ Molecular formula.
        Type `str`. """
        
        self.molecularFormulaByMoiety = None
        """ Specified per moiety according to the Hill system, i.e. first C,
        then H, then alphabetical. and each moiety separated by a dot.
        Type `str`. """
        
        self.molecularWeight = None
        """ The molecular weight or weight range (for proteins, polymers or
        nucleic acids).
        Type `SubstanceSpecificationStructureIsotopeMolecularWeight` (represented as `dict` in JSON). """
        
        self.opticalActivity = None
        """ Optical activity type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.referenceSource = None
        """ Supporting literature.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.stereochemistry = None
        """ Stereochemistry type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.structuralRepresentation = None
        """ Molectular structural representation.
        List of `SubstanceSpecificationStructureStructuralRepresentation` items (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationStructure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationStructure, self).elementProperties()
        js.extend([
            ("isotope", "isotope", SubstanceSpecificationStructureIsotope, True, None, False),
            ("molecularFormula", "molecularFormula", str, False, None, False),
            ("molecularFormulaByMoiety", "molecularFormulaByMoiety", str, False, None, False),
            ("molecularWeight", "molecularWeight", SubstanceSpecificationStructureIsotopeMolecularWeight, False, None, False),
            ("opticalActivity", "opticalActivity", codeableconcept.CodeableConcept, False, None, False),
            ("referenceSource", "referenceSource", fhirreference.FHIRReference, True, None, False),
            ("stereochemistry", "stereochemistry", codeableconcept.CodeableConcept, False, None, False),
            ("structuralRepresentation", "structuralRepresentation", SubstanceSpecificationStructureStructuralRepresentation, True, None, False),
        ])
        return js


class SubstanceSpecificationStructureIsotope(backboneelement.BackboneElement):
    """ Applicable for single substances that contain a radionuclide or a non-
    natural isotopic ratio.
    """
    
    resource_type = "SubstanceSpecificationStructureIsotope"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Quantitative values for this isotope.
        Type `str`. """
        
        self.molecularWeight = None
        """ The molecular weight or weight range (for proteins, polymers or
        nucleic acids).
        Type `SubstanceSpecificationStructureIsotopeMolecularWeight` (represented as `dict` in JSON). """
        
        self.nuclideHalfLife = None
        """ Half life - for a non-natural nuclide.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.nuclideId = None
        """ Substance identifier for each non-natural or radioisotope.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.nuclideName = None
        """ Substance name for each non-natural or radioisotope.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.substitutionType = None
        """ The type of isotopic substitution present in a single substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationStructureIsotope, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationStructureIsotope, self).elementProperties()
        js.extend([
            ("amount", "amount", str, False, None, False),
            ("molecularWeight", "molecularWeight", SubstanceSpecificationStructureIsotopeMolecularWeight, False, None, False),
            ("nuclideHalfLife", "nuclideHalfLife", quantity.Quantity, False, None, False),
            ("nuclideId", "nuclideId", identifier.Identifier, False, None, False),
            ("nuclideName", "nuclideName", codeableconcept.CodeableConcept, False, None, False),
            ("substitutionType", "substitutionType", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SubstanceSpecificationStructureIsotopeMolecularWeight(backboneelement.BackboneElement):
    """ The molecular weight or weight range (for proteins, polymers or nucleic
    acids).
    """
    
    resource_type = "SubstanceSpecificationStructureIsotopeMolecularWeight"
    
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
        Type `str`. """
        
        self.method = None
        """ The method by which the molecular weight was determined.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of molecular weight such as exact, average (also known as.
        number average), weight average.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationStructureIsotopeMolecularWeight, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationStructureIsotopeMolecularWeight, self).elementProperties()
        js.extend([
            ("amount", "amount", str, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SubstanceSpecificationStructureStructuralRepresentation(backboneelement.BackboneElement):
    """ Molectular structural representation.
    """
    
    resource_type = "SubstanceSpecificationStructureStructuralRepresentation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.attachment = None
        """ An attached file with the structural representation.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.representation = None
        """ The structural representation as text string in a format e.g.
        InChI, SMILES, MOLFILE, CDX.
        Type `str`. """
        
        self.type = None
        """ The type of structure (e.g. Full, Partial, Representative).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationStructureStructuralRepresentation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationStructureStructuralRepresentation, self).elementProperties()
        js.extend([
            ("attachment", "attachment", attachment.Attachment, False, None, False),
            ("representation", "representation", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SubstanceSpecificationSubstanceCode(backboneelement.BackboneElement):
    """ Codes associated with the substance.
    """
    
    resource_type = "SubstanceSpecificationSubstanceCode"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ The specific code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.comment = None
        """ Any comment can be provided in this field, if necessary.
        Type `str`. """
        
        self.referenceSource = None
        """ Supporting literature.
        List of `str` items. """
        
        self.status = None
        """ Status of the code assignment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.statusDate = None
        """ The date at which the code status is changed as part of the
        terminology maintenance.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(SubstanceSpecificationSubstanceCode, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationSubstanceCode, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("referenceSource", "referenceSource", str, True, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("statusDate", "statusDate", fhirdate.FHIRDate, False, None, False),
        ])
        return js


class SubstanceSpecificationSubstanceName(backboneelement.BackboneElement):
    """ Names applicable to this substence.
    """
    
    resource_type = "SubstanceSpecificationSubstanceName"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.domain = None
        """ The use context of this name for example if there is a different
        name a drug active ingredient as opposed to a food colour additive.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ The jurisdiction where this name applies.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.language = None
        """ Language of the name.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name = None
        """ The actual name.
        Type `str`. """
        
        self.officialName = None
        """ Details of the official nature of this name.
        List of `SubstanceSpecificationSubstanceNameOfficialName` items (represented as `dict` in JSON). """
        
        self.referenceSource = None
        """ Supporting literature.
        List of `str` items. """
        
        self.type = None
        """ Name type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationSubstanceName, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationSubstanceName, self).elementProperties()
        js.extend([
            ("domain", "domain", codeableconcept.CodeableConcept, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("language", "language", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("officialName", "officialName", SubstanceSpecificationSubstanceNameOfficialName, True, None, False),
            ("referenceSource", "referenceSource", str, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SubstanceSpecificationSubstanceNameOfficialName(backboneelement.BackboneElement):
    """ Details of the official nature of this name.
    """
    
    resource_type = "SubstanceSpecificationSubstanceNameOfficialName"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authority = None
        """ Which authority uses this official name.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.date = None
        """ Date of official name change.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.status = None
        """ The status of the official name.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationSubstanceNameOfficialName, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationSubstanceNameOfficialName, self).elementProperties()
        js.extend([
            ("authority", "authority", codeableconcept.CodeableConcept, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
