#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 (http://hl7.org/fhir/StructureDefinition/ProductPlan) on 2018-05-12.
#  2018, SMART Health IT.


from . import domainresource

class ProductPlan(domainresource.DomainResource):
    """ Details of a Health Insurance product/plan provided by an organization.
    """
    
    resource_type = "ProductPlan"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None
        """ An address for the organization.
        List of `Address` items (represented as `dict` in JSON). """
        
        self.administeredBy = None
        """ Administrator of the product/plan.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.alias = None
        """ A list of alternate names that the product/plan is known as, or was
        known as in the past.
        List of `str` items. """
        
        self.contact = None
        """ Contact for the product/plan for a certain purpose.
        List of `ProductPlanContact` items (represented as `dict` in JSON). """
        
        self.coverage = None
        """ Details about the coverage offered by the insurance product.
        List of `ProductPlanCoverage` items (represented as `dict` in JSON). """
        
        self.coverageArea = None
        """ The geographic region in which this product/plan is available.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.endpoint = None
        """ Technical endpoints providing access to services operated for the
        organization.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifies this product/plan  across multiple systems.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Official name.
        Type `str`. """
        
        self.ownedBy = None
        """ Owner of the product/plan.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ The time period the product/plan is available.
        Type `Period` (represented as `dict` in JSON). """
        
        self.plan = None
        """ Details about an insurance plan.
        List of `ProductPlanPlan` items (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.type = None
        """ Kind of product/plan.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ProductPlan, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProductPlan, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, True, None, False),
            ("administeredBy", "administeredBy", fhirreference.FHIRReference, False, None, False),
            ("alias", "alias", str, True, None, False),
            ("contact", "contact", ProductPlanContact, True, None, False),
            ("coverage", "coverage", ProductPlanCoverage, True, None, False),
            ("coverageArea", "coverageArea", fhirreference.FHIRReference, False, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("name", "name", str, False, None, False),
            ("ownedBy", "ownedBy", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("plan", "plan", ProductPlanPlan, True, None, False),
            ("status", "status", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


from . import backboneelement

class ProductPlanContact(backboneelement.BackboneElement):
    """ Contact for the product/plan for a certain purpose.
    """
    
    resource_type = "ProductPlanContact"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None
        """ Visiting or postal addresses for the contact.
        Type `Address` (represented as `dict` in JSON). """
        
        self.name = None
        """ A name associated with the contact.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.purpose = None
        """ The type of contact.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.telecom = None
        """ Contact details (telephone, email, etc.)  for a contact.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(ProductPlanContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProductPlanContact, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, False, None, False),
            ("name", "name", humanname.HumanName, False, None, False),
            ("purpose", "purpose", codeableconcept.CodeableConcept, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


class ProductPlanCoverage(backboneelement.BackboneElement):
    """ Details about the coverage offered by the insurance product.
    """
    
    resource_type = "ProductPlanCoverage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.benefit = None
        """ Specific benefits under this type of coverage.
        List of `ProductPlanCoverageBenefit` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of coverage.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ProductPlanCoverage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProductPlanCoverage, self).elementProperties()
        js.extend([
            ("benefit", "benefit", ProductPlanCoverageBenefit, True, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ProductPlanCoverageBenefit(backboneelement.BackboneElement):
    """ Specific benefits under this type of coverage.
    """
    
    resource_type = "ProductPlanCoverageBenefit"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.item = None
        """ Specific benefit and related value.
        List of `ProductPlanCoverageBenefitItem` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of benefit.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ProductPlanCoverageBenefit, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProductPlanCoverageBenefit, self).elementProperties()
        js.extend([
            ("item", "item", ProductPlanCoverageBenefitItem, True, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ProductPlanCoverageBenefitItem(backboneelement.BackboneElement):
    """ Specific benefit and related value.
    """
    
    resource_type = "ProductPlanCoverageBenefitItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.benefitValue = None
        """ Value of the specific benefit.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.code = None
        """ Coded Details of the specific benefit (days; visits).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ProductPlanCoverageBenefitItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProductPlanCoverageBenefitItem, self).elementProperties()
        js.extend([
            ("benefitValue", "benefitValue", quantity.Quantity, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ProductPlanPlan(backboneelement.BackboneElement):
    """ Details about an insurance plan.
    """
    
    resource_type = "ProductPlanPlan"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ List of the costs associated with plan benefits.
        List of `ProductPlanPlanCategory` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Additional descriptive content about the plan.
        Type `str`. """
        
        self.premium = None
        """ Plan premium.
        Type `Money` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of plan.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ProductPlanPlan, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProductPlanPlan, self).elementProperties()
        js.extend([
            ("category", "category", ProductPlanPlanCategory, True, None, False),
            ("description", "description", str, False, None, False),
            ("premium", "premium", money.Money, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ProductPlanPlanCategory(backboneelement.BackboneElement):
    """ List of the costs associated with plan benefits.
    """
    
    resource_type = "ProductPlanPlanCategory"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.benefit = None
        """ List of the specific benefits under this category of benefit.
        List of `ProductPlanPlanCategoryBenefit` items (represented as `dict` in JSON). """
        
        self.code = None
        """ General category of benefit (Medical; Dental; Vision; Drug; Mental
        Health; Substance Abuse; Hospice, Home Health).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ProductPlanPlanCategory, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProductPlanPlanCategory, self).elementProperties()
        js.extend([
            ("benefit", "benefit", ProductPlanPlanCategoryBenefit, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ProductPlanPlanCategoryBenefit(backboneelement.BackboneElement):
    """ List of the specific benefits under this category of benefit.
    """
    
    resource_type = "ProductPlanPlanCategoryBenefit"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.cost = None
        """ List of the costs associated with a specific benefit.
        List of `ProductPlanPlanCategoryBenefitCost` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of specific benefit (preventative; primary care office visit;
        speciality office visit; hospitalization; emergency room; urgent
        care).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ProductPlanPlanCategoryBenefit, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProductPlanPlanCategoryBenefit, self).elementProperties()
        js.extend([
            ("cost", "cost", ProductPlanPlanCategoryBenefitCost, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ProductPlanPlanCategoryBenefitCost(backboneelement.BackboneElement):
    """ List of the costs associated with a specific benefit.
    """
    
    resource_type = "ProductPlanPlanCategoryBenefitCost"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.applicability = None
        """ Whether the cost applies to in-network or out-of-network providers
        (in-network; out-of-network; other).
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.qualifiers = None
        """ Additional information about the cost, such as information about
        funding sources (e.g. HSA, HRA, FSA, RRA).
        List of `str` items. """
        
        self.type = None
        """ Type of cost (copay; individual cap; family cap; coinsurance;
        deductible).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
        """ The actual cost value.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(ProductPlanPlanCategoryBenefitCost, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProductPlanPlanCategoryBenefitCost, self).elementProperties()
        js.extend([
            ("applicability", "applicability", coding.Coding, True, None, False),
            ("qualifiers", "qualifiers", str, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("value", "value", quantity.Quantity, False, None, False),
        ])
        return js


from . import address
from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirreference
from . import humanname
from . import identifier
from . import money
from . import period
from . import quantity
