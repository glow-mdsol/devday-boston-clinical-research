#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 (http://hl7.org/fhir/StructureDefinition/VerificationResult) on 2018-05-12.
#  2018, SMART Health IT.


from . import domainresource

class VerificationResult(domainresource.DomainResource):
    """ Describes validation requirements, source(s), status and dates for one or
    more elements.
    """
    
    resource_type = "VerificationResult"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.attestation = None
        """ Information about the entity attesting to information.
        Type `VerificationResultAttestation` (represented as `dict` in JSON). """
        
        self.failureAction = None
        """ fatal | warn | rec-only | none.
        Type `str`. """
        
        self.frequency = None
        """ Frequency of revalidation.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.lastPerformed = None
        """ The date/time validation was last completed (incl. failed
        validations).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.need = None
        """ none | initial | periodic.
        Type `str`. """
        
        self.nextScheduled = None
        """ The date when target is next validated, if appropriate.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.primarySource = None
        """ Information about the primary source(s) involved in validation.
        List of `VerificationResultPrimarySource` items (represented as `dict` in JSON). """
        
        self.status = None
        """ attested | validated | in-process | req-revalid | val-fail | reval-
        fail.
        Type `str`. """
        
        self.statusDate = None
        """ When the validation status was updated.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.target = None
        """ A resource that was validated.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.targetLocation = None
        """ The fhirpath location(s) within the resource that was validated.
        List of `str` items. """
        
        self.validationProcess = None
        """ The primary process by which the target is validated (edit check;
        value set; primary source; multiple sources; standalone; in
        context).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.validationType = None
        """ nothing | primary | multiple.
        Type `str`. """
        
        self.validator = None
        """ Information about the entity validating information.
        List of `VerificationResultValidator` items (represented as `dict` in JSON). """
        
        super(VerificationResult, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(VerificationResult, self).elementProperties()
        js.extend([
            ("attestation", "attestation", VerificationResultAttestation, False, None, False),
            ("failureAction", "failureAction", str, False, None, True),
            ("frequency", "frequency", timing.Timing, False, None, False),
            ("lastPerformed", "lastPerformed", fhirdate.FHIRDate, False, None, False),
            ("need", "need", str, False, None, True),
            ("nextScheduled", "nextScheduled", fhirdate.FHIRDate, False, None, False),
            ("primarySource", "primarySource", VerificationResultPrimarySource, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusDate", "statusDate", fhirdate.FHIRDate, False, None, True),
            ("target", "target", fhirreference.FHIRReference, True, None, False),
            ("targetLocation", "targetLocation", str, True, None, False),
            ("validationProcess", "validationProcess", codeableconcept.CodeableConcept, True, None, True),
            ("validationType", "validationType", str, False, None, True),
            ("validator", "validator", VerificationResultValidator, True, None, False),
        ])
        return js


from . import backboneelement

class VerificationResultAttestation(backboneelement.BackboneElement):
    """ Information about the entity attesting to information.
    """
    
    resource_type = "VerificationResultAttestation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ The date the information was attested to.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.method = None
        """ Who is providing the attested information (owner; authorized
        representative; authorized intermediary; non-authorized source).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.organization = None
        """ The organization attesting to information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.proxyIdentityCertificate = None
        """ A digital identity certificate associated with the proxy entity
        submitting attested information on behalf of the attestation source.
        Type `str`. """
        
        self.source = None
        """ The individual attesting to information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.sourceIdentityCertificate = None
        """ A digital identity certificate associated with the attestation
        source.
        Type `str`. """
        
        super(VerificationResultAttestation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(VerificationResultAttestation, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("method", "method", codeableconcept.CodeableConcept, False, None, True),
            ("organization", "organization", fhirreference.FHIRReference, False, None, True),
            ("proxyIdentityCertificate", "proxyIdentityCertificate", str, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, True),
            ("sourceIdentityCertificate", "sourceIdentityCertificate", str, False, None, False),
        ])
        return js


class VerificationResultPrimarySource(backboneelement.BackboneElement):
    """ Information about the primary source(s) involved in validation.
    """
    
    resource_type = "VerificationResultPrimarySource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.canPushUpdates = None
        """ yes | no | undetermined.
        Type `str`. """
        
        self.identifier = None
        """ URI of the primary source for validation.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.organization = None
        """ Reference to the primary source.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.pushTypeAvailable = None
        """ specific | any | source.
        List of `str` items. """
        
        self.type = None
        """ Type of primary source (License Board; Primary Education;
        Continuing Education; Postal Service; Relationship owner;
        Registration Authority; legal source; issuing source; authoritative
        source).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.validationDate = None
        """ When the target was validated against the primary source.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.validationProcess = None
        """ Method for communicating with the primary source (manual; API;
        Push).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.validationStatus = None
        """ successful | failed | unknown.
        Type `str`. """
        
        super(VerificationResultPrimarySource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(VerificationResultPrimarySource, self).elementProperties()
        js.extend([
            ("canPushUpdates", "canPushUpdates", str, False, None, True),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("pushTypeAvailable", "pushTypeAvailable", str, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, True),
            ("validationDate", "validationDate", fhirdate.FHIRDate, False, None, False),
            ("validationProcess", "validationProcess", codeableconcept.CodeableConcept, True, None, True),
            ("validationStatus", "validationStatus", str, False, None, False),
        ])
        return js


class VerificationResultValidator(backboneelement.BackboneElement):
    """ Information about the entity validating information.
    """
    
    resource_type = "VerificationResultValidator"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dateValidated = None
        """ Date on which the validator last validated the information.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ URI of the validator.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.identityCertificate = None
        """ A digital identity certificate associated with the validator.
        Type `str`. """
        
        self.organization = None
        """ Reference to the organization validating information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(VerificationResultValidator, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(VerificationResultValidator, self).elementProperties()
        js.extend([
            ("dateValidated", "dateValidated", fhirdate.FHIRDate, False, None, True),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("identityCertificate", "identityCertificate", str, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, True),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import timing
