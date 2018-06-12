#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 (http://hl7.org/fhir/StructureDefinition/Measure) on 2018-05-12.
#  2018, SMART Health IT.


from . import domainresource

class Measure(domainresource.DomainResource):
    """ A quality measure definition.
    
    The Measure resource provides the definition of a quality measure.
    """
    
    resource_type = "Measure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.approvalDate = None
        """ When the measure was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.clinicalRecommendationStatement = None
        """ Summary of clinical guidelines.
        Type `str`. """
        
        self.compositeScoring = None
        """ opportunity | all-or-nothing | linear | weighted.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.contributor = None
        """ A content contributor.
        List of `Contributor` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.definition = None
        """ Defined terms used in the measure documentation.
        List of `str` items. """
        
        self.description = None
        """ Natural language description of the measure.
        Type `str`. """
        
        self.disclaimer = None
        """ Disclaimer for use of the measure or its referenced content.
        Type `str`. """
        
        self.effectivePeriod = None
        """ When the measure is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.group = None
        """ Population criteria group.
        List of `MeasureGroup` items (represented as `dict` in JSON). """
        
        self.guidance = None
        """ Additional guidance for implementers.
        Type `str`. """
        
        self.identifier = None
        """ Additional identifier for the measure.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.improvementNotation = None
        """ Improvement notation for the measure, e.g. higher score indicates
        better quality.
        Type `str`. """
        
        self.jurisdiction = None
        """ Intended jurisdiction for measure (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.lastReviewDate = None
        """ When the measure was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.library = None
        """ Logic used by the measure.
        List of `str` items. """
        
        self.name = None
        """ Name for this measure (computer friendly).
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.purpose = None
        """ Why this measure is defined.
        Type `str`. """
        
        self.rateAggregation = None
        """ How is rate aggregation performed for this measure.
        Type `str`. """
        
        self.rationale = None
        """ Why does this measure exist.
        Type `str`. """
        
        self.relatedArtifact = None
        """ Additional documentation, citations, etc..
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.riskAdjustment = None
        """ How risk adjustment is applied for this measure.
        Type `str`. """
        
        self.scoring = None
        """ proportion | ratio | continuous-variable | cohort.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.set = None
        """ The measure set, e.g. Preventive Care and Screening.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.subjectCodeableConcept = None
        """ E.g. Patient, Practitioner, RelatedPerson, Organization, Location,
        Device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subjectReference = None
        """ E.g. Patient, Practitioner, RelatedPerson, Organization, Location,
        Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.subtitle = None
        """ Subordinate title of the measure.
        Type `str`. """
        
        self.supplementalData = None
        """ What other data should be reported with the measure.
        List of `MeasureSupplementalData` items (represented as `dict` in JSON). """
        
        self.title = None
        """ Name for this measure (human friendly).
        Type `str`. """
        
        self.topic = None
        """ The category of the measure, such as Education, Treatment,
        Assessment, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        """ process | outcome | structure | patient-reported-outcome |
        composite.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.url = None
        """ Canonical identifier for this measure, represented as a URI
        (globally unique).
        Type `str`. """
        
        self.usage = None
        """ Describes the clinical usage of the measure.
        Type `str`. """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the measure.
        Type `str`. """
        
        super(Measure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Measure, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("clinicalRecommendationStatement", "clinicalRecommendationStatement", str, False, None, False),
            ("compositeScoring", "compositeScoring", codeableconcept.CodeableConcept, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("contributor", "contributor", contributor.Contributor, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("definition", "definition", str, True, None, False),
            ("description", "description", str, False, None, False),
            ("disclaimer", "disclaimer", str, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("group", "group", MeasureGroup, True, None, False),
            ("guidance", "guidance", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("improvementNotation", "improvementNotation", str, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("library", "library", str, True, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("rateAggregation", "rateAggregation", str, False, None, False),
            ("rationale", "rationale", str, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("riskAdjustment", "riskAdjustment", str, False, None, False),
            ("scoring", "scoring", codeableconcept.CodeableConcept, False, None, False),
            ("set", "set", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("subtitle", "subtitle", str, False, None, False),
            ("supplementalData", "supplementalData", MeasureSupplementalData, True, None, False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class MeasureGroup(backboneelement.BackboneElement):
    """ Population criteria group.
    
    A group of population criteria for the measure.
    """
    
    resource_type = "MeasureGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Meaning of the group.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        """ Summary description.
        Type `str`. """
        
        self.population = None
        """ Population criteria.
        List of `MeasureGroupPopulation` items (represented as `dict` in JSON). """
        
        self.stratifier = None
        """ Stratifier criteria for the measure.
        List of `MeasureGroupStratifier` items (represented as `dict` in JSON). """
        
        super(MeasureGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureGroup, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("population", "population", MeasureGroupPopulation, True, None, False),
            ("stratifier", "stratifier", MeasureGroupStratifier, True, None, False),
        ])
        return js


class MeasureGroupPopulation(backboneelement.BackboneElement):
    """ Population criteria.
    
    A population criteria for the measure.
    """
    
    resource_type = "MeasureGroupPopulation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ initial-population | numerator | numerator-exclusion | denominator
        | denominator-exclusion | denominator-exception | measure-
        population | measure-population-exclusion | measure-observation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.criteria = None
        """ The name of a valid referenced CQL expression (may be namespaced)
        that defines this population criteria.
        Type `str`. """
        
        self.description = None
        """ The human readable description of this population criteria.
        Type `str`. """
        
        super(MeasureGroupPopulation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureGroupPopulation, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("criteria", "criteria", str, False, None, True),
            ("description", "description", str, False, None, False),
        ])
        return js


class MeasureGroupStratifier(backboneelement.BackboneElement):
    """ Stratifier criteria for the measure.
    
    The stratifier criteria for the measure report, specified as either the
    name of a valid CQL expression defined within a referenced library or a
    valid FHIR Resource Path.
    """
    
    resource_type = "MeasureGroupStratifier"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Meaning of the stratifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.criteria = None
        """ How the measure should be stratified.
        Type `str`. """
        
        self.description = None
        """ The human readable description of this stratifier.
        Type `str`. """
        
        self.path = None
        """ Path to the stratifier.
        Type `str`. """
        
        super(MeasureGroupStratifier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureGroupStratifier, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("criteria", "criteria", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("path", "path", str, False, None, False),
        ])
        return js


class MeasureSupplementalData(backboneelement.BackboneElement):
    """ What other data should be reported with the measure.
    
    The supplemental data criteria for the measure report, specified as either
    the name of a valid CQL expression within a referenced library, or a valid
    FHIR Resource Path.
    """
    
    resource_type = "MeasureSupplementalData"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Meaning of the supplemental data.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.criteria = None
        """ Expression describing additional data to be reported.
        Type `str`. """
        
        self.description = None
        """ The human readable description of this supplemental data.
        Type `str`. """
        
        self.path = None
        """ Path to the supplemental data element.
        Type `str`. """
        
        self.usage = None
        """ supplemental-data | risk-adjustment-factor.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(MeasureSupplementalData, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureSupplementalData, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("criteria", "criteria", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("path", "path", str, False, None, False),
            ("usage", "usage", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


from . import codeableconcept
from . import contactdetail
from . import contributor
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import relatedartifact
from . import usagecontext
