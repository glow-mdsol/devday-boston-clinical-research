#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 (http://hl7.org/fhir/StructureDefinition/Signature) on 2018-05-12.
#  2018, SMART Health IT.


from . import element

class Signature(element.Element):
    """ A Signature - XML DigSig, JWS, Graphical image of signature, etc..
    
    A signature along with supporting context. The signature may be a digital
    signature that is cryptographic in nature, or some other signature
    acceptable to the domain. This other signature may be as simple as a
    graphical image representing a hand-written signature, or a signature
    ceremony Different signature approaches have different utilities.
    """
    
    resource_type = "Signature"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.blob = None
        """ The actual signature content (XML DigSig. JWS, picture, etc.).
        Type `str`. """
        
        self.onBehalfOfReference = None
        """ The party represented.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.onBehalfOfUri = None
        """ The party represented.
        Type `str`. """
        
        self.sigFormat = None
        """ The technical format of the signature.
        Type `str`. """
        
        self.targetFormat = None
        """ The technical format of the signed resources.
        Type `str`. """
        
        self.type = None
        """ Indication of the reason the entity signed the object(s).
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.when = None
        """ When the signature was created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.whoReference = None
        """ Who signed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.whoUri = None
        """ Who signed.
        Type `str`. """
        
        super(Signature, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Signature, self).elementProperties()
        js.extend([
            ("blob", "blob", str, False, None, False),
            ("onBehalfOfReference", "onBehalfOfReference", fhirreference.FHIRReference, False, "onBehalfOf", False),
            ("onBehalfOfUri", "onBehalfOfUri", str, False, "onBehalfOf", False),
            ("sigFormat", "sigFormat", str, False, None, False),
            ("targetFormat", "targetFormat", str, False, None, False),
            ("type", "type", coding.Coding, True, None, True),
            ("when", "when", fhirdate.FHIRDate, False, None, True),
            ("whoReference", "whoReference", fhirreference.FHIRReference, False, "who", True),
            ("whoUri", "whoUri", str, False, "who", True),
        ])
        return js


from . import coding
from . import fhirdate
from . import fhirreference
