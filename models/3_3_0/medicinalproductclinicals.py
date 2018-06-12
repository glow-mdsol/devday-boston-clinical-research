#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 (http://hl7.org/fhir/StructureDefinition/MedicinalProductClinicals) on 2018-05-12.
#  2018, SMART Health IT.


from . import domainresource

class MedicinalProductClinicals(domainresource.DomainResource):
    """ MedicinalProductClinicals.
    
    The clinical particulars - indications, contraindications etc. of a
    medicinal product, including for regulatory purposes.
    """
    
    resource_type = "MedicinalProductClinicals"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contraindication = None
        """ Contraindication for the medicinal product.
        List of `MedicinalProductClinicalsContraindication` items (represented as `dict` in JSON). """
        
        self.interactions = None
        """ The interactions of the medicinal product with other medicinal
        products, or other forms of interactions.
        List of `MedicinalProductClinicalsInteractions` items (represented as `dict` in JSON). """
        
        self.therapeuticIndication = None
        """ Indication for the Medicinal Product.
        List of `MedicinalProductClinicalsTherapeuticIndication` items (represented as `dict` in JSON). """
        
        self.undesirableEffects = None
        """ Describe the undesirable effects of the medicinal product.
        List of `MedicinalProductClinicalsUndesirableEffects` items (represented as `dict` in JSON). """
        
        super(MedicinalProductClinicals, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductClinicals, self).elementProperties()
        js.extend([
            ("contraindication", "contraindication", MedicinalProductClinicalsContraindication, True, None, False),
            ("interactions", "interactions", MedicinalProductClinicalsInteractions, True, None, False),
            ("therapeuticIndication", "therapeuticIndication", MedicinalProductClinicalsTherapeuticIndication, True, None, True),
            ("undesirableEffects", "undesirableEffects", MedicinalProductClinicalsUndesirableEffects, True, None, False),
        ])
        return js


from . import backboneelement

class MedicinalProductClinicalsContraindication(backboneelement.BackboneElement):
    """ Contraindication for the medicinal product.
    """
    
    resource_type = "MedicinalProductClinicalsContraindication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comorbidity = None
        """ A comorbidity (concurrent condition) or coinfection.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.disease = None
        """ The disease, symptom or procedure for the contraindication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.diseaseStatus = None
        """ The status of the disease or symptom for the contraindication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.otherTherapy = None
        """ Information about the use of the medicinal product in relation to
        other therapies described as part of the contraindication.
        List of `MedicinalProductClinicalsTherapeuticIndicationOtherTherapy` items (represented as `dict` in JSON). """
        
        self.population = None
        """ The population group to which this applies.
        List of `MedicinalProductClinicalsUndesirableEffectsPopulation` items (represented as `dict` in JSON). """
        
        self.therapeuticIndication = None
        """ Information about the use of the medicinal product in relation to
        other therapies as part of the indication.
        List of `MedicinalProductClinicalsTherapeuticIndication` items (represented as `dict` in JSON). """
        
        super(MedicinalProductClinicalsContraindication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductClinicalsContraindication, self).elementProperties()
        js.extend([
            ("comorbidity", "comorbidity", codeableconcept.CodeableConcept, True, None, False),
            ("disease", "disease", codeableconcept.CodeableConcept, False, None, False),
            ("diseaseStatus", "diseaseStatus", codeableconcept.CodeableConcept, False, None, False),
            ("otherTherapy", "otherTherapy", MedicinalProductClinicalsTherapeuticIndicationOtherTherapy, True, None, False),
            ("population", "population", MedicinalProductClinicalsUndesirableEffectsPopulation, True, None, False),
            ("therapeuticIndication", "therapeuticIndication", MedicinalProductClinicalsTherapeuticIndication, True, None, False),
        ])
        return js


class MedicinalProductClinicalsInteractions(backboneelement.BackboneElement):
    """ The interactions of the medicinal product with other medicinal products, or
    other forms of interactions.
    """
    
    resource_type = "MedicinalProductClinicalsInteractions"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.effect = None
        """ The effect of the interaction.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.incidence = None
        """ The incidence of the interaction.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.interactant = None
        """ The specific medication, food or laboratory test that interacts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.management = None
        """ Actions for managing the interaction.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ The type of the interaction.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductClinicalsInteractions, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductClinicalsInteractions, self).elementProperties()
        js.extend([
            ("effect", "effect", codeableconcept.CodeableConcept, False, None, False),
            ("incidence", "incidence", codeableconcept.CodeableConcept, False, None, False),
            ("interactant", "interactant", codeableconcept.CodeableConcept, True, None, False),
            ("management", "management", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class MedicinalProductClinicalsTherapeuticIndication(backboneelement.BackboneElement):
    """ Indication for the Medicinal Product.
    """
    
    resource_type = "MedicinalProductClinicalsTherapeuticIndication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comorbidity = None
        """ Comorbidity (concurrent condition) or co-infection as part of the
        indication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.diseaseStatus = None
        """ The status of the disease or symptom for which the indication
        applies.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.diseaseSymptomProcedure = None
        """ The disease, symptom or procedure that is the indication for
        treatment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.duration = None
        """ Timing or duration information as part of the indication.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.intendedEffect = None
        """ The intended effect, aim or strategy to be achieved by the
        indication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.otherTherapy = None
        """ Information about the use of the medicinal product in relation to
        other therapies described as part of the indication.
        List of `MedicinalProductClinicalsTherapeuticIndicationOtherTherapy` items (represented as `dict` in JSON). """
        
        self.population = None
        """ The population group to which this applies.
        List of `MedicinalProductClinicalsUndesirableEffectsPopulation` items (represented as `dict` in JSON). """
        
        self.undesirableEffects = None
        """ Information about the use of the medicinal product in relation to
        other therapies as part of the indication.
        List of `MedicinalProductClinicalsUndesirableEffects` items (represented as `dict` in JSON). """
        
        super(MedicinalProductClinicalsTherapeuticIndication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductClinicalsTherapeuticIndication, self).elementProperties()
        js.extend([
            ("comorbidity", "comorbidity", codeableconcept.CodeableConcept, True, None, False),
            ("diseaseStatus", "diseaseStatus", codeableconcept.CodeableConcept, False, None, False),
            ("diseaseSymptomProcedure", "diseaseSymptomProcedure", codeableconcept.CodeableConcept, False, None, False),
            ("duration", "duration", quantity.Quantity, False, None, False),
            ("intendedEffect", "intendedEffect", codeableconcept.CodeableConcept, False, None, False),
            ("otherTherapy", "otherTherapy", MedicinalProductClinicalsTherapeuticIndicationOtherTherapy, True, None, False),
            ("population", "population", MedicinalProductClinicalsUndesirableEffectsPopulation, True, None, False),
            ("undesirableEffects", "undesirableEffects", MedicinalProductClinicalsUndesirableEffects, True, None, False),
        ])
        return js


class MedicinalProductClinicalsTherapeuticIndicationOtherTherapy(backboneelement.BackboneElement):
    """ Information about the use of the medicinal product in relation to other
    therapies described as part of the indication.
    """
    
    resource_type = "MedicinalProductClinicalsTherapeuticIndicationOtherTherapy"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.medicationCodeableConcept = None
        """ Reference to a specific medication (active substance, medicinal
        product or class of products) as part of an indication or
        contraindication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationReference = None
        """ Reference to a specific medication (active substance, medicinal
        product or class of products) as part of an indication or
        contraindication.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.therapyRelationshipType = None
        """ The type of relationship between the medicinal product indication
        or contraindication and another therapy.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductClinicalsTherapeuticIndicationOtherTherapy, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductClinicalsTherapeuticIndicationOtherTherapy, self).elementProperties()
        js.extend([
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("therapyRelationshipType", "therapyRelationshipType", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class MedicinalProductClinicalsUndesirableEffects(backboneelement.BackboneElement):
    """ Describe the undesirable effects of the medicinal product.
    """
    
    resource_type = "MedicinalProductClinicalsUndesirableEffects"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.classification = None
        """ Classification of the effect.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.frequencyOfOccurrence = None
        """ The frequency of occurrence of the effect.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.population = None
        """ The population group to which this applies.
        List of `MedicinalProductClinicalsUndesirableEffectsPopulation` items (represented as `dict` in JSON). """
        
        self.symptomConditionEffect = None
        """ The symptom, condition or undesirable effect.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductClinicalsUndesirableEffects, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductClinicalsUndesirableEffects, self).elementProperties()
        js.extend([
            ("classification", "classification", codeableconcept.CodeableConcept, False, None, False),
            ("frequencyOfOccurrence", "frequencyOfOccurrence", codeableconcept.CodeableConcept, False, None, False),
            ("population", "population", MedicinalProductClinicalsUndesirableEffectsPopulation, True, None, False),
            ("symptomConditionEffect", "symptomConditionEffect", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class MedicinalProductClinicalsUndesirableEffectsPopulation(backboneelement.BackboneElement):
    """ The population group to which this applies.
    """
    
    resource_type = "MedicinalProductClinicalsUndesirableEffectsPopulation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.ageCodeableConcept = None
        """ The age of the specific population.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.ageRange = None
        """ The age of the specific population.
        Type `Range` (represented as `dict` in JSON). """
        
        self.gender = None
        """ The gender of the specific population.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.physiologicalCondition = None
        """ The existing physiological conditions of the specific population to
        which this applies.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.race = None
        """ Race of the specific population.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductClinicalsUndesirableEffectsPopulation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductClinicalsUndesirableEffectsPopulation, self).elementProperties()
        js.extend([
            ("ageCodeableConcept", "ageCodeableConcept", codeableconcept.CodeableConcept, False, "age", False),
            ("ageRange", "ageRange", range.Range, False, "age", False),
            ("gender", "gender", codeableconcept.CodeableConcept, False, None, False),
            ("physiologicalCondition", "physiologicalCondition", codeableconcept.CodeableConcept, False, None, False),
            ("race", "race", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirreference
from . import quantity
from . import range
