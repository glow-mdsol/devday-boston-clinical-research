#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 (http://hl7.org/fhir/StructureDefinition/OrganizationRole) on 2018-05-12.
#  2018, SMART Health IT.


from . import domainresource

class OrganizationRole(domainresource.DomainResource):
    """ Roles/organizations the practitioner is associated with.
    
    A specific set of Roles/Locations/specialties/services that a practitioner
    may perform at an organization for a period of time.
    """
    
    resource_type = "OrganizationRole"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        """ Whether this practitioner role record is in active use.
        Type `bool`. """
        
        self.availabilityExceptions = None
        """ Description of availability exceptions.
        Type `str`. """
        
        self.availableTime = None
        """ Times the Service Site is available.
        List of `OrganizationRoleAvailableTime` items (represented as `dict` in JSON). """
        
        self.code = None
        """ Roles which this practitioner may perform.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.endpoint = None
        """ Technical endpoints providing access to services operated for the
        practitioner with this role.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.healthcareService = None
        """ The list of healthcare services that this worker provides for this
        role's Organization/Location(s).
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business Identifiers that are specific to a role/location.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        """ The location(s) at which this practitioner provides care.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.network = None
        """ The network(s) this association applies to.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.notAvailable = None
        """ Not available during this time due to provided reason.
        List of `OrganizationRoleNotAvailable` items (represented as `dict` in JSON). """
        
        self.organization = None
        """ Organization where the roles are available.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.participatingOrganization = None
        """ Practitioner that is able to provide the defined services for the
        organization.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ The period during which the practitioner is authorized to perform
        in these role(s).
        Type `Period` (represented as `dict` in JSON). """
        
        self.specialty = None
        """ Specific specialty of the practitioner.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.telecom = None
        """ Contact details that are specific to the role/location/service.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(OrganizationRole, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OrganizationRole, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("availabilityExceptions", "availabilityExceptions", str, False, None, False),
            ("availableTime", "availableTime", OrganizationRoleAvailableTime, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("healthcareService", "healthcareService", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("location", "location", fhirreference.FHIRReference, True, None, False),
            ("network", "network", fhirreference.FHIRReference, True, None, False),
            ("notAvailable", "notAvailable", OrganizationRoleNotAvailable, True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("participatingOrganization", "participatingOrganization", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


from . import backboneelement

class OrganizationRoleAvailableTime(backboneelement.BackboneElement):
    """ Times the Service Site is available.
    
    A collection of times that the Service Site is available.
    """
    
    resource_type = "OrganizationRoleAvailableTime"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allDay = None
        """ Always available? e.g. 24-hour service.
        Type `bool`. """
        
        self.availableEndTime = None
        """ Closing time of day (ignored if allDay = true).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.availableStartTime = None
        """ Opening time of day (ignored if allDay = true).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.daysOfWeek = None
        """ mon | tue | wed | thu | fri | sat | sun.
        List of `str` items. """
        
        super(OrganizationRoleAvailableTime, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OrganizationRoleAvailableTime, self).elementProperties()
        js.extend([
            ("allDay", "allDay", bool, False, None, False),
            ("availableEndTime", "availableEndTime", fhirdate.FHIRDate, False, None, False),
            ("availableStartTime", "availableStartTime", fhirdate.FHIRDate, False, None, False),
            ("daysOfWeek", "daysOfWeek", str, True, None, False),
        ])
        return js


class OrganizationRoleNotAvailable(backboneelement.BackboneElement):
    """ Not available during this time due to provided reason.
    
    The HealthcareService is not available during this period of time due to
    the provided reason.
    """
    
    resource_type = "OrganizationRoleNotAvailable"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Reason presented to the user explaining why time not available.
        Type `str`. """
        
        self.during = None
        """ Service not available from this date.
        Type `Period` (represented as `dict` in JSON). """
        
        super(OrganizationRoleNotAvailable, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OrganizationRoleNotAvailable, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("during", "during", period.Period, False, None, False),
        ])
        return js


from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
