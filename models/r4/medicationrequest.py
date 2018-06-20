#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 (http://hl7.org/fhir/StructureDefinition/MedicationRequest) on 2018-05-12.
#  2018, SMART Health IT.


from . import domainresource

class MedicationRequest(domainresource.DomainResource):
    """ Ordering of medication for patient or group.
    
    An order or request for both supply of the medication and the instructions
    for administration of the medication to a patient. The resource is called
    "MedicationRequest" rather than "MedicationPrescription" or
    "MedicationOrder" to generalize the use across inpatient and outpatient
    settings, including care plans, etc., and to harmonize with workflow
    patterns.
    """
    
    resource_type = "MedicationRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authoredOn = None
        """ When request was initially authored.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.basedOn = None
        """ What request fulfills.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.category = None
        """ Type of medication usage.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.context = None
        """ Created during encounter/admission/stay.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.detectedIssue = None
        """ Clinical Issue with action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.dispenseRequest = None
        """ Medication supply authorization.
        Type `MedicationRequestDispenseRequest` (represented as `dict` in JSON). """
        
        self.dosageInstruction = None
        """ How the medication should be taken.
        List of `Dosage` items (represented as `dict` in JSON). """
        
        self.eventHistory = None
        """ A list of events of interest in the lifecycle.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.groupIdentifier = None
        """ Composite request this is part of.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External ids for this request.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiates = None
        """ Instantiates protocol or definition.
        List of `str` items. """
        
        self.insurance = None
        """ Associated insurance coverage.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.intent = None
        """ proposal | plan | order | original-order | instance-order | option.
        Type `str`. """
        
        self.medicationCodeableConcept = None
        """ Medication to be taken.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationReference = None
        """ Medication to be taken.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.note = None
        """ Information about the prescription.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.performer = None
        """ Intended performer of administration.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performerType = None
        """ Desired kind of performer of the medication administration.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.priorPrescription = None
        """ An order/prescription that is being replaced.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """
        
        self.reasonCode = None
        """ Reason or indication for writing the prescription.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Condition or observation that supports why the prescription is
        being written.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.recorder = None
        """ Person who entered the request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requester = None
        """ Who/What requested the Request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | on-hold | cancelled | completed | entered-in-error |
        stopped | draft | unknown.
        Type `str`. """
        
        self.statusReason = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who or group medication request is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.substitution = None
        """ Any restrictions on medication substitution.
        Type `MedicationRequestSubstitution` (represented as `dict` in JSON). """
        
        self.supportingInformation = None
        """ Information to support ordering of the medication.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(MedicationRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationRequest, self).elementProperties()
        js.extend([
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("detectedIssue", "detectedIssue", fhirreference.FHIRReference, True, None, False),
            ("dispenseRequest", "dispenseRequest", MedicationRequestDispenseRequest, False, None, False),
            ("dosageInstruction", "dosageInstruction", dosage.Dosage, True, None, False),
            ("eventHistory", "eventHistory", fhirreference.FHIRReference, True, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiates", "instantiates", str, True, None, False),
            ("insurance", "insurance", fhirreference.FHIRReference, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, False, None, False),
            ("priorPrescription", "priorPrescription", fhirreference.FHIRReference, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("substitution", "substitution", MedicationRequestSubstitution, False, None, False),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import backboneelement

class MedicationRequestDispenseRequest(backboneelement.BackboneElement):
    """ Medication supply authorization.
    
    Indicates the specific details for the dispense or medication supply part
    of a medication request (also known as a Medication Prescription or
    Medication Order).  Note that this information is not always sent with the
    order.  There may be in some settings (e.g. hospitals) institutional or
    system support for completing the dispense details in the pharmacy
    department.
    """
    
    resource_type = "MedicationRequestDispenseRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expectedSupplyDuration = None
        """ Number of days supply per dispense.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.numberOfRepeatsAllowed = None
        """ Number of refills authorized.
        Type `int`. """
        
        self.performer = None
        """ Intended dispenser.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Amount of medication to supply per dispense.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.validityPeriod = None
        """ Time period supply is authorized for.
        Type `Period` (represented as `dict` in JSON). """
        
        super(MedicationRequestDispenseRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationRequestDispenseRequest, self).elementProperties()
        js.extend([
            ("expectedSupplyDuration", "expectedSupplyDuration", duration.Duration, False, None, False),
            ("numberOfRepeatsAllowed", "numberOfRepeatsAllowed", int, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("validityPeriod", "validityPeriod", period.Period, False, None, False),
        ])
        return js


class MedicationRequestSubstitution(backboneelement.BackboneElement):
    """ Any restrictions on medication substitution.
    
    Indicates whether or not substitution can or should be part of the
    dispense. In some cases substitution must happen, in other cases
    substitution must not happen. This block explains the prescriber's intent.
    If nothing is specified substitution may be done.
    """
    
    resource_type = "MedicationRequestSubstitution"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allowed = None
        """ Whether substitution is allowed or not.
        Type `bool`. """
        
        self.reason = None
        """ Why should (not) substitution be made.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationRequestSubstitution, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationRequestSubstitution, self).elementProperties()
        js.extend([
            ("allowed", "allowed", bool, False, None, True),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import dosage
from . import duration
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
