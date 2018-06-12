#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 (http://hl7.org/fhir/StructureDefinition/Contract) on 2018-05-12.
#  2018, SMART Health IT.


from . import domainresource

class Contract(domainresource.DomainResource):
    """ Legal Agreement.
    
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """
    
    resource_type = "Contract"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.applies = None
        """ Effective time.
        Type `Period` (represented as `dict` in JSON). """
        
        self.authority = None
        """ Authority under which this Contract has standing.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.contentDerivative = None
        """ Content derived from the basal information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.domain = None
        """ A sphere of control governed by an authoritative jurisdiction,
        organization, or person.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.friendly = None
        """ Contract Friendly Language.
        List of `ContractFriendly` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Contract number.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.issued = None
        """ When this Contract was issued.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.legal = None
        """ Contract Legal Language.
        List of `ContractLegal` items (represented as `dict` in JSON). """
        
        self.legallyBindingAttachment = None
        """ Binding Contract.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.legallyBindingReference = None
        """ Binding Contract.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.rule = None
        """ Computable Contract Language.
        Type `ContractRule` (represented as `dict` in JSON). """
        
        self.signer = None
        """ Contract Signatory.
        List of `ContractSigner` items (represented as `dict` in JSON). """
        
        self.status = None
        """ amended | appended | cancelled | disputed | entered-in-error |
        executable | executed | negotiable | offered | policy | rejected |
        renewed | revoked | resolved | terminated.
        Type `str`. """
        
        self.subType = None
        """ Subtype within the context of type.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ Contract Target Entity.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.term = None
        """ Contract Term List.
        List of `ContractTerm` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type or form.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Contract, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Contract, self).elementProperties()
        js.extend([
            ("applies", "applies", period.Period, False, None, False),
            ("authority", "authority", fhirreference.FHIRReference, True, None, False),
            ("contentDerivative", "contentDerivative", codeableconcept.CodeableConcept, False, None, False),
            ("domain", "domain", fhirreference.FHIRReference, True, None, False),
            ("friendly", "friendly", ContractFriendly, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("legal", "legal", ContractLegal, True, None, False),
            ("legallyBindingAttachment", "legallyBindingAttachment", attachment.Attachment, False, "legallyBinding", False),
            ("legallyBindingReference", "legallyBindingReference", fhirreference.FHIRReference, False, "legallyBinding", False),
            ("rule", "rule", ContractRule, False, None, False),
            ("signer", "signer", ContractSigner, True, None, False),
            ("status", "status", str, False, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("term", "term", ContractTerm, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class ContractFriendly(backboneelement.BackboneElement):
    """ Contract Friendly Language.
    
    The "patient friendly language" versionof the Contract in whole or in
    parts. "Patient friendly language" means the representation of the Contract
    and Contract Provisions in a manner that is readily accessible and
    understandable by a layperson in accordance with best practices for
    communication styles that ensure that those agreeing to or signing the
    Contract understand the roles, actions, obligations, responsibilities, and
    implication of the agreement.
    """
    
    resource_type = "ContractFriendly"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentAttachment = None
        """ Easily comprehended representation of this Contract.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference = None
        """ Easily comprehended representation of this Contract.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ContractFriendly, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractFriendly, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
        ])
        return js


class ContractLegal(backboneelement.BackboneElement):
    """ Contract Legal Language.
    
    List of Legal expressions or representations of this Contract.
    """
    
    resource_type = "ContractLegal"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentAttachment = None
        """ Contract Legal Text.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference = None
        """ Contract Legal Text.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ContractLegal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractLegal, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
        ])
        return js


class ContractRule(backboneelement.BackboneElement):
    """ Computable Contract Language.
    
    List of Computable Policy Rule Language Representations of this Contract.
    """
    
    resource_type = "ContractRule"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentAttachment = None
        """ Computable Contract Rules.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference = None
        """ Computable Contract Rules.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ContractRule, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractRule, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
        ])
        return js


class ContractSigner(backboneelement.BackboneElement):
    """ Contract Signatory.
    
    Parties with legal standing in the Contract, including the principal
    parties, the grantor(s) and grantee(s), which are any person or
    organization bound by the contract, and any ancillary parties, which
    facilitate the execution of the contract such as a notary or witness.
    """
    
    resource_type = "ContractSigner"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.party = None
        """ Contract Signatory Party.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.signature = None
        """ Contract Documentation Signature.
        List of `Signature` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Contract Signatory Role.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ContractSigner, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractSigner, self).elementProperties()
        js.extend([
            ("party", "party", fhirreference.FHIRReference, False, None, True),
            ("signature", "signature", signature.Signature, True, None, True),
            ("type", "type", coding.Coding, False, None, True),
        ])
        return js


class ContractTerm(backboneelement.BackboneElement):
    """ Contract Term List.
    
    One or more Contract Provisions, which may be related and conveyed as a
    group, and may contain nested groups.
    """
    
    resource_type = "ContractTerm"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ Contract Term Activity.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.actionReason = None
        """ Purpose for the Contract Term Action.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.agent = None
        """ Entity being ascribed responsibility.
        List of `ContractTermAgent` items (represented as `dict` in JSON). """
        
        self.applies = None
        """ Contract Term Effective Time.
        Type `Period` (represented as `dict` in JSON). """
        
        self.asset = None
        """ Contract Term Asset List.
        List of `ContractTermAsset` items (represented as `dict` in JSON). """
        
        self.group = None
        """ Nested Contract Term Group.
        List of `ContractTerm` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Contract Term Number.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.issued = None
        """ Contract Term Issue Date Time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.offer = None
        """ Context of the Contract term.
        Type `ContractTermOffer` (represented as `dict` in JSON). """
        
        self.subType = None
        """ Contract Term Type specific classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ Contract Term Type or Form.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ContractTerm, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTerm, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, True, None, False),
            ("actionReason", "actionReason", codeableconcept.CodeableConcept, True, None, False),
            ("agent", "agent", ContractTermAgent, True, None, False),
            ("applies", "applies", period.Period, False, None, False),
            ("asset", "asset", ContractTermAsset, True, None, False),
            ("group", "group", ContractTerm, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("offer", "offer", ContractTermOffer, False, None, True),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ContractTermAgent(backboneelement.BackboneElement):
    """ Entity being ascribed responsibility.
    
    An actor taking a role in an activity for which it can be assigned some
    degree of responsibility for the activity taking place.
    """
    
    resource_type = "ContractTermAgent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ Contract Agent Type.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.role = None
        """ Role type of the agent.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ContractTermAgent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermAgent, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("role", "role", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class ContractTermAsset(backboneelement.BackboneElement):
    """ Contract Term Asset List.
    """
    
    resource_type = "ContractTermAsset"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.class_fhir = None
        """ Resource Type, Profile, or CDA etc..
        Type `Coding` (represented as `dict` in JSON). """
        
        self.code = None
        """ Code in the content.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.data = None
        """ Data defined by this Asset.
        List of `ContractTermAssetData` items (represented as `dict` in JSON). """
        
        self.dataPeriod = None
        """ Time period of the data for the asset.
        Type `Period` (represented as `dict` in JSON). """
        
        self.period = None
        """ Time period of the asset.
        Type `Period` (represented as `dict` in JSON). """
        
        self.securityLabel = None
        """ Security Labels that define affected terms.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.valuedItem = None
        """ Contract Valued Item List.
        List of `ContractTermAssetValuedItem` items (represented as `dict` in JSON). """
        
        super(ContractTermAsset, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermAsset, self).elementProperties()
        js.extend([
            ("class_fhir", "class", coding.Coding, False, None, False),
            ("code", "code", coding.Coding, False, None, False),
            ("data", "data", ContractTermAssetData, True, None, False),
            ("dataPeriod", "dataPeriod", period.Period, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("securityLabel", "securityLabel", coding.Coding, True, None, False),
            ("valuedItem", "valuedItem", ContractTermAssetValuedItem, True, None, False),
        ])
        return js


class ContractTermAssetData(backboneelement.BackboneElement):
    """ Data defined by this Asset.
    """
    
    resource_type = "ContractTermAssetData"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.meaning = None
        """ instance | related | dependents | authoredby.
        Type `str`. """
        
        self.reference = None
        """ The actual data reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ContractTermAssetData, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermAssetData, self).elementProperties()
        js.extend([
            ("meaning", "meaning", str, False, None, False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class ContractTermAssetValuedItem(backboneelement.BackboneElement):
    """ Contract Valued Item List.
    """
    
    resource_type = "ContractTermAssetValuedItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.effectiveTime = None
        """ Contract Valued Item Effective Tiem.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.entityCodeableConcept = None
        """ Contract Valued Item Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.entityReference = None
        """ Contract Valued Item Type.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.factor = None
        """ Contract Valued Item Price Scaling Factor.
        Type `float`. """
        
        self.identifier = None
        """ Contract Valued Item Number.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.net = None
        """ Total Contract Valued Item Value.
        Type `Money` (represented as `dict` in JSON). """
        
        self.points = None
        """ Contract Valued Item Difficulty Scaling Factor.
        Type `float`. """
        
        self.quantity = None
        """ Count of Contract Valued Items.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Contract Valued Item fee, charge, or cost.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ContractTermAssetValuedItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermAssetValuedItem, self).elementProperties()
        js.extend([
            ("effectiveTime", "effectiveTime", fhirdate.FHIRDate, False, None, False),
            ("entityCodeableConcept", "entityCodeableConcept", codeableconcept.CodeableConcept, False, "entity", False),
            ("entityReference", "entityReference", fhirreference.FHIRReference, False, "entity", False),
            ("factor", "factor", float, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("net", "net", money.Money, False, None, False),
            ("points", "points", float, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ContractTermOffer(backboneelement.BackboneElement):
    """ Context of the Contract term.
    
    The matter of concern in the context of this provision of the agrement.
    """
    
    resource_type = "ContractTermOffer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.decision = None
        """ Decision by Grantor.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.linkId = None
        """ Pointer to text.
        Type `str`. """
        
        self.text = None
        """ Human readable offer text.
        Type `str`. """
        
        self.topic = None
        """ Negotiable offer asset.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ Contract Offer Type or Form.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ContractTermOffer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermOffer, self).elementProperties()
        js.extend([
            ("decision", "decision", codeableconcept.CodeableConcept, False, None, False),
            ("linkId", "linkId", str, False, None, False),
            ("text", "text", str, False, None, False),
            ("topic", "topic", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity
from . import signature
