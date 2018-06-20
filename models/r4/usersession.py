#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 (http://hl7.org/fhir/StructureDefinition/UserSession) on 2018-05-12.
#  2018, SMART Health IT.


from . import domainresource

class UserSession(domainresource.DomainResource):
    """ Information about a user's current session.
    """
    
    resource_type = "UserSession"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.context = None
        """ Additional information about the session.
        List of `UserSessionContext` items (represented as `dict` in JSON). """
        
        self.created = None
        """ When was the session created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.expires = None
        """ When does the session expire.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.focus = None
        """ What is the user's current focus.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.status = None
        """ Status of the session.
        Type `UserSessionStatus` (represented as `dict` in JSON). """
        
        self.user = None
        """ User engaged in the session.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.workstation = None
        """ Where is the session.
        Type `Identifier` (represented as `dict` in JSON). """
        
        super(UserSession, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(UserSession, self).elementProperties()
        js.extend([
            ("context", "context", UserSessionContext, True, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("expires", "expires", fhirdate.FHIRDate, False, None, False),
            ("focus", "focus", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("status", "status", UserSessionStatus, False, None, False),
            ("user", "user", fhirreference.FHIRReference, False, None, True),
            ("workstation", "workstation", identifier.Identifier, False, None, False),
        ])
        return js


from . import backboneelement

class UserSessionContext(backboneelement.BackboneElement):
    """ Additional information about the session.
    
    Provides additional information associated with the context.
    """
    
    resource_type = "UserSessionContext"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ What type of context value.
        Type `str`. """
        
        self.valueCodeableConcept = None
        """ Value of the context.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Value of the context.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(UserSessionContext, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(UserSessionContext, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
        ])
        return js


class UserSessionStatus(backboneelement.BackboneElement):
    """ Status of the session.
    """
    
    resource_type = "UserSessionStatus"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ activating | active | suspended | closing | closed.
        Type `str`. """
        
        self.source = None
        """ user | system.
        Type `str`. """
        
        super(UserSessionStatus, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(UserSessionStatus, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("source", "source", str, False, None, True),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
