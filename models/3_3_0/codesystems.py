#
#  CodeSystems.py
#  client-py
#
#  Generated from FHIR 3.3.0 on 2018-05-12.
#  2018, SMART Health IT.
#
#

from enum import Enum


class CodeSystemValue(Enum):
    """
    Base CodeSystemValue class

    Inheriting from Enum allows us to do things like:
    >>> _type = SampleCodeSystemValue('type')
    """

    def as_json(self):
        return dict(display=self.value, system=self.url, code=self.name)

    @property
    def text(self):
        return self.value

    @property
    def url(self):
        return self.URL.value

    @property
    def experimental(self):
        return self.EXPERIMENTAL.value if hasattr(self, "EXPERIMENTAL") else False


class ACMECodesForCholesterolInSerumPlasma(CodeSystemValue):
    """ This is an example code system that includes all the ACME codes for serum/plasma cholesterol from v2.36.

    URL: http://hl7.org/fhir/CodeSystem/example
    """
    URL = "http://hl7.org/fhir/CodeSystem/example"
    EXPERIMENTAL = True

    """ Serum Cholesterol, in mmol/L
    """
    cholMmol = "chol-mmol"

    """ Serum Cholesterol, in mg/L
    """
    cholMass = "chol-mass"

    """ Serum Cholesterol
    """
    chol = "chol"


class AbstractType(CodeSystemValue):
    """ A list of the base types defined by this version of the FHIR specification - types that are defined, but for which only
specializations actually are created

    URL: http://hl7.org/fhir/abstract-types
    ValueSet: http://hl7.org/fhir/ValueSet/abstract-types
    """
    URL = "http://hl7.org/fhir/abstract-types"
    EXPERIMENTAL = False

    """ A place holder that means any kind of data type
    """
    type = "Type"

    """ A place holder that means any kind of resource
    """
    any = "Any"


class AccountStatus(CodeSystemValue):
    """ Indicates whether the account is available to be used.

    URL: http://hl7.org/fhir/account-status
    ValueSet: http://hl7.org/fhir/ValueSet/account-status
    """
    URL = "http://hl7.org/fhir/account-status"
    EXPERIMENTAL = False

    """ This account is active and may be used.
    """
    active = "active"

    """ This account is inactive and should not be used to track financial information.
    """
    inactive = "inactive"

    """ This instance should not have been part of this patient's medical record.
    """
    enteredInError = "entered-in-error"

    """ This account is on hold
    """
    onHold = "on-hold"

    """ The ccount status is unknown
    """
    unknown = "unknown"


class ActionCardinalityBehavior(CodeSystemValue):
    """ Defines behavior for an action or a group for how many times that item may be repeated

    URL: http://hl7.org/fhir/action-cardinality-behavior
    ValueSet: http://hl7.org/fhir/ValueSet/action-cardinality-behavior
    """
    URL = "http://hl7.org/fhir/action-cardinality-behavior"
    EXPERIMENTAL = False

    """ The action may only be selected one time
    """
    single = "single"

    """ The action may be selected multiple times
    """
    multiple = "multiple"


class ActionConditionKind(CodeSystemValue):
    """ Defines the kinds of conditions that can appear on actions

    URL: http://hl7.org/fhir/action-condition-kind
    ValueSet: http://hl7.org/fhir/ValueSet/action-condition-kind
    """
    URL = "http://hl7.org/fhir/action-condition-kind"
    EXPERIMENTAL = False

    """ The condition describes whether or not a given action is applicable
    """
    applicability = "applicability"

    """ The condition is a starting condition for the action
    """
    start = "start"

    """ The condition is a stop, or exit condition for the action
    """
    stop = "stop"


class ActionGroupingBehavior(CodeSystemValue):
    """ Defines organization behavior of a group

    URL: http://hl7.org/fhir/action-grouping-behavior
    ValueSet: http://hl7.org/fhir/ValueSet/action-grouping-behavior
    """
    URL = "http://hl7.org/fhir/action-grouping-behavior"
    EXPERIMENTAL = False

    """ Any group marked with this behavior should be displayed as a visual group to the end user
    """
    visualGroup = "visual-group"

    """ A group with this behavior logically groups its sub-elements, and may be shown as a visual group to the end
	/// user, but it is not required to do so
    """
    logicalGroup = "logical-group"

    """ A group of related alternative actions is a sentence group if the target referenced by the action is the same in
	/// all the actions and each action simply constitutes a different variation on how to specify the details for the
	/// target. For example, two actions that could be in a SentenceGroup are "aspirin, 500 mg, 2 times per day" and
	/// "aspirin, 300 mg, 3 times per day". In both cases, aspirin is the target referenced by the action, and the two
	/// actions represent different options for how aspirin might be ordered for the patient. Note that a SentenceGroup
	/// would almost always have an associated selection behavior of "AtMostOne", unless it's a required action, in
	/// which case, it would be "ExactlyOne"
    """
    sentenceGroup = "sentence-group"


class ActionList(CodeSystemValue):
    """ List of allowable action which this resource can request.

    URL: http://hl7.org/fhir/actionlist
    ValueSet: http://hl7.org/fhir/ValueSet/actionlist
    """
    URL = "http://hl7.org/fhir/actionlist"
    EXPERIMENTAL = False

    """ Cancel, reverse or nullify the target resource.
    """
    cancel = "cancel"

    """ Check for previously un-read/ not-retrieved resources.
    """
    poll = "poll"

    """ Re-process the target resource.
    """
    reprocess = "reprocess"

    """ Retrieve the processing status of the target resource.
    """
    status = "status"


class ActionParticipantType(CodeSystemValue):
    """ The type of participant for the action

    URL: http://hl7.org/fhir/action-participant-type
    ValueSet: http://hl7.org/fhir/ValueSet/action-participant-type
    """
    URL = "http://hl7.org/fhir/action-participant-type"
    EXPERIMENTAL = False

    """ The participant is the patient under evaluation
    """
    patient = "patient"

    """ The participant is a practitioner involved in the patient's care
    """
    practitioner = "practitioner"

    """ The participant is a person related to the patient
    """
    relatedPerson = "related-person"


class ActionPrecheckBehavior(CodeSystemValue):
    """ Defines selection frequency behavior for an action or group

    URL: http://hl7.org/fhir/action-precheck-behavior
    ValueSet: http://hl7.org/fhir/ValueSet/action-precheck-behavior
    """
    URL = "http://hl7.org/fhir/action-precheck-behavior"
    EXPERIMENTAL = False

    """ An action with this behavior is one of the most frequent action that is, or should be, included by an end user,
	/// for the particular context in which the action occurs. The system displaying the action to the end user should
	/// consider "pre-checking" such an action as a convenience for the user
    """
    yes = "yes"

    """ An action with this behavior is one of the less frequent actions included by the end user, for the particular
	/// context in which the action occurs. The system displaying the actions to the end user would typically not "pre-
	/// check" such an action
    """
    no = "no"


class ActionRelationshipType(CodeSystemValue):
    """ Defines the types of relationships between actions

    URL: http://hl7.org/fhir/action-relationship-type
    ValueSet: http://hl7.org/fhir/ValueSet/action-relationship-type
    """
    URL = "http://hl7.org/fhir/action-relationship-type"
    EXPERIMENTAL = False

    """ The action must be performed before the start of the related action
    """
    beforeStart = "before-start"

    """ The action must be performed before the related action
    """
    before = "before"

    """ The action must be performed before the end of the related action
    """
    beforeEnd = "before-end"

    """ The action must be performed concurrent with the start of the related action
    """
    concurrentWithStart = "concurrent-with-start"

    """ The action must be performed concurrent with the related action
    """
    concurrent = "concurrent"

    """ The action must be performed concurrent with the end of the related action
    """
    concurrentWithEnd = "concurrent-with-end"

    """ The action must be performed after the start of the related action
    """
    afterStart = "after-start"

    """ The action must be performed after the related action
    """
    after = "after"

    """ The action must be performed after the end of the related action
    """
    afterEnd = "after-end"


class ActionRequiredBehavior(CodeSystemValue):
    """ Defines requiredness behavior for selecting an action or an action group

    URL: http://hl7.org/fhir/action-required-behavior
    ValueSet: http://hl7.org/fhir/ValueSet/action-required-behavior
    """
    URL = "http://hl7.org/fhir/action-required-behavior"
    EXPERIMENTAL = False

    """ An action with this behavior must be included in the actions processed by the end user; the end user SHALL not
	/// choose not to include this action
    """
    must = "must"

    """ An action with this behavior may be included in the set of actions processed by the end user
    """
    could = "could"

    """ An action with this behavior must be included in the set of actions processed by the end user, unless the end
	/// user provides documentation as to why the action was not included
    """
    mustUnlessDocumented = "must-unless-documented"


class ActionSelectionBehavior(CodeSystemValue):
    """ Defines selection behavior of a group

    URL: http://hl7.org/fhir/action-selection-behavior
    ValueSet: http://hl7.org/fhir/ValueSet/action-selection-behavior
    """
    URL = "http://hl7.org/fhir/action-selection-behavior"
    EXPERIMENTAL = False

    """ Any number of the actions in the group may be chosen, from zero to all
    """
    any = "any"

    """ All the actions in the group must be selected as a single unit
    """
    all = "all"

    """ All the actions in the group are meant to be chosen as a single unit: either all must be selected by the end
	/// user, or none may be selected
    """
    allOrNone = "all-or-none"

    """ The end user must choose one and only one of the selectable actions in the group. The user SHALL not choose none
	/// of the actions in the group
    """
    exactlyOne = "exactly-one"

    """ The end user may choose zero or at most one of the actions in the group
    """
    atMostOne = "at-most-one"

    """ The end user must choose a minimum of one, and as many additional as desired
    """
    oneOrMore = "one-or-more"


class ActionType(CodeSystemValue):
    """ The type of action to be performed

    URL: http://hl7.org/fhir/action-type
    ValueSet: http://hl7.org/fhir/ValueSet/action-type
    """
    URL = "http://hl7.org/fhir/action-type"
    EXPERIMENTAL = False

    """ The action is to create a new resource
    """
    create = "create"

    """ The action is to update an existing resource
    """
    update = "update"

    """ The action is to remove an existing resource
    """
    remove = "remove"

    """ The action is to fire a specific event
    """
    fireEvent = "fire-event"


class ActivityDefinitionCategory(CodeSystemValue):
    """ High-level categorization of the type of activity

    URL: http://hl7.org/fhir/activity-definition-category
    ValueSet: http://hl7.org/fhir/ValueSet/activity-definition-category
    """
    URL = "http://hl7.org/fhir/activity-definition-category"
    EXPERIMENTAL = False

    """ The activity is intended to provide or is related to treatment of the patient
    """
    treatment = "treatment"

    """ The activity is intended to provide or is related to education of the patient
    """
    education = "education"

    """ The activity is intended to perform or is related to assessment of the patient
    """
    assessment = "assessment"


class AdditionalMaterialCodes(CodeSystemValue):
    """ This value set includes sample additional material type codes.

    URL: http://hl7.org/fhir/additionalmaterials
    ValueSet: http://hl7.org/fhir/ValueSet/additionalmaterials
    """
    URL = "http://hl7.org/fhir/additionalmaterials"
    EXPERIMENTAL = True

    """ XRay
    """
    xray = "xray"

    """ Image
    """
    image = "image"

    """ Email
    """
    email = "email"

    """ Model
    """
    model = "model"

    """ Document
    """
    document = "document"

    """ Other
    """
    other = "other"


class AddressType(CodeSystemValue):
    """ The type of an address (physical / postal)

    URL: http://hl7.org/fhir/address-type
    ValueSet: http://hl7.org/fhir/ValueSet/address-type
    """
    URL = "http://hl7.org/fhir/address-type"
    EXPERIMENTAL = False

    """ Mailing addresses - PO Boxes and care-of addresses.
    """
    postal = "postal"

    """ A physical address that can be visited.
    """
    physical = "physical"

    """ An address that is both physical and postal.
    """
    both = "both"


class AddressUse(CodeSystemValue):
    """ The use of an address

    URL: http://hl7.org/fhir/address-use
    ValueSet: http://hl7.org/fhir/ValueSet/address-use
    """
    URL = "http://hl7.org/fhir/address-use"
    EXPERIMENTAL = False

    """ A communication address at a home.
    """
    home = "home"

    """ An office address. First choice for business related contacts during business hours.
    """
    work = "work"

    """ A temporary address. The period can provide more detailed information.
    """
    temp = "temp"

    """ This address is no longer in use (or was never correct but retained for records).
    """
    old = "old"

    """ An address to be used to send bills, invoices, receipts etc.
    """
    billing = "billing"


class AdjudicationErrorCodes(CodeSystemValue):
    """ This value set includes a smattering of adjudication codes.

    URL: http://hl7.org/fhir/adjudication-error
    ValueSet: http://hl7.org/fhir/ValueSet/adjudication-error
    """
    URL = "http://hl7.org/fhir/adjudication-error"
    EXPERIMENTAL = True

    """ Missing Identifier
    """
    A001 = "a001"

    """ Missing Creation Date
    """
    A002 = "a002"


class AdjudicationReasonCodes(CodeSystemValue):
    """ This value set includes smattering of Adjudication Reason codes.

    URL: http://hl7.org/fhir/adjudication-reason
    ValueSet: http://hl7.org/fhir/ValueSet/adjudication-reason
    """
    URL = "http://hl7.org/fhir/adjudication-reason"
    EXPERIMENTAL = True

    """ Not covered
    """
    ar001 = "ar001"

    """ Plan Limit Reached
    """
    ar002 = "ar002"


class AdjudicationValueCodes(CodeSystemValue):
    """ This value set includes a smattering of Adjudication Value codes which includes codes to indicate the amounts eligible
under the plan, the amount of benefit, copays etc.

    URL: http://hl7.org/fhir/adjudication
    ValueSet: http://hl7.org/fhir/ValueSet/adjudication
    """
    URL = "http://hl7.org/fhir/adjudication"
    EXPERIMENTAL = True

    """ The total submitted amount for the claim or group or line item.
    """
    submitted = "submitted"

    """ Patient Co-Payment
    """
    copay = "copay"

    """ Amount of the change which is considered for adjudication.
    """
    eligible = "eligible"

    """ Amount deducted from the eligible amount prior to adjudication.
    """
    deductible = "deductible"

    """ The amount of deductable which could not allocated to other line items.
    """
    unallocdeduct = "unallocdeduct"

    """ Eligible Percentage.
    """
    eligpercent = "eligpercent"

    """ The amount of tax.
    """
    tax = "tax"

    """ Amount payable under the coverage
    """
    benefit = "benefit"


class AdministrativeGender(CodeSystemValue):
    """ The gender of a person used for administrative purposes.

    URL: http://hl7.org/fhir/administrative-gender
    ValueSet: http://hl7.org/fhir/ValueSet/administrative-gender
    """
    URL = "http://hl7.org/fhir/administrative-gender"
    EXPERIMENTAL = False

    """ Male
    """
    male = "male"

    """ Female
    """
    female = "female"

    """ Other
    """
    other = "other"

    """ Unknown
    """
    unknown = "unknown"


class AdmitSource(CodeSystemValue):
    """ This value set defines a set of codes that can be used to indicate from where the patient came in.

    URL: http://hl7.org/fhir/admit-source
    ValueSet: http://hl7.org/fhir/ValueSet/encounter-admit-source
    """
    URL = "http://hl7.org/fhir/admit-source"
    EXPERIMENTAL = True

    """ The Patient has been transferred from another hospital for this encounter.
    """
    hospTrans = "hosp-trans"

    """ The patient has been transferred from the emergency department within the hospital. This is typically used in
	/// the transition to an inpatient encounter
    """
    emd = "emd"

    """ The patient has been transferred from an outpatient department within the hospital.
    """
    outp = "outp"

    """ The patient is a newborn and the encounter will track the baby related activities (as opposed to the Mothers
	/// encounter - that may be associated using the newborn encounters partof property)
    """
    born = "born"

    """ The patient has been admitted due to a referred from a General Practitioner.
    """
    gp = "gp"

    """ The patient has been admitted due to a referred from a Specialist (as opposed to a General Practitioner).
    """
    mp = "mp"

    """ The patient has been transferred from a nursing home.
    """
    nursing = "nursing"

    """ The patient has been transferred from a psychiatric facility.
    """
    psych = "psych"

    """ The patient has been transferred from a rehabilitiation facility or clinic.
    """
    rehab = "rehab"

    """ The patient has been admitted from a source otherwise not specified here.
    """
    other = "other"


class AdverseEventActuality(CodeSystemValue):
    """ Overall nature of the event, e.g. real or potential

    URL: http://hl7.org/fhir/adverse-event-actuality
    ValueSet: http://hl7.org/fhir/ValueSet/adverse-event-actuality
    """
    URL = "http://hl7.org/fhir/adverse-event-actuality"
    EXPERIMENTAL = False

    """ actual
    """
    actual = "actual"

    """ potential
    """
    potential = "potential"


class AdverseEventCategory(CodeSystemValue):
    """ Overall categorization of the event, e.g. product related or situational

    URL: http://hl7.org/fhir/adverse-event-category
    ValueSet: http://hl7.org/fhir/ValueSet/adverse-event-category
    """
    URL = "http://hl7.org/fhir/adverse-event-category"
    EXPERIMENTAL = False

    """ productProblem
    """
    productProblem = "ProductProblem"

    """ productQuality
    """
    productQuality = "ProductQuality"

    """ productUseError
    """
    productUseError = "ProductUseError"

    """ wrongDose
    """
    wrongDose = "WrongDose"

    """ incorrectPrescribingInformation
    """
    incorrectPrescribingInformation = "IncorrectPrescribingInformation"

    """ wrongTechnique
    """
    wrongTechnique = "WrongTechnique"

    """ wrongRouteOfAdministration
    """
    wrongRouteOfAdministration = "WrongRouteOfAdministration"

    """ wrongRate
    """
    wrongRate = "WrongRate"

    """ wrongDuration
    """
    wrongDuration = "WrongDuration"

    """ wrongTime
    """
    wrongTime = "WrongTime"

    """ expiredDrug
    """
    expiredDrug = "ExpiredDrug"

    """ medicalDeviceUseError
    """
    medicalDeviceUseError = "MedicalDeviceUseError"

    """ problemDifferentManufacturer
    """
    problemDifferentManufacturer = "ProblemDifferentManufacturer"

    """ unsafePhysicalEnvironment
    """
    unsafePhysicalEnvironment = "UnsafePhysicalEnvironment"


class AdverseEventCausalityAssessment(CodeSystemValue):
    """ TODO

    URL: http://hl7.org/fhir/adverse-event-causality-assess
    ValueSet: http://hl7.org/fhir/ValueSet/adverse-event-causality-assess
    """
    URL = "http://hl7.org/fhir/adverse-event-causality-assess"
    EXPERIMENTAL = False

    """ i) Event or laboratory test abnormality, with plausible time relationship to drug intake ii) Cannot be explained
	/// by disease or other drugs iii) Response to withdrawal plausible (pharmacologically, pathologically) iv) Event
	/// definitive pharmacologically or phenomenologically (i.e. an objective and specific medical disorder or a
	/// recognized pharmacological phenomenon) v) Re-challenge satisfactory, if necessary
    """
    certain = "Certain"

    """ i) Event or laboratory test abnormality, with reasonable time relationship to drug intake ii) Unlikely to be
	/// attributed to disease or other drugs iii) Response to withdrawal clinically reasonable iv) Re-challenge not
	/// required
    """
    probablyLikely = "Probably-Likely"

    """ i) Event or laboratory test abnormality, with reasonable time relationship to drug intake ii) Could also be
	/// explained by disease or other drugs iii) Information on drug withdrawal may be lacking or unclear
    """
    possible = "Possible"

    """ i) Event or laboratory test abnormality, with a time to drug intake that makes a relationship improbable (but
	/// not impossible) ii) Disease or other drugs provide plausible explanations
    """
    unlikely = "Unlikely"

    """ i) Event or laboratory test abnormality ii) More data for proper assessment needed, or iii) Additional data
	/// under examination
    """
    conditionalClassified = "Conditional-Classified"

    """ i) Report suggesting an adverse reaction ii) Cannot be judged because information is insufficient or
	/// contradictory iii) Data cannot be supplemented or verified
    """
    unassessableUnclassifiable = "Unassessable-Unclassifiable"


class AdverseEventCausalityMethod(CodeSystemValue):
    """ TODO

    URL: http://hl7.org/fhir/adverse-event-causality-method
    ValueSet: http://hl7.org/fhir/ValueSet/adverse-event-causality-method
    """
    URL = "http://hl7.org/fhir/adverse-event-causality-method"
    EXPERIMENTAL = False

    """ probabilityScale
    """
    probabilityScale = "ProbabilityScale"

    """ bayesian
    """
    bayesian = "Bayesian"

    """ checklist
    """
    checklist = "Checklist"


class AdverseEventOutcome(CodeSystemValue):
    """ TODO (and should this be required?)

    URL: http://hl7.org/fhir/adverse-event-outcome
    ValueSet: http://hl7.org/fhir/ValueSet/adverse-event-outcome
    """
    URL = "http://hl7.org/fhir/adverse-event-outcome"
    EXPERIMENTAL = False

    """ resolved
    """
    resolved = "resolved"

    """ recovering
    """
    recovering = "recovering"

    """ ongoing
    """
    ongoing = "ongoing"

    """ resolvedWithSequelae
    """
    resolvedWithSequelae = "resolvedWithSequelae"

    """ fatal
    """
    fatal = "fatal"

    """ unknown
    """
    unknown = "unknown"


class AdverseEventSeriousness(CodeSystemValue):
    """ Overall seriousness of this event for the patient

    URL: http://hl7.org/fhir/adverse-event-seriousness
    ValueSet: http://hl7.org/fhir/ValueSet/adverse-event-seriousness
    """
    URL = "http://hl7.org/fhir/adverse-event-seriousness"
    EXPERIMENTAL = False

    """ Non-serious
    """
    nonSerious = "Non-serious"

    """ Serious
    """
    serious = "Serious"

    """ Results in death
    """
    seriousResultsInDeath = "SeriousResultsInDeath"

    """ Is Life-threatening
    """
    seriousIsLifeThreatening = "SeriousIsLifeThreatening"

    """ Requires inpatient hospitalization or causes prolongation of existing hospitalization
    """
    seriousResultsInHospitalization = "SeriousResultsInHospitalization"

    """ Results in persistent or significant disability/incapacity
    """
    seriousResultsInDisability = "SeriousResultsInDisability"

    """ Is a congenital anomaly/birth defect
    """
    seriousIsBirthDefect = "SeriousIsBirthDefect"

    """ Requires intervention to prevent permanent impairment or damage (i.e., an important medical event that requires
	/// medical judgement)
    """
    seriousRequiresPreventImpairment = "SeriousRequiresPreventImpairment"


class AdverseEventSeverity(CodeSystemValue):
    """ The severity of the adverse event itself, in direct relation to the subject

    URL: http://hl7.org/fhir/adverse-event-severity
    ValueSet: http://hl7.org/fhir/ValueSet/adverse-event-severity
    """
    URL = "http://hl7.org/fhir/adverse-event-severity"
    EXPERIMENTAL = False

    """ mild
    """
    mild = "Mild"

    """ moderate
    """
    moderate = "Moderate"

    """ severe
    """
    severe = "Severe"


class AggregationMode(CodeSystemValue):
    """ How resource references can be aggregated.

    URL: http://hl7.org/fhir/resource-aggregation-mode
    ValueSet: http://hl7.org/fhir/ValueSet/resource-aggregation-mode
    """
    URL = "http://hl7.org/fhir/resource-aggregation-mode"
    EXPERIMENTAL = False

    """ The reference is a local reference to a contained resource.
    """
    contained = "contained"

    """ The reference to a resource that has to be resolved externally to the resource that includes the reference.
    """
    referenced = "referenced"

    """ The resource the reference points to will be found in the same bundle as the resource that includes the
	/// reference.
    """
    bundled = "bundled"


class AllergyIntoleranceCategory(CodeSystemValue):
    """ Category of an identified substance.

    URL: http://hl7.org/fhir/allergy-intolerance-category
    ValueSet: http://hl7.org/fhir/ValueSet/allergy-intolerance-category
    """
    URL = "http://hl7.org/fhir/allergy-intolerance-category"
    EXPERIMENTAL = False

    """ Any substance consumed to provide nutritional support for the body.
    """
    food = "food"

    """ Substances administered to achieve a physiological effect.
    """
    medication = "medication"

    """ Any substances that are encountered in the environment, including any substance not already classified as food,
	/// medication, or biologic.
    """
    environment = "environment"

    """ A preparation that is synthesized from living organisms or their products, especially a human or animal protein,
	/// such as a hormone or antitoxin, that is used as a diagnostic, preventive, or therapeutic agent. Examples of
	/// biologic medications include: vaccines; allergenic extracts, which are used for both diagnosis and treatment
	/// (for example, allergy shots); gene therapies; cellular therapies.  There are other biologic products, such as
	/// tissues, that are not typically associated with allergies.
    """
    biologic = "biologic"


class AllergyIntoleranceCertainty(CodeSystemValue):
    """ Statement about the degree of clinical certainty that a specific substance was the cause of the manifestation in a
reaction event.

    URL: http://hl7.org/fhir/reaction-event-certainty
    ValueSet: http://hl7.org/fhir/ValueSet/reaction-event-certainty
    """
    URL = "http://hl7.org/fhir/reaction-event-certainty"
    EXPERIMENTAL = False

    """ There is a low level of clinical certainty that the reaction was caused by the identified substance.
    """
    unlikely = "unlikely"

    """ There is a high level of clinical certainty that the reaction was caused by the identified substance.
    """
    likely = "likely"

    """ There is a very high level of clinical certainty that the reaction was due to the identified substance, which
	/// may include clinical evidence by testing or rechallenge.
    """
    confirmed = "confirmed"

    """ The clinical certainty that the reaction was caused by the identified substance is unknown.  It is an explicit
	/// assertion that certainty is not known.
    """
    unknown = "unknown"


class AllergyIntoleranceClinicalStatus(CodeSystemValue):
    """ The clinical status of the allergy or intolerance.

    URL: http://hl7.org/fhir/allergy-clinical-status
    ValueSet: http://hl7.org/fhir/ValueSet/allergy-clinical-status
    """
    URL = "http://hl7.org/fhir/allergy-clinical-status"
    EXPERIMENTAL = False

    """ An active record of a risk of a reaction to the identified substance.
    """
    active = "active"

    """ An inactivated record of a risk of a reaction to the identified substance.
    """
    inactive = "inactive"

    """ A reaction to the identified substance has been clinically reassessed by testing or re-exposure and considered
	/// to be resolved.
    """
    resolved = "resolved"


class AllergyIntoleranceCriticality(CodeSystemValue):
    """ Estimate of the potential clinical harm, or seriousness, of a reaction to an identified substance.

    URL: http://hl7.org/fhir/allergy-intolerance-criticality
    ValueSet: http://hl7.org/fhir/ValueSet/allergy-intolerance-criticality
    """
    URL = "http://hl7.org/fhir/allergy-intolerance-criticality"
    EXPERIMENTAL = False

    """ Worst case result of a future exposure is not assessed to be life-threatening or having high potential for organ
	/// system failure.
    """
    low = "low"

    """ Worst case result of a future exposure is assessed to be life-threatening or having high potential for organ
	/// system failure.
    """
    high = "high"

    """ Unable to assess the worst case result of a future exposure.
    """
    unableToAssess = "unable-to-assess"


class AllergyIntoleranceSeverity(CodeSystemValue):
    """ Clinical assessment of the severity of a reaction event as a whole, potentially considering multiple different
manifestations.

    URL: http://hl7.org/fhir/reaction-event-severity
    ValueSet: http://hl7.org/fhir/ValueSet/reaction-event-severity
    """
    URL = "http://hl7.org/fhir/reaction-event-severity"
    EXPERIMENTAL = False

    """ Causes mild physiological effects.
    """
    mild = "mild"

    """ Causes moderate physiological effects.
    """
    moderate = "moderate"

    """ Causes severe physiological effects.
    """
    severe = "severe"


class AllergyIntoleranceSubstanceExposureRisk(CodeSystemValue):
    """ The risk of an adverse reaction (allergy or intolerance) for this patient upon exposure to the substance (including
pharmaceutical products).

    URL: http://hl7.org/fhir/allerg-intol-substance-exp-risk
    ValueSet: http://hl7.org/fhir/ValueSet/allerg-intol-substance-exp-risk
    """
    URL = "http://hl7.org/fhir/allerg-intol-substance-exp-risk"
    EXPERIMENTAL = False

    """ Known risk of allergy or intolerance reaction upon exposure to the specified substance.
    """
    knownReactionRisk = "known-reaction-risk"

    """ No known risk of allergy or intolerance reaction upon exposure to the specified substance.
    """
    noKnownReactionRisk = "no-known-reaction-risk"


class AllergyIntoleranceType(CodeSystemValue):
    """ Identification of the underlying physiological mechanism for a Reaction Risk.

    URL: http://hl7.org/fhir/allergy-intolerance-type
    ValueSet: http://hl7.org/fhir/ValueSet/allergy-intolerance-type
    """
    URL = "http://hl7.org/fhir/allergy-intolerance-type"
    EXPERIMENTAL = False

    """ A propensity for hypersensitivity reaction(s) to a substance.  These reactions are most typically type I
	/// hypersensitivity, plus other "allergy-like" reactions, including pseudoallergy.
    """
    allergy = "allergy"

    """ A propensity for adverse reactions to a substance that is not judged to be allergic or "allergy-like".  These
	/// reactions are typically (but not necessarily) non-immune.  They are to some degree idiosyncratic and/or
	/// individually specific (i.e. are not a reaction that is expected to occur with most or all patients given similar
	/// circumstances).
    """
    intolerance = "intolerance"


class AllergyIntoleranceVerificationStatus(CodeSystemValue):
    """ Assertion about certainty associated with a propensity, or potential risk, of a reaction to the identified substance.

    URL: http://hl7.org/fhir/allergy-verification-status
    ValueSet: http://hl7.org/fhir/ValueSet/allergy-verification-status
    """
    URL = "http://hl7.org/fhir/allergy-verification-status"
    EXPERIMENTAL = False

    """ A low level of certainty about the propensity for a reaction to the identified substance.
    """
    unconfirmed = "unconfirmed"

    """ A high level of certainty about the propensity for a reaction to the identified substance, which may include
	/// clinical evidence by testing or rechallenge.
    """
    confirmed = "confirmed"

    """ A propensity for a reaction to the identified substance has been disproven with a high level of clinical
	/// certainty, which may include testing or rechallenge, and is refuted.
    """
    refuted = "refuted"

    """ The statement was entered in error and is not valid.
    """
    enteredInError = "entered-in-error"


class AlternativeCodeKind(CodeSystemValue):
    """ Indicates the type of use for which the code is defined

    URL: http://hl7.org/fhir/codesystem-altcode-kind
    ValueSet: http://hl7.org/fhir/ValueSet/codesystem-altcode-kind
    """
    URL = "http://hl7.org/fhir/codesystem-altcode-kind"
    EXPERIMENTAL = False

    """ The code is an alternative code that can be used in any of the circumstances that the primary code can be used
    """
    alternate = "alternate"

    """ The code should no longer be used, but was used in the past
    """
    deprecated = "deprecated"

    """ The code is an alternative to be used when a case insensitive code is required (when the primary codes are case
	/// sensitive)
    """
    caseInsensitive = "case-insensitive"

    """ The code is an alternative to be used when a case sensitive code is required (when the primary codes are case
	/// insensitive)
    """
    caseSensitive = "case-sensitive"

    """ The code is an alternative for the primary code that is built using the expression grammar defined by the code
	/// system
    """
    expression = "expression"


class AnimalSpecies(CodeSystemValue):
    """ This example value set defines a set of codes that can be used to indicate species of animal patients.

    URL: http://hl7.org/fhir/animal-species
    ValueSet: http://hl7.org/fhir/ValueSet/animal-species
    """
    URL = "http://hl7.org/fhir/animal-species"
    EXPERIMENTAL = True

    """ Canis lupus familiaris
    """
    canislf = "canislf"

    """ Ovis aries
    """
    ovisa = "ovisa"

    """ Serinus canaria domestica
    """
    serinuscd = "serinuscd"


class AppointmentStatus(CodeSystemValue):
    """ The free/busy status of an appointment.

    URL: http://hl7.org/fhir/appointmentstatus
    ValueSet: http://hl7.org/fhir/ValueSet/appointmentstatus
    """
    URL = "http://hl7.org/fhir/appointmentstatus"
    EXPERIMENTAL = False

    """ None of the participant(s) have finalized their acceptance of the appointment request, and the start/end time
	/// might not be set yet.
    """
    proposed = "proposed"

    """ Some or all of the participant(s) have not finalized their acceptance of the appointment request.
    """
    pending = "pending"

    """ All participant(s) have been considered and the appointment is confirmed to go ahead at the date/times
	/// specified.
    """
    booked = "booked"

    """ The patient/patients has/have arrived and is/are waiting to be seen
    """
    arrived = "arrived"

    """ This appointment has completed and may have resulted in an encounter.
    """
    fulfilled = "fulfilled"

    """ The appointment has been cancelled.
    """
    cancelled = "cancelled"

    """ Some or all of the participant(s) have not/did not appear for the appointment (usually the patient).
    """
    noshow = "noshow"

    """ This instance should not have been part of this patient's medical record.
    """
    enteredInError = "entered-in-error"

    """ When checked in, all pre-encounter administrative work is complete, and the encounter may begin. (where multiple
	/// patients are involved, they are all present)
    """
    checkedIn = "checked-in"


class AssertionDirectionType(CodeSystemValue):
    """ The type of direction to use for assertion.

    URL: http://hl7.org/fhir/assert-direction-codes
    ValueSet: http://hl7.org/fhir/ValueSet/assert-direction-codes
    """
    URL = "http://hl7.org/fhir/assert-direction-codes"
    EXPERIMENTAL = False

    """ The assertion is evaluated on the response. This is the default value.
    """
    response = "response"

    """ The assertion is evaluated on the request.
    """
    request = "request"


class AssertionOperatorType(CodeSystemValue):
    """ The type of operator to use for assertion.

    URL: http://hl7.org/fhir/assert-operator-codes
    ValueSet: http://hl7.org/fhir/ValueSet/assert-operator-codes
    """
    URL = "http://hl7.org/fhir/assert-operator-codes"
    EXPERIMENTAL = False

    """ Default value. Equals comparison.
    """
    equals = "equals"

    """ Not equals comparison.
    """
    notEquals = "notEquals"

    """ Compare value within a known set of values.
    """
    _in = "in"

    """ Compare value not within a known set of values.
    """
    notIn = "notIn"

    """ Compare value to be greater than a known value.
    """
    greaterThan = "greaterThan"

    """ Compare value to be less than a known value.
    """
    lessThan = "lessThan"

    """ Compare value is empty.
    """
    empty = "empty"

    """ Compare value is not empty.
    """
    notEmpty = "notEmpty"

    """ Compare value string contains a known value.
    """
    contains = "contains"

    """ Compare value string does not contain a known value.
    """
    notContains = "notContains"

    """ Evaluate the FHIRPath expression as a boolean condition.
    """
    eval = "eval"


class AssertionResponseTypes(CodeSystemValue):
    """ The type of response code to use for assertion.

    URL: http://hl7.org/fhir/assert-response-code-types
    ValueSet: http://hl7.org/fhir/ValueSet/assert-response-code-types
    """
    URL = "http://hl7.org/fhir/assert-response-code-types"
    EXPERIMENTAL = False

    """ Response code is 200.
    """
    okay = "okay"

    """ Response code is 201.
    """
    created = "created"

    """ Response code is 204.
    """
    noContent = "noContent"

    """ Response code is 304.
    """
    notModified = "notModified"

    """ Response code is 400.
    """
    bad = "bad"

    """ Response code is 403.
    """
    forbidden = "forbidden"

    """ Response code is 404.
    """
    notFound = "notFound"

    """ Response code is 405.
    """
    methodNotAllowed = "methodNotAllowed"

    """ Response code is 409.
    """
    conflict = "conflict"

    """ Response code is 410.
    """
    gone = "gone"

    """ Response code is 412.
    """
    preconditionFailed = "preconditionFailed"

    """ Response code is 422.
    """
    unprocessable = "unprocessable"


class AuditEventAction(CodeSystemValue):
    """ Indicator for type of action performed during the event that generated the event

    URL: http://hl7.org/fhir/audit-event-action
    ValueSet: http://hl7.org/fhir/ValueSet/audit-event-action
    """
    URL = "http://hl7.org/fhir/audit-event-action"
    EXPERIMENTAL = False

    """ Create a new database object, such as placing an order.
    """
    C = "C"

    """ Display or print data, such as a doctor census.
    """
    R = "R"

    """ Update data, such as revise patient information.
    """
    U = "U"

    """ Delete items, such as a doctor master file record.
    """
    D = "D"

    """ Perform a system or application function such as log-on, program execution or use of an object's method, or
	/// perform a query/search operation.
    """
    E = "E"


class AuditEventID(CodeSystemValue):
    """ Event Types for Audit Events - defined by DICOM with some FHIR specific additions.

    URL: http://hl7.org/fhir/audit-event-type
    ValueSet: http://hl7.org/fhir/ValueSet/audit-event-type
    """
    URL = "http://hl7.org/fhir/audit-event-type"
    EXPERIMENTAL = True

    """ Audit Event: Execution of a RESTful operation as defined by FHIR.
    """
    rest = "rest"


class BasicResourceTypes(CodeSystemValue):
    """ This value set defines codes for resources not yet supported by (or which will never be supported by) FHIR.  Many of the
codes listed here will eventually be turned into official resources.  However, there is no guarantee that any particular
resource will be created nor that the scope will be exactly as defined by the codes presented here.  Codes in this set
will be deprecated if/when formal resources are defined that encompass these concepts.

    URL: http://hl7.org/fhir/basic-resource-type
    ValueSet: http://hl7.org/fhir/ValueSet/basic-resource-type
    """
    URL = "http://hl7.org/fhir/basic-resource-type"
    EXPERIMENTAL = True

    """ An assertion of permission for an activity or set of activities to occur, possibly subject to particular
	/// limitations; e.g. surgical consent, information disclosure consent, etc.
    """
    consent = "consent"

    """ A request that care of a particular type be provided to a patient.  Could involve the transfer of care, a
	/// consult, etc.
    """
    referral = "referral"

    """ An undesired reaction caused by exposure to some agent (e.g. a medication, immunization, food, or environmental
	/// agent).
    """
    advevent = "advevent"

    """ A request that a time be scheduled for a type of service for a specified patient, potentially subject to other
	/// constraints
    """
    aptmtreq = "aptmtreq"

    """ The transition of a patient or set of material from one location to another
    """
    transfer = "transfer"

    """ The specification of a set of food and/or other nutritional material to be delivered to a patient.
    """
    diet = "diet"

    """ An occurrence of a non-care-related event in the healthcare domain, such as approvals, reviews, etc.
    """
    adminact = "adminact"

    """ Record of a situation where a subject was exposed to a substance.  Usually of interest to public health.
    """
    exposure = "exposure"

    """ A formalized inquiry into the circumstances surrounding a particular unplanned event or potential event for the
	/// purposes of identifying possible causes and contributing factors for the event
    """
    investigation = "investigation"

    """ A financial instrument used to track costs, charges or other amounts.
    """
    account = "account"

    """ A request for payment for goods and/or services.  Includes the idea of a healthcare insurance claim.
    """
    invoice = "invoice"

    """ The determination of what will be paid against a particular invoice based on coverage, plan rules, etc.
    """
    adjudicat = "adjudicat"

    """ A request for a pre-determination of the cost that would be paid under an insurance plan for a hypothetical
	/// claim for goods or services
    """
    predetreq = "predetreq"

    """ An adjudication of what would be paid under an insurance plan for a hypothetical claim for goods or services
    """
    predetermine = "predetermine"

    """ An investigation to determine information about a particular therapy or product
    """
    study = "study"

    """ A set of (possibly conditional) steps to be taken to achieve some aim.  Includes study protocols, treatment
	/// protocols, emergency protocols, etc.
    """
    protocol = "protocol"


class BenefitCategoryCodes(CodeSystemValue):
    """ This value set includes a smattering of Benefit Category codes.

    URL: http://hl7.org/fhir/benefit-category
    ValueSet: http://hl7.org/fhir/ValueSet/benefit-category
    """
    URL = "http://hl7.org/fhir/benefit-category"
    EXPERIMENTAL = True

    """ Dental and Oral Health Coverage
    """
    oral = "oral"

    """ Vision Health Coverage
    """
    vision = "vision"

    """ Medical Health Coverage
    """
    medical = "medical"

    """ Pharmacy Coverage
    """
    pharmacy = "pharmacy"


class BenefitTermCodes(CodeSystemValue):
    """ This value set includes a smattering of Benefit Term codes.

    URL: http://hl7.org/fhir/benefit-term
    ValueSet: http://hl7.org/fhir/ValueSet/benefit-term
    """
    URL = "http://hl7.org/fhir/benefit-term"
    EXPERIMENTAL = True

    """ Annual, renewing on the anniversary
    """
    annual = "annual"

    """ Per day
    """
    day = "day"

    """ For the total term, lifetime, of the policy or coverage
    """
    lifetime = "lifetime"


class BenefitTypeCodes(CodeSystemValue):
    """ This value set includes a smattering of Benefit type codes.

    URL: http://hl7.org/fhir/benefit-type
    ValueSet: http://hl7.org/fhir/ValueSet/benefit-type
    """
    URL = "http://hl7.org/fhir/benefit-type"
    EXPERIMENTAL = True

    """ Maximum benefit allowable.
    """
    benefit = "benefit"

    """ Cost to be incurred before benefits are applied
    """
    deductible = "deductible"

    """ Service visit
    """
    visit = "visit"

    """ Type of room
    """
    room = "room"

    """ Copayment per service
    """
    copay = "copay"

    """ Copayment percentage per service
    """
    copayPercent = "copay-percent"

    """ Copayment maximum per service
    """
    copayMaximum = "copay-maximum"

    """ Vision Exam
    """
    visionExam = "vision-exam"

    """ Frames and lenses
    """
    visionGlasses = "vision-glasses"

    """ Contact Lenses
    """
    visionContacts = "vision-contacts"

    """ Medical Primary Health Coverage
    """
    medicalPrimarycare = "medical-primarycare"

    """ Pharmacy Dispense Coverage
    """
    pharmacyDispense = "pharmacy-dispense"


class BindingStrength(CodeSystemValue):
    """ Indication of the degree of conformance expectations associated with a binding.

    URL: http://hl7.org/fhir/binding-strength
    ValueSet: http://hl7.org/fhir/ValueSet/binding-strength
    """
    URL = "http://hl7.org/fhir/binding-strength"
    EXPERIMENTAL = False

    """ To be conformant, the concept in this element SHALL be from the specified value set
    """
    required = "required"

    """ To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within
	/// the value set can apply to the concept being communicated.  If the value set does not cover the concept (based
	/// on human review), alternate codings (or, data type allowing, text) may be included instead.
    """
    extensible = "extensible"

    """ Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to
	/// do so to be considered conformant.
    """
    preferred = "preferred"

    """ Instances are not expected or even encouraged to draw from the specified value set.  The value set merely
	/// provides examples of the types of concepts intended to be included.
    """
    example = "example"


class BiologicallyDerivedProductCategory(CodeSystemValue):
    """ Biologically Derived Product Category

    URL: http://hl7.org/fhir/product-category
    ValueSet: http://hl7.org/fhir/ValueSet/product-category
    """
    URL = "http://hl7.org/fhir/product-category"
    EXPERIMENTAL = False

    """ A collection of tissues joined in a structural unit to serve a common function.
    """
    organ = "organ"

    """ An ensemble of similar cells and their extracellular matrix from the same origin that together carry out a
	/// specific function.
    """
    tissue = "tissue"

    """ Body fluid
    """
    fluid = "fluid"

    """ Collection of cells
    """
    cells = "cells"

    """ Biological agent of unspecified type
    """
    biologicalAgent = "biologicalAgent"


class BiologicallyDerivedProductStatus(CodeSystemValue):
    """ Biologically Derived Product Status

    URL: http://hl7.org/fhir/product-status
    ValueSet: http://hl7.org/fhir/ValueSet/product-status
    """
    URL = "http://hl7.org/fhir/product-status"
    EXPERIMENTAL = False

    """ Product is currently available for use.
    """
    available = "available"

    """ Product is not currently available for use.
    """
    unavailable = "unavailable"


class BiologicallyDerivedProductStorageScale(CodeSystemValue):
    """ BiologicallyDerived Product Storage Scale

    URL: http://hl7.org/fhir/product-storage-scale
    ValueSet: http://hl7.org/fhir/ValueSet/product-storage-scale
    """
    URL = "http://hl7.org/fhir/product-storage-scale"
    EXPERIMENTAL = False

    """ Fahrenheit temperature scale
    """
    farenheit = "farenheit"

    """ Celsius or centigrade temperature scale
    """
    celsius = "celsius"

    """ Kelvin absolute thermodynamic temperature scale
    """
    kelvin = "kelvin"


class BundleType(CodeSystemValue):
    """ Indicates the purpose of a bundle - how it was intended to be used.

    URL: http://hl7.org/fhir/bundle-type
    ValueSet: http://hl7.org/fhir/ValueSet/bundle-type
    """
    URL = "http://hl7.org/fhir/bundle-type"
    EXPERIMENTAL = False

    """ The bundle is a document. The first resource is a Composition.
    """
    document = "document"

    """ The bundle is a message. The first resource is a MessageHeader.
    """
    message = "message"

    """ The bundle is a transaction - intended to be processed by a server as an atomic commit.
    """
    transaction = "transaction"

    """ The bundle is a transaction response. Because the response is a transaction response, the transaction has
	/// succeeded, and all responses are error free.
    """
    transactionResponse = "transaction-response"

    """ The bundle is a transaction - intended to be processed by a server as a group of actions.
    """
    batch = "batch"

    """ The bundle is a batch response. Note that as a batch, some responses may indicate failure and others success.
    """
    batchResponse = "batch-response"

    """ The bundle is a list of resources from a history interaction on a server.
    """
    history = "history"

    """ The bundle is a list of resources returned as a result of a search/query interaction, operation, or message.
    """
    searchset = "searchset"

    """ The bundle is a set of resources collected into a single package for ease of distribution.
    """
    collection = "collection"


class CanPushUpdates(CodeSystemValue):
    """ Ability of the primary source to push updates/alerts

    URL: http://hl7.org/fhir/can-push-updates
    ValueSet: http://hl7.org/fhir/ValueSet/can-push-updates
    """
    URL = "http://hl7.org/fhir/can-push-updates"
    EXPERIMENTAL = False

    """ yes
    """
    yes = "yes"

    """ no
    """
    no = "no"

    """ undetermined
    """
    undetermined = "undetermined"


class CanonicalStatusCodesForFHIRResources(CodeSystemValue):
    """ The master set of status codes used throughout FHIR. All status codes are mapped to one of these codes.

    URL: http://hl7.org/fhir/resource-status
    ValueSet: http://hl7.org/fhir/ValueSet/resource-status
    """
    URL = "http://hl7.org/fhir/resource-status"

    """ The resource was created in error, and should not be treated as valid (note: in many cases, for various data
	/// integrity related reasons, the information cannot be removed from the record)
    """
    error = "error"

    """ The resource describes an action or plan that is proposed, and not yet approved by the participants
    """
    proposed = "proposed"

    """ The resource describes a course of action that is planned and agreed/approved, but at the time of recording was
	/// still future
    """
    planned = "planned"

    """ The information in the resource is still being prepared and edited
    """
    draft = "draft"

    """ A fulfiller has been asked to perform this action, but it has not yet occurred
    """
    requested = "requested"

    """ The fulfiller has received the request, but not yet agreed to carry out the action
    """
    received = "received"

    """ The fulfiller chose not to perform the action
    """
    declined = "declined"

    """ The fulfiller has decided to perform the action, and plans are in train to do this in the future
    """
    accepted = "accepted"

    """ The pre-conditions for the action are all fulfilled, and it is imminent
    """
    arrived = "arrived"

    """ The resource describes information that is currently valid or a process that is presently occuring
    """
    active = "active"

    """ The process described/requested in this resource has been halted for some reason
    """
    suspended = "suspended"

    """ The process described/requested in the resource could not be completed, and no further action is planned
    """
    failed = "failed"

    """ The information in this resource has been replaced by information in another resource
    """
    replaced = "replaced"

    """ The process described/requested in the resource has been completed, and no further action is planned
    """
    complete = "complete"

    """ The resource describes information that is no longer valid or a process that is stopped occurring
    """
    inactive = "inactive"

    """ The process described/requested in the resource did not complete - usually due to some workflow error, and no
	/// further action is planned
    """
    abandoned = "abandoned"

    """ Authoring system does not know the status
    """
    unknown = "unknown"

    """ The information in this resource is not yet approved
    """
    unconfirmed = "unconfirmed"

    """ The information in this resource is approved
    """
    confirmed = "confirmed"

    """ The issue identified by this resource is no longer of concern
    """
    resolved = "resolved"

    """ This information has been ruled out by testing and evaluation
    """
    refuted = "refuted"

    """ Potentially true?
    """
    differential = "differential"

    """ This information is still being assembled
    """
    partial = "partial"

    """ not available at this time/location
    """
    busyUnavailable = "busy-unavailable"

    """ Free for scheduling
    """
    free = "free"

    """ Ready to act
    """
    onTarget = "on-target"

    """ Ahead of the planned timelines
    """
    aheadOfTarget = "ahead-of-target"

    """ behindTarget
    """
    behindTarget = "behind-target"

    """ Behind the planned timelines
    """
    notReady = "not-ready"

    """ The device transducer is disconnected
    """
    transducDiscon = "transduc-discon"

    """ The hardware is disconnected
    """
    hwDiscon = "hw-discon"


class CapabilityStatementKind(CodeSystemValue):
    """ How a capability statement is intended to be used.

    URL: http://hl7.org/fhir/capability-statement-kind
    ValueSet: http://hl7.org/fhir/ValueSet/capability-statement-kind
    """
    URL = "http://hl7.org/fhir/capability-statement-kind"
    EXPERIMENTAL = False

    """ The CapabilityStatement instance represents the present capabilities of a specific system instance.  This is the
	/// kind returned by /metadata for a FHIR server end-point.
    """
    instance = "instance"

    """ The CapabilityStatement instance represents the capabilities of a system or piece of software, independent of a
	/// particular installation.
    """
    capability = "capability"

    """ The CapabilityStatement instance represents a set of requirements for other systems to meet; e.g. as part of an
	/// implementation guide or 'request for proposal'.
    """
    requirements = "requirements"


class CarePlanActivityStatus(CodeSystemValue):
    """ Indicates where the activity is at in its overall life cycle.

    URL: http://hl7.org/fhir/care-plan-activity-status
    ValueSet: http://hl7.org/fhir/ValueSet/care-plan-activity-status
    """
    URL = "http://hl7.org/fhir/care-plan-activity-status"
    EXPERIMENTAL = False

    """ Activity is planned but no action has yet been taken.
    """
    notStarted = "not-started"

    """ Appointment or other booking has occurred but activity has not yet begun.
    """
    scheduled = "scheduled"

    """ Activity has been started but is not yet complete.
    """
    inProgress = "in-progress"

    """ Activity was started but has temporarily ceased with an expectation of resumption at a future time.
    """
    onHold = "on-hold"

    """ The activity has been completed (more or less) as planned.
    """
    completed = "completed"

    """ The planned activity has been withdrawn.
    """
    cancelled = "cancelled"

    """ The planned activity has been ended prior to completion after the activity was started.
    """
    stopped = "stopped"

    """ The current state of the activity is not known.  Note: This concept is not to be used for "other".
    """
    unknown = "unknown"


class CarePlanIntent(CodeSystemValue):
    """ Codes indicating the degree of authority/intentionality associated with a care plan

    URL: http://hl7.org/fhir/care-plan-intent
    ValueSet: http://hl7.org/fhir/ValueSet/care-plan-intent
    """
    URL = "http://hl7.org/fhir/care-plan-intent"
    EXPERIMENTAL = False

    """ The care plan is a suggestion made by someone/something that doesn't have an intention to ensure it occurs and
	/// without providing an authorization to act
    """
    proposal = "proposal"

    """ The care plan represents an intention to ensure something occurs without providing an authorization for others
	/// to act
    """
    plan = "plan"

    """ The care plan represents a request/demand and authorization for action
    """
    order = "order"

    """ The care plan represents a component or option for a RequestGroup that establishes timing, conditionality and/or
	/// other constraints among a set of requests.
	/// 
	/// Refer to [[[RequestGroup]]] for additional information on how this status is used
    """
    option = "option"


class CarePlanStatus(CodeSystemValue):
    """ Indicates whether the plan is currently being acted upon, represents future intentions or is now a historical record.

    URL: http://hl7.org/fhir/care-plan-status
    ValueSet: http://hl7.org/fhir/ValueSet/care-plan-status
    """
    URL = "http://hl7.org/fhir/care-plan-status"
    EXPERIMENTAL = False

    """ The plan is in development or awaiting use but is not yet intended to be acted upon.
    """
    draft = "draft"

    """ The plan is intended to be followed and used as part of patient care.
    """
    active = "active"

    """ The plan has been temporarily stopped but is expected to resume in the future.
    """
    suspended = "suspended"

    """ The plan is no longer in use and is not expected to be followed or used in patient care.
    """
    completed = "completed"

    """ The plan was entered in error and voided.
    """
    enteredInError = "entered-in-error"

    """ The plan has been terminated prior to reaching completion (though it may have been replaced by a new plan).
    """
    cancelled = "cancelled"

    """ The authoring system doesn't know the current state of the care plan.
    """
    unknown = "unknown"


class CareTeamCategory(CodeSystemValue):
    """ Indicates the type of care team.

    URL: http://hl7.org/fhir/care-team-category
    ValueSet: http://hl7.org/fhir/ValueSet/care-team-category
    """
    URL = "http://hl7.org/fhir/care-team-category"
    EXPERIMENTAL = False

    """ This type of team focuses on one specific type of incident, which is non-patient specific. The incident is
	/// determined by the context of use.  For example, code team (code red, code blue, medical emergency treatment) or
	/// the PICC line team.
    """
    event = "event"

    """ This type of team focuses on one specific encounter. The encounter is determined by the context of use.  For
	/// example, during an inpatient encounter, the nutrition support care team
    """
    encounter = "encounter"

    """ This type of team focuses on one specific episode of care with a defined time period or self-limiting process
	/// (e.g. 10 visits). The episode of care is determined by the context of use.  For example, a maternity care team
	/// over 9 months.
    """
    episode = "episode"

    """ This type of team focuses on overall care coordination managing one or more conditions across the continuum of
	/// care ensuring there are smooth transitions of care. The members of the team are determined or selected by an
	/// individual or organization. When determined by an organization, the team may be assigned or based on the
	/// person's enrollment in a particular program. For example, disease management team or patient centered medical
	/// home team.
    """
    longitudinal = "longitudinal"

    """ This type of team focuses on one specific condition. The condition is determined by the context of use.  For
	/// example, a disease management team focused on one condition (e.g. diabetes).
    """
    condition = "condition"

    """ This type of team is responsible for establishing, conducting, coordinating and monitoring the outcomes of
	/// clinical trials. The team focuses on research, clinical care and education.
    """
    clinicalResearch = "clinical-research"


class CareTeamStatus(CodeSystemValue):
    """ Indicates the status of the care team.

    URL: http://hl7.org/fhir/care-team-status
    ValueSet: http://hl7.org/fhir/ValueSet/care-team-status
    """
    URL = "http://hl7.org/fhir/care-team-status"
    EXPERIMENTAL = False

    """ The care team has been drafted and proposed, but not yet participating in the coordination and delivery of care.
    """
    proposed = "proposed"

    """ The care team is currently participating in the coordination and delivery of care.
    """
    active = "active"

    """ The care team is temporarily on hold or suspended and not participating in the coordination and delivery of
	/// care.
    """
    suspended = "suspended"

    """ The care team was, but is no longer, participating in the coordination and delivery of care.
    """
    inactive = "inactive"

    """ The care team should have never existed.
    """
    enteredInError = "entered-in-error"


class CatalogType(CodeSystemValue):
    """ The type of catalog

    URL: http://hl7.org/fhir/catalogType
    ValueSet: http://hl7.org/fhir/ValueSet/catalogType
    """
    URL = "http://hl7.org/fhir/catalogType"
    EXPERIMENTAL = False

    """ Medication Catalog
    """
    medication = "medication"

    """ Device Catalog
    """
    device = "device"

    """ Protocol List
    """
    protocol = "protocol"


class ChargeItemStatus(CodeSystemValue):
    """ Codes identifying the lifecycle stage of a ChargeItem

    URL: http://hl7.org/fhir/chargeitem-status
    ValueSet: http://hl7.org/fhir/ValueSet/chargeitem-status
    """
    URL = "http://hl7.org/fhir/chargeitem-status"
    EXPERIMENTAL = False

    """ The charge item has been entered, but the charged service is not  yet complete, so it shall not be billed yet
	/// but might be used in the context of pre-authorization
    """
    planned = "planned"

    """ The charge item is ready for billing
    """
    billable = "billable"

    """ The charge item has been determined to be not billable (e.g. due to rules associated with the billing code)
    """
    notBillable = "not-billable"

    """ The processing of the charge was aborted
    """
    aborted = "aborted"

    """ The charge item has been billed (e.g. a billing engine has generated financial transactions by applying the
	/// associated ruled for the charge item to the context of the Encounter, and placed them into Claims/Invoices
    """
    billed = "billed"

    """ The charge item has been entered in error and should not be processed for billing
    """
    enteredInError = "entered-in-error"

    """ The authoring system does not know which of the status values currently applies for this charge item  Note: This
	/// concept is not to be used for "other" - one of the listed statuses is presumed to apply, it's just not known
	/// which one.
    """
    unknown = "unknown"


class ChoiceListOrientation(CodeSystemValue):
    """ Direction in which lists of question options should be displayed

    URL: http://hl7.org/fhir/choice-list-orientation
    ValueSet: http://hl7.org/fhir/ValueSet/choice-list-orientation
    """
    URL = "http://hl7.org/fhir/choice-list-orientation"
    EXPERIMENTAL = False

    """ List choices along the horizontal axis
    """
    horizontal = "horizontal"

    """ List choices down the vertical axis
    """
    vertical = "vertical"


class ClaimCareTeamRoleCodes(CodeSystemValue):
    """ This value set includes sample Claim Care Team Role codes.

    URL: http://hl7.org/fhir/claimcareteamrole
    ValueSet: http://hl7.org/fhir/ValueSet/claim-careteamrole
    """
    URL = "http://hl7.org/fhir/claimcareteamrole"
    EXPERIMENTAL = True

    """ The primary care provider.
    """
    primary = "primary"

    """ Assisting care provider.
    """
    assist = "assist"

    """ Supervising care provider.
    """
    supervisor = "supervisor"

    """ Other role on the care team.
    """
    other = "other"


class ClaimInformationCategoryCodes(CodeSystemValue):
    """ This value set includes sample Information Category codes.

    URL: http://hl7.org/fhir/claiminformationcategory
    ValueSet: http://hl7.org/fhir/ValueSet/claim-informationcategory
    """
    URL = "http://hl7.org/fhir/claiminformationcategory"
    EXPERIMENTAL = True

    """ Codes conveying additional situation and condition information.
    """
    info = "info"

    """ Discharge status and discharge to locations.
    """
    discharge = "discharge"

    """ Period, start or end dates of aspects of the Condition.
    """
    onset = "onset"

    """ Nature and date of the related event eg. Last exam, service, Xray etc.
    """
    related = "related"

    """ Insurance policy exceptions.
    """
    exception = "exception"

    """ Materials being forwarded, eg. Models, molds, images, documents.
    """
    material = "material"

    """ Materials attached such as images, documents and resources.
    """
    attachment = "attachment"

    """ Teeth which are missing for any reason, for example: prior extraction, never developed.
    """
    missingtooth = "missingtooth"

    """ The type of prosthesis and date of supply if a previously supplied prosthesis.
    """
    prosthesis = "prosthesis"

    """ Other information identified by the type.system.
    """
    other = "other"

    """ An indication that the patient was hospitalized, the period if known otherwise a Yes/No (boolean).
    """
    hospitalized = "hospitalized"

    """ An indication that the patient was unable to work, the period if known otherwise a Yes/No (boolean).
    """
    employmentimpacted = "employmentimpacted"


class ClaimItemTypeCodes(CodeSystemValue):
    """ This value set includes sample Item Type codes.

    URL: http://hl7.org/fhir/ex-claimitemtype
    ValueSet: http://hl7.org/fhir/ValueSet/fm-itemtype
    """
    URL = "http://hl7.org/fhir/ex-claimitemtype"
    EXPERIMENTAL = True

    """ A group of products and/or Services, amount ar the summary or detail level products and services.
    """
    group = "group"

    """ A billed product line item.
    """
    product = "product"

    """ A billed service line item.
    """
    service = "service"


class ClaimPayeeResourceType(CodeSystemValue):
    """ The type of Claim payee Resource

    URL: http://hl7.org/fhir/ex-payee-resource-type
    ValueSet: http://hl7.org/fhir/ValueSet/ex-payee-resource-type
    """
    URL = "http://hl7.org/fhir/ex-payee-resource-type"
    EXPERIMENTAL = False

    """ Organization resource
    """
    organization = "organization"

    """ Patient resource
    """
    patient = "patient"

    """ Practitioner resource
    """
    practitioner = "practitioner"

    """ RelatedPerson resource
    """
    relatedperson = "relatedperson"


class ClaimPayeeTypeCodes(CodeSystemValue):
    """ This value set includes sample Payee Type codes.

    URL: http://hl7.org/fhir/payeetype
    ValueSet: http://hl7.org/fhir/ValueSet/payeetype
    """
    URL = "http://hl7.org/fhir/payeetype"
    EXPERIMENTAL = True

    """ The subscriber (policy holder) will be reimbursed.
    """
    subscriber = "subscriber"

    """ Any benefit payable will be paid to the provider (Assignment of Benefit).
    """
    provider = "provider"

    """ Any benefit payable will be paid to a third party such as a guarrantor.
    """
    other = "other"


class ClaimProcessingCodes(CodeSystemValue):
    """ This value set includes Claim Processing Outcome codes.

    URL: http://hl7.org/fhir/remittance-outcome
    ValueSet: http://hl7.org/fhir/ValueSet/remittance-outcome
    """
    URL = "http://hl7.org/fhir/remittance-outcome"
    EXPERIMENTAL = True

    """ The Claim/Pre-authorization/Pre-determination has been received but processing has not begun.
    """
    queued = "queued"

    """ The processing has completed without errors
    """
    complete = "complete"

    """ One or more errors have been detected in the Claim
    """
    error = "error"

    """ No errors have been detected in the Claim and some of the adjudication has been performed.
    """
    partial = "partial"


class ClaimTypeCodes(CodeSystemValue):
    """ This value set includes Claim Type codes.

    URL: http://hl7.org/fhir/claim-type
    ValueSet: http://hl7.org/fhir/ValueSet/claim-type
    """
    URL = "http://hl7.org/fhir/claim-type"
    EXPERIMENTAL = True

    """ Hospital, clinic and typically inpatient claims.
    """
    institutional = "institutional"

    """ Dental, Denture and Hygiene claims.
    """
    oral = "oral"

    """ Pharmacy claims for goods and services.
    """
    pharmacy = "pharmacy"

    """ Typically outpatient claims from Physician, Psychological, Chiropractor, Physiotherapy, Speech Pathology,
	/// rehabilitative, consulting.
    """
    professional = "professional"

    """ Vision claims for professional services and products such as glasses and contact lenses.
    """
    vision = "vision"


class ClinicalImpressionStatus(CodeSystemValue):
    """ The workflow state of a clinical impression.

    URL: http://hl7.org/fhir/clinical-impression-status
    ValueSet: http://hl7.org/fhir/ValueSet/clinical-impression-status
    """
    URL = "http://hl7.org/fhir/clinical-impression-status"
    EXPERIMENTAL = False

    """ The assessment is still on-going and results are not yet final.
    """
    draft = "draft"

    """ The assessment is done and the results are final.
    """
    completed = "completed"

    """ This assessment was never actually done and the record is erroneous (e.g. Wrong patient).
    """
    enteredInError = "entered-in-error"


class CodeSearchSupport(CodeSystemValue):
    """ The degree to which the server supports the code search parameter on ValueSet, if it is supported

    URL: http://hl7.org/fhir/code-search-support
    ValueSet: http://hl7.org/fhir/ValueSet/code-search-support
    """
    URL = "http://hl7.org/fhir/code-search-support"
    EXPERIMENTAL = False

    """ The search for code on ValueSet only includes codes explicitly detailed on includes or expansions
    """
    explicit = "explicit"

    """ The search for code on ValueSet only includes all codes based on the expansion of the value set
    """
    all = "all"


class CodeSystemContentMode(CodeSystemValue):
    """ How much of the content of the code system - the concepts and codes it defines - are represented in a code system
resource

    URL: http://hl7.org/fhir/codesystem-content-mode
    ValueSet: http://hl7.org/fhir/ValueSet/codesystem-content-mode
    """
    URL = "http://hl7.org/fhir/codesystem-content-mode"
    EXPERIMENTAL = False

    """ None of the concepts defined by the code system are included in the code system resource
    """
    notPresent = "not-present"

    """ A few representative concepts are included in the code system resource
    """
    example = "example"

    """ A subset of the code system concepts are included in the code system resource
    """
    fragment = "fragment"

    """ All the concepts defined by the code system are included in the code system resource
    """
    complete = "complete"

    """ The resource doesn't define any new concepts; it just provides additional designations and properties to another
	/// code system
    """
    supplement = "supplement"


class CodeSystemHierarchyMeaning(CodeSystemValue):
    """ The meaning of the hierarchy of concepts in a code system

    URL: http://hl7.org/fhir/codesystem-hierarchy-meaning
    ValueSet: http://hl7.org/fhir/ValueSet/codesystem-hierarchy-meaning
    """
    URL = "http://hl7.org/fhir/codesystem-hierarchy-meaning"
    EXPERIMENTAL = False

    """ No particular relationship between the concepts can be assumed, except what can be determined by inspection of
	/// the definitions of the elements (possible reasons to use this: importing from a source where this is not
	/// defined, or where various parts of the hierarchy have different meanings)
    """
    groupedBy = "grouped-by"

    """ A hierarchy where the child concepts have an IS-A relationship with the parents - that is, all the properties of
	/// the parent are also true for its child concepts
    """
    isA = "is-a"

    """ Child elements list the individual parts of a composite whole (e.g. body site)
    """
    partOf = "part-of"

    """ Child concepts in the hierarchy may have only one parent, and there is a presumption that the code system is a
	/// "closed world" meaning all things must be in the hierarchy. This results in concepts such as "not otherwise
	/// classified."
    """
    classifiedWith = "classified-with"


class CommonTags(CodeSystemValue):
    """ Common Tag Codes defined by FHIR project

    URL: http://hl7.org/fhir/common-tags
    ValueSet: http://hl7.org/fhir/ValueSet/common-tags
    """
    URL = "http://hl7.org/fhir/common-tags"
    EXPERIMENTAL = True

    """ This request is intended to be acted upon, not merely stored
    """
    actionable = "actionable"


class CommunicationCategory(CodeSystemValue):
    """ Codes for general categories of communications such as alerts, instruction, etc.

    URL: http://hl7.org/fhir/communication-category
    ValueSet: http://hl7.org/fhir/ValueSet/communication-category
    """
    URL = "http://hl7.org/fhir/communication-category"
    EXPERIMENTAL = False

    """ The communication conveys an alert.
    """
    alert = "alert"

    """ The communication conveys a notification.
    """
    notification = "notification"

    """ The communication conveys a reminder.
    """
    reminder = "reminder"

    """ The communication conveys instruction.
    """
    instruction = "instruction"


class CommunicationNotDoneReason(CodeSystemValue):
    """ Codes for the reason why a communication was not done.

    URL: http://hl7.org/fhir/communication-not-done-reason
    ValueSet: http://hl7.org/fhir/ValueSet/communication-not-done-reason
    """
    URL = "http://hl7.org/fhir/communication-not-done-reason"
    EXPERIMENTAL = False

    """ The communication was not done due to an unknown reason.
    """
    unknown = "unknown"

    """ The communication was not done due to a system error.
    """
    systemError = "system-error"

    """ The communication was not done due to an invalid phone number.
    """
    invalidPhoneNumber = "invalid-phone-number"

    """ The communication was not done due to the recipient being unavailable.
    """
    recipientUnavailable = "recipient-unavailable"

    """ The communication was not done due to a family objection.
    """
    familyObjection = "family-objection"

    """ The communication was not done due to a patient objection.
    """
    patientObjection = "patient-objection"


class CommunicationTopic(CodeSystemValue):
    """ Codes describing the purpose or content of the communication.

    URL: http://hl7.org/fhir/communication-topic
    ValueSet: http://hl7.org/fhir/ValueSet/communication-topic
    """
    URL = "http://hl7.org/fhir/communication-topic"
    EXPERIMENTAL = False

    """ The purpose of the communication is a prescription refill request.
    """
    prescriptionRefillRequest = "prescription-refill-request"

    """ The purpose of the communication is a progress update.
    """
    progressUpdate = "progress-update"

    """ The purpose of the communication is to report labs.
    """
    reportLabs = "report-labs"

    """ The purpose of the communication is an appointment reminder.
    """
    appointmentReminder = "appointment-reminder"

    """ The purpose of the communication is a phone consult.
    """
    phoneConsult = "phone-consult"

    """ The purpose of the communication is a summary report.
    """
    summaryReport = "summary-report"


class CompartmentType(CodeSystemValue):
    """ Which compartment a compartment definition describes

    URL: http://hl7.org/fhir/compartment-type
    ValueSet: http://hl7.org/fhir/ValueSet/compartment-type
    """
    URL = "http://hl7.org/fhir/compartment-type"
    EXPERIMENTAL = False

    """ The compartment definition is for the patient compartment
    """
    patient = "Patient"

    """ The compartment definition is for the encounter compartment
    """
    encounter = "Encounter"

    """ The compartment definition is for the related-person compartment
    """
    relatedPerson = "RelatedPerson"

    """ The compartment definition is for the practitioner compartment
    """
    practitioner = "Practitioner"

    """ The compartment definition is for the device compartment
    """
    device = "Device"


class CompositeMeasureScoring(CodeSystemValue):
    """ The composite scoring method of the measure

    URL: http://hl7.org/fhir/composite-measure-scoring
    ValueSet: http://hl7.org/fhir/ValueSet/composite-measure-scoring
    """
    URL = "http://hl7.org/fhir/composite-measure-scoring"
    EXPERIMENTAL = False

    """ Opportunity scoring combines the scores from component measures by combining the numerators and denominators for
	/// each component
    """
    opportunity = "opportunity"

    """ All-or-nothing scoring includes an individual in the numerator of the composite measure if they are in the
	/// numerators of all of the component measures in which they are in the denominator
    """
    allOrNothing = "all-or-nothing"

    """ Linear scoring gives an individual a score based on the number of numerators in which they appear
    """
    linear = "linear"

    """ Weighted scoring gives an individual a score based on a weighted factor for each component numerator in which
	/// they appear
    """
    weighted = "weighted"


class CompositionAttestationMode(CodeSystemValue):
    """ The way in which a person authenticated a composition.

    URL: http://hl7.org/fhir/composition-attestation-mode
    ValueSet: http://hl7.org/fhir/ValueSet/composition-attestation-mode
    """
    URL = "http://hl7.org/fhir/composition-attestation-mode"
    EXPERIMENTAL = False

    """ The person authenticated the content in their personal capacity.
    """
    personal = "personal"

    """ The person authenticated the content in their professional capacity.
    """
    professional = "professional"

    """ The person authenticated the content and accepted legal responsibility for its content.
    """
    legal = "legal"

    """ The organization authenticated the content as consistent with their policies and procedures.
    """
    official = "official"


class CompositionStatus(CodeSystemValue):
    """ The workflow/clinical status of the composition.

    URL: http://hl7.org/fhir/composition-status
    ValueSet: http://hl7.org/fhir/ValueSet/composition-status
    """
    URL = "http://hl7.org/fhir/composition-status"
    EXPERIMENTAL = False

    """ This is a preliminary composition or document (also known as initial or interim). The content may be incomplete
	/// or unverified.
    """
    preliminary = "preliminary"

    """ This version of the composition is complete and verified by an appropriate person and no further work is
	/// planned. Any subsequent updates would be on a new version of the composition.
    """
    final = "final"

    """ The composition content or the referenced resources have been modified (edited or added to) subsequent to being
	/// released as "final" and the composition is complete and verified by an authorized person.
    """
    amended = "amended"

    """ The composition or document was originally created/issued in error, and this is an amendment that marks that the
	/// entire series should not be considered as valid.
    """
    enteredInError = "entered-in-error"


class ConceptMapEquivalence(CodeSystemValue):
    """ The degree of equivalence between concepts.

    URL: http://hl7.org/fhir/concept-map-equivalence
    ValueSet: http://hl7.org/fhir/ValueSet/concept-map-equivalence
    """
    URL = "http://hl7.org/fhir/concept-map-equivalence"
    EXPERIMENTAL = False

    """ The concepts are related to each other, and have at least some overlap in meaning, but the exact relationship is
	/// not known
    """
    relatedto = "relatedto"

    """ The definitions of the concepts mean the same thing (including when structural implications of meaning are
	/// considered) (i.e. extensionally identical).
    """
    equivalent = "equivalent"

    """ The definitions of the concepts are exactly the same (i.e. only grammatical differences) and structural
	/// implications of meaning are identical or irrelevant (i.e. intentionally identical).
    """
    equal = "equal"

    """ The target mapping is wider in meaning than the source concept.
    """
    wider = "wider"

    """ The target mapping subsumes the meaning of the source concept (e.g. the source is-a target).
    """
    subsumes = "subsumes"

    """ The target mapping is narrower in meaning than the source concept. The sense in which the mapping is narrower
	/// SHALL be described in the comments in this case, and applications should be careful when attempting to use these
	/// mappings operationally.
    """
    narrower = "narrower"

    """ The target mapping specializes the meaning of the source concept (e.g. the target is-a source).
    """
    specializes = "specializes"

    """ The target mapping overlaps with the source concept, but both source and target cover additional meaning, or the
	/// definitions are imprecise and it is uncertain whether they have the same boundaries to their meaning. The sense
	/// in which the mapping is inexact SHALL be described in the comments in this case, and applications should be
	/// careful when attempting to use these mappings operationally.
    """
    inexact = "inexact"

    """ There is no match for this concept in the target code system.
    """
    unmatched = "unmatched"

    """ This is an explicit assertion that there is no mapping between the source and target concept.
    """
    disjoint = "disjoint"


class ConceptMapGroupUnmappedMode(CodeSystemValue):
    """ Defines which action to take if there is no match in the group.

    URL: http://hl7.org/fhir/conceptmap-unmapped-mode
    ValueSet: http://hl7.org/fhir/ValueSet/conceptmap-unmapped-mode
    """
    URL = "http://hl7.org/fhir/conceptmap-unmapped-mode"
    EXPERIMENTAL = False

    """ Use the code as provided in the $translate request
    """
    provided = "provided"

    """ Use the code explicitly provided in the group.unmapped
    """
    fixed = "fixed"

    """ Use the map identified by the canonical URL in URL
    """
    otherMap = "other-map"


class ConditionCategoryCodes(CodeSystemValue):
    """ Preferred value set for Condition Categories.

    URL: http://hl7.org/fhir/condition-category
    ValueSet: http://hl7.org/fhir/ValueSet/condition-category
    """
    URL = "http://hl7.org/fhir/condition-category"
    EXPERIMENTAL = True

    """ An item on a problem list which can be managed over time and can be expressed by a practitioner (e.g. physician,
	/// nurse), patient, or related person.
    """
    problemListItem = "problem-list-item"

    """ A point in time diagnosis (e.g. from a physician or nurse) in context of an encounter.
    """
    encounterDiagnosis = "encounter-diagnosis"


class ConditionClinicalStatusCodes(CodeSystemValue):
    """ Preferred value set for Condition Clinical Status.

    URL: http://hl7.org/fhir/condition-clinical
    ValueSet: http://hl7.org/fhir/ValueSet/condition-clinical
    """
    URL = "http://hl7.org/fhir/condition-clinical"
    EXPERIMENTAL = True

    """ The subject is currently experiencing the symptoms of the condition or there is evidence of the condition.
    """
    active = "active"

    """ The subject is experiencing a re-occurence or repeating of a previously resolved condition, e.g. urinary tract
	/// infection, pancreatitis, cholangitis, conjunctivitis.
    """
    recurrence = "recurrence"

    """ The subject is experiencing a return of a condition, or signs and symptoms after a period of improvement or
	/// remission, e.g. relapse of cancer, multiple sclerosis, rheumatoid arthritis, systemic lupus erythematosus,
	/// bipolar disorder, [psychotic relapse of] schizophrenia, etc.
    """
    relapse = "relapse"

    """ The subject's condition is adequately or well managed such that the recommended evidence-based clinical outcome
	/// targets are met.
    """
    wellControlled = "well-controlled"

    """ The subject's condition is inadequately/poorly managed such that the recommended evidence-based clinical outcome
	/// targets are not met.
    """
    poorlyControlled = "poorly-controlled"

    """ The subject is no longer experiencing the symptoms of the condition or there is no longer evidence of the
	/// condition.
    """
    inactive = "inactive"

    """ The subject is no longer experiencing the symptoms of the condition, but there is a risk of the symptoms
	/// returning.
    """
    remission = "remission"

    """ The subject is no longer experiencing the symptoms of the condition and there is a negligible perceived risk of
	/// the symptoms returning.
    """
    resolved = "resolved"


class ConditionState(CodeSystemValue):
    """ Enumeration indicating whether the condition is currently active, inactive, or has been resolved.

    URL: http://hl7.org/fhir/condition-state
    ValueSet: http://hl7.org/fhir/ValueSet/condition-state
    """
    URL = "http://hl7.org/fhir/condition-state"
    EXPERIMENTAL = False

    """ The condition is active.
    """
    active = "active"

    """ The condition is inactive, but not resolved.
    """
    inactive = "inactive"

    """ The condition is resolved.
    """
    resolved = "resolved"


class ConditionVerificationStatus(CodeSystemValue):
    """ The verification status to support or decline the clinical status of the condition or diagnosis.

    URL: http://hl7.org/fhir/condition-ver-status
    ValueSet: http://hl7.org/fhir/ValueSet/condition-ver-status
    """
    URL = "http://hl7.org/fhir/condition-ver-status"
    EXPERIMENTAL = False

    """ There is not sufficient diagnostic and/or clinical evidence to treat this as a confirmed condition.
    """
    unconfirmed = "unconfirmed"

    """ This is a tentative diagnosis - still a candidate that is under consideration.
    """
    provisional = "provisional"

    """ One of a set of potential (and typically mutually exclusive) diagnoses asserted to further guide the diagnostic
	/// process and preliminary treatment.
    """
    differential = "differential"

    """ There is sufficient diagnostic and/or clinical evidence to treat this as a confirmed condition.
    """
    confirmed = "confirmed"

    """ This condition has been ruled out by diagnostic and clinical evidence.
    """
    refuted = "refuted"

    """ The statement was entered in error and is not valid.
    """
    enteredInError = "entered-in-error"


class ConditionalDeleteStatus(CodeSystemValue):
    """ A code that indicates how the server supports conditional delete.

    URL: http://hl7.org/fhir/conditional-delete-status
    ValueSet: http://hl7.org/fhir/ValueSet/conditional-delete-status
    """
    URL = "http://hl7.org/fhir/conditional-delete-status"
    EXPERIMENTAL = False

    """ No support for conditional deletes.
    """
    notSupported = "not-supported"

    """ Conditional deletes are supported, but only single resources at a time.
    """
    single = "single"

    """ Conditional deletes are supported, and multiple resources can be deleted in a single interaction.
    """
    multiple = "multiple"


class ConditionalReadStatus(CodeSystemValue):
    """ A code that indicates how the server supports conditional read.

    URL: http://hl7.org/fhir/conditional-read-status
    ValueSet: http://hl7.org/fhir/ValueSet/conditional-read-status
    """
    URL = "http://hl7.org/fhir/conditional-read-status"
    EXPERIMENTAL = False

    """ No support for conditional reads
    """
    notSupported = "not-supported"

    """ Conditional reads are supported, but only with the If-Modified-Since HTTP Header.
    """
    modifiedSince = "modified-since"

    """ Conditional reads are supported, but only with the If-None-Match HTTP Header.
    """
    notMatch = "not-match"

    """ Conditional reads are supported, with both If-Modified-Since and If-None-Match HTTP Headers.
    """
    fullSupport = "full-support"


class ConformanceExpectation(CodeSystemValue):
    """ Indicates the degree of adherence to a specified behavior or capability expected for a system to be deemed conformant
with a specification.

    URL: http://hl7.org/fhir/conformance-expectation
    ValueSet: http://hl7.org/fhir/ValueSet/conformance-expectation
    """
    URL = "http://hl7.org/fhir/conformance-expectation"
    EXPERIMENTAL = False

    """ Support for the specified capability is required to be considered conformant.
    """
    SHALL = "SHALL"

    """ Support for the specified capability is strongly encouraged, and failure to support it should only occur after
	/// careful consideration.
    """
    SHOULD = "SHOULD"

    """ Support for the specified capability is not necessary to be considered conformant, and the requirement should be
	/// considered strictly optional.
    """
    MAY = "MAY"

    """ Support for the specified capability is strongly discouraged and should occur only after careful consideration.
    """
    SHOULDNOT = "SHOULD-NOT"


class ConsentActionCodes(CodeSystemValue):
    """ This value set includes sample Consent Action codes.

    URL: http://hl7.org/fhir/consentaction
    ValueSet: http://hl7.org/fhir/ValueSet/consent-action
    """
    URL = "http://hl7.org/fhir/consentaction"
    EXPERIMENTAL = True

    """ Gather/acquire information by an entity to achieve a stated purpose
    """
    collect = "collect"

    """ Provide an entity access to information to achieve a stated purpose
    """
    access = "access"

    """ Use of stored information by an entity fo the stated purpose
    """
    use = "use"

    """ Release / transfer of information to an entity
    """
    disclose = "disclose"

    """ Allowing an entity to correct a patient's information
    """
    correct = "correct"


class ConsentCategoryCodes(CodeSystemValue):
    """ This value set includes sample Consent Directive Type codes, including several consent directive related LOINC codes;
HL7 VALUE SET: ActConsentType(2.16.840.1.113883.1.11.19897); examples of US realm consent directive legal descriptions
and references to online and/or downloadable forms such as the SSA-827 Authorization to Disclose Information to the
Social Security Administration; and other anticipated consent directives related to participation in a clinical trial,
medical procedures, reproductive procedures; health care directive (Living Will); advance directive, do not resuscitate
(DNR); Physician Orders for Life-Sustaining Treatment (POLST)

    URL: http://hl7.org/fhir/consentcategorycodes
    ValueSet: http://hl7.org/fhir/ValueSet/consent-category
    """
    URL = "http://hl7.org/fhir/consentcategorycodes"
    EXPERIMENTAL = True

    """ Any instructions, written or given verbally by a patient to a health care provider in anticipation of potential
	/// need for medical treatment. [2005 Honor My Wishes]
    """
    acd = "acd"

    """ A legal document, signed by both the patient and their provider, stating a desire not to have CPR initiated in
	/// case of a cardiac event. Note: This form was replaced in 2003 with the Physician Orders for Life-Sustaining
	/// Treatment [POLST].
    """
    dnr = "dnr"

    """ Opt-in to disclosure of health information for emergency only consent directive. Comment: This general consent
	/// directive specifically limits disclosure of health information for purpose of emergency treatment. Additional
	/// parameters may further limit the disclosure to specific users, roles, duration, types of information, and impose
	/// uses obligations. [ActConsentDirective (2.16.840.1.113883.1.11.20425)]
    """
    emrgonly = "emrgonly"

    """ Patient's document telling patient's health care provider what the patient wants or does not want if the patient
	/// is diagnosed as being terminally ill and in a persistent vegetative state or in a permanently unconscious
	/// condition.[2005 Honor My Wishes]
    """
    hcd = "hcd"

    """ Acknowledgement of custodian notice of privacy practices. Usage Notes: This type of consent directive
	/// acknowledges a custodian's notice of privacy practices including its permitted collection, access, use and
	/// disclosure of health information to users and for purposes of use specified. [ActConsentDirective
	/// (2.16.840.1.113883.1.11.20425)]
    """
    npp = "npp"

    """ The Physician Order for Life-Sustaining Treatment form records a person's health care wishes for end of life
	/// emergency treatment and translates them into an order by the physician. It must be reviewed and signed by both
	/// the patient and the physician, Advanced Registered Nurse Practitioner or Physician Assistant. [2005 Honor My
	/// Wishes] Comment: Opt-in Consent Directive with restrictions.
    """
    polst = "polst"

    """ Consent to have healthcare information in an electronic health record accessed for research purposes. [VALUE
	/// SET: ActConsentType (2.16.840.1.113883.1.11.19897)]
    """
    research = "research"

    """ Consent to have de-identified healthcare information in an electronic health record that is accessed for
	/// research purposes, but without consent to re-identify the information under any circumstance. [VALUE SET:
	/// ActConsentType (2.16.840.1.113883.1.11.19897)
    """
    rsdid = "rsdid"

    """ Consent to have de-identified healthcare information in an electronic health record that is accessed for
	/// research purposes re-identified under specific circumstances outlined in the consent. [VALUE SET: ActConsentType
	/// (2.16.840.1.113883.1.11.19897)]
    """
    rsreid = "rsreid"


class ConsentDataMeaning(CodeSystemValue):
    """ How a resource reference is interpreted when testing consent restrictions

    URL: http://hl7.org/fhir/consent-data-meaning
    ValueSet: http://hl7.org/fhir/ValueSet/consent-data-meaning
    """
    URL = "http://hl7.org/fhir/consent-data-meaning"
    EXPERIMENTAL = False

    """ The consent applies directly to the instance of the resource
    """
    instance = "instance"

    """ The consent applies directly to the instance of the resource and instances it refers to
    """
    related = "related"

    """ The consent applies directly to the instance of the resource and instances that refer to it
    """
    dependents = "dependents"

    """ The consent applies to instances of resources that are authored by
    """
    authoredby = "authoredby"


class ConsentPolicyRuleCodes(CodeSystemValue):
    """ This value set includes sample Regulatory consent policy types from the US and other regions.

    URL: http://hl7.org/fhir/consentpolicycodes
    ValueSet: http://hl7.org/fhir/ValueSet/consent-policy
    """
    URL = "http://hl7.org/fhir/consentpolicycodes"
    EXPERIMENTAL = True

    """ 45 CFR part 46 Â§46.116 General requirements for informed consent; and Â§46.117 Documentation of informed
	/// consent. https://www.gpo.gov/fdsys/pkg/FR-2017-01-19/pdf/2017-01058.pdf
    """
    cric = "cric"

    """ The consent to the performance of a medical or surgical procedure by a physician licensed to practice medicine
	/// and surgery, a licensed advanced practice nurse, or a licensed physician assistant executed by a married person
	/// who is a minor, by a parent who is a minor, by a pregnant woman who is a minor, or by any person 18 years of age
	/// or older, is not voidable because of such minority, and, for such purpose, a married person who is a minor, a
	/// parent who is a minor, a pregnant woman who is a minor, or any person 18 years of age or older, is deemed to
	/// have the same legal capacity to act and has the same powers and obligations as has a person of legal age.
	/// Consent by Minors to Medical Procedures Act. (410 ILCS 210/0.01) (from Ch. 111, par. 4500) Sec. 0.01. Short
	/// title. This Act may be cited as the Consent by Minors to Medical Procedures Act. (Source: P.A. 86-1324.)
	/// http://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=1539&ChapterID=35
    """
    illinoisMinorProcedure = "illinois-minor-procedure"

    """ HIPAA 45 CFR Section 164.508 Uses and disclosures for which an authorization is required. (a) Standard:
	/// Authorizations for uses and disclosures. (1) Authorization required: General rule. Except as otherwise permitted
	/// or required by this subchapter, a covered entity SJALL not use or disclose protected health information without
	/// an authorization that is valid under this section. When a covered entity obtains or receives a valid
	/// authorization for its use or disclosure of protected health information, such use or disclosure must be
	/// consistent with such authorization. Usage Note: Authorizations governed under this regulation meet the
	/// definition of an opt in class of consent directive.
    """
    hipaaAuth = "hipaa-auth"

    """ Â§ 164.520  Notice of privacy practices for protected health information. (1) Right to notice. Except as
	/// provided by paragraph (a)(2) or (3) of this section, an individual has a right to adequate notice of the uses
	/// and disclosures of protected health information that may be made by the covered entity, and of the individual's
	/// rights and the covered entity's legal duties with respect to protected health information. Usage Note:
	/// Restrictions governed under this regulation meet the definition of an implied with an opportunity to dissent
	/// class of consent directive.
    """
    hipaaNpp = "hipaa-npp"

    """ HIPAA 45 CFR Â§ 164.510 - Uses and disclosures requiring an opportunity for the individual to agree or to
	/// object. A covered entity may use or disclose protected health information, provided that the individual is
	/// informed in advance of the use or disclosure and has the opportunity to agree to or prohibit or restrict the use
	/// or disclosure, in accordance with the applicable requirements of this section. The covered entity may orally
	/// inform the individual of and obtain the individual's oral agreement or objection to a use or disclosure
	/// permitted by this section. Usage Note: Restrictions governed under this regulation meet the definition of an opt
	/// out with exception class of consent directive.
    """
    hipaaRestrictions = "hipaa-restrictions"

    """ HIPAA 45 CFR Â§ 164.508 - Uses and disclosures for which an authorization is required. (a) Standard:
	/// Authorizations for uses and disclosures. (3) Compound authorizations. An authorization for use or disclosure of
	/// protected health information SHALL not be combined with any other document to create a compound authorization,
	/// except as follows: (i) An authorization for the use or disclosure of protected health information for a research
	/// study may be combined with any other type of written permission for the same or another research study. This
	/// exception includes combining an authorization for the use or disclosure of protected health information for a
	/// research study with another authorization for the same research study, with an authorization for the creation or
	/// maintenance of a research database or repository, or with a consent to participate in research. Where a covered
	/// health care provider has conditioned the provision of research-related treatment on the provision of one of the
	/// authorizations, as permitted under paragraph (b)(4)(i) of this section, any compound authorization created under
	/// this paragraph must clearly differentiate between the conditioned and unconditioned components and provide the
	/// individual with an opportunity to opt in to the research activities described in the unconditioned
	/// authorization. Usage Notes: See HHS http://www.hhs.gov/hipaa/for-professionals/special-
	/// topics/research/index.html and OCR http://www.hhs.gov/hipaa/for-professionals/special-topics/research/index.html
    """
    hipaaResearch = "hipaa-research"

    """ HIPAA 45 CFR Â§ 164.522(a) Right To Request a Restriction of Uses and Disclosures. (vi) A covered entity must
	/// agree to the request of an individual to restrict disclosure of protected health information about the
	/// individual to a health plan if: (A) The disclosure is for the purpose of carrying out payment or health care
	/// operations and is not otherwise required by law; and (B) The protected health information pertains solely to a
	/// health care item or service for which the individual, or person other than the health plan on behalf of the
	/// individual, has paid the covered entity in full. Usage Note: Restrictions governed under this regulation meet
	/// the definition of an opt out with exception class of consent directive. Opt out is limited to disclosures to a
	/// payer for payment and operations purpose of use. See HL7 HIPAA Self-Pay code in ActPrivacyLaw
	/// (2.16.840.1.113883.1.11.20426).
    """
    hipaaSelfPay = "hipaa-self-pay"

    """ On January 1, 2015, the Michigan Department of Health and Human Services (MDHHS) released a standard consent
	/// form for the sharing of health information specific to behavioral health and substance use treatment in
	/// accordance with Public Act 129 of 2014. In Michigan, while providers are not required to use this new standard
	/// form (MDHHS-5515), they are required to accept it. Note: Form is available at http://www.michigan.gov/documents/
	/// mdhhs/Consent_to_Share_Behavioral_Health_Information_for_Care_Coordination_Purposes_548835_7.docx For more
	/// information see
	/// http://www.michigan.gov/documents/mdhhs/Behavioral_Health_Consent_Form_Background_Information_548864_7.pdf
    """
    mdhhs5515 = "mdhhs-5515"

    """ The New York State Surgical and Invasive Procedure Protocol (NYSSIPP) applies to all operative and invasive
	/// procedures including endoscopy, general surgery or interventional radiology. Other procedures that involve
	/// puncture or incision of the skin, or insertion of an instrument or foreign material into the body are within the
	/// scope of the protocol. This protocol also applies to those anesthesia procedures either prior to a surgical
	/// procedure or independent of a surgical procedure such as spinal facet blocks. Example: Certain 'minor'
	/// procedures such as venipuncture, peripheral IV placement, insertion of nasogastric tube and foley catheter
	/// insertion are not within the scope of the protocol. From
	/// http://www.health.ny.gov/professionals/protocols_and_guidelines/surgical_and_invasive_procedure/nyssipp_faq.htm
	/// Note: HHC 100B-1 Form is available at
	/// http://www.downstate.edu/emergency_medicine/documents/Consent_CT_with_contrast.pdf
    """
    nyssipp = "nyssipp"

    """ VA Form 10-0484 Revocation for Release of Individually-Identifiable Health Information enables a veteran to
	/// revoke authorization for the VA to release specified copies of individually-identifiable health information with
	/// the non-VA health care provider organizations participating in the eHealth Exchange and partnering with VA.
	/// Comment: Opt-in Consent Directive with status = rescinded (aka 'revoked'). Note: Form is available at
	/// http://www.va.gov/vaforms/medical/pdf/vha-10-0484-fill.pdf
    """
    va100484 = "va-10-0484"

    """ VA Form 10-0485 Request for and Authorization to Release Protected Health Information to eHealth Exchange
	/// enables a veteran to request and authorize a VA health care facility to release protected health information
	/// (PHI) for treatment purposes only to the communities that are participating in the eHealth Exchange, VLER
	/// Directive, and other Health Information Exchanges with who VA has an agreement. This information may consist of
	/// the diagnosis of Sickle Cell Anemia, the treatment of or referral for Drug Abuse, treatment of or referral for
	/// Alcohol Abuse or the treatment of or testing for infection with Human Immunodeficiency Virus. This authorization
	/// covers the diagnoses that I may have upon signing of the authorization and the diagnoses that I may acquire in
	/// the future including those protected by 38 U.S.C. 7332. Comment: Opt-in Consent Directive. Note: Form is
	/// available at http://www.va.gov/vaforms/medical/pdf/10-0485-fill.pdf
    """
    va100485 = "va-10-0485"

    """ VA Form 10-5345 Request for and Authorization to Release Medical Records or Health Information enables a veteran
	/// to request and authorize the VA to release specified copies of protected health information (PHI), such as
	/// hospital summary or outpatient treatment notes, which may include information about conditions governed under
	/// Title 38 Section 7332 (drug abuse, alcoholism or alcohol abuse, testing for or infection with HIV, and sickle
	/// cell anemia). Comment: Opt-in Consent Directive. Note: Form is available at
	/// http://www.va.gov/vaforms/medical/pdf/vha-10-5345-fill.pdf
    """
    va105345 = "va-10-5345"

    """ VA Form 10-5345a Individuals' Request for a Copy of Their Own Health Information enables a veteran to request
	/// and authorize the VA to release specified copies of protected health information (PHI), such as hospital summary
	/// or outpatient treatment notes. Note: Form is available at
	/// http://www.va.gov/vaforms/medical/pdf/vha-10-5345a-fill.pdf
    """
    va105345a = "va-10-5345a"

    """ VA Form 10-5345a-MHV Individualâ€™s Request for a Copy of their own health information from MyHealtheVet enables
	/// a veteran to receive a copy of all available personal health information to be delivered through the veteranâ€™s
	/// My HealtheVet account. Note: Form is available at http://www.va.gov/vaforms/medical/pdf/vha-10-5345a-MHV-
	/// fill.pdf
    """
    va105345aMHV = "va-10-5345a-MHV"

    """ VA Form 10-10116 Revocation of Authorization for Use and Release of Individually Identifiable Health Information
	/// for Veterans Health Administration Research. Comment: Opt-in with Restriction Consent Directive with status =
	/// 'completed'. Note: Form is available at
	/// http://www.northerncalifornia.va.gov/northerncalifornia/services/rnd/docs/vha-10-10116.pdf
    """
    va1010116 = "va-10-10116"

    """ VA Form 21-4142 (Authorization and Consent to Release Information to the Department of Veterans Affairs (VA)
	/// enables a veteran to authorize the US Veterans Administration [VA] to request veteranâ€™s health information
	/// from non-VA providers. Aka VA Compensation Application Note: Form is available at
	/// http://www.vba.va.gov/pubs/forms/VBA-21-4142-ARE.pdf . For additional information regarding VA Form 21-4142,
	/// refer to the following website: www.benefits.va.gov/compensation/consent_privateproviders
    """
    va214142 = "va-21-4142"

    """ SA Form SSA-827 (Authorization to Disclose Information to the Social Security Administration (SSA)). Form is
	/// available at https://www.socialsecurity.gov/forms/ssa-827-inst-sp.pdf
    """
    ssa827 = "ssa-827"

    """ Michigan DCH-3927 Consent to Share Behavioral Health Information for Care Coordination Purposes, which combines
	/// 42 CFR Part 2 and Michigan Mental Health Code, Act 258 of 1974. Form is available at
	/// http://www.michigan.gov/documents/mdch/DCH-3927_Consent_to_Share_Health_Information_477005_7.docx
    """
    dch3927 = "dch-3927"

    """ Squaxin Indian HIPAA and 42 CFR Part 2 Consent for Release and Exchange of Confidential Information, which
	/// permits consenter to select healthcare record type and types of treatment purposes.  This consent requires
	/// disclosers and recipients to comply with 42 C.F.R. Part 2, and HIPAA 45 C.F.R. parts 160 and 164. It includes
	/// patient notice of the refrain policy not to disclose without consent, and revocation rights.
	/// https://www.ncsacw.samhsa.gov/files/SI_ConsentForReleaseAndExchange.PDF
    """
    squaxin = "squaxin"

    """ LSP (National Exchange Point) requires that providers, hospitals and pharmacy obtain explicit permission [opt-
	/// in] from healthcare consumers to submit and retrieve all or only some of a subject of care’s health information
	/// collected by the LSP for purpose of treatment, which can be revoked.  Without permission, a provider cannot
	/// access LSP information even in an emergency. The LSP provides healthcare consumers with accountings of
	/// disclosures. https://www.vzvz.nl/uploaded/FILES/htmlcontent/Formulieren/TOESTEMMINGSFORMULIER.pdf,
	/// https://www.ikgeeftoestemming.nl/en, https://www.ikgeeftoestemming.nl/en/registration/find-healthcare-provider
    """
    nlLsp = "nl-lsp"

    """ Pursuant to Sec. 2 no. 9 Health Telematics Act 2012, ELGA Health Data ( “ELGA-Gesundheitsdaten”) = Medical
	/// documents. Austria opted for an opt-out approach. This means that a person is by default ‘ELGA participant’
	/// unless he/she objects. ELGA participants have the following options: General opt out: No participation in ELGA,
	/// Partial opt-out: No participation in a particular ELGA application, e.g. eMedication and Case-specific opt-out:
	/// No participation in ELGA only regarding a particular case/treatment. There is the possibility to opt-in again.
	/// ELGA participants can also exclude the access of a particular ELGA healthcare provider to a particular piece of
	/// or all of their ELGA data. http://ec.europa.eu/health/ehealth/docs/laws_austria_en.pdf
    """
    atElga = "at-elga"

    """ Guidance and template form https://privacyruleandresearch.nih.gov/pdf/authorization.pdf
    """
    nihHipaa = "nih-hipaa"

    """ see http://ctep.cancer.gov/protocolDevelopment/docs/Informed_Consent_Template.docx
    """
    nci = "nci"

    """ Global Rare Disease Patient Registry and Data Repository (GRDR) consent is an agreement of a healthcare consumer
	/// to permit collection, access, use and disclosure of de-identified rare disease information and collection of
	/// bio-specimens, medical information, family history and other related information from patients to permit the
	/// registry collection of health and genetic information, and specimens for pseudonymized disclosure for research
	/// purpose of use. https://rarediseases.info.nih.gov/files/informed_consent_template.pdf
    """
    nihGrdr = "nih-grdr"

    """ NIH Authorization for the Release of Medical Information is a patient’s consent for the National Institutes of
	/// Health Clinical Center to release medical information to care providers, which can be revoked. Note: Consent
	/// Form available @ http://cc.nih.gov/participate/_pdf/NIH-527.pdf
    """
    nih527 = "nih-527"

    """ Global Alliance for Genomic Health Data Sharing Consent Form is an example of the GA4GH Population origins and
	/// ancestry research consent form. Consenters agree to permitting a specified research project to collect ancestry
	/// and genetic information in controlled-access databases, and to allow other researchers to use deidentified
	/// information from those databases.
	/// http://www.commonaccord.org/index.php?action=doc&file=Wx/org/genomicsandhealth/REWG/Demo/Roberta_Robinson_US
    """
    ga4gh = "ga4gh"


class ConsentProvisionType(CodeSystemValue):
    """ How a rule statement is applied, such as adding additional consent or removing consent

    URL: http://hl7.org/fhir/consent-provision-type
    ValueSet: http://hl7.org/fhir/ValueSet/consent-provision-type
    """
    URL = "http://hl7.org/fhir/consent-provision-type"
    EXPERIMENTAL = False

    """ Consent is denied for actions meeting these rules
    """
    deny = "deny"

    """ Consent is provided for actions meeting these rules
    """
    permit = "permit"


class ConsentScopeCodes(CodeSystemValue):
    """ This value set includes the four Consent scope codes.

    URL: http://hl7.org/fhir/consentscope
    ValueSet: http://hl7.org/fhir/ValueSet/consent-scope
    """
    URL = "http://hl7.org/fhir/consentscope"
    EXPERIMENTAL = True

    """ Actions to be taken if they are no longer able to make decisions for themselves
    """
    adr = "adr"

    """ Consent to participate in research protocol and information sharing required
    """
    research = "research"

    """ Agreement to collect, access, use or disclose (share) information
    """
    patientPrivacy = "patient-privacy"

    """ Consent to undergo a specific treatment
    """
    treatment = "treatment"


class ConstraintSeverity(CodeSystemValue):
    """ SHALL applications comply with this constraint?

    URL: http://hl7.org/fhir/constraint-severity
    ValueSet: http://hl7.org/fhir/ValueSet/constraint-severity
    """
    URL = "http://hl7.org/fhir/constraint-severity"
    EXPERIMENTAL = False

    """ If the constraint is violated, the resource is not conformant.
    """
    error = "error"

    """ If the constraint is violated, the resource is conformant, but it is not necessarily following best practice.
    """
    warning = "warning"


class ContactEntityType(CodeSystemValue):
    """ This example value set defines a set of codes that can be used to indicate the purpose for which you would contact a
contact party.

    URL: http://hl7.org/fhir/contactentity-type
    ValueSet: http://hl7.org/fhir/ValueSet/contactentity-type
    """
    URL = "http://hl7.org/fhir/contactentity-type"
    EXPERIMENTAL = True

    """ Contact details for information regarding to billing/general finance enquiries.
    """
    BILL = "BILL"

    """ Contact details for administrative enquiries.
    """
    ADMIN = "ADMIN"

    """ Contact details for issues related to Human Resources, such as staff matters, OH&S etc.
    """
    HR = "HR"

    """ Contact details for dealing with issues related to insurance claims/adjudication/payment.
    """
    PAYOR = "PAYOR"

    """ Generic information contact for patients.
    """
    PATINF = "PATINF"

    """ Dedicated contact point for matters relating to press enquiries.
    """
    PRESS = "PRESS"


class ContactPointSystem(CodeSystemValue):
    """ Telecommunications form for contact point

    URL: http://hl7.org/fhir/contact-point-system
    ValueSet: http://hl7.org/fhir/ValueSet/contact-point-system
    """
    URL = "http://hl7.org/fhir/contact-point-system"
    EXPERIMENTAL = False

    """ The value is a telephone number used for voice calls. Use of full international numbers starting with + is
	/// recommended to enable automatic dialing support but not required.
    """
    phone = "phone"

    """ The value is a fax machine. Use of full international numbers starting with + is recommended to enable automatic
	/// dialing support but not required.
    """
    fax = "fax"

    """ The value is an email address.
    """
    email = "email"

    """ The value is a pager number. These may be local pager numbers that are only usable on a particular pager system.
    """
    pager = "pager"

    """ A contact that is not a phone, fax, pager or email address and is expressed as a URL.  This is intended for
	/// various personal contacts including blogs, Skype, Twitter, Facebook, etc. Do not use for email addresses.
    """
    url = "url"

    """ A contact that can be used for sending an sms message (e.g. mobile phones, some landlines)
    """
    sms = "sms"

    """ A contact that is not a phone, fax, page or email address and is not expressible as a URL.  E.g. Internal mail
	/// address.  This SHOULD NOT be used for contacts that are expressible as a URL (e.g. Skype, Twitter, Facebook,
	/// etc.)  Extensions may be used to distinguish "other" contact types.
    """
    other = "other"


class ContactPointUse(CodeSystemValue):
    """ Use of contact point

    URL: http://hl7.org/fhir/contact-point-use
    ValueSet: http://hl7.org/fhir/ValueSet/contact-point-use
    """
    URL = "http://hl7.org/fhir/contact-point-use"
    EXPERIMENTAL = False

    """ A communication contact point at a home; attempted contacts for business purposes might intrude privacy and
	/// chances are one will contact family or other household members instead of the person one wishes to call.
	/// Typically used with urgent cases, or if no other contacts are available.
    """
    home = "home"

    """ An office contact point. First choice for business related contacts during business hours.
    """
    work = "work"

    """ A temporary contact point. The period can provide more detailed information.
    """
    temp = "temp"

    """ This contact point is no longer in use (or was never correct, but retained for records).
    """
    old = "old"

    """ A telecommunication device that moves and stays with its owner. May have characteristics of all other use codes,
	/// suitable for urgent matters, not the first choice for routine business.
    """
    mobile = "mobile"


class ContainerCap(CodeSystemValue):
    """ Color of the container cap

    URL: http://hl7.org/fhir/container-cap
    ValueSet: http://hl7.org/fhir/ValueSet/container-cap
    """
    URL = "http://hl7.org/fhir/container-cap"
    EXPERIMENTAL = False

    """ red cap
    """
    red = "red"

    """ yellow cap
    """
    yellow = "yellow"

    """ grey cap
    """
    grey = "grey"

    """ violet cap
    """
    violet = "violet"

    """ blue cap
    """
    blue = "blue"

    """ black cap
    """
    black = "black"

    """ green cap
    """
    green = "green"


class ContractActionCodes(CodeSystemValue):
    """ This value set includes sample Contract Action codes.

    URL: http://www.hl7.org/fhir/contractaction
    ValueSet: http://hl7.org/fhir/ValueSet/contract-action
    """
    URL = "http://www.hl7.org/fhir/contractaction"
    EXPERIMENTAL = True

    """ Definition for Action A
    """
    actionA = "action-a"

    """ Definition for Action B
    """
    actionB = "action-b"


class ContractActorRoleCodes(CodeSystemValue):
    """ This value set includes sample Contract Actor Role codes.

    URL: http://www.hl7.org/fhir/contractactorrole
    ValueSet: http://hl7.org/fhir/ValueSet/contract-actorrole
    """
    URL = "http://www.hl7.org/fhir/contractactorrole"
    EXPERIMENTAL = True

    """ Someone who provides health care related services to people or animals including both clinical and support
	/// services.
    """
    practitioner = "practitioner"

    """ A receiver, human or animal, of health care related goods and services.
    """
    patient = "patient"


class ContractContentDerivationCodes(CodeSystemValue):
    """ This is an example set of Content Derivative type codes, which represent the minimal content derived from the basal
information source at a specific stage in its lifecycle, which is sufficient to manage that source information, for
example, in a repository, registry, processes and workflows, for making access control decisions, and providing query
responses.

    URL: http://hl7.org/fhir/contract-content-derivative
    ValueSet: http://hl7.org/fhir/ValueSet/contract-content-derivative
    """
    URL = "http://hl7.org/fhir/contract-content-derivative"
    EXPERIMENTAL = True

    """ Content derivative that conveys sufficient information needed to register the source basal content from which it
	/// is derived.  This derivative content may be used to register the basal content as it changes status in its
	/// lifecycle.  For example, content registration may occur when the basal content is created, updated, inactive, or
	/// deleted.
    """
    registration = "registration"

    """ A content derivative that conveys sufficient information to locate and retrieve the content.
    """
    retrieval = "retrieval"

    """ Content derivative that has less than full fidelity to the basal information source from which it was
	/// 'transcribed'. It provides recipients with the full content representation they may require for compliance
	/// purposes, and typically include a reference to or an attached unstructured representation for recipients needing
	/// an exact copy of the legal agreement.
    """
    statement = "statement"

    """ A Content Derivative that conveys sufficient information to determine the authorized entities with which the
	/// content may be shared.
    """
    shareable = "shareable"


class ContractDataMeaning(CodeSystemValue):
    """ How a resource reference is interpreted when evaluating contract offers

    URL: http://hl7.org/fhir/contract-data-meaning
    ValueSet: http://hl7.org/fhir/ValueSet/contract-data-meaning
    """
    URL = "http://hl7.org/fhir/contract-data-meaning"
    EXPERIMENTAL = False

    """ The consent applies directly to the instance of the resource
    """
    instance = "instance"

    """ The consent applies directly to the instance of the resource and instances it refers to
    """
    related = "related"

    """ The consent applies directly to the instance of the resource and instances that refer to it
    """
    dependents = "dependents"

    """ The consent applies to instances of resources that are authored by
    """
    authoredby = "authoredby"


class ContractResourceStatusCodes(CodeSystemValue):
    """ This value set contract specific codes for status.

    URL: http://hl7.org/fhir/contract-status
    ValueSet: http://hl7.org/fhir/ValueSet/contract-status
    """
    URL = "http://hl7.org/fhir/contract-status"
    EXPERIMENTAL = True

    """ Contract is augmented with additional information to correct errors in a predecessor or to updated values in a
	/// predecessor. Usage: Contract altered within effective time. Precedence Order = 9. Comparable FHIR and v.3 status
	/// codes: revised; replaced.
    """
    amended = "amended"

    """ Contract is augmented with additional information that was missing from a predecessor Contract. Usage: Contract
	/// altered within effective time. Precedence Order = 9. Comparable FHIR and v.3 status codes: updated, replaced.
    """
    appended = "appended"

    """ Contract is terminated due to failure of the Grantor and/or the Grantee to fulfil one or more contract
	/// provisions. Usage: Abnormal contract termination. Precedence Order = 10. Comparable FHIR and v.3 status codes:
	/// stopped; failed; aborted.
    """
    cancelled = "cancelled"

    """ Contract is pended to rectify failure of the Grantor or the Grantee to fulfil contract provision(s). E.g.,
	/// Grantee complaint about Grantor's failure to comply with contract provisions. Usage: Contract pended. Precedence
	/// Order = 7.Comparable FHIR and v.3 status codes: on hold; pended; suspended.
    """
    disputed = "disputed"

    """ Contract was created in error. No Precedence Order.  Status may be applied to a Contract with any status.
    """
    enteredInError = "entered-in-error"

    """ Contract execution pending; may be executed when either the Grantor or the Grantee accepts the contract
	/// provisions by signing. I.e., where either the Grantor or the Grantee has signed, but not both. E.g., when an
	/// insurance applicant signs the insurers application, which references the policy. Usage: Optional first step of
	/// contract execution activity.  May be skipped and contracting activity moves directly to executed state.
	/// Precedence Order = 3. Comparable FHIR and v.3 status codes: draft; preliminary; planned; intended; active.
    """
    executable = "executable"

    """ Contract is activated for period stipulated when both the Grantor and Grantee have signed it. Usage: Required
	/// state for normal completion of contracting activity.  Precedence Order = 6. Comparable FHIR and v.3 status
	/// codes: accepted; completed.
    """
    executed = "executed"

    """ Contract execution is suspended while either or both the Grantor and Grantee propose and consider new or revised
	/// contract provisions. I.e., where the party which has not signed proposes changes to the terms.  E .g., a life
	/// insurer declines to agree to the signed application because the life insurer has evidence that the applicant,
	/// who asserted to being younger or a non-smoker to get a lower premium rate - but offers instead to agree to a
	/// higher premium based on the applicants actual age or smoking status. Usage: Optional contract activity between
	/// executable and executed state. Precedence Order = 4. Comparable FHIR and v.3 status codes: in progress; review;
	/// held.
    """
    negotiable = "negotiable"

    """ Contract is a proposal by either the Grantor or the Grantee. Aka - A Contract hard copy or electronic
	/// 'template','form' or 'application'. E.g., health insurance application; consent directive form. Usage: Beginning
	/// of contract negotiation, which may have been completed as a precondition because used for 0..* contracts.
	/// Precedence Order = 2. Comparable FHIR and v.3 status codes: requested; new.
    """
    offered = "offered"

    """ Contract template is available as the basis for an application or offer by the Grantor or Grantee. E.g., health
	/// insurance policy; consent directive policy.  Usage: Required initial contract activity, which may have been
	/// completed as a precondition because used for 0..* contracts. Precedence Order = 1. Comparable FHIR and v.3
	/// status codes: proposed; intended.
    """
    policy = "policy"

    """  Execution of the Contract is not completed because either or both the Grantor and Grantee decline to accept
	/// some or all of the contract provisions. Usage: Optional contract activity between executable and abnormal
	/// termination. Precedence Order = 5. Comparable FHIR and v.3 status codes:  stopped; cancelled.
    """
    rejected = "rejected"

    """ Beginning of a successor Contract at the termination of predecessor Contract lifecycle. Usage: Follows
	/// termination of a preceding Contract that has reached its expiry date. Precedence Order = 13. Comparable FHIR and
	/// v.3 status codes: superseded.
    """
    renewed = "renewed"

    """ A Contract that is rescinded.  May be required prior to replacing with an updated Contract. Comparable FHIR and
	/// v.3 status codes: nullified.
    """
    revoked = "revoked"

    """ Contract is reactivated after being pended because of faulty execution. *E.g., competency of the signer(s), or
	/// where the policy is substantially different from and did not accompany the application/form so that the
	/// applicant could not compare them. Aka - ''reactivated''. Usage: Optional stage where a pended contract is
	/// reactivated. Precedence Order = 8. Comparable FHIR and v.3 status codes: reactivated.
    """
    resolved = "resolved"

    """ Contract reaches its expiry date. It might or might not be renewed or renegotiated. Usage: Normal end of
	/// contract period. Precedence Order = 12. Comparable FHIR and v.3 status codes: Obsoleted.
    """
    terminated = "terminated"


class ContractSignerTypeCodes(CodeSystemValue):
    """ This value set includes sample Contract Signer Type codes.

    URL: http://www.hl7.org/fhir/contractsignertypecodes
    ValueSet: http://hl7.org/fhir/ValueSet/contract-signer-type
    """
    URL = "http://www.hl7.org/fhir/contractsignertypecodes"
    EXPERIMENTAL = True

    """ A person who has corrected, edited, or amended pre-existing information.
    """
    AMENDER = "AMENDER"

    """ A person in the role of verifier who attests to the accuracy of an act, but who does not have privileges to
	/// legally authenticate information content. An example would be a resident physician who sees a patient and
	/// dictates a note, then later signs it. The resident's signature constitutes an authentication.
    """
    AUTHN = "AUTHN"

    """ An entity that authored specific content. There can be multiple authors of content, which may take such forms as
	/// a contract, a healthcare record entry or document, a policy, or a consent directive.
    """
    AUT = "AUT"

    """ An entity that has a business or professional relationship with another entity in accordance with an agreement.
    """
    AFFL = "AFFL"

    """ An entity that acts or is authorized to act on behalf of another entity in accordance with an agreement.
    """
    AGNT = "AGNT"

    """ An agent role in which the agent is an Entity acting in the employ of an organization. The focus is on
	/// functional role on behalf of the organization, unlike the Employee role where the focus is on the 'Human
	/// Resources' relationship between the employee and the organization.
    """
    ASSIGNED = "ASSIGNED"

    """ The member of a jurisdiction afforded certain rights and encumbered with certain obligation in accordance with
	/// jurisdictional policy.
    """
    CIT = "CIT"

    """ A party that makes a claim for coverage under a policy.
    """
    CLAIMANT = "CLAIMANT"

    """ The entity that co-authored content. There can be multiple co-authors of content,which may take such forms as a
	/// such as a contract, a healthcare record entry or document, a policy, or a consent directive.
    """
    COAUTH = "COAUTH"

    """ A patient or patient representative who is the grantee in a healthcare related agreement such as a consent for
	/// healthcare services, advanced directive, or a privacy consent directive in accordance with jurisdictional,
	/// organizational, or patient policy.
    """
    CONSENTER = "CONSENTER"

    """ A person who has witnessed and attests to observing a patient being counseled about a healthcare related
	/// agreement such as a consent for healthcare services, advanced directive, or a privacy consent directive.
    """
    CONSWIT = "CONSWIT"

    """ A person or an organization that provides or receives information regarding another entity. Examples; patient
	/// NOK and emergency contacts; guarantor contact; employer contact.
    """
    CONT = "CONT"

    """ A person who participates in the generation of and attest to veracity of content, but is not an author or co-
	/// author. For example a surgeon who is required by institutional, regulatory, or legal rules to sign an operative
	/// report, but who was not involved in the authorship of that report.
    """
    COPART = "COPART"

    """ An entity, which is the insured, that receives benefits such as healthcare services, reimbursement for out-of-
	/// pocket expenses, or compensation for losses through coverage under the terms of an insurance policy. The
	/// underwriter of that policy is the scoping entity. The covered party receives coverage because of some
	/// contractual or other relationship with the holder of that policy. Note that a particular policy may cover
	/// several individuals one of whom may be, but need not be, the policy holder. Thus the notion of covered party is
	/// a role that is distinct from that of the policy holder.
    """
    COVPTY = "COVPTY"

    """ A party to whom some right or authority is delegated by a delegator.
    """
    DELEGATEE = "DELEGATEE"

    """ A party that delegates a right or authority to another party.
    """
    delegator = "delegator"

    """ A person covered under an insurance policy or program based on an association with a subscriber, which is
	/// recognized by the policy holder. The dependent has an association with the subscriber such as a financial
	/// dependency or personal relationship such as that of a spouse, or a natural or adopted child. The policy holder
	/// may be required by law to recognize certain associations or may have discretion about the associations. For
	/// example, a policy holder may dictate the criteria for the dependent status of adult children who are students,
	/// such as requiring full time enrollment, or may recognize domestic partners as dependents. Under certain
	/// circumstances, the dependent may be under the indirect authority of a responsible party acting as a surrogate
	/// for the subscriber, for example, if the subscriber is differently-abled or deceased, a guardian ad Lidem or
	/// estate executor may be appointed to assume the subscriber's legal standing in the relationship with the
	/// dependent.
    """
    DEPEND = "DEPEND"

    """ A person who has been granted the authority to represent or act on another's behalf generally in a manner which
	/// is a legally binding upon the person giving such authority as if he or she personally were to do the acts.
	/// Unlike ordinary powers of attorney, durable powers can survive for long periods of time, and again, unlike
	/// standard powers of attorney, durable powers can continue after incompetency.
    """
    DPOWATT = "DPOWATT"

    """ An entity to be contacted in the event of an emergency
    """
    EMGCON = "EMGCON"

    """ A person who attests to observing an occurrence.  For example, the witness has observed a procedure and is
	/// attesting to this fact.
    """
    EVTWIT = "EVTWIT"

    """ A person who has been granted the authority to act as an estate executor for a deceased person who was the
	/// responsible party.
    """
    EXCEST = "EXCEST"

    """ A person who grants to another person the authority to represent or act on that person's behalf.  Examples
	/// include (1) exercising specific rights belonging to the grantee; (2) performing specific duties on behalf of a
	/// grantee; and (3) making specific decisions concerning a grantee.
    """
    GRANTEE = "GRANTEE"

    """ A person who has been granted the authority to represent or act on another's behalf. Examples include (1)
	/// exercising specific rights belonging to the grantee; (2) performing specific duties on behalf of a grantee; and
	/// (3) making specific decisions concerning a grantee.
    """
    GRANTOR = "GRANTOR"

    """ A person or organization contractually recognized by the issuer as an entity that has assumed fiscal
	/// responsibility (e.g., by making or giving a promise, assurance, or pledge) for another entity's financial
	/// obligations by guaranteeing to pay for amounts owed to a particular account.  In a healthcare context, the
	/// account may be a patient's billing account for services rendered by a provider or a health plan premium account.
    """
    GUAR = "GUAR"

    """ A person or organization legally empowered with responsibility for the care of a ward.
    """
    GUARD = "GUARD"

    """ A person appointed by the court to look out for the best interests of a minor child during the course of legal
	/// proceedings.
    """
    GUADLTM = "GUADLTM"

    """ An entity that is the source of reported information (e.g., a next of kin who answers questions about the
	/// patient's history). For history questions, the patient is logically an informant, yet the informant of history
	/// questions is implicitly the subject.
    """
    INF = "INF"

    """ A person who converts spoken or written language into the language of key participants in an event such as when
	/// a provider is obtaining a patient's consent to treatment or permission to disclose information.
    """
    INTPRT = "INTPRT"

    """ An entity that is the subject of an investigation. This role is scoped by the party responsible for the
	/// investigation.
    """
    INSBJ = "INSBJ"

    """ A person who has been granted the authority to represent or act on another's behalf for healthcare related
	/// matters in a manner which is a legally binding upon the person giving such authority as if he or she personally
	/// were to do the acts. Examples include (1) exercising specific healthcare legal rights belonging to the grantee
	/// such as signing a consent directive; (2) performing specific healthcare related legal duties on behalf of a
	/// grantee such as claims payment; and (3) making specific healthcare legal decisions concerning a grantee such as
	/// consenting to healthcare services.
    """
    HPOWATT = "HPOWATT"

    """ An entity that is authorized to provide health care services by an authorizing organization or jurisdiction.
    """
    HPROV = "HPROV"

    """ A person in the role of verifier who attests to the accuracy of information content, and who has privileges to
	/// certify the legal authenticity of that content with a signature that constitutes a legal authentication.  For
	/// example, a licensed physician who signs a consult authored by a resident physician who authenticated it.
    """
    LEGAUTHN = "LEGAUTHN"

    """ A party to an insurance policy under which the insurer agrees to indemnify for losses, provides benefits for, or
	/// renders services. A named insured may be either a person, non-person living subject, or an organization, or a
	/// group of persons, non-person living subject that is the named insured under a comprehensive automobile,
	/// disability, or property and casualty policy.  The named insured and might or might not be the policy holder.
    """
    NMDINS = "NMDINS"

    """ A person, who is a type of contact, designated to receive notifications on behalf of another person who is a
	/// relative.
    """
    NOK = "NOK"

    """ The party credentialed to legally attest to the contract binding by verifying the identity and capacity of the
	/// grantor and grantee, and witnessing their signing of the contract or agreement such as a real estate
	/// transaction, pre-nuptial agreement, or a will.
    """
    NOTARY = "NOTARY"

    """ A person, animal, or other living subject that is the actual or potential recipient of health care services.
    """
    PAT = "PAT"

    """ A person who has been granted the authority to represent or act on another's behalf generally in a manner which
	/// is a legally binding upon the person giving such authority as if he or she personally were to do the acts.
	/// Examples include (1) exercising specific legal rights belonging to the grantee such as signing a contract; (2)
	/// performing specific legal duties on behalf of a grantee such as making loan payments; and (3) making specific
	/// legal decisions concerning a grantee such as financial investment decisions.
    """
    POWATT = "POWATT"

    """ An entity that is the primary or sole author of information content.  In the healthcare context, there can be
	/// only one primary author of health information content in a record entry or document.
    """
    PRIMAUTH = "PRIMAUTH"

    """ An entity that may, should receive, or has received information or an object to which it was primarily
	/// addressed.
    """
    PRIRECIP = "PRIRECIP"

    """ An entity that may, should receive, or has received information or an object, which might not have been
	/// primarily addressed to it. For example, the staff of a provider, a clearinghouse, or other intermediary.
    """
    RECIP = "RECIP"

    """ An entity that has legal responsibility for another party.
    """
    RESPRSN = "RESPRSN"

    """ A person, device, or algorithm that has used approved criteria for filtered data for inclusion into the patient
	/// record.  Examples: (1) a medical records clerk who scans a document for inclusion in the medical record, enters
	/// header information, or catalogues and classifies the data, or a combination thereof; (2) a gateway that receives
	/// data from another computer system and interprets that data or changes its format, or both, before entering it
	/// into the patient record.
    """
    REVIEWER = "REVIEWER"

    """ An entity entering the data into the originating system. This includes the transcriptionist for dictated text
	/// transcribed into electronic form.
    """
    TRANS = "TRANS"

    """ An automated data source that generates a signature along with content. Examples: (1) the signature for an image
	/// that is generated by a device for inclusion in the patient record; (2) the signature for an ECG derived by an
	/// ECG system for inclusion in the patient record; (3) the data from a biomedical monitoring device or system that
	/// is for inclusion in the patient record.
    """
    SOURCE = "SOURCE"

    """ A person who has been granted the authority to represent or act on another's behalf for a limited set of
	/// specific matters in a manner which is a legally binding upon the person giving such authority as if he or she
	/// personally were to do the acts. Examples include (1) exercising specific legal rights belonging to the grantee
	/// such as drafting a will; (2) performing specific legal duties on behalf of a grantee such as making a reversible
	/// mortgage to pay for end of life expenses; and (3) making specific legal decisions concerning a grantee such as
	/// managing a trust.
    """
    SPOWATT = "SPOWATT"

    """ A person who validates a health information document for inclusion in the patient record. For example, a medical
	/// student or resident is credentialed to perform history or physical examinations and to write progress notes. The
	/// attending physician signs the history and physical examination to validate the entry for inclusion in the
	/// patient's medical record.
    """
    VALID = "VALID"

    """ A person who asserts the correctness and appropriateness of an act or the recording of the act, and is
	/// accountable for the assertion that the act or the recording of the act complies with jurisdictional or
	/// organizational policy. For example, a physician is required to countersign a verbal order that has previously
	/// been recorded in the medical record by a registered nurse who has carried out the verbal order.
    """
    VERF = "VERF"

    """ A person witnessing the signature of another party. A witness is not knowledgeable about the content being
	/// signed, much less approves of anything stated in the content. For example, an advanced directive witness or a
	/// witness that a party to a contract signed that certain demographic or financial information is truthful.
    """
    WIT = "WIT"


class ContractSubtypeCodes(CodeSystemValue):
    """ This value set includes sample Contract Subtype codes.

    URL: http://hl7.org/fhir/contractsubtypecodes
    ValueSet: http://hl7.org/fhir/ValueSet/contract-subtype
    """
    URL = "http://hl7.org/fhir/contractsubtypecodes"
    EXPERIMENTAL = True

    """ Canadian health information disclosure policy.
    """
    disclosureCa = "disclosure-ca"

    """ United States health information disclosure policy.
    """
    disclosureUs = "disclosure-us"


class ContractTermSubtypeCodes(CodeSystemValue):
    """ This value set includes sample Contract Term SubType codes.

    URL: http://hl7.org/fhir/contracttermsubtypecodes
    ValueSet: http://hl7.org/fhir/ValueSet/contract-term-subtype
    """
    URL = "http://hl7.org/fhir/contracttermsubtypecodes"
    EXPERIMENTAL = True

    """ Terms that go to the very root of a contract.
    """
    condition = "condition"

    """ Less imperative than a condition, so the contract will survive a breach
    """
    warranty = "warranty"

    """ Breach of which might or might not go to the root of the contract depending upon the nature of the breach
    """
    innominate = "innominate"


class ContractTermTypeCodes(CodeSystemValue):
    """ This value set includes sample Contract Term Type codes.

    URL: http://hl7.org/fhir/contracttermtypecodes
    ValueSet: http://hl7.org/fhir/ValueSet/contract-term-type
    """
    URL = "http://hl7.org/fhir/contracttermtypecodes"
    EXPERIMENTAL = True

    """ Based on specialized statutes that deal with particular subjects.
    """
    statutory = "statutory"

    """ Execution of the term in the contract is conditional on the execution of other actions.
    """
    subjectTo = "subject-to"


class ContractTypeCodes(CodeSystemValue):
    """ This value set includes sample Contract Type codes.

    URL: http://hl7.org/fhir/contracttypecodes
    ValueSet: http://hl7.org/fhir/ValueSet/contract-type
    """
    URL = "http://hl7.org/fhir/contracttypecodes"
    EXPERIMENTAL = True

    """ Privacy policy.
    """
    privacy = "privacy"

    """ Information disclosure policy.
    """
    disclosure = "disclosure"

    """ Health Insurance policy.
    """
    healthinsurance = "healthinsurance"

    """ Contract to supply goods or services.
    """
    supply = "supply"

    """ Consent Directive.
    """
    consent = "consent"


class ContributorType(CodeSystemValue):
    """ The type of contributor

    URL: http://hl7.org/fhir/contributor-type
    ValueSet: http://hl7.org/fhir/ValueSet/contributor-type
    """
    URL = "http://hl7.org/fhir/contributor-type"
    EXPERIMENTAL = False

    """ An author of the content of the module
    """
    author = "author"

    """ An editor of the content of the module
    """
    editor = "editor"

    """ A reviewer of the content of the module
    """
    reviewer = "reviewer"

    """ An endorser of the content of the module
    """
    endorser = "endorser"


class CopyNumberEvent(CodeSystemValue):
    """ Copy Number Event

    URL: http://hl7.org/fhir/copy-number-event
    ValueSet: http://hl7.org/fhir/ValueSet/copy-number-event
    """
    URL = "http://hl7.org/fhir/copy-number-event"
    EXPERIMENTAL = False

    """ amplification
    """
    amp = "amp"

    """ deletion
    """
    _del = "del"

    """ loss of function
    """
    lof = "lof"


class CoverageClassCodes(CodeSystemValue):
    """ This value set includes Coverage Class codes.

    URL: http://hl7.org/fhir/coverage-class
    ValueSet: http://hl7.org/fhir/ValueSet/coverage-class
    """
    URL = "http://hl7.org/fhir/coverage-class"
    EXPERIMENTAL = True

    """ An employee group
    """
    group = "group"

    """ A sub-group of an employee group
    """
    subgroup = "subgroup"

    """ A specific suite of benefits.
    """
    plan = "plan"

    """ A subset of a specific suite of benefits.
    """
    subplan = "subplan"

    """ A class of benefits.
    """
    class_fhir = "class"

    """ A subset of a class of benefits.
    """
    subclass = "subclass"

    """ A sequence number associated with a short-term continuance of the coverage.
    """
    sequence = "sequence"

    """ Pharmacy benefit manager's Business Identification Number.
    """
    rxbin = "rxbin"

    """ A Pharmacy Benefit Manager specified Processor Control Number.
    """
    rxpcn = "rxpcn"

    """ A Pharmacy Benefit Manager specified Member ID.
    """
    rxid = "rxid"

    """ A Pharmacy Benefit Manager specified Group number.
    """
    rxgroup = "rxgroup"


class CoverageCopayTypeCodes(CodeSystemValue):
    """ This value set includes sample Coverage Copayment Type codes.

    URL: http://hl7.org/fhir/coverage-copay-type
    ValueSet: http://hl7.org/fhir/ValueSet/coverage-copay-type
    """
    URL = "http://hl7.org/fhir/coverage-copay-type"
    EXPERIMENTAL = True

    """ An office visit for a general practitioner of a discipline.
    """
    gpvisit = "gpvisit"

    """ An office visit for a specialist practitioner of a discipline
    """
    spvisit = "spvisit"

    """ An episode in an emergency department.
    """
    emergency = "emergency"

    """ An episode of an Inpatient hospital stay.
    """
    inpthosp = "inpthosp"

    """ A visit held where the patient is remote relative to the practitioner, eg. by phone, computer or video
	/// conference.
    """
    televisit = "televisit"

    """ A visit to an urgent care facility - typically a community care clinic.
    """
    urgentcare = "urgentcare"

    """ A standard amount, percentage or fixed currency amount, applied to all classes or service or product not
	/// otherwise specified.
    """
    copaypct = "copaypct"


class CoverageSelfPayCodes(CodeSystemValue):
    """ This value set includes Coverage SelfPay codes.

    URL: http://hl7.org/fhir/coverage-selfpay
    ValueSet: http://hl7.org/fhir/ValueSet/coverage-selfpay
    """
    URL = "http://hl7.org/fhir/coverage-selfpay"
    EXPERIMENTAL = True

    """ An individual or oraganization is paying directly for goods and services.
    """
    pay = "pay"


class DataAbsentReason(CodeSystemValue):
    """ Used to specify why the normally expected content of the data element is missing.

    URL: http://hl7.org/fhir/data-absent-reason
    ValueSet: http://hl7.org/fhir/ValueSet/data-absent-reason
    """
    URL = "http://hl7.org/fhir/data-absent-reason"
    EXPERIMENTAL = False

    """ The value is expected to exist but is not known.
    """
    unknown = "unknown"

    """ The source was asked but does not know the value.
    """
    askedUnknown = "asked-unknown"

    """ There is reason to expect (from the workflow) that the value may become known.
    """
    tempUnknown = "temp-unknown"

    """ The workflow didn't lead to this value being known.
    """
    notAsked = "not-asked"

    """ The source was asked but declined to answer.
    """
    askedDeclined = "asked-declined"

    """ The information is not available due to security, privacy or related reasons.
    """
    masked = "masked"

    """ There is no proper value for this element (e.g. last menstrual period for a male)
    """
    notApplicable = "not-applicable"

    """ The source system wasn't capable of supporting this element.
    """
    unsupported = "unsupported"

    """ The content of the data is represented in the resource narrative.
    """
    asText = "as-text"

    """ Some system or workflow process error means that the information is not available.
    """
    error = "error"

    """ The numeric value is undefined or unrepresentable due to a floating point processing error.
    """
    notANumber = "not-a-number"

    """ The numeric value is excessively low and unrepresentable due to a floating point processing error.
    """
    negativeInfinity = "negative-infinity"

    """ The numeric value is excessively high and unrepresentable due to a floating point processing error.
    """
    positiveInfinity = "positive-infinity"

    """ The value is not available because the observation procedure (test, etc.) was not performed.
    """
    notPerformed = "not-performed"

    """ The value is not permitted in this context (e.g. due to profiles, or the base data types)
    """
    notPermitted = "not-permitted"


class DataType(CodeSystemValue):
    """ A version specific list of the data types defined by the FHIR specification for use as an element  type (any of the FHIR
defined data types)

    URL: http://hl7.org/fhir/data-types
    ValueSet: http://hl7.org/fhir/ValueSet/data-types
    """
    URL = "http://hl7.org/fhir/data-types"
    EXPERIMENTAL = False

    """ An address expressed using postal conventions (as opposed to GPS or other location definition formats).  This
	/// data type may be used to convey addresses for use in delivering mail as well as for visiting locations which
	/// might not be valid for mail delivery.  There are a variety of postal address formats defined around the world.
    """
    address = "Address"

    """ A duration of time during which an organism (or a process) has existed.
    """
    age = "Age"

    """ A  text note which also  contains information about who made the statement and when.
    """
    annotation = "Annotation"

    """ For referring to data content defined in other formats.
    """
    attachment = "Attachment"

    """ Base definition for all elements that are defined inside a resource - but not those in a data type.
    """
    backboneElement = "BackboneElement"

    """ A concept that may be defined by a formal reference to a terminology or ontology or may be provided by text.
    """
    codeableConcept = "CodeableConcept"

    """ A reference to a code defined by a terminology system.
    """
    coding = "Coding"

    """ Specifies contact information for a person or organization.
    """
    contactDetail = "ContactDetail"

    """ Details for all kinds of technology mediated contact points for a person or organization, including telephone,
	/// email, etc.
    """
    contactPoint = "ContactPoint"

    """ A contributor to the content of a knowledge asset, including authors, editors, reviewers, and endorsers.
    """
    contributor = "Contributor"

    """ A measured amount (or an amount that can potentially be measured). Note that measured amounts include amounts
	/// that are not precisely quantified, including amounts involving arbitrary units and floating currencies.
    """
    count = "Count"

    """ Describes a required data item for evaluation in terms of the type of data, and optional code or date-based
	/// filters of the data.
    """
    dataRequirement = "DataRequirement"

    """ A length - a value with a unit that is a physical distance.
    """
    distance = "Distance"

    """ Indicates how the medication is/was taken or should be taken by the patient.
    """
    dosage = "Dosage"

    """ A length of time.
    """
    duration = "Duration"

    """ Base definition for all elements in a resource.
    """
    element = "Element"

    """ Captures constraints on each element within the resource, profile, or extension.
    """
    elementDefinition = "ElementDefinition"

    """ Optional Extension Element - found in all resources.
    """
    extension = "Extension"

    """ A human's name with the ability to identify parts and usage.
    """
    humanName = "HumanName"

    """ A technical identifier - identifies some entity uniquely and unambiguously.
    """
    identifier = "Identifier"

    """ The marketing status describes the date when a medicinal product is actually put on the market or the date as of
	/// which it is no longer available.
    """
    marketingStatus = "MarketingStatus"

    """ The metadata about a resource. This is content in the resource that is maintained by the infrastructure. Changes
	/// to the content might not always be associated with version changes to the resource.
    """
    meta = "Meta"

    """ An amount of economic utility in some recognized currency.
    """
    money = "Money"

    """ A human-readable formatted text, including images.
    """
    narrative = "Narrative"

    """ The parameters to the module. This collection specifies both the input and output parameters. Input parameters
	/// are provided by the caller as part of the $evaluate operation. Output parameters are included in the
	/// GuidanceResponse.
    """
    parameterDefinition = "ParameterDefinition"

    """ A time period defined by a start and end date and optionally time.
    """
    period = "Period"

    """ The marketing status describes the date when a medicinal product is actually put on the market or the date as of
	/// which it is no longer available.
    """
    prodCharacteristic = "ProdCharacteristic"

    """ The shelf-life and storage information for a medicinal product item or container can be described using this
	/// class.
    """
    productShelfLife = "ProductShelfLife"

    """ A measured amount (or an amount that can potentially be measured). Note that measured amounts include amounts
	/// that are not precisely quantified, including amounts involving arbitrary units and floating currencies.
    """
    quantity = "Quantity"

    """ A set of ordered Quantities defined by a low and high limit.
    """
    range = "Range"

    """ A relationship of two Quantity values - expressed as a numerator and a denominator.
    """
    ratio = "Ratio"

    """ A reference from one resource to another.
    """
    reference = "Reference"

    """ Related artifacts such as additional documentation, justification, or bibliographic references.
    """
    relatedArtifact = "RelatedArtifact"

    """ A series of measurements taken by a device, with upper and lower limits. There may be more than one dimension in
	/// the data.
    """
    sampledData = "SampledData"

    """ A signature along with supporting context. The signature may be a digital signature that is cryptographic in
	/// nature, or some other signature acceptable to the domain. This other signature may be as simple as a graphical
	/// image representing a hand-written signature, or a signature ceremony Different signature approaches have
	/// different utilities.
    """
    signature = "Signature"

    """ simpleQuantity
    """
    simpleQuantity = "SimpleQuantity"

    """ Chemical substances are a single substance type whose primary defining element is the molecular structure.
	/// Chemical substances shall be defined on the basis of their complete covalent molecular structure; the presence
	/// of a salt (counter-ion) and/or solvates (water, alcohols) is also captured. Purity, grade, physical form or
	/// particle size are not taken into account in the definition of a chemical substance or in the assignment of a
	/// Substance ID.
    """
    substanceAmount = "SubstanceAmount"

    """ Chemical substances are a single substance type whose primary defining element is the molecular structure.
	/// Chemical substances shall be defined on the basis of their complete covalent molecular structure; the presence
	/// of a salt (counter-ion) and/or solvates (water, alcohols) is also captured. Purity, grade, physical form or
	/// particle size are not taken into account in the definition of a chemical substance or in the assignment of a
	/// Substance ID.
    """
    substanceMoiety = "SubstanceMoiety"

    """ Specifies an event that may occur multiple times. Timing schedules are used to record when things are planned,
	/// expected or requested to occur. The most common usage is in dosage instructions for medications. They are also
	/// used when planning care of various kinds, and may be used for reporting the schedule to which past regular
	/// activities were carried out.
    """
    timing = "Timing"

    """ A description of a triggering event. Triggering events can be named events, data events, or periodic, as
	/// determined by the type element.
    """
    triggerDefinition = "TriggerDefinition"

    """ Specifies clinical/business/etc. metadata that can be used to retrieve, index and/or categorize an artifact.
	/// This metadata can either be specific to the applicable population (e.g., age category, DRG) or the specific
	/// context of care (e.g., venue, care setting, provider of care).
    """
    usageContext = "UsageContext"

    """ A stream of bytes
    """
    base64Binary = "base64Binary"

    """ Value of "true" or "false"
    """
    boolean = "boolean"

    """ A URI that is a reference to a canonical URI on a FHIR resource
    """
    canonical = "canonical"

    """ A string which has at least one character and no leading or trailing whitespace and where there is no whitespace
	/// other than single spaces in the contents
    """
    code = "code"

    """ A date or partial date (e.g. just year or year + month). There is no time zone. The format is a union of the
	/// schema types gYear, gYearMonth and date.  Dates SHALL be valid dates.
    """
    date = "date"

    """ A date, date-time or partial date (e.g. just year or year + month).  If hours and minutes are specified, a time
	/// zone SHALL be populated. The format is a union of the schema types gYear, gYearMonth, date and dateTime. Seconds
	/// must be provided due to schema type constraints but may be zero-filled and may be ignored.                 Dates
	/// SHALL be valid dates.
    """
    dateTime = "dateTime"

    """ A rational number with implicit precision
    """
    decimal = "decimal"

    """ Any combination of letters, numerals, "-" and ".", with a length limit of 64 characters.  (This might be an
	/// integer, an unprefixed OID, UUID or any other identifier pattern that meets these constraints.)  Ids are case-
	/// insensitive.
    """
    id = "id"

    """ An instant in time - known at least to the second
    """
    instant = "instant"

    """ A whole number
    """
    integer = "integer"

    """ A string that may contain Github Flavored Markdown syntax for optional processing by a mark down presentation
	/// engine
    """
    markdown = "markdown"

    """ An OID represented as a URI
    """
    oid = "oid"

    """ An integer with a value that is positive (e.g. >0)
    """
    positiveInt = "positiveInt"

    """ A sequence of Unicode characters
    """
    string = "string"

    """ A time during the day, with no date specified
    """
    time = "time"

    """ An integer with a value that is not negative (e.g. >= 0)
    """
    unsignedInt = "unsignedInt"

    """ String of characters used to identify a name or a resource
    """
    uri = "uri"

    """ A URI that is a literal reference
    """
    url = "url"

    """ A UUID, represented as a URI
    """
    uuid = "uuid"

    """ XHTML format, as defined by W3C, but restricted usage (mainly, no active content)
    """
    xhtml = "xhtml"


class DaysOfWeek(CodeSystemValue):
    """ The days of the week.

    URL: http://hl7.org/fhir/days-of-week
    ValueSet: http://hl7.org/fhir/ValueSet/days-of-week
    """
    URL = "http://hl7.org/fhir/days-of-week"
    EXPERIMENTAL = False

    """ Monday
    """
    mon = "mon"

    """ Tuesday
    """
    tue = "tue"

    """ Wednesday
    """
    wed = "wed"

    """ Thursday
    """
    thu = "thu"

    """ Friday
    """
    fri = "fri"

    """ Saturday
    """
    sat = "sat"

    """ Sunday
    """
    sun = "sun"


class DefinitionStatus(CodeSystemValue):
    """ Codes identifying the lifecycle stage of a definition

    URL: http://hl7.org/fhir/definition-status
    ValueSet: http://hl7.org/fhir/ValueSet/definition-status
    """
    URL = "http://hl7.org/fhir/definition-status"
    EXPERIMENTAL = False

    """ The definition is in the design stage and is not yet considered to be "ready for use"
    """
    draft = "draft"

    """ The definition is considered ready for use
    """
    active = "active"

    """ The definition should no longer be used
    """
    withdrawn = "withdrawn"

    """ The authoring system does not know which of the status values currently applies for this request.  Note: This
	/// concept is not to be used for "other" - one of the listed statuses is presumed to apply, it's just not known
	/// which one.
    """
    unknown = "unknown"


class DefinitionTopic(CodeSystemValue):
    """ High-level categorization of the definition, used for searching, sorting, and filtering

    URL: http://hl7.org/fhir/definition-topic
    ValueSet: http://hl7.org/fhir/ValueSet/definition-topic
    """
    URL = "http://hl7.org/fhir/definition-topic"
    EXPERIMENTAL = False

    """ The definition is related to treatment of the patient
    """
    treatment = "treatment"

    """ The definition is related to education of the patient
    """
    education = "education"

    """ The definition is related to assessment of the patient
    """
    assessment = "assessment"


class DetectedIssueSeverity(CodeSystemValue):
    """ Indicates the potential degree of impact of the identified issue on the patient.

    URL: http://hl7.org/fhir/detectedissue-severity
    ValueSet: http://hl7.org/fhir/ValueSet/detectedissue-severity
    """
    URL = "http://hl7.org/fhir/detectedissue-severity"
    EXPERIMENTAL = False

    """ Indicates the issue may be life-threatening or has the potential to cause permanent injury.
    """
    high = "high"

    """ Indicates the issue may result in noticeable adverse consequences but is unlikely to be life-threatening or
	/// cause permanent injury.
    """
    moderate = "moderate"

    """ Indicates the issue may result in some adverse consequences but is unlikely to substantially affect the
	/// situation of the subject.
    """
    low = "low"


class DeviceComponentOperationalStatus(CodeSystemValue):
    """ Codes representing the current status of the device - on, off, suspended, etc.

    URL: http://hl7.org/fhir/operational-status
    ValueSet: http://hl7.org/fhir/ValueSet/operational-status
    """
    URL = "http://hl7.org/fhir/operational-status"
    EXPERIMENTAL = False

    """ The device is off.
    """
    off = "off"

    """ The device is fully operational.
    """
    on = "on"

    """ The device is not ready.
    """
    notReady = "not-ready"

    """ The device is ready but not actively operating.
    """
    standby = "standby"

    """ The device transducer is disconnected.
    """
    transducDiscon = "transduc-discon"

    """ The device hardware is disconnected.
    """
    hwDiscon = "hw-discon"

    """ The device was entered in error.
    """
    enteredInError = "entered-in-error"


class DeviceComponentParameterGroup(CodeSystemValue):
    """ Codes identifying groupings of parameters; e.g. Cardiovascular.

    URL: http://hl7.org/fhir/parameter-group
    ValueSet: http://hl7.org/fhir/ValueSet/parameter-group
    """
    URL = "http://hl7.org/fhir/parameter-group"
    EXPERIMENTAL = False

    """ Haemodynamic Parameter Group - MDC_PGRP_HEMO
    """
    haemodynamic = "haemodynamic"

    """ ECG Parameter Group - MDC_PGRP_ECG
    """
    ecg = "ecg"

    """ Respiratory Parameter Group - MDC_PGRP_RESP
    """
    respiratory = "respiratory"

    """ Ventilation Parameter Group - MDC_PGRP_VENT
    """
    ventilation = "ventilation"

    """ Neurological Parameter Group - MDC_PGRP_NEURO
    """
    neurological = "neurological"

    """ Drug Delivery Parameter Group - MDC_PGRP_DRUG
    """
    drugDelivery = "drug-delivery"

    """ Fluid Chemistry Parameter Group - MDC_PGRP_FLUID
    """
    fluidChemistry = "fluid-chemistry"

    """ Blood Chemistry Parameter Group - MDC_PGRP_BLOOD_CHEM
    """
    bloodChemistry = "blood-chemistry"

    """ Miscellaneous Parameter Group - MDC_PGRP_MISC
    """
    miscellaneous = "miscellaneous"


class DeviceMetricCalibrationState(CodeSystemValue):
    """ Describes the state of a metric calibration.

    URL: http://hl7.org/fhir/metric-calibration-state
    ValueSet: http://hl7.org/fhir/ValueSet/metric-calibration-state
    """
    URL = "http://hl7.org/fhir/metric-calibration-state"
    EXPERIMENTAL = False

    """ The metric has not been calibrated.
    """
    notCalibrated = "not-calibrated"

    """ The metric needs to be calibrated.
    """
    calibrationRequired = "calibration-required"

    """ The metric has been calibrated.
    """
    calibrated = "calibrated"

    """ The state of calibration of this metric is unspecified.
    """
    unspecified = "unspecified"


class DeviceMetricCalibrationType(CodeSystemValue):
    """ Describes the type of a metric calibration.

    URL: http://hl7.org/fhir/metric-calibration-type
    ValueSet: http://hl7.org/fhir/ValueSet/metric-calibration-type
    """
    URL = "http://hl7.org/fhir/metric-calibration-type"
    EXPERIMENTAL = False

    """ Metric calibration method has not been identified.
    """
    unspecified = "unspecified"

    """ Offset metric calibration method
    """
    offset = "offset"

    """ Gain metric calibration method
    """
    gain = "gain"

    """ Two-point metric calibration method
    """
    twoPoint = "two-point"


class DeviceMetricCategory(CodeSystemValue):
    """ Describes the category of the metric.

    URL: http://hl7.org/fhir/metric-category
    ValueSet: http://hl7.org/fhir/ValueSet/metric-category
    """
    URL = "http://hl7.org/fhir/metric-category"
    EXPERIMENTAL = False

    """ DeviceObservations generated for this DeviceMetric are measured.
    """
    measurement = "measurement"

    """ DeviceObservations generated for this DeviceMetric is a setting that will influence the behavior of the Device.
    """
    setting = "setting"

    """ DeviceObservations generated for this DeviceMetric are calculated.
    """
    calculation = "calculation"

    """ The category of this DeviceMetric is unspecified.
    """
    unspecified = "unspecified"


class DeviceMetricColor(CodeSystemValue):
    """ Describes the typical color of representation.

    URL: http://hl7.org/fhir/metric-color
    ValueSet: http://hl7.org/fhir/ValueSet/metric-color
    """
    URL = "http://hl7.org/fhir/metric-color"
    EXPERIMENTAL = False

    """ Color for representation - black.
    """
    black = "black"

    """ Color for representation - red.
    """
    red = "red"

    """ Color for representation - green.
    """
    green = "green"

    """ Color for representation - yellow.
    """
    yellow = "yellow"

    """ Color for representation - blue.
    """
    blue = "blue"

    """ Color for representation - magenta.
    """
    magenta = "magenta"

    """ Color for representation - cyan.
    """
    cyan = "cyan"

    """ Color for representation - white.
    """
    white = "white"


class DeviceMetricOperationalStatus(CodeSystemValue):
    """ Describes the operational status of the DeviceMetric.

    URL: http://hl7.org/fhir/metric-operational-status
    ValueSet: http://hl7.org/fhir/ValueSet/metric-operational-status
    """
    URL = "http://hl7.org/fhir/metric-operational-status"
    EXPERIMENTAL = False

    """ The DeviceMetric is operating and will generate DeviceObservations.
    """
    on = "on"

    """ The DeviceMetric is not operating.
    """
    off = "off"

    """ The DeviceMetric is operating, but will not generate any DeviceObservations.
    """
    standby = "standby"

    """ The DeviceMetric was entered in error.
    """
    enteredInError = "entered-in-error"


class DeviceSpecificationSpecType(CodeSystemValue):
    """ Codes for device specification types such as serial number, part number, hardware revision, software revision, etc.

    URL: http://hl7.org/fhir/specification-type
    ValueSet: http://hl7.org/fhir/ValueSet/specification-type
    """
    URL = "http://hl7.org/fhir/specification-type"
    EXPERIMENTAL = False

    """ Unspecified Production Specification - MDC_ID_PROD_SPEC_UNSPECIFIED
    """
    unspecified = "unspecified"

    """ Serial Number - MDC_ID_PROD_SPEC_SERIAL
    """
    serialNumber = "serial-number"

    """ Part Number - MDC_ID_PROD_SPEC_PART
    """
    partNumber = "part-number"

    """ Hardware Revision - MDC_ID_PROD_SPEC_HW
    """
    hardwareRevision = "hardware-revision"

    """ Software Revision - MDC_ID_PROD_SPEC_SW
    """
    softwareRevision = "software-revision"

    """ Firmware Revision - MDC_ID_PROD_SPEC_FW
    """
    firmwareRevision = "firmware-revision"

    """ Protocol Revision - MDC_ID_PROD_SPEC_PROTOCOL
    """
    protocolRevision = "protocol-revision"

    """ GMDN - MDC_ID_PROD_SPEC_GMDN
    """
    gmdn = "gmdn"


class DeviceUseStatementStatus(CodeSystemValue):
    """ A coded concept indicating the current status of a the Device Usage

    URL: http://hl7.org/fhir/device-statement-status
    ValueSet: http://hl7.org/fhir/ValueSet/device-statement-status
    """
    URL = "http://hl7.org/fhir/device-statement-status"
    EXPERIMENTAL = False

    """ The device is still being used.
    """
    active = "active"

    """ The device is no longer being used.
    """
    completed = "completed"

    """ The statement was recorded incorrectly.
    """
    enteredInError = "entered-in-error"

    """ The device may be used at some time in the future.
    """
    intended = "intended"

    """ Actions implied by the statement have been permanently halted, before all of them occurred.
    """
    stopped = "stopped"

    """ Actions implied by the statement have been temporarily halted, but are expected to continue later. May also be
	/// called "suspended".
    """
    onHold = "on-hold"


class DiagnosisRole(CodeSystemValue):
    """ This value set defines a set of codes that can be used to express the role of a diagnosis on the Encounter or
EpisodeOfCare record.

    URL: http://hl7.org/fhir/diagnosis-role
    ValueSet: http://hl7.org/fhir/ValueSet/diagnosis-role
    """
    URL = "http://hl7.org/fhir/diagnosis-role"
    EXPERIMENTAL = True

    """ AD
    """
    AD = "AD"

    """ DD
    """
    DD = "DD"

    """ CC
    """
    CC = "CC"

    """ CM
    """
    CM = "CM"

    """ preOp
    """
    preOp = "pre-op"

    """ postOp
    """
    postOp = "post-op"

    """ billing
    """
    billing = "billing"


class DiagnosticReportStatus(CodeSystemValue):
    """ The status of the diagnostic report.

    URL: http://hl7.org/fhir/diagnostic-report-status
    ValueSet: http://hl7.org/fhir/ValueSet/diagnostic-report-status
    """
    URL = "http://hl7.org/fhir/diagnostic-report-status"
    EXPERIMENTAL = False

    """ The existence of the report is registered, but there is nothing yet available.
    """
    registered = "registered"

    """ This is a partial (e.g. initial, interim or preliminary) report: data in the report may be incomplete or
	/// unverified.
    """
    partial = "partial"

    """ Verified early results are available, but not all  results are final.
    """
    preliminary = "preliminary"

    """ The report is complete and verified by an authorized person.
    """
    final = "final"

    """ Subsequent to being final, the report has been modified.  This includes any change in the results, diagnosis,
	/// narrative text, or other content of a report that has been issued.
    """
    amended = "amended"

    """ Subsequent to being final, the report has been modified  to correct an error in the report or referenced
	/// results.
    """
    corrected = "corrected"

    """ Subsequent to being final, the report has been modified by adding new content. The existing content is
	/// unchanged.
    """
    appended = "appended"

    """ The report is unavailable because the measurement was not started or not completed (also sometimes called
	/// "aborted").
    """
    cancelled = "cancelled"

    """ The report has been withdrawn following a previous final release.  This electronic record should never have
	/// existed, though it is possible that real-world decisions were based on it. (If real-world activity has occurred,
	/// the status should be "cancelled" rather than "entered-in-error".)
    """
    enteredInError = "entered-in-error"

    """ The authoring system does not know which of the status values currently applies to this report. Note: This
	/// concept is not to be used for "other" - one of the listed statuses is presumed to apply although which one is
	/// not known.
    """
    unknown = "unknown"


class Diet(CodeSystemValue):
    """ This value set defines a set of codes that can be used to indicate dietary preferences or restrictions a patient may
have.

    URL: http://hl7.org/fhir/diet
    ValueSet: http://hl7.org/fhir/ValueSet/encounter-diet
    """
    URL = "http://hl7.org/fhir/diet"
    EXPERIMENTAL = True

    """ Food without meat, poultry or seafood.
    """
    vegetarian = "vegetarian"

    """ Excludes dairy products.
    """
    dairyFree = "dairy-free"

    """ Excludes ingredients containing nuts.
    """
    nutFree = "nut-free"

    """ Excludes ingredients containing gluten.
    """
    glutenFree = "gluten-free"

    """ Food without meat, poultry, seafood, eggs, dairy products and other animal-derived substances.
    """
    vegan = "vegan"

    """ Foods that conform to Islamic law.
    """
    halal = "halal"

    """ Foods that conform to Jewish dietary law.
    """
    kosher = "kosher"


class DischargeDisposition(CodeSystemValue):
    """ This value set defines a set of codes that can be used to where the patient left the hospital.

    URL: http://hl7.org/fhir/discharge-disposition
    ValueSet: http://hl7.org/fhir/ValueSet/encounter-discharge-disposition
    """
    URL = "http://hl7.org/fhir/discharge-disposition"
    EXPERIMENTAL = True

    """ The patient was dicharged and has indicated that they are going to return home afterwards.
    """
    home = "home"

    """ The patient was discharged and has indicated that they are going to return home afterwards, but not the
	/// patient's home - e.g. a family member's home.
    """
    altHome = "alt-home"

    """ The patient was transferred to another healthcare facility.
    """
    otherHcf = "other-hcf"

    """ The patient has been discharged into palliative care.
    """
    hosp = "hosp"

    """ The patient has been discharged into long-term care where is likely to be monitored through an ongoing episode-
	/// of-care.
    """
    long = "long"

    """ The patient self discharged against medical advice.
    """
    aadvice = "aadvice"

    """ The patient has deceased during this encounter.
    """
    exp = "exp"

    """ The patient has been transferred to a psychiatric facility.
    """
    psy = "psy"

    """ The patient was discharged and is to receive post acute care rehabilitation services.
    """
    rehab = "rehab"

    """ The patient has been discharged to a skilled nursing facility for the patient to receive additional care.
    """
    snf = "snf"

    """ The discharge disposition has not otherwise defined.
    """
    oth = "oth"


class DiscriminatorType(CodeSystemValue):
    """ How an element value is interpreted when discrimination is evaluated

    URL: http://hl7.org/fhir/discriminator-type
    ValueSet: http://hl7.org/fhir/ValueSet/discriminator-type
    """
    URL = "http://hl7.org/fhir/discriminator-type"
    EXPERIMENTAL = False

    """ The slices have different values in the nominated element
    """
    value = "value"

    """ The slices are differentiated by the presence or absence of the nominated element
    """
    exists = "exists"

    """ The slices have different values in the nominated element, as determined by testing them against the applicable
	/// ElementDefinition.pattern[x]
    """
    pattern = "pattern"

    """ The slices are differentiated by type of the nominated element
    """
    type = "type"

    """ The slices are differentiated by conformance of the nominated element to a specified profile. Note that if the
	/// path specifies .resolve() then the profile is the target profile on the reference. In this case, validation by
	/// the possible profiles is required to differentiate the slices
    """
    profile = "profile"


class DocumentMode(CodeSystemValue):
    """ Whether the application produces or consumes documents.

    URL: http://hl7.org/fhir/document-mode
    ValueSet: http://hl7.org/fhir/ValueSet/document-mode
    """
    URL = "http://hl7.org/fhir/document-mode"
    EXPERIMENTAL = False

    """ The application produces documents of the specified type.
    """
    producer = "producer"

    """ The application consumes documents of the specified type.
    """
    consumer = "consumer"


class DocumentReferenceStatus(CodeSystemValue):
    """ The status of the document reference.

    URL: http://hl7.org/fhir/document-reference-status
    ValueSet: http://hl7.org/fhir/ValueSet/document-reference-status
    """
    URL = "http://hl7.org/fhir/document-reference-status"
    EXPERIMENTAL = False

    """ This is the current reference for this document.
    """
    current = "current"

    """ This reference has been superseded by another reference.
    """
    superseded = "superseded"

    """ This reference was created in error.
    """
    enteredInError = "entered-in-error"


class DocumentRelationshipType(CodeSystemValue):
    """ The type of relationship between documents.

    URL: http://hl7.org/fhir/document-relationship-type
    ValueSet: http://hl7.org/fhir/ValueSet/document-relationship-type
    """
    URL = "http://hl7.org/fhir/document-relationship-type"
    EXPERIMENTAL = False

    """ This document logically replaces or supersedes the target document.
    """
    replaces = "replaces"

    """ This document was generated by transforming the target document (e.g. format or language conversion).
    """
    transforms = "transforms"

    """ This document is a signature of the target document.
    """
    signs = "signs"

    """ This document adds additional information to the target document.
    """
    appends = "appends"


class DoseAndRateType(CodeSystemValue):
    """ The kind of dose or rate specified

    URL: http://hl7.org/fhir/dose-rate-type
    ValueSet: http://hl7.org/fhir/ValueSet/dose-rate-type
    """
    URL = "http://hl7.org/fhir/dose-rate-type"
    EXPERIMENTAL = False

    """ The dose specified is calculated by the prescriber or the system
    """
    calculated = "calculated"

    """ The dose specified is as ordered by the prescriber
    """
    ordered = "ordered"


class EnableWhenBehavior(CodeSystemValue):
    """ Controls how multiple enableWhen values are interpreted -  whether all or any must be true

    URL: http://hl7.org/fhir/questionnaire-enable-behavior
    ValueSet: http://hl7.org/fhir/ValueSet/questionnaire-enable-behavior
    """
    URL = "http://hl7.org/fhir/questionnaire-enable-behavior"
    EXPERIMENTAL = False

    """ Enable the question when all the enableWhen criteria are satisfied
    """
    all = "all"

    """ Enable the question when any of the enableWhen criteria are satisfied
    """
    any = "any"


class EncounterLocationStatus(CodeSystemValue):
    """ The status of the location.

    URL: http://hl7.org/fhir/encounter-location-status
    ValueSet: http://hl7.org/fhir/ValueSet/encounter-location-status
    """
    URL = "http://hl7.org/fhir/encounter-location-status"
    EXPERIMENTAL = False

    """ The patient is planned to be moved to this location at some point in the future.
    """
    planned = "planned"

    """ The patient is currently at this location, or was between the period specified.
	/// 
	/// A system may update these records when the patient leaves the location to either reserved, or completed
    """
    active = "active"

    """ This location is held empty for this patient.
    """
    reserved = "reserved"

    """ The patient was at this location during the period specified.
	/// 
	/// Not to be used when the patient is currently at the location
    """
    completed = "completed"


class EncounterStatus(CodeSystemValue):
    """ Current state of the encounter

    URL: http://hl7.org/fhir/encounter-status
    ValueSet: http://hl7.org/fhir/ValueSet/encounter-status
    """
    URL = "http://hl7.org/fhir/encounter-status"
    EXPERIMENTAL = False

    """ The Encounter has not yet started.
    """
    planned = "planned"

    """ The Patient is present for the encounter, however is not currently meeting with a practitioner.
    """
    arrived = "arrived"

    """ The patient has been assessed for the priority of their treatment based on the severity of their condition.
    """
    triaged = "triaged"

    """ The Encounter has begun and the patient is present / the practitioner and the patient are meeting.
    """
    inProgress = "in-progress"

    """ The Encounter has begun, but the patient is temporarily on leave.
    """
    onleave = "onleave"

    """ The Encounter has ended.
    """
    finished = "finished"

    """ The Encounter has ended before it has begun.
    """
    cancelled = "cancelled"

    """ This instance should not have been part of this patient's medical record.
    """
    enteredInError = "entered-in-error"

    """ The encounter status is unknown. Note that "unknown" is a value of last resort and every attempt should be made
	/// to provide a meaningful value other than "unknown".
    """
    unknown = "unknown"


class EncounterType(CodeSystemValue):
    """ This example value set defines a set of codes that can be used to indicate the type of encounter: a specific code
indicating type of service provided.

    URL: http://hl7.org/fhir/encounter-type
    ValueSet: http://hl7.org/fhir/ValueSet/encounter-type
    """
    URL = "http://hl7.org/fhir/encounter-type"
    EXPERIMENTAL = True

    """ ADMS
    """
    ADMS = "ADMS"

    """ bDBMClin
    """
    bDBMClin = "BD/BM-clin"

    """ CCS60
    """
    CCS60 = "CCS60"

    """ OKI
    """
    OKI = "OKI"


class EndpointConnectionType(CodeSystemValue):
    """ This is an example value set defined by the FHIR project, that could be used to represent possible connection type
profile values.

    URL: http://hl7.org/fhir/endpoint-connection-type
    ValueSet: http://hl7.org/fhir/ValueSet/endpoint-connection-type
    """
    URL = "http://hl7.org/fhir/endpoint-connection-type"
    EXPERIMENTAL = True

    """ IHE Cross Community Patient Discovery Profile (XCPD) - http://wiki.ihe.net/index.php/Cross-
	/// Community_Patient_Discovery
    """
    iheXcpd = "ihe-xcpd"

    """ IHE Cross Community Access Profile (XCA) - http://wiki.ihe.net/index.php/Cross-Community_Access
    """
    iheXca = "ihe-xca"

    """ IHE Cross-Enterprise Document Reliable Exchange (XDR) - http://wiki.ihe.net/index.php/Cross-
	/// enterprise_Document_Reliable_Interchange
    """
    iheXdr = "ihe-xdr"

    """ IHE Cross-Enterprise Document Sharing (XDS) - http://wiki.ihe.net/index.php/Cross-Enterprise_Document_Sharing
    """
    iheXds = "ihe-xds"

    """ IHE Invoke Image Display (IID) - http://wiki.ihe.net/index.php/Invoke_Image_Display
    """
    iheIid = "ihe-iid"

    """ DICOMweb RESTful Image Retrieve - http://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect_6.5.html
    """
    dicomWadoRs = "dicom-wado-rs"

    """ DICOMweb RESTful Image query - http://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect_6.7.html
    """
    dicomQidoRs = "dicom-qido-rs"

    """ DICOMweb RESTful image sending and storage -
	/// http://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect_6.6.html
    """
    dicomStowRs = "dicom-stow-rs"

    """ DICOMweb Image Retrieve - http://dicom.nema.org/dicom/2013/output/chtml/part18/sect_6.3.html
    """
    dicomWadoUri = "dicom-wado-uri"

    """ Interact with the server interface using FHIR's RESTful interface. For details on its version/capabilities you
	/// should connect the value in Endpoint.address and retrieve the FHIR CapabilityStatement.
    """
    hl7FhirRest = "hl7-fhir-rest"

    """ Use the servers FHIR Messaging interface. Details can be found on the messaging.html page in the FHIR
	/// Specification. The FHIR server's base address is specified in the Endpoint.address property.
    """
    hl7FhirMsg = "hl7-fhir-msg"

    """ HL7v2 messages over an LLP TCP connection
    """
    hl7v2Mllp = "hl7v2-mllp"

    """ Email delivery using a digital certificate to encrypt the content using the public key, receiver must have the
	/// private key to decrypt the content
    """
    secureEmail = "secure-email"

    """ Direct Project information - http://wiki.directproject.org/
    """
    directProject = "direct-project"


class EndpointPayloadType(CodeSystemValue):
    """ This is an example value set defined by the FHIR project, that could be used to represent possible payload document
types.

    URL: http://hl7.org/fhir/endpoint-payload-type
    ValueSet: http://hl7.org/fhir/ValueSet/endpoint-payload-type
    """
    URL = "http://hl7.org/fhir/endpoint-payload-type"
    EXPERIMENTAL = True

    """ Any payload type can be used with this endpoint, it is either a payload agnostic infrastructure (such as a
	/// storage repository), or some other type of endpoint where payload considerations are internally handled, and not
	/// available
    """
    any = "any"

    """ This endpoint does not require any content to be sent, simply connecting to the endpoint is enough notification.
	/// This can be used as a 'ping' to wakeup a service to retrieve content, which could be to ensure security
	/// considerations are correctly handled
    """
    none = "none"


class EndpointStatus(CodeSystemValue):
    """ The status of the endpoint

    URL: http://hl7.org/fhir/endpoint-status
    ValueSet: http://hl7.org/fhir/ValueSet/endpoint-status
    """
    URL = "http://hl7.org/fhir/endpoint-status"
    EXPERIMENTAL = False

    """ This endpoint is expected to be active and can be used
    """
    active = "active"

    """ This endpoint is temporarily unavailable
    """
    suspended = "suspended"

    """ This endpoint has exceeded connectivity thresholds and is considered in an error state and should no longer be
	/// attempted to connect to until corrective action is taken
    """
    error = "error"

    """ This endpoint is no longer to be used
    """
    off = "off"

    """ This instance should not have been part of this patient's medical record.
    """
    enteredInError = "entered-in-error"

    """ This endpoint is not intended for production usage.
    """
    test = "test"


class EnteralFormulaAdditiveTypeCode(CodeSystemValue):
    """ EnteralFormulaAdditiveType: Codes for the type of modular component such as protein, carbohydrate or fiber to be
provided in addition to or mixed with the base formula. This value set is provided as a suggestive example.

    URL: http://hl7.org/fhir/entformula-additive
    ValueSet: http://hl7.org/fhir/ValueSet/entformula-additive
    """
    URL = "http://hl7.org/fhir/entformula-additive"
    EXPERIMENTAL = True

    """ Modular lipid enteral formula component
    """
    lipid = "lipid"

    """ Modular protein enteral formula component
    """
    protein = "protein"

    """ Modular carbohydrate enteral formula component
    """
    carbohydrate = "carbohydrate"

    """ Modular fiber enteral formula component
    """
    fiber = "fiber"

    """ Added water
    """
    water = "water"


class EpisodeOfCareStatus(CodeSystemValue):
    """ The status of the episode of care.

    URL: http://hl7.org/fhir/episode-of-care-status
    ValueSet: http://hl7.org/fhir/ValueSet/episode-of-care-status
    """
    URL = "http://hl7.org/fhir/episode-of-care-status"
    EXPERIMENTAL = False

    """ This episode of care is planned to start at the date specified in the period.start. During this status, an
	/// organization may perform assessments to determine if the patient is eligible to receive services, or be
	/// organizing to make resources available to provide care services.
    """
    planned = "planned"

    """ This episode has been placed on a waitlist, pending the episode being made active (or cancelled).
    """
    waitlist = "waitlist"

    """ This episode of care is current.
    """
    active = "active"

    """ This episode of care is on hold, the organization has limited responsibility for the patient (such as while on
	/// respite).
    """
    onhold = "onhold"

    """ This episode of care is finished and the organization is not expecting to be providing further care to the
	/// patient. Can also be known as "closed", "completed" or other similar terms.
    """
    finished = "finished"

    """ The episode of care was cancelled, or withdrawn from service, often selected during the planned stage as the
	/// patient may have gone elsewhere, or the circumstances have changed and the organization is unable to provide the
	/// care. It indicates that services terminated outside the planned/expected workflow.
    """
    cancelled = "cancelled"

    """ This instance should not have been part of this patient's medical record.
    """
    enteredInError = "entered-in-error"


class EpisodeOfCareType(CodeSystemValue):
    """ This example value set defines a set of codes that can be used to express the usage type of an EpisodeOfCare record.

    URL: http://hl7.org/fhir/episodeofcare-type
    ValueSet: http://hl7.org/fhir/ValueSet/episodeofcare-type
    """
    URL = "http://hl7.org/fhir/episodeofcare-type"
    EXPERIMENTAL = True

    """ hacc
    """
    hacc = "hacc"

    """ pac
    """
    pac = "pac"

    """ diab
    """
    diab = "diab"

    """ da
    """
    da = "da"

    """ cacp
    """
    cacp = "cacp"


class EventCapabilityMode(CodeSystemValue):
    """ The mode of a message capability statement.

    URL: http://hl7.org/fhir/event-capability-mode
    ValueSet: http://hl7.org/fhir/ValueSet/event-capability-mode
    """
    URL = "http://hl7.org/fhir/event-capability-mode"
    EXPERIMENTAL = False

    """ The application sends requests and receives responses.
    """
    sender = "sender"

    """ The application receives requests and sends responses.
    """
    receiver = "receiver"


class EventStatus(CodeSystemValue):
    """ Codes identifying the lifecycle stage of a event

    URL: http://hl7.org/fhir/event-status
    ValueSet: http://hl7.org/fhir/ValueSet/event-status
    """
    URL = "http://hl7.org/fhir/event-status"
    EXPERIMENTAL = False

    """ The core event has not started yet, but some staging activities have begun (e.g. surgical suite preparation).
	/// Preparation stages may be tracked for billing purposes.
    """
    preparation = "preparation"

    """ The event is currently occurring
    """
    inProgress = "in-progress"

    """ The event was terminated prior to any impact on the subject (though preparatory actions may have been taken)
    """
    notDone = "not-done"

    """ The event has been temporarily stopped but is expected to resume in the future
    """
    suspended = "suspended"

    """ The event was  terminated prior to the full completion of the intended actions but after having at least some
	/// impact on the subject.
    """
    aborted = "aborted"

    """ The event has now concluded
    """
    completed = "completed"

    """ This electronic record should never have existed, though it is possible that real-world decisions were based on
	/// it.  (If real-world activity has occurred, the status should be "cancelled" rather than "entered-in-error".)
    """
    enteredInError = "entered-in-error"

    """ The authoring system does not know which of the status values currently applies for this request.  Note: This
	/// concept is not to be used for "other" - one of the listed statuses is presumed to apply, it's just not known
	/// which one.
    """
    unknown = "unknown"


class EventTiming(CodeSystemValue):
    """ Real world event relating to the schedule.

    URL: http://hl7.org/fhir/event-timing
    ValueSet: http://hl7.org/fhir/ValueSet/event-timing
    """
    URL = "http://hl7.org/fhir/event-timing"
    EXPERIMENTAL = False

    """ Event occurs during the morning. The exact time is unspecified and established by institution convention or
	/// patient interpretation
    """
    MORN = "MORN"

    """ Event occurs during the early morning. The exact time is unspecified and established by institution convention
	/// or patient interpretation
    """
    mORNEarly = "MORN.early"

    """ Event occurs during the late morning. The exact time is unspecified and established by institution convention or
	/// patient interpretation
    """
    mORNLate = "MORN.late"

    """ Event occurs around 12:00pm. The exact time is unspecified and established by institution convention or patient
	/// interpretation
    """
    NOON = "NOON"

    """ Event occurs during the afternoon. The exact time is unspecified and established by institution convention or
	/// patient interpretation
    """
    AFT = "AFT"

    """ Event occurs during the early afternoon. The exact time is unspecified and established by institution convention
	/// or patient interpretation
    """
    aFTEarly = "AFT.early"

    """ Event occurs during the late afternoon. The exact time is unspecified and established by institution convention
	/// or patient interpretation
    """
    aFTLate = "AFT.late"

    """ Event occurs during the evening. The exact time is unspecified and established by institution convention or
	/// patient interpretation
    """
    EVE = "EVE"

    """ Event occurs during the early evening. The exact time is unspecified and established by institution convention
	/// or patient interpretation
    """
    eVEEarly = "EVE.early"

    """ Event occurs during the late evening. The exact time is unspecified and established by institution convention or
	/// patient interpretation
    """
    eVELate = "EVE.late"

    """ Event occurs during the night. The exact time is unspecified and established by institution convention or
	/// patient interpretation
    """
    NIGHT = "NIGHT"

    """ Event occurs [offset] after subject goes to sleep. The exact time is unspecified and established by institution
	/// convention or patient interpretation
    """
    PHS = "PHS"


class ExampleClaimSubTypeCodes(CodeSystemValue):
    """ This value set includes sample Claim SubType codes which are used to distinguish the claim types for example within type
institutional there may be subtypes for emergency services, bedstay and transportation.

    URL: http://hl7.org/fhir/ex-claimsubtype
    ValueSet: http://hl7.org/fhir/ValueSet/claim-subtype
    """
    URL = "http://hl7.org/fhir/ex-claimsubtype"
    EXPERIMENTAL = True

    """ A claim for Orthodontic Services.
    """
    ortho = "ortho"

    """ A claim for emergency services.
    """
    emergency = "emergency"


class ExampleDiagnosisTypeCodes(CodeSystemValue):
    """ This value set includes example Diagnosis Type codes.

    URL: http://hl7.org/fhir/ex-diagnosistype
    ValueSet: http://hl7.org/fhir/ValueSet/ex-diagnosistype
    """
    URL = "http://hl7.org/fhir/ex-diagnosistype"
    EXPERIMENTAL = True

    """ The diagnosis given as the reason why the patient was admitted to the hospital.
    """
    admitting = "admitting"

    """ A diagnosis made on the basis of medical signs and patient-reported symptoms, rather than diagnostic tests.
    """
    clinical = "clinical"

    """ One of a set of the possible diagnoses that could be connected to the signs, symptoms, and lab findings.
    """
    differential = "differential"

    """ The diagnosis given when the patient is discharged from the hospital.
    """
    discharge = "discharge"

    """ A diagnosis based significantly on laboratory reports or test results, rather than the physical examination of
	/// the patient.
    """
    laboratory = "laboratory"

    """ A diagnosis which identifies people's responses to situations in their lives, such as a readiness to change or a
	/// willingness to accept assistance.
    """
    nursing = "nursing"

    """ A diagnosis determined prior to birth.
    """
    prenatal = "prenatal"

    """ The single medical diagnosis that is most relevant to the patient's chief complaint or need for treatment.
    """
    principal = "principal"

    """ A diagnosis based primarily on the results from medical imaging studies.
    """
    radiology = "radiology"

    """ A diagnosis determined using telemedicine techniques.
    """
    remote = "remote"

    """ The labeling of an illness in a specific historical event using modern knowledge, methods and disease
	/// classifications.
    """
    retrospective = "retrospective"

    """ A diagnosis determined by the patient.
    """
    self = "self"


class ExampleMessageReasonCodes(CodeSystemValue):
    """ Example Message Reasons. These are the set of codes that might be used an updating an encounter using admin-update.

    URL: http://hl7.org/fhir/message-reasons-encounter
    ValueSet: http://hl7.org/fhir/ValueSet/message-reason-encounter
    """
    URL = "http://hl7.org/fhir/message-reasons-encounter"
    EXPERIMENTAL = True

    """ The patient has been admitted.
    """
    admit = "admit"

    """ The patient has been discharged.
    """
    discharge = "discharge"

    """ The patient has temporarily left the institution.
    """
    absent = "absent"

    """ The patient has returned from a temporary absence.
    """
    _return = "return"

    """ The patient has been moved to a new location.
    """
    moved = "moved"

    """ Encounter details have been updated (e.g. to correct a coding error).
    """
    edit = "edit"


class ExampleOnsetTypeReasonCodes(CodeSystemValue):
    """ This value set includes example Onset Type codes which are used to identify the event for which the onset, starting
date, is required.

    URL: http://hl7.org/fhir/ex-onsettype
    ValueSet: http://hl7.org/fhir/ValueSet/ex-onsettype
    """
    URL = "http://hl7.org/fhir/ex-onsettype"
    EXPERIMENTAL = True

    """ Date of last examination.
    """
    lxm = "lxm"

    """ Date when symptoms were first noticed.
    """
    sym = "sym"

    """ Start date of last menstruation.
    """
    lmn = "lmn"


class ExamplePaymentTypeCodes(CodeSystemValue):
    """ This value set includes example Payment Type codes.

    URL: http://hl7.org/fhir/ex-paymenttype
    ValueSet: http://hl7.org/fhir/ValueSet/ex-paymenttype
    """
    URL = "http://hl7.org/fhir/ex-paymenttype"
    EXPERIMENTAL = True

    """ Complete (final) payment of the benefit under the Claim less any adjustments.
    """
    complete = "complete"

    """ Partial payment of the benefit under the Claim less any adjustments.
    """
    partial = "partial"


class ExamplePharmacyServiceCodes(CodeSystemValue):
    """ This value set includes a smattering of Pharmacy Service codes.

    URL: http://hl7.org/fhir/ex-pharmaservice
    ValueSet: http://hl7.org/fhir/ValueSet/service-pharmacy
    """
    URL = "http://hl7.org/fhir/ex-pharmaservice"
    EXPERIMENTAL = True

    """ Smoking cessation
    """
    smokecess = "smokecess"

    """ Flu Shot
    """
    flushot = "flushot"

    """ The wholesale price of the medication.
    """
    drugcost = "drugcost"

    """ The additional cost assessed on the drug.
    """
    markup = "markup"

    """ The professional fee charged for dispensing the product or service.
    """
    dispensefee = "dispensefee"

    """ The professional fee charged for compounding the medication.
    """
    compoundfee = "compoundfee"


class ExampleProgramReasonCodes(CodeSystemValue):
    """ This value set includes sample Program Reason Span codes.

    URL: http://hl7.org/fhir/ex-programcode
    ValueSet: http://hl7.org/fhir/ValueSet/ex-program-code
    """
    URL = "http://hl7.org/fhir/ex-programcode"
    EXPERIMENTAL = True

    """ Child Asthma Program
    """
    _as = "as"

    """ Hemodialysis Program.
    """
    hd = "hd"

    """ Autism Screening Program.
    """
    auscr = "auscr"

    """ No program code applies.
    """
    none = "none"


class ExampleRelatedClaimRelationshipCodes(CodeSystemValue):
    """ This value set includes sample Related Claim Relationship codes.

    URL: http://hl7.org/fhir/ex-relatedclaimrelationship
    ValueSet: http://hl7.org/fhir/ValueSet/related-claim-relationship
    """
    URL = "http://hl7.org/fhir/ex-relatedclaimrelationship"
    EXPERIMENTAL = True

    """ A prior claim instance for the same intended suite of services.
    """
    prior = "prior"

    """ A claim for a different suite of services which is related the suite claimed here.
    """
    associated = "associated"


class ExampleScenarioActorType(CodeSystemValue):
    """ The type of actor - system or human

    URL: http://hl7.org/fhir/examplescenario-actor-type
    ValueSet: http://hl7.org/fhir/ValueSet/examplescenario-actor-type
    """
    URL = "http://hl7.org/fhir/examplescenario-actor-type"
    EXPERIMENTAL = False

    """ A person
    """
    person = "person"

    """ A system
    """
    entity = "entity"


class ExampleServiceModifierCodes(CodeSystemValue):
    """ This value set includes sample Service Modifier codes which may support differential payment.

    URL: http://hl7.org/fhir/ex-servicemodifier
    ValueSet: http://hl7.org/fhir/ValueSet/service-modifiers
    """
    URL = "http://hl7.org/fhir/ex-servicemodifier"
    EXPERIMENTAL = True

    """ Services provided on the side of the road or such other non-conventional setting.
    """
    sr = "sr"

    """ Services provided outside or normal business hours.
    """
    ah = "ah"


class ExampleServiceProductCodes(CodeSystemValue):
    """ This value set includes a smattering of Service/Product codes.

    URL: http://hl7.org/fhir/ex-serviceproduct
    ValueSet: http://hl7.org/fhir/ValueSet/service-product
    """
    URL = "http://hl7.org/fhir/ex-serviceproduct"
    EXPERIMENTAL = True

    """ Exam
    """
    exam = "exam"

    """ Flu shot
    """
    flushot = "flushot"


class ExampleUseCodesForList(CodeSystemValue):
    """ Example use codes for the List resource - typical kinds of use.

    URL: http://hl7.org/fhir/list-example-use-codes
    ValueSet: http://hl7.org/fhir/ValueSet/list-example-codes
    """
    URL = "http://hl7.org/fhir/list-example-use-codes"
    EXPERIMENTAL = True

    """ A list of alerts for the patient.
    """
    alerts = "alerts"

    """ A list of part adverse reactions.
    """
    adverserxns = "adverserxns"

    """ A list of Allergies for the patient.
    """
    allergies = "allergies"

    """ A list of medication statements for the patient.
    """
    medications = "medications"

    """ A list of problems that the patient is known of have (or have had in the past).
    """
    problems = "problems"

    """ A list of items that constitute a set of work to be performed (typically this code would be specialized for more
	/// specific uses, such as a ward round list).
    """
    worklist = "worklist"

    """ A list of items waiting for an event (perhaps a surgical patient waiting list).
    """
    waiting = "waiting"

    """ A set of protocols to be followed.
    """
    protocols = "protocols"

    """ A set of care plans that apply in a particular context of care.
    """
    plans = "plans"


class ExampleVisionPrescriptionProductCodes(CodeSystemValue):
    """ This value set includes a smattering of Prescription Product codes.

    URL: http://hl7.org/fhir/ex-visionprescriptionproduct
    ValueSet: http://hl7.org/fhir/ValueSet/vision-product
    """
    URL = "http://hl7.org/fhir/ex-visionprescriptionproduct"
    EXPERIMENTAL = True

    """ A lens to be fitted to a frame to comprise a pair of glasses.
    """
    lens = "lens"

    """ A lens to be fitted for wearing directly on an eye.
    """
    contact = "contact"


class ExceptionCodes(CodeSystemValue):
    """ This value set includes sample Exception codes.

    URL: http://hl7.org/fhir/claim-exception
    ValueSet: http://hl7.org/fhir/ValueSet/claim-exception
    """
    URL = "http://hl7.org/fhir/claim-exception"
    EXPERIMENTAL = True

    """ Fulltime Student
    """
    student = "student"

    """ Disabled
    """
    disabled = "disabled"


class ExplanationOfBenefitStatus(CodeSystemValue):
    """ A code specifying the state of the resource instance.

    URL: http://hl7.org/fhir/explanationofbenefit-status
    ValueSet: http://hl7.org/fhir/ValueSet/explanationofbenefit-status
    """
    URL = "http://hl7.org/fhir/explanationofbenefit-status"
    EXPERIMENTAL = False

    """ The resource instance is currently in-force.
    """
    active = "active"

    """ The resource instance is withdrawn, rescinded or reversed.
    """
    cancelled = "cancelled"

    """ A new resource instance the contents of which is not complete.
    """
    draft = "draft"

    """ The resource instance was entered in error.
    """
    enteredInError = "entered-in-error"


class ExpressionLanguage(CodeSystemValue):
    """ The media type of the expression language

    URL: http://hl7.org/fhir/expression-language
    ValueSet: http://hl7.org/fhir/ValueSet/expression-language
    """
    URL = "http://hl7.org/fhir/expression-language"
    EXPERIMENTAL = False

    """ Clinical Quality Language
    """
    textCql = "text/cql"

    """ FHIRPath
    """
    textFhirpath = "text/fhirpath"


class ExtensionContextType(CodeSystemValue):
    """ How an extension context is interpreted.

    URL: http://hl7.org/fhir/extension-context-type
    ValueSet: http://hl7.org/fhir/ValueSet/extension-context-type
    """
    URL = "http://hl7.org/fhir/extension-context-type"
    EXPERIMENTAL = False

    """ The context is all elements that match the FHIRPath query found in the expression.
    """
    fhirpath = "fhirpath"

    """ The context is any element that has an ElementDefinition.id that matches that found in the expression. This
	/// includes ElementDefinition Ids that have slicing identifiers. The full path for the element is
	/// [url]#[elementid]. If there is no #, the Element id is one defined in the base specification
    """
    element = "element"

    """ The context is a particular extension from a particular profile, and the expression is just a uri that
	/// identifies the extension
    """
    extension = "extension"


class ExtraActivityType(CodeSystemValue):
    """ This value set includes coded concepts not well covered in any of the included valuesets.

    URL: http://hl7.org/fhir/extra-activity-type
    """
    URL = "http://hl7.org/fhir/extra-activity-type"
    EXPERIMENTAL = True

    """ Activity resulting in a structured collection of preexisting content that does not necessarily result in an
	/// integral object with semantic context making it more than the sum of component parts, from which components
	/// could be disaggregated without loss of semantic context, e.g., the assembly of multiple stand-alone documents.
    """
    aggregate = "aggregate"

    """ Activity resulting in the structured compilation of new and preexisting content for the purposes of forming an
	/// integral object with  semantic context making it more than the sum of component parts, which would be lost if
	/// decomposed. For example, the composition of a document that includes in whole or part other documents along with
	/// new content that result in a new document that has unique semantic meaning.
    """
    compose = "compose"

    """ The means used to associate a set of security attributes with a specific information object as part of the data
	/// structure for that object. [ISO-10181-3 Access Control]
    """
    label = "label"


class FHIRDefinedConceptProperties(CodeSystemValue):
    """ A set of common concept properties for use on coded systems throughout the FHIR eco-system.

    URL: http://hl7.org/fhir/concept-properties
    ValueSet: http://hl7.org/fhir/ValueSet/concept-properties
    """
    URL = "http://hl7.org/fhir/concept-properties"

    """ True if the concept is not considered active - e.g. not a valid concept any more. Property type is boolean,
	/// default value is false
    """
    inactive = "inactive"

    """ The date at which a concept was deprecated. Concepts that are deprecated but not inactive can still be used, but
	/// their use is discouraged, and they should be expected to be made inactive in a future release. Property type is
	/// dateTime
    """
    deprecated = "deprecated"

    """ The concept is not intended to be chosen by the user - only intended to be used as a selector for other
	/// concepts. Note, though, that the interpretation of this is highly contextual; all concepts are selectable in
	/// some context. Property type is boolean
    """
    notSelectable = "notSelectable"

    """ The concept identified in this property is a parent of the concept on which it is a property. The property type
	/// will be 'code'. The meaning of 'parent' is defined by the hierarchyMeaning attribute
    """
    parent = "parent"

    """ The concept identified in this property is a child of the concept on which it is a property. The property type
	/// will be 'code'. The meaning of 'child' is defined by the hierarchyMeaning attribute
    """
    child = "child"


class FHIRDeviceStatus(CodeSystemValue):
    """ The availability status of the device.

    URL: http://hl7.org/fhir/device-status
    ValueSet: http://hl7.org/fhir/ValueSet/device-status
    """
    URL = "http://hl7.org/fhir/device-status"
    EXPERIMENTAL = False

    """ The device is available for use.  Note: For *implanted devices*  this means that the device is implanted in the
	/// patient.
    """
    active = "active"

    """ The device is no longer available for use (e.g. lost, expired, damaged).  Note: For *implanted devices*  this
	/// means that the device has been removed from the patient.
    """
    inactive = "inactive"

    """ The device was entered in error and voided.
    """
    enteredInError = "entered-in-error"

    """ The status of the device has not been determined.
    """
    unknown = "unknown"


class FHIRRestfulInteractions(CodeSystemValue):
    """ The set of interactions defined by the RESTful part of the FHIR specification.

    URL: http://hl7.org/fhir/restful-interaction
    ValueSet: http://hl7.org/fhir/ValueSet/restful-interaction
    """
    URL = "http://hl7.org/fhir/restful-interaction"

    """ Read the current state of the resource.
    """
    read = "read"

    """ Read the state of a specific version of the resource.
    """
    vread = "vread"

    """ Update an existing resource by its id (or create it if it is new).
    """
    update = "update"

    """ Update an existing resource by posting a set of changes to it.
    """
    patch = "patch"

    """ Delete a resource.
    """
    delete = "delete"

    """ Retrieve the change history for a particular resource, type of resource, or the entire system.
    """
    history = "history"

    """ Retrieve the change history for a particular resource.
    """
    historyInstance = "history-instance"

    """ Retrieve the change history for all resources of a particular type.
    """
    historyType = "history-type"

    """ Retrieve the change history for all resources on a system.
    """
    historySystem = "history-system"

    """ Create a new resource with a server assigned id.
    """
    create = "create"

    """ Search a resource type or all resources based on some filter criteria.
    """
    search = "search"

    """ Search all resources of the specified type based on some filter criteria.
    """
    searchType = "search-type"

    """ Search all resources based on some filter criteria.
    """
    searchSystem = "search-system"

    """ Get a Capability Statement for the system.
    """
    capabilities = "capabilities"

    """ Update, create or delete a set of resources as a single transaction.
    """
    transaction = "transaction"

    """ perform a set of a separate interactions in a single http operation
    """
    batch = "batch"

    """ Perform an operation as defined by an OperationDefinition.
    """
    operation = "operation"


class FHIRSubstanceStatus(CodeSystemValue):
    """ A code to indicate if the substance is actively used

    URL: http://hl7.org/fhir/substance-status
    ValueSet: http://hl7.org/fhir/ValueSet/substance-status
    """
    URL = "http://hl7.org/fhir/substance-status"
    EXPERIMENTAL = False

    """ The substance is considered for use or reference
    """
    active = "active"

    """ The substance is considered for reference, but not for use
    """
    inactive = "inactive"

    """ The substance was entered in error
    """
    enteredInError = "entered-in-error"


class FailureAction(CodeSystemValue):
    """ The result if validation fails

    URL: http://hl7.org/fhir/failure-action
    ValueSet: http://hl7.org/fhir/ValueSet/failure-action
    """
    URL = "http://hl7.org/fhir/failure-action"
    EXPERIMENTAL = False

    """ fatal
    """
    fatal = "fatal"

    """ warn
    """
    warn = "warn"

    """ recOnly
    """
    recOnly = "rec-only"

    """ none
    """
    none = "none"


class FamilyHistoryAbsentReason(CodeSystemValue):
    """ Codes describing the reason why a family member's history is not available.

    URL: http://hl7.org/fhir/history-absent-reason
    ValueSet: http://hl7.org/fhir/ValueSet/history-absent-reason
    """
    URL = "http://hl7.org/fhir/history-absent-reason"
    EXPERIMENTAL = False

    """ Patient does not know the subject, e.g. the biological parent of an adopted patient.
    """
    subjectUnknown = "subject-unknown"

    """ The patient withheld or refused to share the information.
    """
    withheld = "withheld"

    """ Information cannot be obtained; e.g. unconscious patient
    """
    unableToObtain = "unable-to-obtain"

    """ Patient does not have the information now, but can provide the information at a later date.
    """
    deferred = "deferred"


class FamilyHistoryStatus(CodeSystemValue):
    """ A code that identifies the status of the family history record.

    URL: http://hl7.org/fhir/history-status
    ValueSet: http://hl7.org/fhir/ValueSet/history-status
    """
    URL = "http://hl7.org/fhir/history-status"
    EXPERIMENTAL = False

    """ Some health information is known and captured, but not complete - see notes for details.
    """
    partial = "partial"

    """ All available related health information is captured as of the date (and possibly time) when the family member
	/// history was taken.
    """
    completed = "completed"

    """ This instance should not have been part of this patient's medical record.
    """
    enteredInError = "entered-in-error"

    """ Health information for this individual is unavailable/unknown.
    """
    healthUnknown = "health-unknown"


class FeedingDeviceCodes(CodeSystemValue):
    """ Materials used or needed to feed the patient.

    URL: http://hl7.org/fhir/feeding-device
    ValueSet: http://hl7.org/fhir/ValueSet/feeding-device
    """
    URL = "http://hl7.org/fhir/feeding-device"
    EXPERIMENTAL = True

    """ Standard nipple definition:
    """
    standardNipple = "standard-nipple"

    """ Preemie nipple definition:
    """
    preemieNipple = "preemie-nipple"

    """ Orthodontic nipple definition:
    """
    orthoNipple = "ortho-nipple"

    """ Slow flow nipple definition:
    """
    slofloNipple = "sloflo-nipple"

    """ Middle flow nipple definition:
    """
    midfloNipple = "midflo-nipple"

    """ Enlarged, cross-cut nipple definition:
    """
    bigcutNipple = "bigcut-nipple"

    """ Haberman bottle definition:
    """
    habermanBottle = "haberman-bottle"

    """ Sippy cup with valve definition:
    """
    sippyValve = "sippy-valve"

    """ Sippy cup without valve definition:
    """
    sippyNoValve = "sippy-no-valve"

    """ Provale Cup definition:
    """
    provaleCup = "provale-cup"

    """ Glass with lid/sippy cup definition:
    """
    glassLid = "glass-lid"

    """ Double handhold on glass/cup definition:
    """
    handholdCup = "handhold-cup"

    """ Rubber matting under tray definition:
    """
    rubberMat = "rubber-mat"

    """ Straw definition:
    """
    straw = "straw"

    """ Nose cup definition:
    """
    noseCup = "nose-cup"

    """ Scoop plate definition:
    """
    scoopPlate = "scoop-plate"

    """ Hand wrap utensil holder definition:
    """
    utensilHolder = "utensil-holder"

    """ Foam handle utensils definition:
    """
    foamHandle = "foam-handle"

    """ Angled utensils definition:
    """
    angledUtensil = "angled-utensil"

    """ Spout cup definition:
    """
    spoutCup = "spout-cup"

    """ Automated feeding devices definition:
    """
    autofeedingDevice = "autofeeding-device"

    """ Rocker knife definition:
    """
    rockerKnife = "rocker-knife"


class FilterOperator(CodeSystemValue):
    """ The kind of operation to perform as a part of a property based filter.

    URL: http://hl7.org/fhir/filter-operator
    ValueSet: http://hl7.org/fhir/ValueSet/filter-operator
    """
    URL = "http://hl7.org/fhir/filter-operator"
    EXPERIMENTAL = False

    """ The specified property of the code equals the provided value.
    """
    eq = "="

    """ Includes all concept ids that have a transitive is-a relationship with the concept Id provided as the value,
	/// including the provided concept itself (i.e. include child codes)
    """
    isA = "is-a"

    """ Includes all concept ids that have a transitive is-a relationship with the concept Id provided as the value,
	/// excluding the provided concept itself (i.e. include child codes)
    """
    descendentOf = "descendent-of"

    """ The specified property of the code does not have an is-a relationship with the provided value.
    """
    isNotA = "is-not-a"

    """ The specified property of the code  matches the regex specified in the provided value.
    """
    regex = "regex"

    """ The specified property of the code is in the set of codes or concepts specified in the provided value (comma
	/// separated list).
    """
    _in = "in"

    """ The specified property of the code is not in the set of codes or concepts specified in the provided value (comma
	/// separated list).
    """
    notIn = "not-in"

    """ Includes all concept ids that have a transitive is-a relationship from the concept Id provided as the value,
	/// including the provided concept itself (e.g. include parent codes)
    """
    generalizes = "generalizes"

    """ The specified property of the code has at least one value (if the specified value is true; if the specified
	/// value is false, then matches when the specified property of the code has no values)
    """
    exists = "exists"


class FinancialResourceStatusCodes(CodeSystemValue):
    """ This value set includes Status codes.

    URL: http://hl7.org/fhir/fm-status
    ValueSet: http://hl7.org/fhir/ValueSet/fm-status
    """
    URL = "http://hl7.org/fhir/fm-status"
    EXPERIMENTAL = True

    """ The instance is currently in-force.
    """
    active = "active"

    """ The instance is withdrawn, rescinded or reversed.
    """
    cancelled = "cancelled"

    """ A new instance the contents of which is not complete.
    """
    draft = "draft"

    """ The instance was entered in error.
    """
    enteredInError = "entered-in-error"


class FlagCategory(CodeSystemValue):
    """ Example list of general categories for flagged issues. (Not complete or necessarily appropriate.)

    URL: http://hl7.org/fhir/flag-category
    ValueSet: http://hl7.org/fhir/ValueSet/flag-category
    """
    URL = "http://hl7.org/fhir/flag-category"
    EXPERIMENTAL = True

    """ Flags related to the subject's dietary needs.
    """
    diet = "diet"

    """ Flags related to the subject's medications.
    """
    drug = "drug"

    """ Flags related to performing laboratory tests and related processes (e.g. phlebotomy).
    """
    lab = "lab"

    """ Flags related to administrative and financial processes.
    """
    admin = "admin"

    """ Flags related to coming into contact with the patient.
    """
    contact = "contact"

    """ Flags related to the subject's clinical data.
    """
    clinical = "clinical"

    """ Flags related to behavior.
    """
    behavioral = "behavioral"

    """ Flags related to research.
    """
    research = "research"

    """ Flags related to subject's advance directives.
    """
    advanceDirective = "advance-directive"

    """ Flags related to safety precautions.
    """
    safety = "safety"


class FlagPriorityCodes(CodeSystemValue):
    """ This value set is provided as an exemplar. The value set is driven by IHE Table B.8-4: Abnormal Flags, Alert Priority.

    URL: http://hl7.org/fhir/flag-priority-code
    ValueSet: http://hl7.org/fhir/ValueSet/flag-priority
    """
    URL = "http://hl7.org/fhir/flag-priority-code"
    EXPERIMENTAL = True

    """ No alarm.
    """
    PN = "PN"

    """ Low priority.
    """
    PL = "PL"

    """ Medium priority.
    """
    PM = "PM"

    """ High priority.
    """
    PH = "PH"


class FlagStatus(CodeSystemValue):
    """ Indicates whether this flag is active and needs to be displayed to a user, or whether it is no longer needed or entered
in error.

    URL: http://hl7.org/fhir/flag-status
    ValueSet: http://hl7.org/fhir/ValueSet/flag-status
    """
    URL = "http://hl7.org/fhir/flag-status"
    EXPERIMENTAL = False

    """ A current flag that should be displayed to a user. A system may use the category to determine which roles should
	/// view the flag.
    """
    active = "active"

    """ The flag does not need to be displayed any more.
    """
    inactive = "inactive"

    """ The flag was added in error, and should no longer be displayed.
    """
    enteredInError = "entered-in-error"


class FundsReservationCodes(CodeSystemValue):
    """ This value set includes sample funds reservation type codes.

    URL: http://hl7.org/fhir/fundsreserve
    ValueSet: http://hl7.org/fhir/ValueSet/fundsreserve
    """
    URL = "http://hl7.org/fhir/fundsreserve"
    EXPERIMENTAL = True

    """ The payor is requested to reserve funds for the provision of the named services by any provider for settlement
	/// of future claims related to this request.
    """
    patient = "patient"

    """ The payor is requested to reserve funds solely for the named provider for settlement of future claims related to
	/// this request.
    """
    provider = "provider"

    """ The payor is not being requested to reserve any funds for the settlement of future claims.
    """
    none = "none"


class GenderIdentity(CodeSystemValue):
    """ This example value set defines a set of codes that can be used to indicate a patient's gender identity.

    URL: http://hl7.org/fhir/gender-identity
    ValueSet: http://hl7.org/fhir/ValueSet/gender-identity
    """
    URL = "http://hl7.org/fhir/gender-identity"
    EXPERIMENTAL = True

    """ the patient identifies as transgender male-to-female
    """
    transgenderFemale = "transgender-female"

    """ the patient identifies as transgender female-to-male
    """
    transgenderMale = "transgender-male"

    """ the patient identifies with neither/both female and male
    """
    nonBinary = "non-binary"

    """ the patient identifies as male
    """
    male = "male"

    """ the patient identifies as female
    """
    female = "female"

    """ other gender identity
    """
    other = "other"

    """ the patient does not wish to disclose his gender identity
    """
    nonDisclose = "non-disclose"


class GenderStatus(CodeSystemValue):
    """ This example value set defines a set of codes that can be used to indicate the current state of the animal's
reproductive organs.

    URL: http://hl7.org/fhir/animal-genderstatus
    ValueSet: http://hl7.org/fhir/ValueSet/animal-genderstatus
    """
    URL = "http://hl7.org/fhir/animal-genderstatus"
    EXPERIMENTAL = True

    """ The animal has been sterilized, castrated or otherwise made infertile.
    """
    neutered = "neutered"

    """ The animal's reproductive organs are intact.
    """
    intact = "intact"

    """ Unable to determine whether the animal has been neutered.
    """
    unknown = "unknown"


class GoalAcceptanceStatus(CodeSystemValue):
    """ Codes indicating whether the goal has been accepted by a stakeholder

    URL: http://hl7.org/fhir/goal-acceptance-status
    ValueSet: http://hl7.org/fhir/ValueSet/goal-acceptance-status
    """
    URL = "http://hl7.org/fhir/goal-acceptance-status"
    EXPERIMENTAL = False

    """ Stakeholder supports pursuit of the goal
    """
    agree = "agree"

    """ Stakeholder is not in support of the pursuit of the goal
    """
    disagree = "disagree"

    """ Stakeholder has not yet made a decision on whether they support the goal
    """
    pending = "pending"


class GoalCategory(CodeSystemValue):
    """ Example codes for grouping goals for filtering or presentation.

    URL: http://hl7.org/fhir/goal-category
    ValueSet: http://hl7.org/fhir/ValueSet/goal-category
    """
    URL = "http://hl7.org/fhir/goal-category"
    EXPERIMENTAL = True

    """ Goals related to the consumption of food and/or beverages.
    """
    dietary = "dietary"

    """ Goals related to the personal protection of the subject.
    """
    safety = "safety"

    """ Goals related to the manner in which the subject acts.
    """
    behavioral = "behavioral"

    """ Goals related to the practice of nursing or established by nurses.
    """
    nursing = "nursing"

    """ Goals related to the mobility and motor capability of the subject.
    """
    physiotherapy = "physiotherapy"


class GoalPriority(CodeSystemValue):
    """ Indicates the level of importance associated with reaching or sustaining a goal.

    URL: http://hl7.org/fhir/goal-priority
    ValueSet: http://hl7.org/fhir/ValueSet/goal-priority
    """
    URL = "http://hl7.org/fhir/goal-priority"
    EXPERIMENTAL = True

    """ Indicates that the goal is of considerable importance and should be a primary focus of care delivery.
    """
    highPriority = "high-priority"

    """ Indicates that the goal has a reasonable degree of importance and that concrete action should be taken towards
	/// the goal.  Attainment is not as critical as high-priority goals.
    """
    mediumPriority = "medium-priority"

    """ The goal is desirable but is not sufficiently important to devote significant resources to.  Achievement of the
	/// goal may be sought when incidental to achieving other goals.
    """
    lowPriority = "low-priority"


class GoalRelationshipType(CodeSystemValue):
    """ Types of relationships between two goals

    URL: http://hl7.org/fhir/goal-relationship-type
    ValueSet: http://hl7.org/fhir/ValueSet/goal-relationship-type
    """
    URL = "http://hl7.org/fhir/goal-relationship-type"
    EXPERIMENTAL = False

    """ Indicates that the target goal is one which must be met before striving for the current goal
    """
    predecessor = "predecessor"

    """ Indicates that the target goal is a desired objective once the current goal is met
    """
    successor = "successor"

    """ Indicates that this goal has been replaced by the target goal
    """
    replacement = "replacement"

    """ Indicates that the target goal is considered to be a "piece" of attaining this goal.
    """
    milestone = "milestone"

    """ Indicates that the relationship is not covered by one of the pre-defined codes.  (An extension may convey more
	/// information about the meaning of the relationship.)
    """
    other = "other"


class GoalStatus(CodeSystemValue):
    """ Indicates whether the goal has been met and is still being targeted

    URL: http://hl7.org/fhir/goal-status
    ValueSet: http://hl7.org/fhir/ValueSet/goal-status
    """
    URL = "http://hl7.org/fhir/goal-status"
    EXPERIMENTAL = False

    """ A goal is proposed for this patient
    """
    proposed = "proposed"

    """ A proposed goal was accepted or acknowledged
    """
    accepted = "accepted"

    """ A goal is planned for this patient
    """
    planned = "planned"

    """ The goal is being sought but has not yet been reached.  (Also applies if goal was reached in the past but there
	/// has been regression and goal is being sought again)
    """
    inProgress = "in-progress"

    """ The goal is on schedule for the planned timelines
    """
    onTarget = "on-target"

    """ The goal is ahead of the planned timelines
    """
    aheadOfTarget = "ahead-of-target"

    """ The goal is behind the planned timelines
    """
    behindTarget = "behind-target"

    """ The goal has been met, but ongoing activity is needed to sustain the goal objective
    """
    sustaining = "sustaining"

    """ The goal has been met and no further action is needed
    """
    achieved = "achieved"

    """ The goal remains a long term objective but is no longer being actively pursued for a temporary period of time.
    """
    onHold = "on-hold"

    """ The previously accepted goal is no longer being sought
    """
    cancelled = "cancelled"

    """ The goal was entered in error and voided.
    """
    enteredInError = "entered-in-error"

    """ A proposed goal was rejected
    """
    rejected = "rejected"


class GoalStatusReason(CodeSystemValue):
    """ Example codes indicating the reason for a current status.  Note that these are in no way complete and might not even be
appropriate for some uses.

    URL: http://hl7.org/fhir/goal-status-reason
    ValueSet: http://hl7.org/fhir/ValueSet/goal-status-reason
    """
    URL = "http://hl7.org/fhir/goal-status-reason"
    EXPERIMENTAL = True

    """ Goal suspended or ended because of a surgical procedure.
    """
    surgery = "surgery"

    """ Goal suspended or ended because of a significant life event (marital change, bereavement, etc.).
    """
    lifeEvent = "life-event"

    """ Goal has been superseded by a new goal.
    """
    replaced = "replaced"

    """ Patient wishes the goal to be set aside, at least temporarily.
    """
    patientRequest = "patient-request"

    """ Goal cannot be reached temporarily.
    """
    tempNotAttainable = "temp-not-attainable"

    """ Goal cannot be reached permanently.
    """
    permanentNotAttainable = "permanent-not-attainable"

    """ Goal cannot be reached due to financial barrier or reason.
    """
    financialBarrier = "financial-barrier"

    """ Goal cannot be reached due to a lack of transportation.
    """
    lackOfTransportation = "lack-of-transportation"

    """ Goal cannot be reached due to a lack of social support.
    """
    lackOfSocialSupport = "lack-of-social-support"


class GraphCompartmentRule(CodeSystemValue):
    """ How a compartment must be linked

    URL: http://hl7.org/fhir/graph-compartment-rule
    ValueSet: http://hl7.org/fhir/ValueSet/graph-compartment-rule
    """
    URL = "http://hl7.org/fhir/graph-compartment-rule"
    EXPERIMENTAL = False

    """ The compartment must be identical (the same literal reference)
    """
    identical = "identical"

    """ The compartment must be the same - the record must be about the same patient, but the reference may be different
    """
    matching = "matching"

    """ The compartment must be different
    """
    different = "different"

    """ The compartment rule is defined in the accompanying FHIRPath expression
    """
    custom = "custom"


class GraphCompartmentUse(CodeSystemValue):
    """ Defines how a compartment rule is used

    URL: http://hl7.org/fhir/graph-compartment-use
    ValueSet: http://hl7.org/fhir/ValueSet/graph-compartment-use
    """
    URL = "http://hl7.org/fhir/graph-compartment-use"
    EXPERIMENTAL = False

    """ This compartment rule is a condition for whether the rule applies
    """
    condition = "condition"

    """ This compartment rule is enforced on any relationships that meet the conditions
    """
    requirement = "requirement"


class GroupType(CodeSystemValue):
    """ Types of resources that are part of group

    URL: http://hl7.org/fhir/group-type
    ValueSet: http://hl7.org/fhir/ValueSet/group-type
    """
    URL = "http://hl7.org/fhir/group-type"
    EXPERIMENTAL = False

    """ Group contains "person" Patient resources
    """
    person = "person"

    """ Group contains "animal" Patient resources
    """
    animal = "animal"

    """ Group contains healthcare practitioner resources (Practitioner or PractitionerRole)
    """
    practitioner = "practitioner"

    """ Group contains Device resources
    """
    device = "device"

    """ Group contains Medication resources
    """
    medication = "medication"

    """ Group contains Substance resources
    """
    substance = "substance"


class GuidanceResponseStatus(CodeSystemValue):
    """ The status of a guidance response

    URL: http://hl7.org/fhir/guidance-response-status
    ValueSet: http://hl7.org/fhir/ValueSet/guidance-response-status
    """
    URL = "http://hl7.org/fhir/guidance-response-status"
    EXPERIMENTAL = False

    """ The request was processed successfully
    """
    success = "success"

    """ The request was processed successfully, but more data may result in a more complete evaluation
    """
    dataRequested = "data-requested"

    """ The request was processed, but more data is required to complete the evaluation
    """
    dataRequired = "data-required"

    """ The request is currently being processed
    """
    inProgress = "in-progress"

    """ The request was not processed successfully
    """
    failure = "failure"

    """ The response was entered in error
    """
    enteredInError = "entered-in-error"


class GuidePageGeneration(CodeSystemValue):
    """ A code that indicates how the page is generated

    URL: http://hl7.org/fhir/guide-page-generation
    ValueSet: http://hl7.org/fhir/ValueSet/guide-page-generation
    """
    URL = "http://hl7.org/fhir/guide-page-generation"
    EXPERIMENTAL = False

    """ Page is proper xhtml with no templating.  Will be brought across unchanged for standard post-processing
    """
    html = "html"

    """ Page is markdown with templating.  Will use the template to create a file that imports the markdown file prior
	/// to post-processing
    """
    markdown = "markdown"

    """ Page is xml with templating.  Will use the template to create a file that imports the source file and run the
	/// nominated XSLT transform (see parameters) if present prior to post-processing
    """
    xml = "xml"

    """ Page will be generated by the publication process - no source to bring across
    """
    generated = "generated"


class GuideParameterCode(CodeSystemValue):
    """ Code of parameter that is input to the guide

    URL: http://hl7.org/fhir/guide-parameter-code
    ValueSet: http://hl7.org/fhir/ValueSet/guide-parameter-code
    """
    URL = "http://hl7.org/fhir/guide-parameter-code"
    EXPERIMENTAL = False

    """ If the value of this boolean 0..1 parameter is "true" then all conformance resources will have any specified
	/// [Resource].version overwritten with the ImplementationGuide.version
    """
    applyBusinessVersion = "apply-business-version"

    """ If the value of this boolean 0..1 parameter is "true" then all conformance resources will have any specified
	/// [Resource].jurisdiction overwritten with the ImplementationGuide.jurisdiction
    """
    applyJurisdiction = "apply-jurisdiction"

    """ The value of this string 0..* parameter is a subfolder of the build context's location that is to be scanned to
	/// load resources. Scope is (if present) a particular resource type
    """
    pathResource = "path-resource"

    """ The value of this string 0..1 parameter is a subfolder of the build context's location that contains files that
	/// are part of the html content processed by the builder
    """
    pathPages = "path-pages"

    """ The value of this string 0..1 parameter is a subfolder of the build context's location that is used as the
	/// terminology cache. If this is not present, the terminology cache is on the local system, not under version
	/// control
    """
    pathTxCache = "path-tx-cache"

    """ The value of this string 0..1 parameter is a path to the ExpansionProfile used when expanding value sets for
	/// this implementation guide. This is particularly used to specify the versions of published terminologies such as
	/// SNOMED CT
    """
    expansionProfile = "expansion-profile"

    """ The value of this string 0..1 parameter is either "warning" or "error" (default = "error"). If the value is
	/// "warning" then IG build tools allow the IG to be considered successfully build even when there is no internal
	/// broken links
    """
    ruleBrokenLinks = "rule-broken-links"

    """ The value of this boolean 0..1 parameter specifies whether the IG publisher creates examples in XML format. If
	/// not present, the Publication Tool decides whether to generate XML
    """
    generateXml = "generate-xml"

    """ The value of this boolean 0..1 parameter specifies whether the IG publisher creates examples in JSON format. If
	/// not present, the Publication Tool decides whether to generate JSON
    """
    generateJson = "generate-json"

    """ The value of this boolean 0..1 parameter specifies whether the IG publisher creates examples in Turtle format.
	/// If not present, the Publication Tool decides whether to generate Turtle
    """
    generateTurtle = "generate-turtle"

    """ The value of this string singleton parameter is the name of the file to use as the builder template for each
	/// generated page (see templating)
    """
    htmlTemplate = "html-template"


class HL7Workgroup(CodeSystemValue):
    """ An HL7 administrative unit that owns artifacts in the FHIR specification

    URL: http://hl7.org/fhir/hl7-work-group
    ValueSet: http://hl7.org/fhir/ValueSet/hl7-work-group
    """
    URL = "http://hl7.org/fhir/hl7-work-group"
    EXPERIMENTAL = False

    """ Community Based Collaborative Care (http://www.hl7.org/Special/committees/cbcc/index.cfm)
    """
    cbcc = "cbcc"

    """ Clinical Decision Support (http://www.hl7.org/Special/committees/dss/index.cfm)
    """
    cds = "cds"

    """ Clinical Quality Information (http://www.hl7.org/Special/committees/cqi/index.cfm)
    """
    cqi = "cqi"

    """ Clinical Genomics (http://www.hl7.org/Special/committees/clingenomics/index.cfm)
    """
    cg = "cg"

    """ Health Care Devices (http://www.hl7.org/Special/committees/healthcaredevices/index.cfm)
    """
    dev = "dev"

    """ Electronic Health Records (http://www.hl7.org/special/committees/ehr/index.cfm)
    """
    ehr = "ehr"

    """ FHIR Infrastructure (http://www.hl7.org/Special/committees/fiwg/index.cfm)
    """
    fhir = "fhir"

    """ Financial Management (http://www.hl7.org/Special/committees/fm/index.cfm)
    """
    fm = "fm"

    """ Health Standards Integration (http://www.hl7.org/Special/committees/hsi/index.cfm)
    """
    hsi = "hsi"

    """ Imaging Integration (http://www.hl7.org/Special/committees/imagemgt/index.cfm)
    """
    ii = "ii"

    """ Infrastructure And Messaging (http://www.hl7.org/special/committees/inm/index.cfm)
    """
    inm = "inm"

    """ Implementable Technology Specifications (http://www.hl7.org/special/committees/xml/index.cfm)
    """
    its = "its"

    """ Orders and Observations (http://www.hl7.org/Special/committees/orders/index.cfm)
    """
    oo = "oo"

    """ Patient Administration (http://www.hl7.org/Special/committees/pafm/index.cfm)
    """
    pa = "pa"

    """ Patient Care (http://www.hl7.org/Special/committees/patientcare/index.cfm)
    """
    pc = "pc"

    """ Public Health and Emergency Response (http://www.hl7.org/Special/committees/pher/index.cfm)
    """
    pher = "pher"

    """ Pharmacy (http://www.hl7.org/Special/committees/medication/index.cfm)
    """
    phx = "phx"

    """ Regulated Clinical Research Information Management (http://www.hl7.org/Special/committees/rcrim/index.cfm)
    """
    rcrim = "rcrim"

    """ Structured Documents (http://www.hl7.org/Special/committees/structure/index.cfm)
    """
    sd = "sd"

    """ Security (http://www.hl7.org/Special/committees/secure/index.cfm)
    """
    sec = "sec"

    """ US Realm Taskforce (http://wiki.hl7.org/index.php?title=US_Realm_Task_Force)
    """
    us = "us"

    """ Vocabulary (http://www.hl7.org/Special/committees/Vocab/index.cfm)
    """
    vocab = "vocab"

    """ Application Implementation and Design (http://www.hl7.org/Special/committees/java/index.cfm)
    """
    aid = "aid"


class HTTPVerb(CodeSystemValue):
    """ HTTP verbs (in the HTTP command line).

    URL: http://hl7.org/fhir/http-verb
    ValueSet: http://hl7.org/fhir/ValueSet/http-verb
    """
    URL = "http://hl7.org/fhir/http-verb"
    EXPERIMENTAL = False

    """ HTTP GET
    """
    GET = "GET"

    """ HTTP HEAD
    """
    HEAD = "HEAD"

    """ HTTP POST
    """
    POST = "POST"

    """ HTTP PUT
    """
    PUT = "PUT"

    """ HTTP DELETE
    """
    DELETE = "DELETE"

    """ HTTP PATCH
    """
    PATCH = "PATCH"


class HandlingConditionSet(CodeSystemValue):
    """ Set of handling instructions prior testing of the specimen

    URL: http://hl7.org/fhir/handling-condition
    ValueSet: http://hl7.org/fhir/ValueSet/handling-condition
    """
    URL = "http://hl7.org/fhir/handling-condition"
    EXPERIMENTAL = False

    """ room temperature
    """
    room = "room"

    """ refrigerated temperature
    """
    refrigerated = "refrigerated"

    """ frozen temperature
    """
    frozen = "frozen"


class HumanNameAssemblyOrder(CodeSystemValue):
    """ A code that represents the preferred display order of the components of a human name

    URL: http://hl7.org/fhir/name-assembly-order
    ValueSet: http://hl7.org/fhir/ValueSet/name-assembly-order
    """
    URL = "http://hl7.org/fhir/name-assembly-order"
    EXPERIMENTAL = False

    """ NL1
    """
    NL1 = "NL1"

    """ NL2
    """
    NL2 = "NL2"

    """ NL3
    """
    NL3 = "NL3"

    """ NL4
    """
    NL4 = "NL4"


class ISO210892017HealthRecordLifecycleEvents(CodeSystemValue):
    """ Attached is vocabulary for the 27 record lifecycle events, as per ISO TS 21089-2017, Health Informatics - Trusted End-
to-End Information Flows, Section 3, Terms and Definitions (2017, at ISO Central Secretariat, passed ballot and ready
for publication).  This will also be included in the FHIR EHR Record Lifecycle Event Implementation Guide, balloted and
(to be) published with FHIR STU-3.

    URL: http://hl7.org/fhir/iso-21089-lifecycle
    """
    URL = "http://hl7.org/fhir/iso-21089-lifecycle"
    EXPERIMENTAL = False

    """ Occurs when an agent causes the system to obtain and open a record entry for inspection or review.
    """
    access = "access"

    """ Occurs when an agent causes the system to tag or otherwise indicate special access management and suspension of
	/// record entry deletion/destruction, if deemed relevant to a lawsuit or which are reasonably anticipated to be
	/// relevant or to fulfill organizational policy under the legal doctrine of “duty to preserve”.
    """
    hold = "hold"

    """ Occurs when an agent makes any change to record entry content currently residing in storage considered permanent
	/// (persistent).
    """
    amend = "amend"

    """ Occurs when an agent causes the system to create and move archive artifacts containing record entry content,
	/// typically to long-term offline storage.
    """
    archive = "archive"

    """ Occurs when an agent causes the system to capture the agent’s digital signature (or equivalent indication)
	/// during formal validation of record entry content.
    """
    attest = "attest"

    """ Occurs when an agent causes the system to decode record entry content from a cipher.
    """
    decrypt = "decrypt"

    """ Occurs when an agent causes the system to scrub record entry content to reduce the association between a set of
	/// identifying data and the data subject in a way that might or might not be reversible.
    """
    deidentify = "deidentify"

    """ Occurs when an agent causes the system to tag record entry(ies) as obsolete, erroneous or untrustworthy, to warn
	/// against its future use.
    """
    deprecate = "deprecate"

    """ Occurs when an agent causes the system to permanently erase record entry content from the system.
    """
    destroy = "destroy"

    """ Occurs when an agent causes the system to release, transfer, provision access to, or otherwise divulge record
	/// entry content.
    """
    disclose = "disclose"

    """ Occurs when an agent causes the system to encode record entry content in a cipher.
    """
    encrypt = "encrypt"

    """ Occurs when an agent causes the system to selectively pull out a subset of record entry content, based on
	/// explicit criteria.
    """
    extract = "extract"

    """ Occurs when an agent causes the system to connect related record entries.
    """
    link = "link"

    """ Occurs when an agent causes the system to combine or join content from two or more record entries, resulting in
	/// a single logical record entry.
    """
    merge = "merge"

    """ Occurs when an agent causes the system to: a) initiate capture of potential record content, and b) incorporate
	/// that content into the storage considered a permanent part of the health record.
    """
    originate = "originate"

    """ Occurs when an agent causes the system to remove record entry content to reduce the association between a set of
	/// identifying data and the data subject in a way that may be reversible.
    """
    pseudonymize = "pseudonymize"

    """ Occurs when an agent causes the system to recreate or restore full status to record entries previously deleted
	/// or deprecated.
    """
    reactivate = "reactivate"

    """ Occurs when an agent causes the system to a) initiate capture of data content from elsewhere, and b) incorporate
	/// that content into the storage considered a permanent part of the health record.
    """
    receive = "receive"

    """ Occurs when an agent causes the system to restore information to data that allows identification of information
	/// source and/or information subject.
    """
    reidentify = "reidentify"

    """ Occurs when an agent causes the system to remove a tag or other cues for special access management had required
	/// to fulfill organizational policy under the legal doctrine of “duty to preserve”.
    """
    unhold = "unhold"

    """ Occurs when an agent causes the system to produce and deliver record entry content in a particular form and
	/// manner.
    """
    report = "report"

    """ Occurs when an agent causes the system to recreate record entries and their content from a previous created
	/// archive artefact.
    """
    restore = "restore"

    """ Occurs when an agent causes the system to change the form, language or code system used to represent record
	/// entry content.
    """
    transform = "transform"

    """ Occurs when an agent causes the system to send record entry content from one (EHR/PHR/other) system to another.
    """
    transmit = "transmit"

    """ Occurs when an agent causes the system to disconnect two or more record entries previously connected, rendering
	/// them separate (disconnected) again.
    """
    unlink = "unlink"

    """ Occurs when an agent causes the system to reverse a previous record entry merge operation, rendering them
	/// separate again.
    """
    unmerge = "unmerge"

    """ Occurs when an agent causes the system to confirm compliance of data or data objects with regulations,
	/// requirements, specifications, or other imposed conditions based on organizational policy.
    """
    verify = "verify"


class IdentifierTypeCodes(CodeSystemValue):
    """ A coded type for an identifier that can be used to determine which identifier to use for a specific purpose.

    URL: http://hl7.org/fhir/identifier-type
    ValueSet: http://hl7.org/fhir/ValueSet/identifier-type
    """
    URL = "http://hl7.org/fhir/identifier-type"
    EXPERIMENTAL = True

    """ An identifier assigned to a device using the Universal Device Identifier framework as defined by FDA
	/// (http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/UniqueDeviceIdentification/).
    """
    UDI = "UDI"

    """ An identifier affixed to an item by the manufacturer when it is first made, where each item has a different
	/// identifier.
    """
    SNO = "SNO"

    """ An identifier issued by a governmental organization to an individual for the purpose of the receipt of social
	/// services and benefits.
    """
    SB = "SB"

    """ The identifier associated with the person or service that requests or places an order.
    """
    PLAC = "PLAC"

    """ The Identifier associated with the person, or service, who produces the observations or fulfills the order
	/// requested by the requestor.
    """
    FILL = "FILL"


class IdentifierUse(CodeSystemValue):
    """ Identifies the purpose for this identifier, if known .

    URL: http://hl7.org/fhir/identifier-use
    ValueSet: http://hl7.org/fhir/ValueSet/identifier-use
    """
    URL = "http://hl7.org/fhir/identifier-use"
    EXPERIMENTAL = False

    """ The identifier recommended for display and use in real-world interactions.
    """
    usual = "usual"

    """ The identifier considered to be most trusted for the identification of this item.
    """
    official = "official"

    """ A temporary identifier.
    """
    temp = "temp"

    """ An identifier that was assigned in secondary use - it serves to identify the object in a relative context, but
	/// cannot be consistently assigned to the same object again in a different context.
    """
    secondary = "secondary"

    """ The identifier id no longer considered valid, but may be relevant for search purposes.  E.g. Changes to
	/// identifier schemes, account merges, etc.
    """
    old = "old"


class IdentityAssuranceLevel(CodeSystemValue):
    """ The level of confidence that this link represents the same actual person, based on NIST Authentication Levels.

    URL: http://hl7.org/fhir/identity-assuranceLevel
    ValueSet: http://hl7.org/fhir/ValueSet/identity-assuranceLevel
    """
    URL = "http://hl7.org/fhir/identity-assuranceLevel"
    EXPERIMENTAL = False

    """ Little or no confidence in the asserted identity's accuracy.
    """
    level1 = "level1"

    """ Some confidence in the asserted identity's accuracy.
    """
    level2 = "level2"

    """ High confidence in the asserted identity's accuracy.
    """
    level3 = "level3"

    """ Very high confidence in the asserted identity's accuracy.
    """
    level4 = "level4"


class ImagingStudyStatus(CodeSystemValue):
    """ The status of the ImagingStudy

    URL: http://hl7.org/fhir/imagingstudy-status
    ValueSet: http://hl7.org/fhir/ValueSet/imagingstudy-status
    """
    URL = "http://hl7.org/fhir/imagingstudy-status"
    EXPERIMENTAL = False

    """ The existence of the imaging study is registered, but there is nothing yet available.
    """
    registered = "registered"

    """ At least one instance has been associated with this imaging study.
    """
    available = "available"

    """ The imaging study is unavailable because the imaging study was not started or not completed (also sometimes
	/// called "aborted").
    """
    cancelled = "cancelled"

    """ The imaging study has been withdrawn following a previous final release.  This electronic record should never
	/// have existed, though it is possible that real-world decisions were based on it. (If real-world activity has
	/// occurred, the status should be "cancelled" rather than "entered-in-error".)
    """
    enteredInError = "entered-in-error"

    """ The system does not know which of the status values currently applies for this request. Note: This concept is
	/// not to be used for "other" - one of the listed statuses is presumed to apply, it's just not known which one.
    """
    unknown = "unknown"


class ImmunizationEvaluationDoseStatusCodes(CodeSystemValue):
    """ The value set to instantiate this attribute should be drawn from a terminologically robust code system that consists of
or contains concepts to support describing the validity of a dose relative to a particular recommended schedule. This
value set is provided as a suggestive example.

    URL: http://hl7.org/fhir/immunization-evaluation-dose-status
    ValueSet: http://hl7.org/fhir/ValueSet/immunization-evaluation-dose-status
    """
    URL = "http://hl7.org/fhir/immunization-evaluation-dose-status"
    EXPERIMENTAL = True

    """ The dose counts toward fulfilling a path to immunity for a patient, providing protection against the target
	/// disease.
    """
    valid = "valid"

    """ The dose does not count toward fulfilling a path to immunity for a patient.
    """
    notvalid = "notvalid"


class ImmunizationEvaluationDoseStatusReasonCodes(CodeSystemValue):
    """ The value set to instantiate this attribute should be drawn from a terminologically robust code system that consists of
or contains concepts to support describing the reason why an administered dose has been assigned a particular status.
Often, this reason describes why a dose is considered invalid. This value set is provided as a suggestive example.

    URL: http://hl7.org/fhir/immunization-evaluation-dose-status-reason
    ValueSet: http://hl7.org/fhir/ValueSet/immunization-evaluation-dose-status-reason
    """
    URL = "http://hl7.org/fhir/immunization-evaluation-dose-status-reason"
    EXPERIMENTAL = True

    """ The product was stored in a manner inconsistent with manufacturer guidelines potentially reducing the
	/// effectiveness of the product.
    """
    advstorage = "advstorage"

    """ The product was stored at a temperature inconsistent with manufacturer guidelines potentially reducing the
	/// effectiveness of the product.
    """
    coldchbrk = "coldchbrk"

    """ The product was administered after the expiration date associated with lot of vaccine.
    """
    explot = "explot"

    """ The product was administered at a time inconsistent with the documented schedule.
    """
    outsidesched = "outsidesched"

    """ The product administered has been recalled by the manufacturer.
    """
    prodrecall = "prodrecall"


class ImmunizationFundingSource(CodeSystemValue):
    """ The value set to instantiate this attribute should be drawn from a terminologically robust code system that consists of
or contains concepts to support describing the source of the vaccine administered. This value set is provided as a
suggestive example.

    URL: http://hl7.org/fhir/immunization-funding-source
    ValueSet: http://hl7.org/fhir/ValueSet/immunization-funding-source
    """
    URL = "http://hl7.org/fhir/immunization-funding-source"
    EXPERIMENTAL = True

    """ The vaccine was purchased with private funds.
    """
    private = "private"

    """ The vaccine was purchased with public funds.
    """
    public = "public"


class ImmunizationOriginCodes(CodeSystemValue):
    """ The value set to instantiate this attribute should be drawn from a terminologically robust code system that consists of
or contains concepts to support describing the source of the data when the report of the immunization event is not based
on information from the person, entity or organization who administered the vaccine. This value set is provided as a
suggestive example.

    URL: http://hl7.org/fhir/immunization-origin
    ValueSet: http://hl7.org/fhir/ValueSet/immunization-origin
    """
    URL = "http://hl7.org/fhir/immunization-origin"
    EXPERIMENTAL = True

    """ The data for the immunization event originated with another provider.
    """
    provider = "provider"

    """ The data for the immunization event originated with a written record for the patient.
    """
    record = "record"

    """ The data for the immunization event originated from the recollection of the patient or parent/guardian of the
	/// patient.
    """
    recall = "recall"

    """ The data for the immunization event originated with a school record for the patient.
    """
    school = "school"


class ImmunizationProgramEligibility(CodeSystemValue):
    """ The value set to instantiate this attribute should be drawn from a terminologically robust code system that consists of
or contains concepts to support describing the patient's elibigility for a vaccination program. This value set is
provided as a suggestive example.

    URL: http://hl7.org/fhir/immunization-program-eligibility
    ValueSet: http://hl7.org/fhir/ValueSet/immunization-program-eligibility
    """
    URL = "http://hl7.org/fhir/immunization-program-eligibility"
    EXPERIMENTAL = True

    """ The patient is not eligible for the funding program.
    """
    ineligible = "ineligible"

    """ The patient is eligible for the funding program because they are uninsured.
    """
    uninsured = "uninsured"


class ImmunizationRecommendationStatusCodes(CodeSystemValue):
    """ The value set to instantiate this attribute should be drawn from a terminologically robust code system that consists of
or contains concepts to support describing the status of the patient towards perceived immunity against a vaccine
preventable disease. This value set is provided as a suggestive example.

    URL: http://hl7.org/fhir/immunization-recommendation-status
    ValueSet: http://hl7.org/fhir/ValueSet/immunization-recommendation-status
    """
    URL = "http://hl7.org/fhir/immunization-recommendation-status"
    EXPERIMENTAL = True

    """ The patient is due for their next vaccination.
    """
    due = "due"

    """ The patient is considered overdue for their next vaccination.
    """
    overdue = "overdue"

    """ The patient is immune to the target disease and further immunization against the disease is not likely to
	/// provide benefit.
    """
    immune = "immune"

    """ The patient is contraindicated for futher doses.
    """
    contraindicated = "contraindicated"

    """ The patient is fully protected and no further doses are recommended.
    """
    complete = "complete"


class ImmunizationSubpotentReason(CodeSystemValue):
    """ The value set to instantiate this attribute should be drawn from a terminologically robust code system that consists of
or contains concepts to support describing the reason why a dose is considered to be subpotent. This value set is
provided as a suggestive example.

    URL: http://hl7.org/fhir/immunization-subpotent-reason
    ValueSet: http://hl7.org/fhir/ValueSet/immunization-subpotent-reason
    """
    URL = "http://hl7.org/fhir/immunization-subpotent-reason"
    EXPERIMENTAL = True

    """ The full volume of the dose was not administered to the patient.
    """
    partial = "partial"

    """ The vaccine experienced a cold chain break.
    """
    coldchainbreak = "coldchainbreak"

    """ The vaccine was recalled by the manufacturer.
    """
    recall = "recall"


class ImplantStatus(CodeSystemValue):
    """ A set codes that define the functional status of an implanted device.

    URL: http://hl7.org/fhir/implant-status
    ValueSet: http://hl7.org/fhir/ValueSet/implant-status
    """
    URL = "http://hl7.org/fhir/implant-status"
    EXPERIMENTAL = False

    """ The implanted device is working normally
    """
    functional = "functional"

    """ The implanted device is not working
    """
    nonFunctional = "non-functional"

    """ The implanted device has been turned off
    """
    disabled = "disabled"

    """ the functional status of the implant has not been determined
    """
    unknown = "unknown"


class InterventionCodes(CodeSystemValue):
    """ This value set includes sample Intervention codes.

    URL: http://hl7.org/fhir/intervention
    ValueSet: http://hl7.org/fhir/ValueSet/intervention
    """
    URL = "http://hl7.org/fhir/intervention"
    EXPERIMENTAL = True

    """ Unknown
    """
    unknown = "unknown"

    """ Other
    """
    other = "other"


class InvoicePriceComponentType(CodeSystemValue):
    """ Codes indicating the details of what is/was done.  These will vary significantly based on the type of request resource
and will often be example/preferred rather than extensible/required.

    URL: http://hl7.org/fhir/invoice-priceComponentType
    ValueSet: http://hl7.org/fhir/ValueSet/invoice-priceComponentType
    """
    URL = "http://hl7.org/fhir/invoice-priceComponentType"
    EXPERIMENTAL = False

    """ the amount is the base price used for calculating the total price before applying surcharges, discount or taxes
    """
    base = "base"

    """ the amount is a surcharge applied on the base price
    """
    surcharge = "surcharge"

    """ the amount is a deduction applied on the base price
    """
    deduction = "deduction"

    """ the amount is a discount applied on the base price
    """
    discount = "discount"

    """ the amount is the tax component of the total price
    """
    tax = "tax"

    """ the amount is of informational character, it has not been applied in the calculation of the total price
    """
    informational = "informational"


class InvoiceStatus(CodeSystemValue):
    """ Codes identifying the lifecycle stage of an Invoice

    URL: http://hl7.org/fhir/invoice-status
    ValueSet: http://hl7.org/fhir/ValueSet/invoice-status
    """
    URL = "http://hl7.org/fhir/invoice-status"
    EXPERIMENTAL = False

    """ the invoice has been prepared but not yet finalized
    """
    draft = "draft"

    """ the invoice has been finalized and sent to the recipient
    """
    issued = "issued"

    """ the invoice has been balaced / completely paid
    """
    balanced = "balanced"

    """ the invoice was cancelled
    """
    cancelled = "cancelled"

    """ the invoice was determined as entered in error before it was issued
    """
    enteredInError = "entered-in-error"


class IssueSeverity(CodeSystemValue):
    """ How the issue affects the success of the action.

    URL: http://hl7.org/fhir/issue-severity
    ValueSet: http://hl7.org/fhir/ValueSet/issue-severity
    """
    URL = "http://hl7.org/fhir/issue-severity"
    EXPERIMENTAL = False

    """ The issue caused the action to fail, and no further checking could be performed.
    """
    fatal = "fatal"

    """ The issue is sufficiently important to cause the action to fail.
    """
    error = "error"

    """ The issue is not important enough to cause the action to fail but may cause it to be performed suboptimally or
	/// in a way that is not as desired.
    """
    warning = "warning"

    """ The issue has no relation to the degree of success of the action.
    """
    information = "information"


class IssueType(CodeSystemValue):
    """ A code that describes the type of issue.

    URL: http://hl7.org/fhir/issue-type
    ValueSet: http://hl7.org/fhir/ValueSet/issue-type
    """
    URL = "http://hl7.org/fhir/issue-type"
    EXPERIMENTAL = False

    """ Content invalid against the specification or a profile.
    """
    invalid = "invalid"

    """ A structural issue in the content such as wrong namespace, or unable to parse the content completely, or invalid
	/// json syntax.
    """
    structure = "structure"

    """ A required element is missing.
    """
    required = "required"

    """ An element value is invalid.
    """
    value = "value"

    """ A content validation rule failed - e.g. a schematron rule.
    """
    invariant = "invariant"

    """ An authentication/authorization/permissions issue of some kind.
    """
    security = "security"

    """ The client needs to initiate an authentication process.
    """
    login = "login"

    """ The user or system was not able to be authenticated (either there is no process, or the proferred token is
	/// unacceptable).
    """
    unknown = "unknown"

    """ User session expired; a login may be required.
    """
    expired = "expired"

    """ The user does not have the rights to perform this action.
    """
    forbidden = "forbidden"

    """ Some information was not or might not have been returned due to business rules, consent or privacy rules, or
	/// access permission constraints.  This information may be accessible through alternate processes.
    """
    suppressed = "suppressed"

    """ Processing issues. These are expected to be final e.g. there is no point resubmitting the same content
	/// unchanged.
    """
    processing = "processing"

    """ The resource or profile is not supported.
    """
    notSupported = "not-supported"

    """ An attempt was made to create a duplicate record.
    """
    duplicate = "duplicate"

    """ The reference provided was not found. In a pure RESTful environment, this would be an HTTP 404 error, but this
	/// code may be used where the content is not found further into the application architecture.
    """
    notFound = "not-found"

    """ Provided content is too long (typically, this is a denial of service protection type of error).
    """
    tooLong = "too-long"

    """ The code or system could not be understood, or it was not valid in the context of a particular ValueSet.code.
    """
    codeInvalid = "code-invalid"

    """ An extension was found that was not acceptable, could not be resolved, or a modifierExtension was not
	/// recognized.
    """
    extension = "extension"

    """ The operation was stopped to protect server resources; e.g. a request for a value set expansion on all of SNOMED
	/// CT.
    """
    tooCostly = "too-costly"

    """ The content/operation failed to pass some business rule, and so could not proceed.
    """
    businessRule = "business-rule"

    """ Content could not be accepted because of an edit conflict (i.e. version aware updates) (In a pure RESTful
	/// environment, this would be an HTTP 404 error, but this code may be used where the conflict is discovered further
	/// into the application architecture.)
    """
    conflict = "conflict"

    """ Not all data sources typically accessed could be reached, or responded in time, so the returned information
	/// might not be complete.
    """
    incomplete = "incomplete"

    """ Transient processing issues. The system receiving the error may be able to resubmit the same content once an
	/// underlying issue is resolved.
    """
    transient = "transient"

    """ A resource/record locking failure (usually in an underlying database).
    """
    lockError = "lock-error"

    """ The persistent store is unavailable; e.g. the database is down for maintenance or similar action.
    """
    noStore = "no-store"

    """ An unexpected internal error has occurred.
    """
    exception = "exception"

    """ An internal timeout has occurred.
    """
    timeout = "timeout"

    """ The system is not prepared to handle this request due to load management.
    """
    throttled = "throttled"

    """ A message unrelated to the processing success of the completed operation (examples of the latter include things
	/// like reminders of password expiry, system maintenance times, etc.).
    """
    informational = "informational"


class LanguagePreferenceType(CodeSystemValue):
    """ This value set defines the set of codes for describing the type or mode of the patient's preferred language.

    URL: http://hl7.org/fhir/language-preference-type
    ValueSet: http://hl7.org/fhir/ValueSet/language-preference-type
    """
    URL = "http://hl7.org/fhir/language-preference-type"
    EXPERIMENTAL = True

    """ The patient prefers to verbally communicate with the associated language.
    """
    verbal = "verbal"

    """ The patient prefers to communicate in writing with the associated language.
    """
    written = "written"


class LibraryType(CodeSystemValue):
    """ The type of knowledge asset this library contains

    URL: http://hl7.org/fhir/library-type
    ValueSet: http://hl7.org/fhir/ValueSet/library-type
    """
    URL = "http://hl7.org/fhir/library-type"
    EXPERIMENTAL = False

    """ The resource is a shareable library of formalized knowledge
    """
    logicLibrary = "logic-library"

    """ The resource is a definition of an information model
    """
    modelDefinition = "model-definition"

    """ The resource is a collection of knowledge assets
    """
    assetCollection = "asset-collection"

    """ The resource defines the dependencies, parameters, and data requirements for a particular module or evaluation
	/// context
    """
    moduleDefinition = "module-definition"


class LinkType(CodeSystemValue):
    """ The type of link between this patient resource and another patient resource.

    URL: http://hl7.org/fhir/link-type
    ValueSet: http://hl7.org/fhir/ValueSet/link-type
    """
    URL = "http://hl7.org/fhir/link-type"
    EXPERIMENTAL = False

    """ The patient resource containing this link must no longer be used. The link points forward to another patient
	/// resource that must be used in lieu of the patient resource that contains this link.
    """
    replacedBy = "replaced-by"

    """ The patient resource containing this link is the current active patient record. The link points back to an
	/// inactive patient resource that has been merged into this resource, and should be consulted to retrieve
	/// additional referenced information.
    """
    replaces = "replaces"

    """ The patient resource containing this link is in use and valid but not considered the main source of information
	/// about a patient. The link points forward to another patient resource that should be consulted to retrieve
	/// additional patient information.
    """
    refer = "refer"

    """ The patient resource containing this link is in use and valid, but points to another patient resource that is
	/// known to contain data about the same person. Data in this resource might overlap or contradict information found
	/// in the other patient resource. This link does not indicate any relative importance of the resources concerned,
	/// and both should be regarded as equally valid.
    """
    seealso = "seealso"


class LinkageType(CodeSystemValue):
    """ Used to distinguish different roles a resource can play within a set of linked resources

    URL: http://hl7.org/fhir/linkage-type
    ValueSet: http://hl7.org/fhir/ValueSet/linkage-type
    """
    URL = "http://hl7.org/fhir/linkage-type"
    EXPERIMENTAL = False

    """ The record represents the "source of truth" (from the perspective of this Linkage resource) for the underlying
	/// event/condition/etc.
    """
    source = "source"

    """ The record represents the alternative view of the underlying event/condition/etc.  The record may still be
	/// actively maintained, even though it is not considered to be the source of truth.
    """
    alternate = "alternate"

    """ The record represents an obsolete record of the underlying event/condition/etc.  It is not expected to be
	/// actively maintained.
    """
    historical = "historical"


class ListEmptyReasons(CodeSystemValue):
    """ General reasons for a list to be empty. Reasons are either related to a summary list (i.e. problem or medication list)
or to a workflow related list (i.e. consultation list).

    URL: http://hl7.org/fhir/list-empty-reason
    ValueSet: http://hl7.org/fhir/ValueSet/list-empty-reason
    """
    URL = "http://hl7.org/fhir/list-empty-reason"
    EXPERIMENTAL = True

    """ Clinical judgment that there are no known items for this list after reasonable investigation. Note that this a
	/// positive statement by a clinical user, and not a default position asserted by a computer system in the lack of
	/// other information. Example uses:  * For allergies: the patient or patient's agent/guardian has asserted that
	/// he/she is not aware of any allergies (NKA - nil known allergies)  * For medications: the patient or patient's
	/// agent/guardian has asserted that the patient is known to be taking no medications  * For diagnoses, problems and
	/// procedures: the patient or patient's agent/guardian has asserted that there is no known event to record.
    """
    nilknown = "nilknown"

    """ The investigation to find out whether there are items for this list has not occurred.
    """
    notasked = "notasked"

    """ The content of the list was not provided due to privacy or confidentiality concerns. Note that it should not be
	/// assumed that this means that the particular information in question was withheld due to its contents - it can
	/// also be a policy decision.
    """
    withheld = "withheld"

    """ Information to populate this list cannot be obtained; e.g. unconscious patient.
    """
    unavailable = "unavailable"

    """ The work to populate this list has not yet begun.
    """
    notstarted = "notstarted"

    """ This list has now closed or has ceased to be relevant or useful.
    """
    closed = "closed"


class ListMode(CodeSystemValue):
    """ The processing mode that applies to this list

    URL: http://hl7.org/fhir/list-mode
    ValueSet: http://hl7.org/fhir/ValueSet/list-mode
    """
    URL = "http://hl7.org/fhir/list-mode"
    EXPERIMENTAL = False

    """ This list is the master list, maintained in an ongoing fashion with regular updates as the real world list it is
	/// tracking changes
    """
    working = "working"

    """ This list was prepared as a snapshot. It should not be assumed to be current
    """
    snapshot = "snapshot"

    """ A point-in-time list that shows what changes have been made or recommended.  E.g. a discharge medication list
	/// showing what was added and removed during an encounter
    """
    changes = "changes"


class ListOrderCodes(CodeSystemValue):
    """ Base values for the order of the items in a list resource.

    URL: http://hl7.org/fhir/list-order
    ValueSet: http://hl7.org/fhir/ValueSet/list-order
    """
    URL = "http://hl7.org/fhir/list-order"
    EXPERIMENTAL = True

    """ The list was sorted by a user. The criteria the user used are not specified.
    """
    user = "user"

    """ The list was sorted by the system. The criteria the user used are not specified; define additional codes to
	/// specify a particular order (or use other defined codes).
    """
    system = "system"

    """ The list is sorted by the data of the event. This can be used when the list has items which are dates with past
	/// or future events.
    """
    eventDate = "event-date"

    """ The list is sorted by the date the item was added to the list. Note that the date added to the list is not
	/// explicit in the list itself.
    """
    entryDate = "entry-date"

    """ The list is sorted by priority. The exact method in which priority has been determined is not specified.
    """
    priority = "priority"

    """ The list is sorted alphabetically by an unspecified property of the items in the list.
    """
    alphabetic = "alphabetic"

    """ The list is sorted categorically by an unspecified property of the items in the list.
    """
    category = "category"

    """ The list is sorted by patient, with items for each patient grouped together.
    """
    patient = "patient"


class ListStatus(CodeSystemValue):
    """ The current state of the list

    URL: http://hl7.org/fhir/list-status
    ValueSet: http://hl7.org/fhir/ValueSet/list-status
    """
    URL = "http://hl7.org/fhir/list-status"
    EXPERIMENTAL = False

    """ The list is considered to be an active part of the patient's record.
    """
    current = "current"

    """ The list is "old" and should no longer be considered accurate or relevant.
    """
    retired = "retired"

    """ The list was never accurate.  It is retained for medico-legal purposes only.
    """
    enteredInError = "entered-in-error"


class LocationMode(CodeSystemValue):
    """ Indicates whether a resource instance represents a specific location or a class of locations.

    URL: http://hl7.org/fhir/location-mode
    ValueSet: http://hl7.org/fhir/ValueSet/location-mode
    """
    URL = "http://hl7.org/fhir/location-mode"
    EXPERIMENTAL = False

    """ The Location resource represents a specific instance of a location (e.g. Operating Theatre 1A).
    """
    instance = "instance"

    """ The Location represents a class of locations (e.g. Any Operating Theatre) although this class of locations could
	/// be constrained within a specific boundary (such as organization, or parent location, address etc.).
    """
    kind = "kind"


class LocationStatus(CodeSystemValue):
    """ Indicates whether the location is still in use.

    URL: http://hl7.org/fhir/location-status
    ValueSet: http://hl7.org/fhir/ValueSet/location-status
    """
    URL = "http://hl7.org/fhir/location-status"
    EXPERIMENTAL = False

    """ The location is operational.
    """
    active = "active"

    """ The location is temporarily closed.
    """
    suspended = "suspended"

    """ The location is no longer used.
    """
    inactive = "inactive"


class LocationType(CodeSystemValue):
    """ This example value set defines a set of codes that can be used to indicate the physical form of the Location.

    URL: http://hl7.org/fhir/location-physical-type
    ValueSet: http://hl7.org/fhir/ValueSet/location-physical-type
    """
    URL = "http://hl7.org/fhir/location-physical-type"
    EXPERIMENTAL = True

    """ A collection of buildings or other locations such as a site or a campus.
    """
    si = "si"

    """ Any Building or structure. This may contain rooms, corridors, wings, etc. It might not have walls, or a roof,
	/// but is considered a defined/allocated space.
    """
    bu = "bu"

    """ A Wing within a Building, this often contains levels, rooms and corridors.
    """
    wi = "wi"

    """ A Ward is a section of a medical facility that may contain rooms and other types of location.
    """
    wa = "wa"

    """ A Level in a multi-level Building/Structure.
    """
    lvl = "lvl"

    """ Any corridor within a Building, that may connect rooms.
    """
    co = "co"

    """ A space that is allocated as a room, it may have walls/roof etc., but does not require these.
    """
    ro = "ro"

    """ A space that is allocated for sleeping/laying on. This is not the physical bed/trolley that may be moved about,
	/// but the space it may occupy.
    """
    bd = "bd"

    """ A means of transportation.
    """
    ve = "ve"

    """ A residential dwelling. Usually used to reference a location that a person/patient may reside.
    """
    ho = "ho"

    """ A container that can store goods, equipment, medications or other items.
    """
    ca = "ca"

    """ A defined path to travel between 2 points that has a known name.
    """
    rd = "rd"

    """ A defined physical boundary of something, such as a flood risk zone, region, postcode
    """
    area = "area"

    """ A wide scope that covers a conceptual domain, such as a Nation (Country wide community or Federal Government -
	/// e.g. Ministry of Health),  Province or State (community or Government), Business (throughout the enterprise),
	/// Nation with a business scope of an agency (e.g. CDC, FDA etc.) or a Business segment (UK Pharmacy), not just an
	/// physical boundry
    """
    jdn = "jdn"


class MaritalStatusCodes(CodeSystemValue):
    """ This value set defines the set of codes that can be used to indicate the marital status of a person.

    URL: http://hl7.org/fhir/marital-status
    ValueSet: http://hl7.org/fhir/ValueSet/marital-status
    """
    URL = "http://hl7.org/fhir/marital-status"
    EXPERIMENTAL = True

    """ The person is not presently married. The marital history is not known or stated.
    """
    U = "U"


class MatchGrade(CodeSystemValue):
    """ A Master Patient Index (MPI) assessment of whether a candidate patient record is a match or not.

    URL: http://hl7.org/fhir/match-grade
    ValueSet: http://hl7.org/fhir/ValueSet/match-grade
    """
    URL = "http://hl7.org/fhir/match-grade"
    EXPERIMENTAL = False

    """ This record meets the matching criteria to be automatically considered as a full match.
    """
    certain = "certain"

    """ This record is a close match, but not a certain match. Additional review (e.g. by a human) may be required
	/// before using this as a match.
    """
    probable = "probable"

    """ This record may be a matching one. Additional review (e.g. by a human) SHOULD be performed before using this as
	/// a match.
    """
    possible = "possible"

    """ This record is known not to be a match. Note that usually non-matching records are not returned, but in some
	/// cases records previously or likely considered as a match may specifically be negated by the matching engine
    """
    certainlyNot = "certainly-not"


class MaxOccurs(CodeSystemValue):
    """ Flags an element as having unlimited repetitions

    URL: http://hl7.org/fhir/question-max-occurs
    ValueSet: http://hl7.org/fhir/ValueSet/question-max-occurs
    """
    URL = "http://hl7.org/fhir/question-max-occurs"
    EXPERIMENTAL = False

    """ Element can repeat an unlimited number of times
    """
    max = "*"


class MeasmntPrinciple(CodeSystemValue):
    """ Different measurement principle supported by the device.

    URL: http://hl7.org/fhir/measurement-principle
    ValueSet: http://hl7.org/fhir/ValueSet/measurement-principle
    """
    URL = "http://hl7.org/fhir/measurement-principle"
    EXPERIMENTAL = False

    """ Measurement principle isn't in the list.
    """
    other = "other"

    """ Measurement is done using the chemical principle.
    """
    chemical = "chemical"

    """ Measurement is done using the electrical principle.
    """
    electrical = "electrical"

    """ Measurement is done using the impedance principle.
    """
    impedance = "impedance"

    """ Measurement is done using the nuclear principle.
    """
    nuclear = "nuclear"

    """ Measurement is done using the optical principle.
    """
    optical = "optical"

    """ Measurement is done using the thermal principle.
    """
    thermal = "thermal"

    """ Measurement is done using the biological principle.
    """
    biological = "biological"

    """ Measurement is done using the mechanical principle.
    """
    mechanical = "mechanical"

    """ Measurement is done using the acoustical principle.
    """
    acoustical = "acoustical"

    """ Measurement is done using the manual principle.
    """
    manual = "manual"


class MeasureDataUsage(CodeSystemValue):
    """ The intended usage for supplemental data elements in the measure

    URL: http://hl7.org/fhir/measure-data-usage
    ValueSet: http://hl7.org/fhir/ValueSet/measure-data-usage
    """
    URL = "http://hl7.org/fhir/measure-data-usage"
    EXPERIMENTAL = False

    """ The data is intended to be provided as additional information alongside the measure results
    """
    supplementalData = "supplemental-data"

    """ The data is intended to be used to calculate and apply a risk adjustment model for the measure
    """
    riskAdjustmentFactor = "risk-adjustment-factor"


class MeasurePopulationType(CodeSystemValue):
    """ The type of population

    URL: http://hl7.org/fhir/measure-population
    ValueSet: http://hl7.org/fhir/ValueSet/measure-population
    """
    URL = "http://hl7.org/fhir/measure-population"
    EXPERIMENTAL = False

    """ The initial population refers to all patients or events to be evaluated by a quality measure involving patients
	/// who share a common set of specified characterstics. All patients or events counted (for example, as numerator,
	/// as denominator) are drawn from the initial population
    """
    initialPopulation = "initial-population"

    """ The upper portion of a fraction used to calculate a rate, proportion, or ratio. Also called the measure focus,
	/// it is the target process, condition, event, or outcome. Numerator criteria are the processes or outcomes
	/// expected for each patient, or event defined in the denominator. A numerator statement describes the clinical
	/// action that satisfies the conditions of the measure
    """
    numerator = "numerator"

    """ Numerator exclusion criteria define patients or events to be removed from the numerator. Numerator exclusions
	/// are used in proportion and ratio measures to help narrow the numerator (for inverted measures)
    """
    numeratorExclusion = "numerator-exclusion"

    """ The lower portion of a fraction used to calculate a rate, proportion, or ratio. The denominator can be the same
	/// as the initial population, or a subset of the initial population to further constrain the population for the
	/// purpose of the measure
    """
    denominator = "denominator"

    """ Denominator exclusion criteria define patients or events that should be removed from the denominator before
	/// determining if numerator criteria are met. Denominator exclusions are used in proportion and ratio measures to
	/// help narrow the denominator. For example, patients with bilateral lower extremity amputations would be listed as
	/// a denominator exclusion for a measure requiring foot exams
    """
    denominatorExclusion = "denominator-exclusion"

    """ Denominator exceptions are conditions that should remove a patient or event from the denominator of a measure
	/// only if the numerator criteria are not met. Denominator exception allows for adjustment of the calculated score
	/// for those providers with higher risk populations. Denominator exception criteria are only used in proportion
	/// measures
    """
    denominatorException = "denominator-exception"

    """ Measure population criteria define the patients or events for which the individual observation for the measure
	/// should be taken. Measure populations are used for continuous variable measures rather than numerator and
	/// denominator criteria
    """
    measurePopulation = "measure-population"

    """ Measure population criteria define the patients or events that should be removed from the measure population
	/// before determining the outcome of one or more continuous variables defined for the measure observation. Measure
	/// population exclusion criteria are used within continuous variable measures to help narrow the measure population
    """
    measurePopulationExclusion = "measure-population-exclusion"

    """ Defines the individual observation to be performed for each patient or event in the measure population. Measure
	/// observations for each case in the population are aggregated to determine the overall measure score for the
	/// population
    """
    measureObservation = "measure-observation"


class MeasureReportStatus(CodeSystemValue):
    """ The status of the measure report

    URL: http://hl7.org/fhir/measure-report-status
    ValueSet: http://hl7.org/fhir/ValueSet/measure-report-status
    """
    URL = "http://hl7.org/fhir/measure-report-status"
    EXPERIMENTAL = False

    """ The report is complete and ready for use
    """
    complete = "complete"

    """ The report is currently being generated
    """
    pending = "pending"

    """ An error occurred attempting to generate the report
    """
    error = "error"


class MeasureReportType(CodeSystemValue):
    """ The type of the measure report

    URL: http://hl7.org/fhir/measure-report-type
    ValueSet: http://hl7.org/fhir/ValueSet/measure-report-type
    """
    URL = "http://hl7.org/fhir/measure-report-type"
    EXPERIMENTAL = False

    """ An individual report that provides information on the performance for a given measure with respect to a single
	/// subject
    """
    individual = "individual"

    """ A subject list report that includes a listing of subjects that satisfied each population criteria in the measure
    """
    subjectList = "subject-list"

    """ A summary report that returns the number of members in each population criteria for the measure
    """
    summary = "summary"


class MeasureScoring(CodeSystemValue):
    """ The scoring type of the measure

    URL: http://hl7.org/fhir/measure-scoring
    ValueSet: http://hl7.org/fhir/ValueSet/measure-scoring
    """
    URL = "http://hl7.org/fhir/measure-scoring"
    EXPERIMENTAL = False

    """ The measure score is defined using a proportion
    """
    proportion = "proportion"

    """ The measure score is defined using a ratio
    """
    ratio = "ratio"

    """ The score is defined by a calculation of some quantity
    """
    continuousVariable = "continuous-variable"

    """ The measure is a cohort definition
    """
    cohort = "cohort"


class MeasureType(CodeSystemValue):
    """ The type of measure (includes codes from 2.16.840.1.113883.1.11.20368)

    URL: http://hl7.org/fhir/measure-type
    ValueSet: http://hl7.org/fhir/ValueSet/measure-type
    """
    URL = "http://hl7.org/fhir/measure-type"
    EXPERIMENTAL = False

    """ A measure which focuses on a process which leads to a certain outcome, meaning that a scientific basis exists
	/// for believing that the process, when executed well, will increase the probability of achieving a desired outcome
    """
    process = "process"

    """ A measure that indicates the result of the performance (or non-performance) of a function or process
    """
    outcome = "outcome"

    """ A measure that focuses on a health care provider's capacity, systems, and processes to provide high-quality care
    """
    structure = "structure"

    """ A measure that focuses on patient-reported information such as patient engagement or patient experience measures
    """
    patientReportedOutcome = "patient-reported-outcome"

    """ A measure that combines multiple component measures in to a single quality measure
    """
    composite = "composite"


class MediaModality(CodeSystemValue):
    """ Detailed information about the type of the image - its kind, purpose, or the kind of equipment used to generate it.

    URL: http://hl7.org/fhir/media-modality
    ValueSet: http://hl7.org/fhir/ValueSet/media-modality
    """
    URL = "http://hl7.org/fhir/media-modality"
    EXPERIMENTAL = True

    """ A diagram. Often used in diagnostic reports
    """
    diagram = "diagram"

    """ A digital record of a fax document
    """
    fax = "fax"

    """ A digital scan of a document. This is reserved for when there is not enough metadata to create a document
	/// reference
    """
    scan = "scan"

    """ A retinal image used for identification purposes
    """
    retina = "retina"

    """ A finger print scan used for identification purposes
    """
    fingerprint = "fingerprint"

    """ An iris scan used for identification purposes
    """
    iris = "iris"

    """ A palm scan used for identification purposes
    """
    palm = "palm"

    """ A face scan used for identification purposes
    """
    face = "face"


class MediaType(CodeSystemValue):
    """ Codes for high level media categories.

    URL: http://hl7.org/fhir/CodeSystem/media-type
    ValueSet: http://hl7.org/fhir/ValueSet/media-type
    """
    URL = "http://hl7.org/fhir/CodeSystem/media-type"
    EXPERIMENTAL = True

    """ The media consists of one or more unmoving images, including photographs, computer-generated graphs and charts,
	/// and scanned documents
    """
    image = "image"

    """ The media consists of a series of frames that capture a moving image
    """
    video = "video"

    """ The media consists of a sound recording
    """
    audio = "audio"


class MedicationAdministrationCategory(CodeSystemValue):
    """ A coded concept describing where the medication administered is expected to occur

    URL: http://hl7.org/fhir/medication-admin-category
    ValueSet: http://hl7.org/fhir/ValueSet/medication-admin-category
    """
    URL = "http://hl7.org/fhir/medication-admin-category"
    EXPERIMENTAL = False

    """ Includes administrations in an inpatient or acute care setting
    """
    inpatient = "inpatient"

    """ Includes administrations in an outpatient setting (for example, Emergency Department, Outpatient Clinic,
	/// Outpatient Surgery, Doctor's office)
    """
    outpatient = "outpatient"

    """ Includes administrations by the patient in their home (this would include long term care or nursing homes,
	/// hospices, etc.)
    """
    community = "community"


class MedicationAdministrationPerformerFunction(CodeSystemValue):
    """ A code describing the role an individual played in administering the medication

    URL: http://hl7.org/fhir/med-admin-perform-function
    ValueSet: http://hl7.org/fhir/ValueSet/med-admin-perform-function
    """
    URL = "http://hl7.org/fhir/med-admin-perform-function"
    EXPERIMENTAL = False

    """ A person, non-person living subject, organization or device that who actually and principally carries out the
	/// action
    """
    performer = "performer"

    """ A person who verifies the correctness and appropriateness of the service (plan, order, event, etc.) and hence
	/// takes on accountability.
    """
    verifier = "verifier"

    """ A person witnessing the action happening without doing anything. A witness is not necessarily aware, much less
	/// approves of anything stated in the service event. Example for a witness is students watching an operation or an
	/// advanced directive witness.
    """
    witness = "witness"


class MedicationAdministrationStatus(CodeSystemValue):
    """ A set of codes indicating the current status of a MedicationAdministration.

    URL: http://hl7.org/fhir/medication-admin-status
    ValueSet: http://hl7.org/fhir/ValueSet/medication-admin-status
    """
    URL = "http://hl7.org/fhir/medication-admin-status"
    EXPERIMENTAL = False

    """ The administration has started but has not yet completed.
    """
    inProgress = "in-progress"

    """ The administration was terminated prior to any impact on the subject (though preparatory actions may have been
	/// taken)
    """
    notDone = "not-done"

    """ Actions implied by the administration have been temporarily halted, but are expected to continue later. May also
	/// be called "suspended".
    """
    onHold = "on-hold"

    """ All actions that are implied by the administration have occurred.
    """
    completed = "completed"

    """ The administration was entered in error and therefore nullified.
    """
    enteredInError = "entered-in-error"

    """ Actions implied by the administration have been permanently halted, before all of them occurred.
    """
    stopped = "stopped"

    """ The authoring system does not know which of the status values currently applies for this request. Note: This
	/// concept is not to be used for "other" - one of the listed statuses is presumed to apply, it's just not known
	/// which one.
    """
    unknown = "unknown"


class MedicationDispenseCategory(CodeSystemValue):
    """ A code describing where the dispensed medication is expected to be consumed or administered

    URL: http://hl7.org/fhir/medication-dispense-category
    ValueSet: http://hl7.org/fhir/ValueSet/medication-dispense-category
    """
    URL = "http://hl7.org/fhir/medication-dispense-category"
    EXPERIMENTAL = False

    """ Includes dispenses for medications to be administered or consumed in an inpatient or acute care setting
    """
    inpatient = "inpatient"

    """ Includes dispenses for medications to be administered or consumed in an outpatient setting (for example,
	/// Emergency Department, Outpatient Clinic, Outpatient Surgery, Doctor's office)
    """
    outpatient = "outpatient"

    """ Includes dispenses for medications to be administered or consumed by the patient in their home (this would
	/// include long term care or nursing homes, hospices, etc.)
    """
    community = "community"


class MedicationDispensePerformerFunction(CodeSystemValue):
    """ A code describing the role an individual played in dispensing a medication

    URL: http://hl7.org/fhir/med-dispense-perform-function
    ValueSet: http://hl7.org/fhir/ValueSet/med-dispense-perform-function
    """
    URL = "http://hl7.org/fhir/med-dispense-perform-function"
    EXPERIMENTAL = False

    """ Recorded the details of the request
    """
    dataenterer = "dataenterer"

    """ Prepared the medication
    """
    packager = "packager"

    """ Performed initial quality assurance on the prepared medication
    """
    checker = "checker"

    """ Performed the final quality assurance on the prepared medication against the request. Typically, this is a
	/// pharmacist function.
    """
    finalchecker = "finalchecker"


class MedicationDispenseStatus(CodeSystemValue):
    """ A coded concept specifying the state of the dispense event.

    URL: http://hl7.org/fhir/medication-dispense-status
    ValueSet: http://hl7.org/fhir/ValueSet/medication-dispense-status
    """
    URL = "http://hl7.org/fhir/medication-dispense-status"
    EXPERIMENTAL = False

    """ The core event has not started yet, but some staging activities have begun (e.g. initial compounding or
	/// packaging of medication). Preparation stages may be tracked for billing purposes.
    """
    preparation = "preparation"

    """ The dispensed product is ready for pickup.
    """
    inProgress = "in-progress"

    """ The dispensed product was not and will never be picked up by the patient.
    """
    cancelled = "cancelled"

    """ The dispense process is paused while waiting for an external event to reactivate the dispense.  For example, new
	/// stock has arrived or the prescriber has called.
    """
    onHold = "on-hold"

    """ The dispensed product has been picked up.
    """
    completed = "completed"

    """ The dispense was entered in error and therefore nullified.
    """
    enteredInError = "entered-in-error"

    """ Actions implied by the dispense have been permanently halted, before all of them occurred.
    """
    stopped = "stopped"

    """ The authoring system does not know which of the status values applies for this medication dispense.  Note: this
	/// concept is not to be used for "other" - one of the listed statuses is presumed to apply, it's just now known
	/// which one.
    """
    unknown = "unknown"


class MedicationDispenseStatusReason(CodeSystemValue):
    """ A code describing why a dispense was not performed

    URL: http://hl7.org/fhir/med-dispense-status-reason
    ValueSet: http://hl7.org/fhir/ValueSet/med-dispense-status-reason
    """
    URL = "http://hl7.org/fhir/med-dispense-status-reason"
    EXPERIMENTAL = False

    """ The order has been stopped by the prescriber but this fact has not necessarily captured electronically. Example:
	/// A verbal stop, a fax, etc.
    """
    frr01 = "frr01"

    """ Order has not been fulfilled within a reasonable amount of time, and might not be current.
    """
    frr02 = "frr02"

    """ Data needed to safely act on the order which was expected to become available independent of the order is not
	/// yet available. Example: Lab results, diagnostic imaging, etc.
    """
    frr03 = "frr03"

    """ Product not available or manufactured. Cannot supply.
    """
    frr04 = "frr04"

    """ The dispenser has ethical, religious or moral objections to fulfilling the order/dispensing the product.
    """
    frr05 = "frr05"

    """ Fulfiller not able to provide appropriate care associated with fulfilling the order.
	/// Example: Therapy requires ongoing monitoring by fulfiller and fulfiller will be ending practice, leaving town,
	/// unable to schedule necessary time, etc.
    """
    frr06 = "frr06"

    """ This therapy has been ordered as a backup to a preferred therapy. This order will be released when and if the
	/// preferred therapy is unsuccessful.
    """
    altchoice = "altchoice"

    """ Clarification is required before the order can be acted upon.
    """
    clarif = "clarif"

    """ The current level of the medication in the patient's system is too high. The medication is suspended to allow
	/// the level to subside to a safer level.
    """
    drughigh = "drughigh"

    """ The patient has been admitted to a care facility and their community medications are suspended until hospital
	/// discharge.
    """
    hospadm = "hospadm"

    """ The therapy would interfere with a planned lab test and the therapy is being withdrawn until the test is
	/// completed.
    """
    labint = "labint"

    """ Patient not available for a period of time due to a scheduled therapy, leave of absence or other reason.
    """
    nonAvail = "non-avail"

    """ The patient is pregnant or breast feeding. The therapy will be resumed when the pregnancy is complete and the
	/// patient is no longer breastfeeding.
    """
    preg = "preg"

    """ The patient is believed to be allergic to a substance that is part of the therapy and the therapy is being
	/// temporarily withdrawn to confirm.
    """
    salg = "salg"

    """ The drug interacts with a short-term treatment that is more urgently required. This order will be resumed when
	/// the short-term treatment is complete.
    """
    sddi = "sddi"

    """ Another short-term co-occurring therapy fulfills the same purpose as this therapy. This therapy will be resumed
	/// when the co-occuring therapy is complete.
    """
    sdupther = "sdupther"

    """ The patient is believed to have an intolerance to a substance that is part of the therapy and the therapy is
	/// being temporarily withdrawn to confirm.
    """
    sintol = "sintol"

    """ The drug is contraindicated for patients receiving surgery and the patient is scheduled to be admitted for
	/// surgery in the near future. The drug will be resumed when the patient has sufficiently recovered from the
	/// surgery.
    """
    surg = "surg"

    """ The patient was previously receiving a medication contraindicated with the current medication. The current
	/// medication will remain on hold until the prior medication has been cleansed from their system.
    """
    washout = "washout"


class MedicationRequestCategory(CodeSystemValue):
    """ A coded concept identifying the category of medication request.  For example, where the medication is to be consumed or
administered, or the type of medication treatment).

    URL: http://hl7.org/fhir/medication-request-category
    ValueSet: http://hl7.org/fhir/ValueSet/medication-request-category
    """
    URL = "http://hl7.org/fhir/medication-request-category"
    EXPERIMENTAL = False

    """ Includes orders for medications to be administered or consumed in an inpatient or acute care setting
    """
    inpatient = "inpatient"

    """ Includes orders for medications to be administered or consumed in an outpatient setting (for example, Emergency
	/// Department, Outpatient Clinic, Outpatient Surgery, Doctor's office)
    """
    outpatient = "outpatient"

    """ Includes orders for medications to be administered or consumed by the patient in their home (this would include
	/// long term care or nursing homes, hospices, etc.)
    """
    community = "community"

    """ Includes orders for medications created when the patient is being released from a facility
    """
    discharge = "discharge"


class MedicationRequestIntent(CodeSystemValue):
    """ The kind of medication order

    URL: http://hl7.org/fhir/medication-request-intent
    ValueSet: http://hl7.org/fhir/ValueSet/medication-request-intent
    """
    URL = "http://hl7.org/fhir/medication-request-intent"
    EXPERIMENTAL = False

    """ The request is a suggestion made by someone/something that doesn't have an intention to ensure it occurs and
	/// without providing an authorization to act
    """
    proposal = "proposal"

    """ The request represents an intension to ensure something occurs without providing an authorization for others to
	/// act
    """
    plan = "plan"

    """ The request represents a request/demand and authorization for action
    """
    order = "order"

    """ The request represents the original authorization for the medication request.
    """
    originalOrder = "original-order"

    """ The request represents an instance for the particular order, for example a medication administration record.
    """
    instanceOrder = "instance-order"

    """ The request represents a component or option for a RequestGroup that establishes timing, conditionality and/or
	/// other constraints among a set of requests.
    """
    option = "option"


class MedicationRequestStatus(CodeSystemValue):
    """ A coded concept specifying the state of the prescribing event. Describes the lifecycle of the prescription

    URL: http://hl7.org/fhir/medication-request-status
    ValueSet: http://hl7.org/fhir/ValueSet/medication-request-status
    """
    URL = "http://hl7.org/fhir/medication-request-status"
    EXPERIMENTAL = False

    """ The prescription is 'actionable', but not all actions that are implied by it have occurred yet.
    """
    active = "active"

    """ Actions implied by the prescription are to be temporarily halted, but are expected to continue later.  May also
	/// be called "suspended".
    """
    onHold = "on-hold"

    """ The prescription has been withdrawn before any administrations have occurred
    """
    cancelled = "cancelled"

    """ All actions that are implied by the prescription have occurred.
    """
    completed = "completed"

    """ Some of the actions that are implied by the medication request may have occurred.  For example, the medication
	/// may have been dispensed and the patient may have taken some of the medication.  Clinical decision support
	/// systems should take this status into account
    """
    enteredInError = "entered-in-error"

    """ Actions implied by the prescription are to be permanently halted, before all of the administrations occurred.
	/// This should not be used if the original order was entered in error
    """
    stopped = "stopped"

    """ The prescription is not yet 'actionable', i.e. it is a work in progress, requires sign-off or verification, and
	/// needs to be run through decision support process.
    """
    draft = "draft"

    """ The authoring system does not know which of the status values currently applies for this request
    """
    unknown = "unknown"


class MedicationRequestStatusReason(CodeSystemValue):
    """ Identifies the reasons for a given status

    URL: http://hl7.org/fhir/med-request-status-reason
    ValueSet: http://hl7.org/fhir/ValueSet/med-request-status-reason
    """
    URL = "http://hl7.org/fhir/med-request-status-reason"
    EXPERIMENTAL = False

    """ This therapy has been ordered as a backup to a preferred therapy. This order will be released when and if the
	/// preferred therapy is unsuccessful.
    """
    altchoice = "altchoice"

    """ Clarification is required before the order can be acted upon.
    """
    clarif = "clarif"

    """ The current level of the medication in the patient's system is too high. The medication is suspended to allow
	/// the level to subside to a safer level.
    """
    drughigh = "drughigh"

    """ The patient has been admitted to a care facility and their community medications are suspended until hospital
	/// discharge.
    """
    hospadm = "hospadm"

    """ The therapy would interfere with a planned lab test and the therapy is being withdrawn until the test is
	/// completed.
    """
    labint = "labint"

    """ Patient not available for a period of time due to a scheduled therapy, leave of absence or other reason.
    """
    nonAvail = "non-avail"

    """ The patient is pregnant or breast feeding. The therapy will be resumed when the pregnancy is complete and the
	/// patient is no longer breastfeeding.
    """
    preg = "preg"

    """ The patient is believed to be allergic to a substance that is part of the therapy and the therapy is being
	/// temporarily withdrawn to confirm.
    """
    salg = "salg"

    """ The drug interacts with a short-term treatment that is more urgently required. This order will be resumed when
	/// the short-term treatment is complete.
    """
    sddi = "sddi"

    """ Another short-term concurrent therapy fulfills the same purpose as this therapy. This therapy will be resumed
	/// when the concurrent therapy is complete.
    """
    sdupther = "sdupther"

    """ The patient is believed to have an intolerance to a substance that is part of the therapy and the therapy is
	/// being temporarily withdrawn to confirm.
    """
    sintol = "sintol"

    """ The drug is contraindicated for patients receiving surgery and the patient is scheduled to be admitted for
	/// surgery in the near future. The drug will be resumed when the patient has sufficiently recovered from the
	/// surgery.
    """
    surg = "surg"

    """ The patient was previously receiving a medication contraindicated with the current medication. The current
	/// medication will remain on hold until the prior medication has been cleansed from their system.
    """
    washout = "washout"


class MedicationStatementCategory(CodeSystemValue):
    """ A coded concept identifying where the medication included in the MedicationStatement is expected to be consumed or
administered

    URL: http://hl7.org/fhir/medication-statement-category
    ValueSet: http://hl7.org/fhir/ValueSet/medication-statement-category
    """
    URL = "http://hl7.org/fhir/medication-statement-category"
    EXPERIMENTAL = False

    """ Includes orders for medications to be administered or consumed in an inpatient or acute care setting
    """
    inpatient = "inpatient"

    """ Includes orders for medications to be administered or consumed in an outpatient setting (for example, Emergency
	/// Department, Outpatient Clinic, Outpatient Surgery, Doctor's office)
    """
    outpatient = "outpatient"

    """ Includes orders for medications to be administered or consumed by the patient in their home (this would include
	/// long term care or nursing homes, hospices, etc.)
    """
    community = "community"

    """ Includes statements about medication use, including over the counter medication, provided by the patient, agent
	/// or another provider
    """
    patientspecified = "patientspecified"


class MedicationStatementStatus(CodeSystemValue):
    """ A coded concept indicating the current status of a MedicationStatement.

    URL: http://hl7.org/fhir/medication-statement-status
    ValueSet: http://hl7.org/fhir/ValueSet/medication-statement-status
    """
    URL = "http://hl7.org/fhir/medication-statement-status"
    EXPERIMENTAL = False

    """ The medication is still being taken.
    """
    active = "active"

    """ The medication is no longer being taken.
    """
    completed = "completed"

    """ Some of the actions that are implied by the medication statement may have occurred.  For example, the patient
	/// may have taken some of the medication.  Clinical decision support systems should take this status into account
    """
    enteredInError = "entered-in-error"

    """ The medication may be taken at some time in the future.
    """
    intended = "intended"

    """ Actions implied by the statement have been permanently halted, before all of them occurred. This should not be
	/// used if the statement was entered in error
    """
    stopped = "stopped"

    """ Actions implied by the statement have been temporarily halted, but are expected to continue later. May also be
	/// called "suspended".
    """
    onHold = "on-hold"

    """ The state of the medication use is not currently known.
    """
    unknown = "unknown"

    """ The medication was not consumed by the patient
    """
    notTaken = "not-taken"


class MedicationStatementTaken(CodeSystemValue):
    """ A coded concept identifying level of certainty if patient has taken or has not taken the medication

    URL: http://hl7.org/fhir/medication-statement-taken
    ValueSet: http://hl7.org/fhir/ValueSet/medication-statement-taken
    """
    URL = "http://hl7.org/fhir/medication-statement-taken"
    EXPERIMENTAL = False

    """ Positive assertion that patient has taken medication
    """
    Y = "y"

    """ Negative assertion that patient has not taken medication
    """
    N = "n"

    """ Unknown assertion if patient has taken medication
    """
    unk = "unk"

    """ Patient reporting does not apply
    """
    na = "na"


class MedicationStatus(CodeSystemValue):
    """ A coded concept defining if the medication is in active use

    URL: http://hl7.org/fhir/medication-status
    ValueSet: http://hl7.org/fhir/ValueSet/medication-status
    """
    URL = "http://hl7.org/fhir/medication-status"
    EXPERIMENTAL = False

    """ The medication is available for use
    """
    active = "active"

    """ The medication is not available for use
    """
    inactive = "inactive"

    """ The medication was entered in error
    """
    enteredInError = "entered-in-error"


class MessageSignificanceCategory(CodeSystemValue):
    """ The impact of the content of a message.

    URL: http://hl7.org/fhir/message-significance-category
    ValueSet: http://hl7.org/fhir/ValueSet/message-significance-category
    """
    URL = "http://hl7.org/fhir/message-significance-category"
    EXPERIMENTAL = False

    """ The message represents/requests a change that should not be processed more than once; e.g., making a booking for
	/// an appointment.
    """
    consequence = "consequence"

    """ The message represents a response to query for current information. Retrospective processing is wrong and/or
	/// wasteful.
    """
    currency = "currency"

    """ The content is not necessarily intended to be current, and it can be reprocessed, though there may be version
	/// issues created by processing old notifications.
    """
    notification = "notification"


class MessageTransport(CodeSystemValue):
    """ The protocol used for message transport.

    URL: http://hl7.org/fhir/message-transport
    ValueSet: http://hl7.org/fhir/ValueSet/message-transport
    """
    URL = "http://hl7.org/fhir/message-transport"
    EXPERIMENTAL = False

    """ The application sends or receives messages using HTTP POST (may be over http: or https:).
    """
    http = "http"

    """ The application sends or receives messages using File Transfer Protocol.
    """
    ftp = "ftp"

    """ The application sends or receives messages using HL7's Minimal Lower Level Protocol.
    """
    mllp = "mllp"


class MessageheaderResponseRequest(CodeSystemValue):
    """ HL7-defined table of codes which identify conditions under which acknowledgments are required to be returned in response
to a message.

    URL: http://hl7.org/fhir/messageheader-response-request
    ValueSet: http://hl7.org/fhir/ValueSet/messageheader-response-request
    """
    URL = "http://hl7.org/fhir/messageheader-response-request"
    EXPERIMENTAL = False

    """ initiator expects a response for this message
    """
    always = "always"

    """ initiator expects a response only if in error
    """
    onError = "on-error"

    """ initiator does not expect a response
    """
    never = "never"

    """ initiator expects a response only if successful
    """
    onSuccess = "on-success"


class MissingToothReasonCodes(CodeSystemValue):
    """ This value set includes sample Missing Tooth Reason codes.

    URL: http://hl7.org/fhir/missingtoothreason
    ValueSet: http://hl7.org/fhir/ValueSet/missing-tooth-reason
    """
    URL = "http://hl7.org/fhir/missingtoothreason"
    EXPERIMENTAL = True

    """ Extraction
    """
    E = "e"

    """ Congenital
    """
    C = "c"

    """ Unknown
    """
    U = "u"

    """ Other
    """
    O = "o"


class ModifierTypeCodes(CodeSystemValue):
    """ This value set includes sample Modifier type codes.

    URL: http://hl7.org/fhir/modifiers
    ValueSet: http://hl7.org/fhir/ValueSet/claim-modifiers
    """
    URL = "http://hl7.org/fhir/modifiers"
    EXPERIMENTAL = True

    """ Repair of prior service or installation.
    """
    A = "a"

    """ Temporary service or installation.
    """
    B = "b"

    """ Treatment associated with TMJ.
    """
    C = "c"

    """ Implant or associated with an implant.
    """
    E = "e"

    """ A Rush service or service performed outside of normal office hours.
    """
    rooh = "rooh"

    """ None.
    """
    X = "x"


class NHINPurposeOfUse(CodeSystemValue):
    """ This value set is suitable for use with the provenance resource. It is derived from, but not compatible with, the HL7 v3
Purpose of use Code system.

    URL: http://healthit.gov/nhin/purposeofuse
    ValueSet: http://hl7.org/fhir/ValueSet/nhin-purposeofuse
    """
    URL = "http://healthit.gov/nhin/purposeofuse"
    EXPERIMENTAL = False

    """ Treatment
    """
    TREATMENT = "TREATMENT"

    """ Payment
    """
    PAYMENT = "PAYMENT"

    """ Healthcare Operations
    """
    OPERATIONS = "OPERATIONS"

    """ System Administration
    """
    SYSADMIN = "SYSADMIN"

    """ Fraud detection
    """
    FRAUD = "FRAUD"

    """ Use or disclosure of Psychotherapy Notes
    """
    PSYCHOTHERAPY = "PSYCHOTHERAPY"

    """ Use or disclosure by the covered entity for its own training programs
    """
    TRAINING = "TRAINING"

    """ Use or disclosure by the covered entity to defend itself in a legal action
    """
    LEGAL = "LEGAL"

    """ Marketing
    """
    MARKETING = "MARKETING"

    """ Use and disclosure for facility directories
    """
    DIRECTORY = "DIRECTORY"

    """ Disclose to a family member, other relative, or a close personal friend of the individual
    """
    FAMILY = "FAMILY"

    """ Uses and disclosures with the individual present.
    """
    PRESENT = "PRESENT"

    """ Permission cannot practicably be provided because of the individual's incapacity or an emergency.
    """
    EMERGENCY = "EMERGENCY"

    """ Use and disclosures for disaster relief purposes.
    """
    DISASTER = "DISASTER"

    """ Uses and disclosures for public health activities.
    """
    PUBLICHEALTH = "PUBLICHEALTH"

    """ Disclosures about victims of abuse, neglect or domestic violence.
    """
    ABUSE = "ABUSE"

    """ Uses and disclosures for health oversight activities.
    """
    OVERSIGHT = "OVERSIGHT"

    """ Disclosures for judicial and administrative proceedings.
    """
    JUDICIAL = "JUDICIAL"

    """ Disclosures for law enforcement purposes.
    """
    LAW = "LAW"

    """ Uses and disclosures about decedents.
    """
    DECEASED = "DECEASED"

    """ Uses and disclosures for cadaveric organ,  eye or tissue donation purposes
    """
    DONATION = "DONATION"

    """ Uses and disclosures for research purposes.
    """
    RESEARCH = "RESEARCH"

    """ Uses and disclosures to avert a serious threat to health or safety.
    """
    THREAT = "THREAT"

    """ Uses and disclosures for specialized government functions.
    """
    GOVERNMENT = "GOVERNMENT"

    """ Disclosures for workers' compensation.
    """
    WORKERSCOMP = "WORKERSCOMP"

    """ Disclosures for insurance or disability coverage determination
    """
    COVERAGE = "COVERAGE"

    """ Request of the Individual
    """
    REQUEST = "REQUEST"


class NameUse(CodeSystemValue):
    """ The use of a human name

    URL: http://hl7.org/fhir/name-use
    ValueSet: http://hl7.org/fhir/ValueSet/name-use
    """
    URL = "http://hl7.org/fhir/name-use"
    EXPERIMENTAL = False

    """ Known as/conventional/the one you normally use
    """
    usual = "usual"

    """ The formal name as registered in an official (government) registry, but which name might not be commonly used.
	/// May be called "legal name".
    """
    official = "official"

    """ A temporary name. Name.period can provide more detailed information. This may also be used for temporary names
	/// assigned at birth or in emergency situations.
    """
    temp = "temp"

    """ A name that is used to address the person in an informal manner, but is not part of their formal or usual name
    """
    nickname = "nickname"

    """ Anonymous assigned name, alias, or pseudonym (used to protect a person's identity for privacy reasons)
    """
    anonymous = "anonymous"

    """ This name is no longer in use (or was never correct, but retained for records)
    """
    old = "old"

    """ A name used prior to changing name because of marriage. This name use is for use by applications that collect
	/// and store names that were used prior to a marriage. Marriage naming customs vary greatly around the world, and
	/// are constantly changing. This term is not gender specific. The use of this term does not imply any particular
	/// history for a person's name
    """
    maiden = "maiden"


class NamingSystemIdentifierType(CodeSystemValue):
    """ Identifies the style of unique identifier used to identify a namespace.

    URL: http://hl7.org/fhir/namingsystem-identifier-type
    ValueSet: http://hl7.org/fhir/ValueSet/namingsystem-identifier-type
    """
    URL = "http://hl7.org/fhir/namingsystem-identifier-type"
    EXPERIMENTAL = False

    """ An ISO object identifier; e.g. 1.2.3.4.5.
    """
    oid = "oid"

    """ A universally unique identifier of the form a5afddf4-e880-459b-876e-e4591b0acc11.
    """
    uuid = "uuid"

    """ A uniform resource identifier (ideally a URL - uniform resource locator); e.g. http://unitsofmeasure.org.
    """
    uri = "uri"

    """ Some other type of unique identifier; e.g. HL7-assigned reserved string such as LN for LOINC.
    """
    other = "other"


class NamingSystemType(CodeSystemValue):
    """ Identifies the purpose of the naming system.

    URL: http://hl7.org/fhir/namingsystem-type
    ValueSet: http://hl7.org/fhir/ValueSet/namingsystem-type
    """
    URL = "http://hl7.org/fhir/namingsystem-type"
    EXPERIMENTAL = False

    """ The naming system is used to define concepts and symbols to represent those concepts; e.g. UCUM, LOINC, NDC
	/// code, local lab codes, etc.
    """
    codesystem = "codesystem"

    """ The naming system is used to manage identifiers (e.g. license numbers, order numbers, etc.).
    """
    identifier = "identifier"

    """ The naming system is used as the root for other identifiers and naming systems.
    """
    root = "root"


class NarrativeStatus(CodeSystemValue):
    """ The status of a resource narrative

    URL: http://hl7.org/fhir/narrative-status
    ValueSet: http://hl7.org/fhir/ValueSet/narrative-status
    """
    URL = "http://hl7.org/fhir/narrative-status"
    EXPERIMENTAL = False

    """ The contents of the narrative are entirely generated from the structured data in the content.
    """
    generated = "generated"

    """ The contents of the narrative are entirely generated from the structured data in the content and some of the
	/// content is generated from extensions
    """
    extensions = "extensions"

    """ The contents of the narrative may contain additional information not found in the structured data. Note that
	/// there is no computable way to determine what the extra information is, other than by human inspection
    """
    additional = "additional"

    """ The contents of the narrative are some equivalent of "No human-readable text provided in this case"
    """
    empty = "empty"


class Need(CodeSystemValue):
    """ The frequency with which the target must be validated

    URL: http://hl7.org/fhir/need
    ValueSet: http://hl7.org/fhir/ValueSet/need
    """
    URL = "http://hl7.org/fhir/need"
    EXPERIMENTAL = False

    """ none
    """
    none = "none"

    """ initial
    """
    initial = "initial"

    """ periodic
    """
    periodic = "periodic"


class NetworkTypeCodes(CodeSystemValue):
    """ This value set includes a smattering of Network type codes.

    URL: http://hl7.org/fhir/benefit-network
    ValueSet: http://hl7.org/fhir/ValueSet/benefit-network
    """
    URL = "http://hl7.org/fhir/benefit-network"
    EXPERIMENTAL = True

    """ Services rendered by a Network provider
    """
    _in = "in"

    """ Services rendered by a provider who is not in the Network
    """
    out = "out"


class NoteType(CodeSystemValue):
    """ The presentation types of notes.

    URL: http://hl7.org/fhir/note-type
    ValueSet: http://hl7.org/fhir/ValueSet/note-type
    """
    URL = "http://hl7.org/fhir/note-type"
    EXPERIMENTAL = False

    """ Display the note.
    """
    display = "display"

    """ Print the note on the form.
    """
    print = "print"

    """ Print the note for the operator.
    """
    printoper = "printoper"


class ObservationCategoryCodes(CodeSystemValue):
    """ Observation Category codes.

    URL: http://hl7.org/fhir/observation-category
    ValueSet: http://hl7.org/fhir/ValueSet/observation-category
    """
    URL = "http://hl7.org/fhir/observation-category"
    EXPERIMENTAL = True

    """ Social History Observations define the patient's occupational, personal (e.g., lifestyle), social, and
	/// environmental history and health risk factors, as well as administrative data such as marital status, race,
	/// ethnicity and religious affiliation.
    """
    socialHistory = "social-history"

    """  Clinical observations measure the body's basic functions such as blood pressure, heart rate, respiratory rate,
	/// height, weight, body mass index, head circumference, pulse oximetry, temperature, and body surface area.
    """
    vitalSigns = "vital-signs"

    """ Observations generated by imaging. The scope includes observations, plain x-ray, ultrasound, CT, MRI,
	/// angiography, echocardiography, and nuclear medicine.
    """
    imaging = "imaging"

    """ The results of observations generated by laboratories.  Laboratory results are typically generated by
	/// laboratories providing analytic services in areas such as chemistry, hematology, serology, histology, cytology,
	/// anatomic pathology, microbiology, and/or virology. These observations are based on analysis of specimens
	/// obtained from the patient and submitted to the laboratory.
    """
    laboratory = "laboratory"

    """ Observations generated by other procedures.  This category includes observations resulting from interventional
	/// and non-interventional procedures excluding laboratory and imaging (e.g., cardiology catheterization, endoscopy,
	/// electrodiagnostics, etc.).  Procedure results are typically generated by a clinician to provide more granular
	/// information about component observations made during a procedure, such as where a gastroenterologist reports the
	/// size of a polyp observed during a colonoscopy.
    """
    procedure = "procedure"

    """ Assessment tool/survey instrument observations (e.g., Apgar Scores, Montreal Cognitive Assessment (MoCA)).
    """
    survey = "survey"

    """ Observations generated by physical exam findings including direct observations made by a clinician and use of
	/// simple instruments and the result of simple maneuvers performed directly on the patient's body.
    """
    exam = "exam"

    """ Observations generated by non-interventional treatment protocols (e.g. occupational, physical, radiation,
	/// nutritional and medication therapy)
    """
    therapy = "therapy"

    """ Observations that measure or record any bodily activity that enhances or maintains physical fitness and overall
	/// health and wellness.  Not under direct supervision of practitioner such as a physical therapist. (e.g., laps
	/// swum, steps, sleep data)
    """
    activity = "activity"


class ObservationReferenceRangeMeaningCodes(CodeSystemValue):
    """ This value set defines a set of codes that can be used to indicate the meaning/use of a reference range for a particular
target population.

    URL: http://hl7.org/fhir/referencerange-meaning
    ValueSet: http://hl7.org/fhir/ValueSet/referencerange-meaning
    """
    URL = "http://hl7.org/fhir/referencerange-meaning"
    EXPERIMENTAL = True

    """ General types of reference range.
    """
    type = "type"

    """ Based on 95th percentile for the relevant control population.
    """
    normal = "normal"

    """ The range that is recommended by a relevant professional body.
    """
    recommended = "recommended"

    """ The range at which treatment would/should be considered.
    """
    treatment = "treatment"

    """ The optimal range for best therapeutic outcomes.
    """
    therapeutic = "therapeutic"

    """ The optimal range for best therapeutic outcomes for a specimen taken immediately before administration.
    """
    pre = "pre"

    """ The optimal range for best therapeutic outcomes for a specimen taken immediately after administration.
    """
    post = "post"

    """ Endocrine related states that change the expected value.
    """
    endocrine = "endocrine"

    """ An expected range in an individual prior to puberty.
    """
    prePuberty = "pre-puberty"

    """ An expected range in an individual during the follicular stage of the cycle.
    """
    follicular = "follicular"

    """ An expected range in an individual during the follicular stage of the cycle.
    """
    midcycle = "midcycle"

    """ An expected range in an individual during the luteal stage of the cycle.
    """
    luteal = "luteal"

    """ An expected range in an individual post-menopause.
    """
    postmenopausal = "postmenopausal"


class ObservationStatus(CodeSystemValue):
    """ Codes providing the status of an observation.

    URL: http://hl7.org/fhir/observation-status
    ValueSet: http://hl7.org/fhir/ValueSet/observation-status
    """
    URL = "http://hl7.org/fhir/observation-status"
    EXPERIMENTAL = False

    """ The existence of the observation is registered, but there is no result yet available.
    """
    registered = "registered"

    """ This is an initial or interim observation: data may be incomplete or unverified.
    """
    preliminary = "preliminary"

    """ The observation is complete.
    """
    final = "final"

    """ Subsequent to being Final, the observation has been modified subsequent.  This includes updates/new information
	/// and corrections.
    """
    amended = "amended"

    """ Subsequent to being Final, the observation has been modified to correct an error in the test result.
    """
    corrected = "corrected"

    """ The observation is unavailable because the measurement was not started or not completed (also sometimes called
	/// "aborted").
    """
    cancelled = "cancelled"

    """ The observation has been withdrawn following previous final release.  This electronic record should never have
	/// existed, though it is possible that real-world decisions were based on it. (If real-world activity has occurred,
	/// the status should be "cancelled" rather than "entered-in-error".)
    """
    enteredInError = "entered-in-error"

    """ The authoring system does not know which of the status values currently applies for this request. Note: This
	/// concept is not to be used for "other" - one of the listed statuses is presumed to apply, but the authoring
	/// system does not know which.
    """
    unknown = "unknown"


class OperationKind(CodeSystemValue):
    """ Whether an operation is a normal operation or a query.

    URL: http://hl7.org/fhir/operation-kind
    ValueSet: http://hl7.org/fhir/ValueSet/operation-kind
    """
    URL = "http://hl7.org/fhir/operation-kind"
    EXPERIMENTAL = False

    """ This operation is invoked as an operation.
    """
    operation = "operation"

    """ This operation is a named query, invoked using the search mechanism.
    """
    query = "query"


class OperationParameterUse(CodeSystemValue):
    """ Whether an operation parameter is an input or an output parameter.

    URL: http://hl7.org/fhir/operation-parameter-use
    ValueSet: http://hl7.org/fhir/ValueSet/operation-parameter-use
    """
    URL = "http://hl7.org/fhir/operation-parameter-use"
    EXPERIMENTAL = False

    """ This is an input parameter.
    """
    _in = "in"

    """ This is an output parameter.
    """
    out = "out"


class OrganizationRole(CodeSystemValue):
    """ This example value set defines a set of codes that can be used to indicate the role of one Organization in relation to
another.

    URL: http://hl7.org/fhir/organization-role
    ValueSet: http://hl7.org/fhir/ValueSet/organization-role
    """
    URL = "http://hl7.org/fhir/organization-role"
    EXPERIMENTAL = True

    """ provider
    """
    provider = "provider"

    """ An organization such as a public health agency, community/social services provider, etc.
    """
    agency = "agency"

    """ An organization providing research-related services such as conducting research, recruiting research
	/// participants, analyzing data, etc.
    """
    research = "research"

    """ An organization providing reimbursement, payment, or related services
    """
    payer = "payer"

    """ An organization providing diagnostic testing/laboratory services
    """
    diagnostics = "diagnostics"

    """ An organization that provides medical supplies (e.g. medical devices, equipment, pharmaceutical products, etc.)
    """
    supplier = "supplier"

    """ An organization that facilitates electronic clinical data exchange between entities
    """
    HIEHIO = "HIE/HIO"

    """ A type of non-ownership relationship between entities (encompassess partnerships, collaboration, joint ventures,
	/// etc.)
    """
    member = "member"


class OrganizationType(CodeSystemValue):
    """ This example value set defines a set of codes that can be used to indicate a type of organization.

    URL: http://hl7.org/fhir/organization-type
    ValueSet: http://hl7.org/fhir/ValueSet/organization-type
    """
    URL = "http://hl7.org/fhir/organization-type"
    EXPERIMENTAL = True

    """ An organization that provides healthcare services.
    """
    prov = "prov"

    """ A department or ward within a hospital (Generally is not applicable to top level organizations)
    """
    dept = "dept"

    """ An organizational team is usually a grouping of practitioners that perform a specific function within an
	/// organization (which could be a top level organization, or a department).
    """
    team = "team"

    """ A political body, often used when including organization records for government bodies such as a Federal
	/// Government, State or Local Government.
    """
    govt = "govt"

    """ A company that provides insurance to its subscribers that may include healthcare related policies.
    """
    ins = "ins"

    """ A company, charity, or governmental organization which processes claims and/or issues payments to providers on
	/// behalf of patients or groups of patients.
    """
    pay = "pay"

    """ An educational institution that provides education or research facilities.
    """
    edu = "edu"

    """ An organization that is identified as a part of a religious institution.
    """
    reli = "reli"

    """ An organization that is identified as a Pharmaceutical/Clinical Research Sponsor.
    """
    crs = "crs"

    """ An un-incorporated community group.
    """
    cg = "cg"

    """ An organization that is a registered business or corporation but not identified by other types.
    """
    bus = "bus"

    """ Other type of organization not already specified.
    """
    other = "other"


class OrientationType(CodeSystemValue):
    """ Type for orientation

    URL: http://hl7.org/fhir/orientation-type
    ValueSet: http://hl7.org/fhir/ValueSet/orientation-type
    """
    URL = "http://hl7.org/fhir/orientation-type"
    EXPERIMENTAL = False

    """ Sense orientation of reference sequence.
    """
    sense = "sense"

    """ Antisense orientation of reference sequence
    """
    antisense = "antisense"


class ParticipantRequired(CodeSystemValue):
    """ Is the Participant required to attend the appointment.

    URL: http://hl7.org/fhir/participantrequired
    ValueSet: http://hl7.org/fhir/ValueSet/participantrequired
    """
    URL = "http://hl7.org/fhir/participantrequired"
    EXPERIMENTAL = False

    """ The participant is required to attend the appointment.
    """
    required = "required"

    """ The participant may optionally attend the appointment.
    """
    optional = "optional"

    """ The participant is excluded from the appointment, and might not be informed of the appointment taking place.
	/// (Appointment is about them, not for them - such as 2 doctors discussing results about a patient's test).
    """
    informationOnly = "information-only"


class ParticipantType(CodeSystemValue):
    """ This value set defines a set of codes that can be used to indicate how an individual participates in an encounter.

    URL: http://hl7.org/fhir/participant-type
    ValueSet: http://hl7.org/fhir/ValueSet/encounter-participant-type
    """
    URL = "http://hl7.org/fhir/participant-type"
    EXPERIMENTAL = True

    """ A translator who is facilitating communication with the patient during the encounter.
    """
    translator = "translator"

    """ A person to be contacted in case of an emergency during the encounter.
    """
    emergency = "emergency"


class ParticipationStatus(CodeSystemValue):
    """ The Participation status of an appointment.

    URL: http://hl7.org/fhir/participationstatus
    ValueSet: http://hl7.org/fhir/ValueSet/participationstatus
    """
    URL = "http://hl7.org/fhir/participationstatus"
    EXPERIMENTAL = False

    """ The participant has accepted the appointment.
    """
    accepted = "accepted"

    """ The participant has declined the appointment and will not participate in the appointment.
    """
    declined = "declined"

    """ The participant has  tentatively accepted the appointment. This could be automatically created by a system and
	/// requires further processing before it can be accepted. There is no commitment that attendance will occur.
    """
    tentative = "tentative"

    """ The participant needs to indicate if they accept the appointment by changing this status to one of the other
	/// statuses.
    """
    needsAction = "needs-action"


class PaymentAdjustmentReasonCodes(CodeSystemValue):
    """ This value set includes smattering of Payment Adjustment Reason codes.

    URL: http://hl7.org/fhir/payment-adjustment-reason
    ValueSet: http://hl7.org/fhir/ValueSet/payment-adjustment-reason
    """
    URL = "http://hl7.org/fhir/payment-adjustment-reason"
    EXPERIMENTAL = True

    """ Prior Payment Reversal
    """
    A001 = "a001"

    """ Prior Overpayment
    """
    A002 = "a002"


class PaymentStatusCodes(CodeSystemValue):
    """ This value set includes a sample set of Payment Status codes.

    URL: http://hl7.org/fhir/paymentstatus
    ValueSet: http://hl7.org/fhir/ValueSet/payment-status
    """
    URL = "http://hl7.org/fhir/paymentstatus"
    EXPERIMENTAL = True

    """ The payment has been sent physically or electronically.
    """
    paid = "paid"

    """ The payment has been received by the payee.
    """
    cleared = "cleared"


class PaymentTypeCodes(CodeSystemValue):
    """ This value set includes sample Payment Type codes.

    URL: http://hl7.org/fhir/payment-type
    ValueSet: http://hl7.org/fhir/ValueSet/payment-type
    """
    URL = "http://hl7.org/fhir/payment-type"
    EXPERIMENTAL = True

    """ The amount is partial or complete settlement of the amounts due.
    """
    payment = "payment"

    """ The amount is an adjustment regarding claims already paid.
    """
    adjustment = "adjustment"

    """ The amount is an advance against future claims.
    """
    advance = "advance"


class PlanDefinitionType(CodeSystemValue):
    """ The type of PlanDefinition

    URL: http://hl7.org/fhir/plan-definition-type
    ValueSet: http://hl7.org/fhir/ValueSet/plan-definition-type
    """
    URL = "http://hl7.org/fhir/plan-definition-type"
    EXPERIMENTAL = False

    """ A pre-defined and approved group of orders related to a particular clinical condition (e.g. hypertension
	/// treatment and monitoring) or stage of care (e.g. hospital admission to Coronary Care Unit). An order set is used
	/// as a checklist for the clinician when managing a patient with a specific condition. It is a structured
	/// collection of orders relevant to that condition and presented to the clinician in a computerized provider order
	/// entry (CPOE) system
    """
    orderSet = "order-set"

    """ Defines a desired/typical sequence of clinical activities including preconditions, triggers and temporal
	/// relationships
    """
    clinicalProtocol = "clinical-protocol"

    """ A decision support rule of the form [on Event] if Condition then Action. It is intended to be a shareable,
	/// computable definition of actions that should be taken whenever some condition is met in response to a particular
	/// event or events
    """
    ecaRule = "eca-rule"

    """ Defines the steps for a group of one or more systems in an event flow process along with the step
	/// constraints, sequence, pre-conditions and decision points to complete a particular objective
    """
    workflowDefinition = "workflow-definition"


class PolicyholderRelationshipCodes(CodeSystemValue):
    """ This value set includes codes for the relationship between the Policyholder and the Beneficiary (insured/covered
party/patient)..

    URL: http://hl7.org/fhir/policyholder-relationship
    ValueSet: http://hl7.org/fhir/ValueSet/policyholder-relationship
    """
    URL = "http://hl7.org/fhir/policyholder-relationship"
    EXPERIMENTAL = True

    """ The Beneficiary is a child of the Policyholder
    """
    child = "child"

    """ The Beneficiary is a parent of the Policyholder
    """
    parent = "parent"

    """ The Beneficiary is a spouse or equivalent of the Policyholder
    """
    spouse = "spouse"

    """ The Beneficiary is a common law spouse or equivalent of the Policyholder
    """
    common = "common"

    """ The Beneficiary has some other relationship the Policyholder
    """
    other = "other"

    """ The Beneficiary is the Policyholder
    """
    self = "self"


class PractitionerRole(CodeSystemValue):
    """ This example value set defines a set of codes that can be used to indicate the role of a Practitioner.

    URL: http://hl7.org/fhir/practitioner-role
    ValueSet: http://hl7.org/fhir/ValueSet/practitioner-role
    """
    URL = "http://hl7.org/fhir/practitioner-role"
    EXPERIMENTAL = True

    """ A qualified/registered medical practitioner
    """
    doctor = "doctor"

    """ A practitoner with nursing experience that may be qualified/registered
    """
    nurse = "nurse"

    """ A qualified/registered/licensed pharmacist
    """
    pharmacist = "pharmacist"

    """ A practitioner that may perform research
    """
    researcher = "researcher"

    """ Someone who is able to provide educational services
    """
    teacher = "teacher"

    """ Someone who is qualified in Information and Communication Technologies
    """
    ict = "ict"


class PractitionerSpecialty(CodeSystemValue):
    """ This example value set defines a set of codes that can be used to indicate the specialty of a Practitioner.

    URL: http://hl7.org/fhir/practitioner-specialty
    ValueSet: http://hl7.org/fhir/ValueSet/practitioner-specialty
    """
    URL = "http://hl7.org/fhir/practitioner-specialty"
    EXPERIMENTAL = True

    """ cardio
    """
    cardio = "cardio"

    """ dent
    """
    dent = "dent"

    """ dietary
    """
    dietary = "dietary"

    """ midw
    """
    midw = "midw"

    """ sysarch
    """
    sysarch = "sysarch"


class PrimarySourceType(CodeSystemValue):
    """ Type of the validation primary source

    URL: http://hl7.org/fhir/primary-source-type
    ValueSet: http://hl7.org/fhir/ValueSet/primary-source-type
    """
    URL = "http://hl7.org/fhir/primary-source-type"
    EXPERIMENTAL = False

    """ licBoard
    """
    licBoard = "lic-board"

    """ prim
    """
    prim = "prim"

    """ contEd
    """
    contEd = "cont-ed"

    """ postServ
    """
    postServ = "post-serv"

    """ relOwn
    """
    relOwn = "rel-own"

    """ regAuth
    """
    regAuth = "reg-auth"

    """ legal
    """
    legal = "legal"

    """ issuer
    """
    issuer = "issuer"

    """ authSource
    """
    authSource = "auth-source"


class ProcedureDeviceActionCodes(CodeSystemValue):
    """ Example codes indicating the change that happened to the device during the procedure.  Note that these are in no way
complete and might not even be appropriate for some uses.

    URL: http://hl7.org/fhir/device-action
    ValueSet: http://hl7.org/fhir/ValueSet/device-action
    """
    URL = "http://hl7.org/fhir/device-action"
    EXPERIMENTAL = True

    """ The device was implanted in the patient during the procedure.
    """
    implanted = "implanted"

    """ The device was explanted from the patient during the procedure.
    """
    explanted = "explanted"

    """ The device remains in that patient, but its location, settings, or functionality was changed.
    """
    manipulated = "manipulated"


class ProcedureProgressStatusCodes(CodeSystemValue):
    """ This value set is provided as an example. The value set to instantiate this attribute should be drawn from a robust
terminology code system that consists of or contains concepts to support the procedure performance process.

    URL: http://hl7.org/fhir/procedure-progress-status-code
    ValueSet: http://hl7.org/fhir/ValueSet/procedure-progress-status-codes
    """
    URL = "http://hl7.org/fhir/procedure-progress-status-code"
    EXPERIMENTAL = True

    """ A patient is in the Operating Room.
    """
    inOperatingRoom = "in-operating-room"

    """ The patient is prepared for a procedure.
    """
    prepared = "prepared"

    """ The patient is under anesthesia.
    """
    anesthesiaInduced = "anesthesia-induced"

    """ The patient has open incision(s).
    """
    openIncision = "open-incision"

    """ The patient has incision(s) closed.
    """
    closedIncision = "closed-incision"

    """ The patient is in the recovery room.
    """
    inRecoveryRoom = "in-recovery-room"


class ProcessOutcomeCodes(CodeSystemValue):
    """ This value set includes sample Process Outcome codes.

    URL: http://hl7.org/fhir/processoutcomecodes
    ValueSet: http://hl7.org/fhir/ValueSet/process-outcome
    """
    URL = "http://hl7.org/fhir/processoutcomecodes"
    EXPERIMENTAL = True

    """ The requested processing has completed.
    """
    complete = "complete"

    """ The requested processing has been suspended.
    """
    pended = "pended"

    """ The requested processing has terminated with some errors being found.
    """
    error = "error"


class ProcessPriorityCodes(CodeSystemValue):
    """ This value set includes the financial processing priority codes.

    URL: http://hl7.org/fhir/processpriority
    ValueSet: http://hl7.org/fhir/ValueSet/process-priority
    """
    URL = "http://hl7.org/fhir/processpriority"
    EXPERIMENTAL = True

    """ Immediately in real time.
    """
    stat = "stat"

    """ With best effort.
    """
    normal = "normal"

    """ Later, when possible.
    """
    deferred = "deferred"


class PropertyRepresentation(CodeSystemValue):
    """ How a property is represented when serialized.

    URL: http://hl7.org/fhir/property-representation
    ValueSet: http://hl7.org/fhir/ValueSet/property-representation
    """
    URL = "http://hl7.org/fhir/property-representation"
    EXPERIMENTAL = False

    """ In XML, this property is represented as an attribute not an element.
    """
    xmlAttr = "xmlAttr"

    """ This element is represented using the XML text attribute (primitives only)
    """
    xmlText = "xmlText"

    """ The type of this element is indicated using xsi:type
    """
    typeAttr = "typeAttr"

    """ Use CDA narrative instead of XHTML
    """
    cdaText = "cdaText"

    """ The property is represented using XHTML
    """
    xhtml = "xhtml"


class PropertyType(CodeSystemValue):
    """ The type of a property value

    URL: http://hl7.org/fhir/concept-property-type
    ValueSet: http://hl7.org/fhir/ValueSet/concept-property-type
    """
    URL = "http://hl7.org/fhir/concept-property-type"
    EXPERIMENTAL = False

    """ The property value is a code that identifies a concept defined in the code system
    """
    code = "code"

    """ The property  value is a code defined in an external code system. This may be used for translations, but is not
	/// the intent
    """
    coding = "Coding"

    """ The property value is a string
    """
    string = "string"

    """ The property value is a string (often used to assign ranking values to concepts for supporting score
	/// assessments)
    """
    integer = "integer"

    """ The property value is a boolean true | false
    """
    boolean = "boolean"

    """ The property is a date or a date + time
    """
    dateTime = "dateTime"

    """ The property value is a decimal number
    """
    decimal = "decimal"


class ProvenanceEntityRole(CodeSystemValue):
    """ How an entity was used in an activity.

    URL: http://hl7.org/fhir/provenance-entity-role
    ValueSet: http://hl7.org/fhir/ValueSet/provenance-entity-role
    """
    URL = "http://hl7.org/fhir/provenance-entity-role"
    EXPERIMENTAL = False

    """ A transformation of an entity into another, an update of an entity resulting in a new one, or the construction
	/// of a new entity based on a preexisting entity.
    """
    derivation = "derivation"

    """ A derivation for which the resulting entity is a revised version of some original.
    """
    revision = "revision"

    """ The repeat of (some or all of) an entity, such as text or image, by someone who might or might not be its
	/// original author.
    """
    quotation = "quotation"

    """ A primary source for a topic refers to something produced by some agent with direct experience and knowledge
	/// about the topic, at the time of the topic's study, without benefit from hindsight.
    """
    source = "source"

    """ A derivation for which the entity is removed from accessibility usually through the use of the Delete operation.
    """
    removal = "removal"


class ProvenanceParticipantType(CodeSystemValue):
    """ The type of participation a provenance participant.

    URL: http://hl7.org/fhir/provenance-participant-type
    ValueSet: http://hl7.org/fhir/ValueSet/provenance-agent-type
    """
    URL = "http://hl7.org/fhir/provenance-participant-type"
    EXPERIMENTAL = True

    """ A person entering the data into the originating system
    """
    enterer = "enterer"

    """ A person, animal, organization or device that who actually and principally carries out the activity
    """
    performer = "performer"

    """ A party that originates the resource and therefore has responsibility for the information given in the resource
	/// and ownership of this resource
    """
    author = "author"

    """ A person who verifies the correctness and appropriateness of activity
    """
    verifier = "verifier"

    """ The person authenticated the content and accepted legal responsibility for its content
    """
    legal = "legal"

    """ A verifier who attests to the accuracy of the resource
    """
    attester = "attester"

    """ A person who reported information that contributed to the resource
    """
    informant = "informant"

    """ The entity that is accountable for maintaining a true an accurate copy of the original record
    """
    custodian = "custodian"

    """ A device that operates independently of an author on custodian's algorithms for data extraction of existing
	/// information for purpose of generating a new artifact.
    """
    assembler = "assembler"

    """ A device used by an author to record new information, which may also be used by the author to select existing
	/// information for aggregation with newly recorded information for the purpose of generating a new artifact.
    """
    composer = "composer"


class PublicationStatus(CodeSystemValue):
    """ The lifecycle status of an artifact.

    URL: http://hl7.org/fhir/publication-status
    ValueSet: http://hl7.org/fhir/ValueSet/publication-status
    """
    URL = "http://hl7.org/fhir/publication-status"
    EXPERIMENTAL = False

    """ This resource is still under development and is not yet considered to be ready for normal use.
    """
    draft = "draft"

    """ This resource is ready for normal use.
    """
    active = "active"

    """ This resource has been withdrawn or superseded and should no longer be used.
    """
    retired = "retired"

    """ The authoring system does not know which of the status values currently applies for this resource.  Note: This
	/// concept is not to be used for "other" - one of the listed statuses is presumed to apply, it's just not known
	/// which one.
    """
    unknown = "unknown"


class PushTypeAvailable(CodeSystemValue):
    """ Type of alerts/updates the primary source can send

    URL: http://hl7.org/fhir/push-type-available
    ValueSet: http://hl7.org/fhir/ValueSet/push-type-available
    """
    URL = "http://hl7.org/fhir/push-type-available"
    EXPERIMENTAL = False

    """ specific
    """
    specific = "specific"

    """ any
    """
    any = "any"

    """ source
    """
    source = "source"


class QualityOfEvidenceRating(CodeSystemValue):
    """ A rating system that describes the quality of evidence such as the GRADE, DynaMed, or Oxford CEBM systems

    URL: http://hl7.org/fhir/evidence-quality
    ValueSet: http://hl7.org/fhir/ValueSet/evidence-quality
    """
    URL = "http://hl7.org/fhir/evidence-quality"
    EXPERIMENTAL = False

    """ High quality evidence
    """
    high = "high"

    """ Moderate quality evidence
    """
    moderate = "moderate"

    """ Low quality evidence
    """
    low = "low"

    """ Very low quality evidence
    """
    veryLow = "very-low"


class QualityType(CodeSystemValue):
    """ Type for quality report

    URL: http://hl7.org/fhir/quality-type
    ValueSet: http://hl7.org/fhir/ValueSet/quality-type
    """
    URL = "http://hl7.org/fhir/quality-type"
    EXPERIMENTAL = False

    """ INDEL Comparison
    """
    indel = "indel"

    """ SNP Comparison
    """
    snp = "snp"

    """ UNKNOWN Comparison
    """
    unknown = "unknown"


class QuantityComparator(CodeSystemValue):
    """ How the Quantity should be understood and represented.

    URL: http://hl7.org/fhir/quantity-comparator
    ValueSet: http://hl7.org/fhir/ValueSet/quantity-comparator
    """
    URL = "http://hl7.org/fhir/quantity-comparator"
    EXPERIMENTAL = False

    """ The actual value is less than the given value.
    """
    lt = "<"

    """ The actual value is less than or equal to the given value.
    """
    lte = "<="

    """ The actual value is greater than or equal to the given value.
    """
    gte = ">="

    """ The actual value is greater than the given value.
    """
    gt = ">"


class QuestionnaireItemOperator(CodeSystemValue):
    """ The criteria by which a question is enabled

    URL: http://hl7.org/fhir/questionnaire-enable-operator
    ValueSet: http://hl7.org/fhir/ValueSet/questionnaire-enable-operator
    """
    URL = "http://hl7.org/fhir/questionnaire-enable-operator"
    EXPERIMENTAL = False

    """ True if whether an answer exists is equal to the enableWhen answer (which must be a boolean)
    """
    exists = "exists"

    """ True if whether at least one answer has a value that is equal to the enableWhen answer
    """
    eq = "="

    """ True if whether at least no answer has a value that is equal to the enableWhen answer
    """
    ne = "!="

    """ True if whether at least no answer has a value that is greater than the enableWhen answer
    """
    gt = ">"

    """ True if whether at least no answer has a value that is less than the enableWhen answer
    """
    lt = "<"

    """ True if whether at least no answer has a value that is greater or equal to the enableWhen answer
    """
    gte = ">="

    """ True if whether at least no answer has a value that is less or equal to the enableWhen answer
    """
    lte = "<="


class QuestionnaireItemType(CodeSystemValue):
    """ Distinguishes groups from questions and display text and indicates data type for questions

    URL: http://hl7.org/fhir/item-type
    ValueSet: http://hl7.org/fhir/ValueSet/item-type
    """
    URL = "http://hl7.org/fhir/item-type"
    EXPERIMENTAL = False

    """ An item with no direct answer but should have at least one child item.
    """
    group = "group"

    """ Text for display that will not capture an answer or have child items.
    """
    display = "display"

    """ An item that defines a specific answer to be captured, and which may have child items. (the answer provided in
	/// the QuestionnaireResponse should be of the defined datatype)
    """
    question = "question"

    """ Question with a yes/no answer (valueBoolean)
    """
    boolean = "boolean"

    """ Question with is a real number answer (valueDecimal)
    """
    decimal = "decimal"

    """ Question with an integer answer (valueInteger)
    """
    integer = "integer"

    """ Question with a date answer (valueDate)
    """
    date = "date"

    """ Question with a date and time answer (valueDateTime)
    """
    dateTime = "dateTime"

    """ Question with a time (hour:minute:second) answer independent of date. (valueTime)
    """
    time = "time"

    """ Question with a short (few words to short sentence) free-text entry answer (valueString)
    """
    string = "string"

    """ Question with a long (potentially multi-paragraph) free-text entry answer (valueString)
    """
    text = "text"

    """ Question with a URL (website, FTP site, etc.) answer (valueUri)
    """
    url = "url"

    """ Question with a Coding drawn from a list of options (specified in either the option property, or via the
	/// valueset referenced in the options property) as an answer (valueCoding)
    """
    choice = "choice"

    """ Answer is a Coding drawn from a list of options (as with the choice type) or a free-text entry in a string
	/// (valueCoding or valueString)
    """
    openChoice = "open-choice"

    """ Question with binary content such as a image, PDF, etc. as an answer (valueAttachment)
    """
    attachment = "attachment"

    """ Question with a reference to another resource (practitioner, organization, etc.) as an answer (valueReference)
    """
    reference = "reference"

    """ Question with a combination of a numeric value and unit, potentially with a comparator (<, >, etc.) as an
	/// answer. (valueQuantity) There is an extension 'http://hl7.org/fhir/StructureDefinition/questionnaire-unit' that
	/// can be used to define what unit should be captured (or the a unit that has a ucum conversion from the provided
	/// unit)
    """
    quantity = "quantity"


class QuestionnaireItemUIControlCodes(CodeSystemValue):
    """ Starter set of user interface control/display mechanisms that might be used when rendering an item in a questionnaire.

    URL: http://hl7.org/fhir/questionnaire-item-control
    ValueSet: http://hl7.org/fhir/ValueSet/questionnaire-item-control
    """
    URL = "http://hl7.org/fhir/questionnaire-item-control"
    EXPERIMENTAL = True

    """ UI controls relevant to organizing groups of questions
    """
    group = "group"

    """ Questions within the group should be listed sequentially
    """
    list = "list"

    """ Questions within the group are rows in the table with possible answers as columns
    """
    table = "table"

    """ The group is to be continuously visible at the top of the questionnaire
    """
    header = "header"

    """ The group is to be continuously visible at the bottom of the questionnaire
    """
    footer = "footer"

    """ UI controls relevant to rendering questionnaire text items
    """
    text = "text"

    """ Text is displayed as a paragraph in a sequential position between sibling items (default behavior)
    """
    inline = "inline"

    """ Text is displayed immediately below or within the answer-entry area of the containing question item (typically
	/// as a guide for what to enter)
    """
    prompt = "prompt"

    """ Text is displayed adjacent (horizontally or vertically) to the answer space for the parent question, typically
	/// to indicate a unit of measure
    """
    unit = "unit"

    """ Text is displayed to the left of the set of answer choices or a scaling control for the parent question item to
	/// indicate the meaning of the 'lower' bound.  E.g. 'Strongly disagree'
    """
    lower = "lower"

    """ Text is displayed to the right of the set of answer choices or a scaling control for the parent question item to
	/// indicate the meaning of the 'upper' bound.  E.g. 'Strongly agree'
    """
    upper = "upper"

    """ Text is temporarily visible over top of an item if the mouse is positioned over top of the text for the
	/// containing item
    """
    flyover = "flyover"

    """ Text is displayed in a dialog box or similar control if invoked by pushing a button or some other UI-appropriate
	/// action to request 'help' for a question, group or the questionnaire as a whole (depending what the text is
	/// nested within)
    """
    help = "help"

    """ UI controls relevant to capturing question data
    """
    question = "question"

    """ A control which provides a list of potential matches based on text entered into a control.  Used for large
	/// choice sets where text-matching is an appropriate discovery mechanism.
    """
    autocomplete = "autocomplete"

    """ A control where an item (or multiple items) can be selected from a list that is only displayed when the user is
	/// editing the field.
    """
    dropDown = "drop-down"

    """ A control where choices are listed with a box beside them.  The box can be toggled to select or de-select a
	/// given choice.  Multiple selections may be possible.
    """
    checkBox = "check-box"

    """ A control where editing an item spawns a separate dialog box or screen permitting a user to navigate, filter or
	/// otherwise discover an appropriate match.  Useful for large choice sets where text matching is not an appropriate
	/// discovery mechanism.  Such screens must generally be tuned for the specific choice list structure.
    """
    lookup = "lookup"

    """ A control where choices are listed with a button beside them.  The button can be toggled to select or de-select
	/// a given choice.  Selecting one item deselects all others.
    """
    radioButton = "radio-button"

    """ A control where an axis is displayed between the high and low values and the control can be visually manipulated
	/// to select a value anywhere on the axis.
    """
    slider = "slider"

    """ A control where a list of numeric or other ordered values can be scrolled through via arrows.
    """
    spinner = "spinner"

    """ A control where a user can type in their answer freely.
    """
    textBox = "text-box"


class QuestionnaireItemUsageMode(CodeSystemValue):
    """ Identifies the modes of usage of a questionnaire that should enable a particular questionnaire item

    URL: http://hl7.org/fhir/questionnaire-usage-mode
    ValueSet: http://hl7.org/fhir/ValueSet/questionnaire-usage-mode
    """
    URL = "http://hl7.org/fhir/questionnaire-usage-mode"
    EXPERIMENTAL = False

    """ Render the item regardless of usage mode
    """
    captureDisplay = "capture-display"

    """ Render the item only when capturing data
    """
    capture = "capture"

    """ Render the item only when displaying a completed form
    """
    display = "display"

    """ Render the item only when displaying a completed form and the item has been answered (or has child items that
	/// have been answered)
    """
    displayNonEmpty = "display-non-empty"

    """ Render the item when capturing data or when displaying a completed form and the item has been answered (or has
	/// child items that have been answered)
    """
    captureDisplayNonEmpty = "capture-display-non-empty"


class QuestionnaireResponseStatus(CodeSystemValue):
    """ Lifecycle status of the questionnaire response.

    URL: http://hl7.org/fhir/questionnaire-answers-status
    ValueSet: http://hl7.org/fhir/ValueSet/questionnaire-answers-status
    """
    URL = "http://hl7.org/fhir/questionnaire-answers-status"
    EXPERIMENTAL = False

    """ This QuestionnaireResponse has been partially filled out with answers but changes or additions are still
	/// expected to be made to it.
    """
    inProgress = "in-progress"

    """ This QuestionnaireResponse has been filled out with answers and the current content is regarded as definitive.
    """
    completed = "completed"

    """ This QuestionnaireResponse has been filled out with answers, then marked as complete, yet changes or additions
	/// have been made to it afterwards.
    """
    amended = "amended"

    """ This QuestionnaireResponse was entered in error and voided.
    """
    enteredInError = "entered-in-error"

    """ This QuestionnaireResponse has been partially filled out with answers but has been abandoned. It is unknown
	/// whether changes or additions are expected to be made to it.
    """
    stopped = "stopped"


class QuestionnaireTextCategories(CodeSystemValue):
    """ Codes defining the purpose of a Questionnaire item of type 'text'.

    URL: http://hl7.org/fhir/questionnaire-display-category
    ValueSet: http://hl7.org/fhir/ValueSet/questionnaire-display-category
    """
    URL = "http://hl7.org/fhir/questionnaire-display-category"
    EXPERIMENTAL = True

    """ The text provides guidance on how to populate or use a portion of the questionnaire (or the questionnaire as a
	/// whole).
    """
    instructions = "instructions"

    """ The text provides guidance on how the information should be or will be handled from a
	/// security/confidentiality/access control perspective when completed
    """
    security = "security"


class ReasonMedicationGivenCodes(CodeSystemValue):
    """ This value set is provided as an example. The value set to instantiate this attribute should be drawn from a robust
terminology code system that consists of or contains concepts to support the medication process.

    URL: http://hl7.org/fhir/reason-medication-given
    ValueSet: http://hl7.org/fhir/ValueSet/reason-medication-given-codes
    """
    URL = "http://hl7.org/fhir/reason-medication-given"
    EXPERIMENTAL = True

    """ No reason known.
    """
    A = "a"

    """ The administration was following an ordered protocol.
    """
    B = "b"

    """ The administration was needed to treat an emergency.
    """
    C = "c"


class ReferenceHandlingPolicy(CodeSystemValue):
    """ A set of flags that defines how references are supported.

    URL: http://hl7.org/fhir/reference-handling-policy
    ValueSet: http://hl7.org/fhir/ValueSet/reference-handling-policy
    """
    URL = "http://hl7.org/fhir/reference-handling-policy"
    EXPERIMENTAL = False

    """ The server supports and populates Literal references where they are known (this code does not guarantee that all
	/// references are literal; see 'enforced')
    """
    literal = "literal"

    """ The server allows logical references
    """
    logical = "logical"

    """ The server will attempt to resolve logical references to literal references (if resolution fails, the server may
	/// still accept resources; see logical)
    """
    resolves = "resolves"

    """ The server enforces that references have integrity - e.g. it ensures that references can always be resolved.
	/// This is typically the case for clinical record systems, but often not the case for middleware/proxy systems
    """
    enforced = "enforced"

    """ The server does not support references that point to other servers
    """
    local = "local"


class ReferenceVersionRules(CodeSystemValue):
    """ Whether a reference needs to be version specific or version independent, or whether either can be used

    URL: http://hl7.org/fhir/reference-version-rules
    ValueSet: http://hl7.org/fhir/ValueSet/reference-version-rules
    """
    URL = "http://hl7.org/fhir/reference-version-rules"
    EXPERIMENTAL = False

    """ The reference may be either version independent or version specific
    """
    either = "either"

    """ The reference must be version independent
    """
    independent = "independent"

    """ The reference must be version specific
    """
    specific = "specific"


class ReferralMethod(CodeSystemValue):
    """ The methods of referral can be used when referring to a specific HealthCareService resource.

    URL: http://hl7.org/fhir/service-referral-method
    ValueSet: http://hl7.org/fhir/ValueSet/service-referral-method
    """
    URL = "http://hl7.org/fhir/service-referral-method"
    EXPERIMENTAL = False

    """ Referrals may be accepted by fax.
    """
    fax = "fax"

    """ Referrals may be accepted over the phone from a practitioner.
    """
    phone = "phone"

    """ Referrals may be accepted via a secure messaging system. To determine the types of secure messaging systems
	/// supported, refer to the identifiers collection. Callers will need to understand the specific identifier system
	/// used to know that they are able to transmit messages.
    """
    elec = "elec"

    """ Referrals may be accepted via a secure email. To send please encrypt with the services public key.
    """
    semail = "semail"

    """ Referrals may be accepted via regular postage (or hand delivered).
    """
    mail = "mail"


class RejectionCriterion(CodeSystemValue):
    """ Criterion for rejection of the specimen by laboratory

    URL: http://hl7.org/fhir/rejection-criteria
    ValueSet: http://hl7.org/fhir/ValueSet/rejection-criteria
    """
    URL = "http://hl7.org/fhir/rejection-criteria"
    EXPERIMENTAL = False

    """ blood specimen hemolized
    """
    hemolized = "hemolized"

    """ insufficient quantity of specimen
    """
    insufficient = "insufficient"

    """ specimen container broken
    """
    broken = "broken"

    """ specimen clotted
    """
    clotted = "clotted"

    """ specimen temperature inappropriate
    """
    wrongTemperature = "wrong-temperature"


class RelatedArtifactType(CodeSystemValue):
    """ The type of relationship to the related artifact

    URL: http://hl7.org/fhir/related-artifact-type
    ValueSet: http://hl7.org/fhir/ValueSet/related-artifact-type
    """
    URL = "http://hl7.org/fhir/related-artifact-type"
    EXPERIMENTAL = False

    """ Additional documentation for the knowledge resource. This would include additional instructions on usage as well
	/// as additional information on clinical context or appropriateness
    """
    documentation = "documentation"

    """ A summary of the justification for the knowledge resource including supporting evidence, relevant guidelines, or
	/// other clinically important information. This information is intended to provide a way to make the justification
	/// for the knowledge resource available to the consumer of interventions or results produced by the knowledge
	/// resource
    """
    justification = "justification"

    """ Bibliographic citation for papers, references, or other relevant material for the knowledge resource. This is
	/// intended to allow for citation of related material, but that was not necessarily specifically prepared in
	/// connection with this knowledge resource
    """
    citation = "citation"

    """ The previous version of the knowledge resource
    """
    predecessor = "predecessor"

    """ The next version of the knowledge resource
    """
    successor = "successor"

    """ The knowledge resource is derived from the related artifact. This is intended to capture the relationship in
	/// which a particular knowledge resource is based on the content of another artifact, but is modified to capture
	/// either a different set of overall requirements, or a more specific set of requirements such as those involved in
	/// a particular institution or clinical setting
    """
    derivedFrom = "derived-from"

    """ The knowledge resource depends on the given related artifact
    """
    dependsOn = "depends-on"

    """ The knowledge resource is composed of the given related artifact
    """
    composedOf = "composed-of"


class RepositoryType(CodeSystemValue):
    """ Type for access of external URI

    URL: http://hl7.org/fhir/repository-type
    ValueSet: http://hl7.org/fhir/ValueSet/repository-type
    """
    URL = "http://hl7.org/fhir/repository-type"
    EXPERIMENTAL = False

    """ When URL is clicked, the resource can be seen directly (by webpage or by download link format)
    """
    directlink = "directlink"

    """ When the API method (e.g. [base_url]/[parameter]) related with the URL of the website is executed, the resource
	/// can be seen directly (usually in JSON or XML format)
    """
    openapi = "openapi"

    """ When logged into the website, the resource can be seen.
    """
    login = "login"

    """ When logged in and  follow the API in the website related with URL, the resource can be seen.
    """
    oauth = "oauth"

    """ Some other complicated or particular way to get resource from URL.
    """
    other = "other"


class RequestIntent(CodeSystemValue):
    """ Codes indicating the degree of authority/intentionality associated with a request

    URL: http://hl7.org/fhir/request-intent
    ValueSet: http://hl7.org/fhir/ValueSet/request-intent
    """
    URL = "http://hl7.org/fhir/request-intent"
    EXPERIMENTAL = False

    """ The request is a suggestion made by someone/something that does not have an intention to ensure it occurs and
	/// without providing an authorization to act
    """
    proposal = "proposal"

    """ The request represents an intention to ensure something occurs without providing an authorization for others to
	/// act
    """
    plan = "plan"

    """ The request represents a request/demand and authorization for action
    """
    order = "order"

    """ The request represents an original authorization for action
    """
    originalOrder = "original-order"

    """ The request represents an automatically generated supplemental authorization for action based on a parent
	/// authorization together with initial results of the action taken against that parent authorization
    """
    reflexOrder = "reflex-order"

    """ The request represents the view of an authorization instantiated by a fulfilling system representing the details
	/// of the fulfiller's intention to act upon a submitted order
    """
    fillerOrder = "filler-order"

    """ An order created in fulfillment of a broader order that represents the authorization for a single activity
	/// occurrence.  E.g. The administration of a single dose of a drug.
    """
    instanceOrder = "instance-order"

    """ The request represents a component or option for a RequestGroup that establishes timing, conditionality and/or
	/// other constraints among a set of requests.  Refer to [[[RequestGroup]]] for additional information on how this
	/// status is used
    """
    option = "option"


class RequestPriority(CodeSystemValue):
    """ Identifies the level of importance to be assigned to actioning the request

    URL: http://hl7.org/fhir/request-priority
    ValueSet: http://hl7.org/fhir/ValueSet/request-priority
    """
    URL = "http://hl7.org/fhir/request-priority"
    EXPERIMENTAL = False

    """ The request has normal priority
    """
    routine = "routine"

    """ The request should be actioned promptly - higher priority than routine
    """
    urgent = "urgent"

    """ The request should be actioned as soon as possible - higher priority than urgent
    """
    asap = "asap"

    """ The request should be actioned immediately - highest possible priority.  E.g. an emergency
    """
    stat = "stat"


class RequestStatus(CodeSystemValue):
    """ Codes identifying the lifecycle stage of a request

    URL: http://hl7.org/fhir/request-status
    ValueSet: http://hl7.org/fhir/ValueSet/request-status
    """
    URL = "http://hl7.org/fhir/request-status"
    EXPERIMENTAL = False

    """ The request has been created but is not yet complete or ready for action
    """
    draft = "draft"

    """ The request is in force and ready to be acted upon
    """
    active = "active"

    """ The authorization/request to act has been temporarily withdrawn but is expected to resume in the future
    """
    suspended = "suspended"

    """ The authorization/request to act has been terminated prior to the full completion of the intended actions.  No
	/// further activity should occur.
    """
    cancelled = "cancelled"

    """ Activity against the request has been sufficiently completed to the satisfaction of the requester
    """
    completed = "completed"

    """ This electronic record should never have existed, though it is possible that real-world decisions were based on
	/// it.  (If real-world activity has occurred, the status should be "cancelled" rather than "entered-in-error".)
    """
    enteredInError = "entered-in-error"

    """ The authoring system does not know which of the status values currently applies for this request.  Note: This
	/// concept is not to be used for "other" . One of the listed statuses is presumed to apply,  but the system
	/// creating the request does not know.
    """
    unknown = "unknown"


class ResearchStudyObjectiveType(CodeSystemValue):
    """ Codes for the kind of study objective

    URL: http://hl7.org/fhir/research-study-objective-type
    ValueSet: http://hl7.org/fhir/ValueSet/research-study-objective-type
    """
    URL = "http://hl7.org/fhir/research-study-objective-type"
    EXPERIMENTAL = False

    """ The main question to be answered, and the one that drives any statistical planning for the study—e.g.,
	/// calculation of the sample size to provide the appropriate power for statistical testing.
    """
    primary = "primary"

    """ Question to be answered in the study that is of lesser importance than the primary objective.
    """
    secondary = "secondary"

    """ Exploratory questions to be answered in the study.
    """
    exploratory = "exploratory"


class ResearchStudyPhase(CodeSystemValue):
    """ Codes for the stage in the progression of a therapy from initial experimental use in humans in clinical trials to post-
market evaluation.

    URL: http://hl7.org/fhir/research-study-phase
    ValueSet: http://hl7.org/fhir/ValueSet/research-study-phase
    """
    URL = "http://hl7.org/fhir/research-study-phase"
    EXPERIMENTAL = False

    """ Trials without phases (for example, studies of devices or behavioral interventions).
    """
    NA = "n-a"

    """ Designation for optional exploratory trials conducted in accordance with the United States Food and Drug
	/// Administration's (FDA) 2006 Guidance on Exploratory Investigational New Drug (IND) Studies. Formerly called
	/// Phase 0.
    """
    earlyPhase1 = "early-phase-1"

    """ Includes initial studies to determine the metabolism and pharmacologic actions of drugs in humans, the side
	/// effects associated with increasing doses, and to gain early evidence of effectiveness; may include healthy
	/// participants and/or patients.
    """
    phase1 = "phase-1"

    """ Trials that are a combination of phases 1 and 2.
    """
    phase1Phase2 = "phase-1-phase-2"

    """ Includes controlled clinical studies conducted to evaluate the effectiveness of the drug for a particular
	/// indication or indications in participants with the disease or condition under study and to determine the common
	/// short-term side effects and risks.
    """
    phase2 = "phase-2"

    """ Trials that are a combination of phases 2 and 3.
    """
    phase2Phase3 = "phase-2-phase-3"

    """ Includes trials conducted after preliminary evidence suggesting effectiveness of the drug has been obtained, and
	/// are intended to gather additional information to evaluate the overall benefit-risk relationship of the drug.
    """
    phase3 = "phase-3"

    """ Studies of FDA-approved drugs to delineate additional information including the drug's risks, benefits, and
	/// optimal use.
    """
    phase4 = "phase-4"


class ResearchStudyPrimaryPurposeType(CodeSystemValue):
    """ Codes for the main intent of the study

    URL: http://hl7.org/fhir/research-study-prim-purp-type
    ValueSet: http://hl7.org/fhir/ValueSet/research-study-prim-purp-type
    """
    URL = "http://hl7.org/fhir/research-study-prim-purp-type"
    EXPERIMENTAL = False

    """ One or more interventions are being evaluated for treating a disease, syndrome, or condition.
    """
    treatment = "treatment"

    """ One or more interventions are being assessed for preventing the development of a specific disease or health
	/// condition.
    """
    prevention = "prevention"

    """ One or more interventions are being evaluated for identifying a disease or health condition.
    """
    diagnostic = "diagnostic"

    """ One or more interventions are evaluated for maximizing comfort, minimizing side effects, or mitigating against a
	/// decline in the participant's health or function.
    """
    supportiveCare = "supportive-care"

    """ One or more interventions are assessed or examined for identifying a condition, or risk factors for a condition,
	/// in people who are not yet known to have the condition or risk factor.
    """
    screening = "screening"

    """ One or more interventions for evaluating the delivery, processes, management, organization, or financing of
	/// healthcare.
    """
    healthServicesResearch = "health-services-research"

    """ One or more interventions for examining the basic mechanism of action (for example, physiology or biomechanics
	/// of an intervention).
    """
    basicScience = "basic-science"

    """ An intervention of a device product is being evaluated to determine the feasibility of the product or to test a
	/// prototype device and not health outcomes. Such studies are conducted to confirm the design and operating
	/// specifications of a device before beginning a full clinical trial.
    """
    deviceFeasibility = "device-feasibility"


class ResearchStudyReasonStopped(CodeSystemValue):
    """ Codes for why the study ended prematurely

    URL: http://hl7.org/fhir/research-study-reason-stopped
    ValueSet: http://hl7.org/fhir/ValueSet/research-study-reason-stopped
    """
    URL = "http://hl7.org/fhir/research-study-reason-stopped"
    EXPERIMENTAL = False

    """ The study prematurely ended because the accrual goal was met.
    """
    accrualGoalMet = "accrual-goal-met"

    """ The study prematurely ended due to toxicity.
    """
    closedDueToToxicity = "closed-due-to-toxicity"

    """ The study prematurely ended due to lack of study progress.
    """
    closedDueToLackOfStudyProgress = "closed-due-to-lack-of-study-progress"

    """ The study prematurely ended temporarily per study design.
    """
    temporarilyClosedPerStudyDesign = "temporarily-closed-per-study-design"


class ResearchStudyStatus(CodeSystemValue):
    """ Codes that convey the current status of the research study

    URL: http://hl7.org/fhir/research-study-status
    ValueSet: http://hl7.org/fhir/ValueSet/research-study-status
    """
    URL = "http://hl7.org/fhir/research-study-status"
    EXPERIMENTAL = False

    """ Study is opened for accrual.
    """
    active = "active"

    """ Study is completed prematurely and will not resume; patients are no longer examined nor treated.
	/// Tagged
    """
    administrativelyCompleted = "administratively-completed"

    """ Protocol is approved by the review board.
    """
    approved = "approved"

    """ Study is closed for accrual; patients can be examined and treated.
    """
    closedToAccrual = "closed-to-accrual"

    """ Study is closed to accrual and intervention, i.e. the study is closed to enrollment, all study subjects have
	/// completed treatment or intervention but are still being followed according to the primary objective of the
	/// study.
    """
    closedToAccrualAndIntervention = "closed-to-accrual-and-intervention"

    """ Study is closed to accrual and intervention, i.e. the study is closed to enrollment, all study subjects have
	/// completed treatment
	/// or intervention but are still being followed according to the primary objective of the study.
    """
    completed = "completed"

    """ Protocol was disapproved by the review board.
    """
    disapproved = "disapproved"

    """ Protocol is submitted to the review board for approval.
    """
    inReview = "in-review"

    """ Study is temporarily closed for accrual; can be potentially resumed in the future; patients can be examined and
	/// treated.
    """
    temporarilyClosedToAccrual = "temporarily-closed-to-accrual"

    """ Study is temporarily closed for accrual and intervention and potentially can be resumed in the future.
    """
    temporarilyClosedToAccrualAndIntervention = "temporarily-closed-to-accrual-and-intervention"

    """ Protocol was withdrawn by the lead organization.
    """
    withdrawn = "withdrawn"


class ResearchSubjectStatus(CodeSystemValue):
    """ Indicates the progression of a study subject through a study

    URL: http://hl7.org/fhir/research-subject-status
    ValueSet: http://hl7.org/fhir/ValueSet/research-subject-status
    """
    URL = "http://hl7.org/fhir/research-subject-status"
    EXPERIMENTAL = False

    """ An identified person that can be considered for inclusion in a study.
    """
    candidate = "candidate"

    """ A person that has met the eligibility criteria for inclusion in a study.
    """
    eligible = "eligible"

    """ A person is no longer receiving study intervention and/or being evaluated with tests and procedures according to
	/// the protocol, but they are being monitored on a protocol-prescribed schedule.
    """
    followUp = "follow-up"

    """ A person who did not meet one or more criteria required for participation in a study is considered to have
	/// failed screening or
	/// is ineligible for the study.
    """
    ineligible = "ineligible"

    """ A person for whom registration was not completed
    """
    notRegistered = "not-registered"

    """ A person that has ended their participation on a study either because their treatment/observation is complete or
	/// through not
	/// responding, withdrawal, non-compliance and/or adverse event.
    """
    offStudy = "off-study"

    """ A person that is enrolled or registered on a study.
    """
    onStudy = "on-study"

    """ The person is receiving the treatment or participating in an activity (e.g. yoga, diet, etc.) that the study is
	/// evaluating.
    """
    onStudyIntervention = "on-study-intervention"

    """ The subject is being evaluated via tests and assessments according to the study calendar, but is not receiving
	/// any intervention. Note that this state is study-dependent and might not exist in all studies.  A synonym for
	/// this is "short-term follow-up".
    """
    onStudyObservation = "on-study-observation"

    """ A person is pre-registered for a study.
    """
    pendingOnStudy = "pending-on-study"

    """ A person that is potentially eligible for participation in the study.
    """
    potentialCandidate = "potential-candidate"

    """ A person who is being evaluated for eligibility for a study.
    """
    screening = "screening"

    """ The person has withdrawn their participation in the study before registration.
    """
    withdrawn = "withdrawn"


class ResourceType(CodeSystemValue):
    """ One of the resource types defined as part of this version of FHIR.

    URL: http://hl7.org/fhir/resource-types
    ValueSet: http://hl7.org/fhir/ValueSet/resource-types
    """
    URL = "http://hl7.org/fhir/resource-types"
    EXPERIMENTAL = False

    """ A financial tool for tracking value accrued for a particular purpose.  In the healthcare field, used to track
	/// charges for a patient, cost centers, etc.
    """
    account = "Account"

    """ This resource allows for the definition of some activity to be performed, independent of a particular patient,
	/// practitioner, or other performance context.
    """
    activityDefinition = "ActivityDefinition"

    """ Actual or  potential/avoided event causing unintended physical injury resulting from or contributed to by
	/// medical care, a research study or other healthcare setting factors that requires additional monitoring,
	/// treatment, or hospitalization, or that results in death.
    """
    adverseEvent = "AdverseEvent"

    """ Risk of harmful or undesirable, physiological response which is unique to an individual and associated with
	/// exposure to a substance.
    """
    allergyIntolerance = "AllergyIntolerance"

    """ A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a
	/// specific date/time. This may result in one or more Encounter(s).
    """
    appointment = "Appointment"

    """ A reply to an appointment request for a patient and/or practitioner(s), such as a confirmation or rejection.
    """
    appointmentResponse = "AppointmentResponse"

    """ A record of an event made for purposes of maintaining a security log. Typical uses include detection of
	/// intrusion attempts and monitoring for inappropriate usage.
    """
    auditEvent = "AuditEvent"

    """ Basic is used for handling concepts not yet defined in FHIR, narrative-only resources that don't map to an
	/// existing resource, and custom resources not appropriate for inclusion in the FHIR specification.
    """
    basic = "Basic"

    """ A binary resource can contain any content, whether text, image, pdf, zip archive, etc.
    """
    binary = "Binary"

    """ A material substance originating from a biological entity intended to be transplanted or infused
	/// into another (possibly the same) biological entity.
    """
    biologicallyDerivedProduct = "BiologicallyDerivedProduct"

    """ Record details about an anatomical structure.  This resource may be used when a coded concept does not provide
	/// the necessary detail needed for the use case.
    """
    bodyStructure = "BodyStructure"

    """ A container for a collection of resources.
    """
    bundle = "Bundle"

    """ A Capability Statement documents a set of capabilities (behaviors) of a FHIR Server that may be used as a
	/// statement of actual server functionality or a statement of required or desired server implementation.
    """
    capabilityStatement = "CapabilityStatement"

    """ Describes the intention of how one or more practitioners intend to deliver care for a particular patient, group
	/// or community for a period of time, possibly limited to care for a specific condition or set of conditions.
    """
    carePlan = "CarePlan"

    """ The Care Team includes all the people and organizations who plan to participate in the coordination and delivery
	/// of care for a patient.
    """
    careTeam = "CareTeam"

    """ The resource ChargeItem describes the provision of healthcare provider products for a certain patient, therefore
	/// referring not only to the product, but containing in addition details of the provision, like date, time, amounts
	/// and participating organizations and persons. Main Usage of the ChargeItem is to enable the billing process and
	/// internal cost allocation.
    """
    chargeItem = "ChargeItem"

    """ A provider issued list of services and products provided, or to be provided, to a patient which is provided to
	/// an insurer for payment recovery.
    """
    claim = "Claim"

    """ This resource provides the adjudication details from the processing of a Claim resource.
    """
    claimResponse = "ClaimResponse"

    """ A record of a clinical assessment performed to determine what problem(s) may affect the patient and before
	/// planning the treatments or management strategies that are best to manage a patient's condition. Assessments are
	/// often 1:1 with a clinical consultation / encounter,  but this varies greatly depending on the clinical workflow.
	/// This resource is called "ClinicalImpression" rather than "ClinicalAssessment" to avoid confusion with the
	/// recording of assessment tools such as Apgar score.
    """
    clinicalImpression = "ClinicalImpression"

    """ The CodeSystem resource is used to declare the existence of and describe a code system or code system supplement
	/// and its key properties, and optionally define a part or all of its content.
    """
    codeSystem = "CodeSystem"

    """ An occurrence of information being transmitted; e.g. an alert that was sent to a responsible provider, a public
	/// health agency was notified about a reportable condition.
    """
    communication = "Communication"

    """ A request to convey information; e.g. the CDS system proposes that an alert be sent to a responsible provider,
	/// the CDS system proposes that the public health agency be notified about a reportable condition.
    """
    communicationRequest = "CommunicationRequest"

    """ A compartment definition that defines how resources are accessed on a server.
    """
    compartmentDefinition = "CompartmentDefinition"

    """ A set of healthcare-related information that is assembled together into a single logical package that provides a
	/// single coherent statement of meaning, establishes its own context and that has clinical attestation with regard
	/// to who is making the statement. A Composition defines the structure and narrative content necessary for a
	/// document. However, a Composition alone does not constitute a document. Rather, the Composition must be the first
	/// entry in a Bundle where Bundle.type=document, and any other resources referenced from Composition must be
	/// included as subsequent entries in the Bundle (for example Patient, Practitioner, Encounter, etc.).
    """
    composition = "Composition"

    """ A statement of relationships from one set of concepts to one or more other concepts - either code systems or
	/// data elements, or classes in class models.
    """
    conceptMap = "ConceptMap"

    """ A clinical condition, problem, diagnosis, or other event, situation, issue, or clinical concept that has risen
	/// to a level of concern.
    """
    condition = "Condition"

    """ A record of a healthcare consumer’s  choices, which permits or denies identified recipient(s) or recipient
	/// role(s) to perform one or more actions within a given policy context, for specific purposes and periods of time.
    """
    consent = "Consent"

    """ A formal agreement between parties regarding the conduct of business, exchange of information or other matters.
    """
    contract = "Contract"

    """ Financial instrument which may be used to reimburse or pay for health care products and services.
    """
    coverage = "Coverage"

    """ Indicates an actual or potential clinical issue with or between one or more active or proposed clinical actions
	/// for a patient; e.g. Drug-drug interaction, Ineffective treatment frequency, Procedure-condition conflict, etc.
    """
    detectedIssue = "DetectedIssue"

    """ This resource identifies an instance or a type of a manufactured item that is used in the provision of
	/// healthcare without being substantially changed through that activity. The device may be a medical or non-medical
	/// device.  Medical devices include durable (reusable) medical equipment, implantable devices, as well as
	/// disposable equipment used for diagnostic, treatment, and research for healthcare and public health.  Non-medical
	/// devices may include items such as a machine, cellphone, computer, application, etc.
    """
    device = "Device"

    """ The characteristics, operational status and capabilities of a medical-related component of a medical device.
    """
    deviceComponent = "DeviceComponent"

    """ Describes a measurement, calculation or setting capability of a medical device.
    """
    deviceMetric = "DeviceMetric"

    """ Represents a request for a patient to employ a medical device. The device may be an implantable device, or an
	/// external assistive device, such as a walker.
    """
    deviceRequest = "DeviceRequest"

    """ A record of a device being used by a patient where the record is the result of a report from the patient or
	/// another clinician.
    """
    deviceUseStatement = "DeviceUseStatement"

    """ The findings and interpretation of diagnostic  tests performed on patients, groups of patients, devices, and
	/// locations, and/or specimens derived from these. The report includes clinical context such as requesting and
	/// provider information, and some mix of atomic results, images, textual and coded interpretations, and formatted
	/// representation of diagnostic reports.
    """
    diagnosticReport = "DiagnosticReport"

    """ A collection of documents compiled for a purpose together with metadata that applies to the collection.
    """
    documentManifest = "DocumentManifest"

    """ A reference to a document.
    """
    documentReference = "DocumentReference"

    """ A resource that includes narrative, extensions, and contained resources.
    """
    domainResource = "DomainResource"

    """ The EligibilityRequest provides patient and insurance coverage information to an insurer for them to respond, in
	/// the form of an EligibilityResponse, with information regarding whether the stated coverage is valid and in-force
	/// and optionally to provide the insurance details of the policy.
    """
    eligibilityRequest = "EligibilityRequest"

    """ This resource provides eligibility and plan details from the processing of an Eligibility resource.
    """
    eligibilityResponse = "EligibilityResponse"

    """ An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s)
	/// or assessing the health status of a patient.
    """
    encounter = "Encounter"

    """ The technical details of an endpoint that can be used for electronic services, such as for web services
	/// providing XDS.b or a REST endpoint for another FHIR server. This may include any security context information.
    """
    endpoint = "Endpoint"

    """ This resource provides the insurance enrollment details to the insurer regarding a specified coverage.
    """
    enrollmentRequest = "EnrollmentRequest"

    """ This resource provides enrollment and plan details from the processing of an Enrollment resource.
    """
    enrollmentResponse = "EnrollmentResponse"

    """ Catalog entries are wrappers that contextualize items included in a catalog.
    """
    entryDefinition = "EntryDefinition"

    """ An association between a patient and an organization / healthcare provider(s) during which time encounters may
	/// occur. The managing organization assumes a level of responsibility for the patient during this time.
    """
    episodeOfCare = "EpisodeOfCare"

    """ The EventDefinition resource provides a reusable description of when a particular event can occur.
    """
    eventDefinition = "EventDefinition"

    """ Example of workflow instance.
    """
    exampleScenario = "ExampleScenario"

    """ Resource to define constraints on the Expansion of a FHIR ValueSet.
    """
    expansionProfile = "ExpansionProfile"

    """ This resource provides: the claim details; adjudication details from the processing of a Claim; and optionally
	/// account balance information, for informing the subscriber of the benefits provided.
    """
    explanationOfBenefit = "ExplanationOfBenefit"

    """ Significant health conditions for a person related to the patient relevant in the context of care for the
	/// patient.
    """
    familyMemberHistory = "FamilyMemberHistory"

    """ Prospective warnings of potential issues when providing care to the patient.
    """
    flag = "Flag"

    """ Describes the intended objective(s) for a patient, group or organization care, for example, weight loss,
	/// restoring an activity of daily living, obtaining herd immunity via immunization, meeting a process improvement
	/// objective, etc.
    """
    goal = "Goal"

    """ A formal computable definition of a graph of resources - that is, a coherent set of resources that form a graph
	/// by following references. The Graph Definition resource defines a set and makes rules about the set.
    """
    graphDefinition = "GraphDefinition"

    """ Represents a defined collection of entities that may be discussed or acted upon collectively but which are not
	/// expected to act collectively and are not formally or legally recognized; i.e. a collection of entities that
	/// isn't an Organization.
    """
    group = "Group"

    """ A guidance response is the formal response to a guidance request, including any output parameters returned by
	/// the evaluation, as well as the description of any proposed actions to be taken.
    """
    guidanceResponse = "GuidanceResponse"

    """ The details of a healthcare service available at a location.
    """
    healthcareService = "HealthcareService"

    """ Representation of the content produced in a DICOM imaging study. A study comprises a set of series, each of
	/// which includes a set of Service-Object Pair Instances (SOP Instances - images or other data) acquired or
	/// produced in a common context.  A series is of only one modality (e.g. X-ray, CT, MR, ultrasound), but a study
	/// may have multiple series of different modalities.
    """
    imagingStudy = "ImagingStudy"

    """ Describes the event of a patient being administered a vaccine or a record of an immunization as reported by a
	/// patient, a clinician or another party.
    """
    immunization = "Immunization"

    """ Describes a comparison of an immunization event against published recommendations to determine if the
	/// administration is "valid" in relation to those  recommendations.
    """
    immunizationEvaluation = "ImmunizationEvaluation"

    """ A patient's point-in-time set of recommendations (i.e. forecasting) according to a published schedule with
	/// optional supporting justification.
    """
    immunizationRecommendation = "ImmunizationRecommendation"

    """ A set of rules of how FHIR is used to solve a particular problem. This resource is used to gather all the parts
	/// of an implementation guide into a logical whole and to publish a computable definition of all the parts.
    """
    implementationGuide = "ImplementationGuide"

    """ Invoice containing collected ChargeItems from an Account with calculated individual and total price for Billing
	/// purpose.
    """
    invoice = "Invoice"

    """ A physical, countable instance of an item, for example one box or one unit.
    """
    itemInstance = "ItemInstance"

    """ The Library resource is a general-purpose container for knowledge asset definitions. It can be used to describe
	/// and expose existing knowledge assets such as logic libraries and information model descriptions, as well as to
	/// describe a collection of knowledge assets.
    """
    library = "Library"

    """ Identifies two or more records (resource instances) that are referring to the same real-world "occurrence".
    """
    linkage = "Linkage"

    """ A set of information summarized from a list of other resources.
    """
    list = "List"

    """ Details and position information for a physical place where services are provided and resources and participants
	/// may be stored, found, contained, or accommodated.
    """
    location = "Location"

    """ The Measure resource provides the definition of a quality measure.
    """
    measure = "Measure"

    """ The MeasureReport resource contains the results of the calculation of a measure; and optionally a reference to
	/// the resources involved in that calculation.
    """
    measureReport = "MeasureReport"

    """ A photo, video, or audio recording acquired or used in healthcare. The actual content may be inline or provided
	/// by direct reference.
    """
    media = "Media"

    """ This resource is primarily used for the identification and definition of a medication for the purposes of
	/// prescribing, dispensing, and administering a medication as well as for making statements about medication use.
    """
    medication = "Medication"

    """ Describes the event of a patient consuming or otherwise being administered a medication.  This may be as simple
	/// as swallowing a tablet or it may be a long running infusion.  Related resources tie this event to the
	/// authorizing prescription, and the specific encounter between patient and health care practitioner.
    """
    medicationAdministration = "MedicationAdministration"

    """ Indicates that a medication product is to be or has been dispensed for a named person/patient.  This includes a
	/// description of the medication product (supply) provided and the instructions for administering the medication.
	/// The medication dispense is the result of a pharmacy system responding to a medication order.
    """
    medicationDispense = "MedicationDispense"

    """ An order or request for both supply of the medication and the instructions for administration of the medication
	/// to a patient. The resource is called "MedicationRequest" rather than "MedicationPrescription" or
	/// "MedicationOrder" to generalize the use across inpatient and outpatient settings, including care plans, etc.,
	/// and to harmonize with workflow patterns.
    """
    medicationRequest = "MedicationRequest"

    """ A record of a medication that is being consumed by a patient.   A MedicationStatement may indicate that the
	/// patient may be taking the medication now, or has taken the medication in the past or will be taking the
	/// medication in the future.  The source of this information can be the patient, significant other (such as a
	/// family member or spouse), or a clinician.  A common scenario where this information is captured is during the
	/// history taking process during a patient visit or stay.   The medication information may come from sources such
	/// as the patient's memory, from a prescription bottle,  or from a list of medications the patient, clinician or
	/// other party maintains.
	/// 
	/// The primary difference between a medication statement and a medication administration is that the medication
	/// administration has complete administration information and is based on actual administration information from
	/// the person who administered the medication.  A medication statement is often, if not always, less specific.
	/// There is no required date/time when the medication was administered, in fact we only know that a source has
	/// reported the patient is taking this medication, where details such as time, quantity, or rate or even medication
	/// product may be incomplete or missing or less precise.  As stated earlier, the medication statement information
	/// may come from the patient's memory, from a prescription bottle or from a list of medications the patient,
	/// clinician or other party maintains.  Medication administration is more formal and is not missing detailed
	/// information.
    """
    medicationStatement = "MedicationStatement"

    """ Detailed definition of a medicinal product, typically for uses other than direct patient care (e.g. regulatory
	/// use).
    """
    medicinalProduct = "MedicinalProduct"

    """ The regulatory authorization of a medicinal product.
    """
    medicinalProductAuthorization = "MedicinalProductAuthorization"

    """ The clinical particulars - indications, contraindications etc. of a medicinal product, including for regulatory
	/// purposes.
    """
    medicinalProductClinicals = "MedicinalProductClinicals"

    """ A detailed description of a device, typically as part of a regulated medicinal product. It is not intended to
	/// relace the Device resource, which covers use of device instances.
    """
    medicinalProductDeviceSpec = "MedicinalProductDeviceSpec"

    """ An ingredient of a manufactured item or pharmaceutical product.
    """
    medicinalProductIngredient = "MedicinalProductIngredient"

    """ A medicinal product in a container or package.
    """
    medicinalProductPackaged = "MedicinalProductPackaged"

    """ A pharmaceutical product described in terms of its composition and dose form.
    """
    medicinalProductPharmaceutical = "MedicinalProductPharmaceutical"

    """ Defines the characteristics of a message that can be shared between systems, including the type of event that
	/// initiates the message, the content to be transmitted and what response(s), if any, are permitted.
    """
    messageDefinition = "MessageDefinition"

    """ The header for a message exchange that is either requesting or responding to an action.  The reference(s) that
	/// are the subject of the action as well as other information related to the action are typically transmitted in a
	/// bundle in which the MessageHeader resource instance is the first resource in the bundle.
    """
    messageHeader = "MessageHeader"

    """ A curated namespace that issues unique symbols within that namespace for the identification of concepts, people,
	/// devices, etc.  Represents a "System" used within the Identifier and Coding data types.
    """
    namingSystem = "NamingSystem"

    """ A request to supply a diet, formula feeding (enteral) or oral nutritional supplement to a patient/resident.
    """
    nutritionOrder = "NutritionOrder"

    """ Measurements and simple assertions made about a patient, device or other subject.
    """
    observation = "Observation"

    """ Set of definitional characteristics for a kind of observation or measurement produced or consumed by an
	/// orderable health care service.
    """
    observationDefinition = "ObservationDefinition"

    """ A person's work information, structured to facilitate individual, population, and public health use; not
	/// intended to support billing.
    """
    occupationalData = "OccupationalData"

    """ A formal computable definition of an operation (on the RESTful interface) or a named query (using the search
	/// interaction).
    """
    operationDefinition = "OperationDefinition"

    """ A collection of error, warning or information messages that result from a system action.
    """
    operationOutcome = "OperationOutcome"

    """ A formally or informally recognized grouping of people or organizations formed for the purpose of achieving some
	/// form of collective action.  Includes companies, institutions, corporations, departments, community groups,
	/// healthcare practice groups, etc.
    """
    organization = "Organization"

    """ A specific set of Roles/Locations/specialties/services that a practitioner may perform at an organization for a
	/// period of time.
    """
    organizationRole = "OrganizationRole"

    """ This special resource type is used to represent an operation request and response (operations.html). It has no
	/// other use, and there is no RESTful endpoint associated with it.
    """
    parameters = "Parameters"

    """ Demographics and other administrative information about an individual or animal receiving care or other health-
	/// related services.
    """
    patient = "Patient"

    """ This resource provides the status of the payment for goods and services rendered, and the request and response
	/// resource references.
    """
    paymentNotice = "PaymentNotice"

    """ This resource provides payment details and claim references supporting a bulk payment.
    """
    paymentReconciliation = "PaymentReconciliation"

    """ Demographics and administrative information about a person independent of a specific health-related context.
    """
    person = "Person"

    """ This resource allows for the definition of various types of plans as a sharable, consumable, and executable
	/// artifact. The resource is general enough to support the description of a broad range of clinical artifacts such
	/// as clinical decision support rules, order sets and protocols.
    """
    planDefinition = "PlanDefinition"

    """ A person who is directly or indirectly involved in the provisioning of healthcare.
    """
    practitioner = "Practitioner"

    """ A specific set of Roles/Locations/specialties/services that a practitioner may perform at an organization for a
	/// period of time.
    """
    practitionerRole = "PractitionerRole"

    """ An action that is or was performed on a patient. This can be a physical intervention like an operation, or less
	/// invasive like counseling or hypnotherapy.
    """
    procedure = "Procedure"

    """ This resource provides the target, request and response, and action details for an action to be performed by the
	/// target on or about existing resources.
    """
    processRequest = "ProcessRequest"

    """ This resource provides processing status, errors and notes from the processing of a resource.
    """
    processResponse = "ProcessResponse"

    """ Details of a Health Insurance product/plan provided by an organization.
    """
    productPlan = "ProductPlan"

    """ Provenance of a resource is a record that describes entities and processes involved in producing and delivering
	/// or otherwise influencing that resource. Provenance provides a critical foundation for assessing authenticity,
	/// enabling trust, and allowing reproducibility. Provenance assertions are a form of contextual metadata and can
	/// themselves become important records with their own provenance. Provenance statement indicates clinical
	/// significance in terms of confidence in authenticity, reliability, and trustworthiness, integrity, and stage in
	/// lifecycle (e.g. Document Completion - has the artifact been legally authenticated), all of which may impact
	/// security, privacy, and trust policies.
    """
    provenance = "Provenance"

    """ A structured set of questions intended to guide the collection of answers from end-users. Questionnaires provide
	/// detailed control over order, presentation, phraseology and grouping to allow coherent, consistent data
	/// collection.
    """
    questionnaire = "Questionnaire"

    """ A structured set of questions and their answers. The questions are ordered and grouped into coherent subsets,
	/// corresponding to the structure of the grouping of the questionnaire being responded to.
    """
    questionnaireResponse = "QuestionnaireResponse"

    """ Information about a person that is involved in the care for a patient, but who is not the target of healthcare,
	/// nor has a formal responsibility in the care process.
    """
    relatedPerson = "RelatedPerson"

    """ A group of related requests that can be used to capture intended activities that have inter-dependencies such as
	/// "give this medication after that one".
    """
    requestGroup = "RequestGroup"

    """ A process where a researcher or organization plans and then executes a series of steps intended to increase the
	/// field of healthcare-related knowledge.  This includes studies of safety, efficacy, comparative effectiveness and
	/// other information about medications, devices, therapies and other interventional and investigative techniques.
	/// A ResearchStudy involves the gathering of information about human or animal subjects.
    """
    researchStudy = "ResearchStudy"

    """ A physical entity which is the primary unit of operational and/or administrative interest in a study.
    """
    researchSubject = "ResearchSubject"

    """ This is the base resource type for everything.
    """
    resource = "Resource"

    """ An assessment of the likely outcome(s) for a patient or other subject as well as the likelihood of each outcome.
    """
    riskAssessment = "RiskAssessment"

    """ A container for slots of time that may be available for booking appointments.
    """
    schedule = "Schedule"

    """ A search parameter that defines a named search item that can be used to search/filter on a resource.
    """
    searchParameter = "SearchParameter"

    """ Raw data describing a biological sequence.
    """
    sequence = "Sequence"

    """ A record of a request for service such as diagnostic investigations, treatments, or operations to be performed.
    """
    serviceRequest = "ServiceRequest"

    """ A slot of time on a schedule that may be available for booking appointments.
    """
    slot = "Slot"

    """ A sample to be used for analysis.
    """
    specimen = "Specimen"

    """ A kind of specimen with associated set of requirements.
    """
    specimenDefinition = "SpecimenDefinition"

    """ A definition of a FHIR structure. This resource is used to describe the underlying resources, data types defined
	/// in FHIR, and also for describing extensions and constraints on resources and data types.
    """
    structureDefinition = "StructureDefinition"

    """ A Map of relationships between 2 structures that can be used to transform data.
    """
    structureMap = "StructureMap"

    """ The subscription resource is used to define a push-based subscription from a server to another system. Once a
	/// subscription is registered with the server, the server checks every resource that is created or updated, and if
	/// the resource matches the given criteria, it sends a message on the defined "channel" so that another system can
	/// take an appropriate action.
    """
    subscription = "Subscription"

    """ A homogeneous material with a definite composition.
    """
    substance = "Substance"

    """ Todo.
    """
    substancePolymer = "SubstancePolymer"

    """ Todo.
    """
    substanceReferenceInformation = "SubstanceReferenceInformation"

    """ The detailed description of a substance, typically at a level beyond what is used for prescribing.
    """
    substanceSpecification = "SubstanceSpecification"

    """ Record of delivery of what is supplied.
    """
    supplyDelivery = "SupplyDelivery"

    """ A record of a request for a medication, substance or device used in the healthcare setting.
    """
    supplyRequest = "SupplyRequest"

    """ A task to be performed.
    """
    task = "Task"

    """ A Terminology Capabilities documents a set of capabilities (behaviors) of a FHIR Server that may be used as a
	/// statement of actual server functionality or a statement of required or desired server implementation.
    """
    terminologyCapabilities = "TerminologyCapabilities"

    """ A summary of information based on the results of executing a TestScript.
    """
    testReport = "TestReport"

    """ A structured set of tests against a FHIR server or client implementation to determine compliance against the
	/// FHIR specification.
    """
    testScript = "TestScript"

    """ Information about a user's current session.
    """
    userSession = "UserSession"

    """ A ValueSet resource specifies a set of codes drawn from one or more code systems, intended for use in a
	/// particular context. Value sets link between [[[CodeSystem]]] definitions and their use in [coded
	/// elements](terminologies.html).
    """
    valueSet = "ValueSet"

    """ Describes validation requirements, source(s), status and dates for one or more elements.
    """
    verificationResult = "VerificationResult"

    """ An authorization for the supply of glasses and/or contact lenses to a patient.
    """
    visionPrescription = "VisionPrescription"


class ResourceTypeLink(CodeSystemValue):
    """ The type of payee Resource

    URL: http://hl7.org/fhir/resource-type-link
    ValueSet: http://hl7.org/fhir/ValueSet/resource-type-link
    """
    URL = "http://hl7.org/fhir/resource-type-link"
    EXPERIMENTAL = False

    """ Organization resource
    """
    organization = "organization"

    """ Patient resource
    """
    patient = "patient"

    """ Practitioner resource
    """
    practitioner = "practitioner"

    """ RelatedPerson resource
    """
    relatedperson = "relatedperson"


class ResourceValidationMode(CodeSystemValue):
    """ Codes indicating the type of validation to perform

    URL: http://hl7.org/fhir/resource-validation-mode
    ValueSet: http://hl7.org/fhir/ValueSet/resource-validation-mode
    """
    URL = "http://hl7.org/fhir/resource-validation-mode"
    EXPERIMENTAL = False

    """ The server checks the content, and then checks that the content would be acceptable as a create (e.g. that the
	/// content would not violate any uniqueness constraints).
    """
    create = "create"

    """ The server checks the content, and then checks that it would accept it as an update against the nominated
	/// specific resource (e.g. that there are no changes to immutable fields the server does not allow to change and
	/// checking version integrity if appropriate).
    """
    update = "update"

    """ The server ignores the content and checks that the nominated resource is allowed to be deleted (e.g. checking
	/// referential integrity rules).
    """
    delete = "delete"


class ResourceVersionPolicy(CodeSystemValue):
    """ How the system supports versioning for a resource.

    URL: http://hl7.org/fhir/versioning-policy
    ValueSet: http://hl7.org/fhir/ValueSet/versioning-policy
    """
    URL = "http://hl7.org/fhir/versioning-policy"
    EXPERIMENTAL = False

    """ VersionId meta-property is not supported (server) or used (client).
    """
    noVersion = "no-version"

    """ VersionId meta-property is supported (server) or used (client).
    """
    versioned = "versioned"

    """ VersionId must be correct for updates (server) or will be specified (If-match header) for updates (client).
    """
    versionedUpdate = "versioned-update"


class ResponseType(CodeSystemValue):
    """ The kind of response to a message

    URL: http://hl7.org/fhir/response-code
    ValueSet: http://hl7.org/fhir/ValueSet/response-code
    """
    URL = "http://hl7.org/fhir/response-code"
    EXPERIMENTAL = False

    """ The message was accepted and processed without error.
    """
    ok = "ok"

    """ Some internal unexpected error occurred - wait and try again. Note - this is usually used for things like
	/// database unavailable, which may be expected to resolve, though human intervention may be required.
    """
    transientError = "transient-error"

    """ The message was rejected because of a problem with the content. There is no point in re-sending without change.
	/// The response narrative SHALL describe the issue.
    """
    fatalError = "fatal-error"


class RestfulCapabilityMode(CodeSystemValue):
    """ The mode of a RESTful capability statement.

    URL: http://hl7.org/fhir/restful-capability-mode
    ValueSet: http://hl7.org/fhir/ValueSet/restful-capability-mode
    """
    URL = "http://hl7.org/fhir/restful-capability-mode"
    EXPERIMENTAL = False

    """ The application acts as a client for this resource.
    """
    client = "client"

    """ The application acts as a server for this resource.
    """
    server = "server"


class RestfulSecurityService(CodeSystemValue):
    """ Types of security services used with FHIR.

    URL: http://hl7.org/fhir/restful-security-service
    ValueSet: http://hl7.org/fhir/ValueSet/restful-security-service
    """
    URL = "http://hl7.org/fhir/restful-security-service"
    EXPERIMENTAL = False

    """ OAuth (unspecified version see oauth.net).
    """
    oAuth = "OAuth"

    """ OAuth2 using SMART-on-FHIR profile (see http://docs.smarthealthit.org/).
    """
    sMARTOnFHIR = "SMART-on-FHIR"

    """ Microsoft NTLM Authentication.
    """
    NTLM = "NTLM"

    """ Basic authentication defined in HTTP specification.
    """
    basic = "Basic"

    """ see http://www.ietf.org/rfc/rfc4120.txt.
    """
    kerberos = "Kerberos"

    """ SSL where client must have a certificate registered with the server.
    """
    certificates = "Certificates"


class RiskProbability(CodeSystemValue):
    """ Codes representing the likelihood of a particular outcome in a risk assessment.

    URL: http://hl7.org/fhir/risk-probability
    ValueSet: http://hl7.org/fhir/ValueSet/risk-probability
    """
    URL = "http://hl7.org/fhir/risk-probability"
    EXPERIMENTAL = True

    """ The specified outcome is exceptionally unlikely.
    """
    negligible = "negligible"

    """ The specified outcome is possible but unlikely.
    """
    low = "low"

    """ The specified outcome has a reasonable likelihood of occurrence.
    """
    moderate = "moderate"

    """ The specified outcome is more likely to occur than not.
    """
    high = "high"

    """ The specified outcome is effectively guaranteed.
    """
    certain = "certain"


class SNOMEDCTReasonMedicationNotGivenCodes(CodeSystemValue):
    """ This value set includes all medication refused, medication not administered, and non-administration of necessary drug or
medicine codes from SNOMED CT - provided as an exemplar value set.

    URL: http://hl7.org/fhir/reason-medication-not-given
    ValueSet: http://hl7.org/fhir/ValueSet/reason-medication-not-given-codes
    """
    URL = "http://hl7.org/fhir/reason-medication-not-given"
    EXPERIMENTAL = True

    """ No reason known.
    """
    A = "a"

    """ The patient was not available when the dose was scheduled.
    """
    B = "b"

    """ The patient was asleep when the dose was scheduled.
    """
    C = "c"

    """ The patient was given the medication and immediately vomited it back.
    """
    D = "d"


class SearchComparator(CodeSystemValue):
    """ What Search Comparator Codes are supported in search

    URL: http://hl7.org/fhir/search-comparator
    ValueSet: http://hl7.org/fhir/ValueSet/search-comparator
    """
    URL = "http://hl7.org/fhir/search-comparator"
    EXPERIMENTAL = False

    """ the value for the parameter in the resource is equal to the provided value
    """
    eq = "eq"

    """ the value for the parameter in the resource is not equal to the provided value
    """
    ne = "ne"

    """ the value for the parameter in the resource is greater than the provided value
    """
    gt = "gt"

    """ the value for the parameter in the resource is less than the provided value
    """
    lt = "lt"

    """ the value for the parameter in the resource is greater or equal to the provided value
    """
    ge = "ge"

    """ the value for the parameter in the resource is less or equal to the provided value
    """
    le = "le"

    """ the value for the parameter in the resource starts after the provided value
    """
    sa = "sa"

    """ the value for the parameter in the resource ends before the provided value
    """
    eb = "eb"

    """ the value for the parameter in the resource is approximately the same to the provided value.
    """
    ap = "ap"


class SearchEntryMode(CodeSystemValue):
    """ Why an entry is in the result set - whether it's included as a match or because of an _include requirement.

    URL: http://hl7.org/fhir/search-entry-mode
    ValueSet: http://hl7.org/fhir/ValueSet/search-entry-mode
    """
    URL = "http://hl7.org/fhir/search-entry-mode"
    EXPERIMENTAL = False

    """ This resource matched the search specification.
    """
    match = "match"

    """ This resource is returned because it is referred to from another resource in the search set.
    """
    include = "include"

    """ An OperationOutcome that provides additional information about the processing of a search.
    """
    outcome = "outcome"


class SearchModifierCode(CodeSystemValue):
    """ A supported modifier for a search parameter.

    URL: http://hl7.org/fhir/search-modifier-code
    ValueSet: http://hl7.org/fhir/ValueSet/search-modifier-code
    """
    URL = "http://hl7.org/fhir/search-modifier-code"
    EXPERIMENTAL = False

    """ The search parameter returns resources that have a value or not.
    """
    missing = "missing"

    """ The search parameter returns resources that have a value that exactly matches the supplied parameter (the whole
	/// string, including casing and accents).
    """
    exact = "exact"

    """ The search parameter returns resources that include the supplied parameter value anywhere within the field being
	/// searched.
    """
    contains = "contains"

    """ The search parameter returns resources that do not contain a match.
    """
    _not = "not"

    """ The search parameter is processed as a string that searches text associated with the code/value - either
	/// CodeableConcept.text, Coding.display, or Identifier.type.text.
    """
    text = "text"

    """ The search parameter is a URI (relative or absolute) that identifies a value set, and the search parameter tests
	/// whether the coding is in the specified value set.
    """
    _in = "in"

    """ The search parameter is a URI (relative or absolute) that identifies a value set, and the search parameter tests
	/// whether the coding is not in the specified value set.
    """
    notIn = "not-in"

    """ The search parameter tests whether the value in a resource is subsumed by the specified value (is-a, or
	/// hierarchical relationships).
    """
    below = "below"

    """ The search parameter tests whether the value in a resource subsumes the specified value (is-a, or hierarchical
	/// relationships).
    """
    above = "above"

    """ The search parameter only applies to the Resource Type specified as a modifier (e.g. the modifier is not
	/// actually :type, but :Patient etc.).
    """
    type = "type"


class SearchParamType(CodeSystemValue):
    """ Data types allowed to be used for search parameters.

    URL: http://hl7.org/fhir/search-param-type
    ValueSet: http://hl7.org/fhir/ValueSet/search-param-type
    """
    URL = "http://hl7.org/fhir/search-param-type"
    EXPERIMENTAL = False

    """ Search parameter SHALL be a number (a whole number, or a decimal).
    """
    number = "number"

    """ Search parameter is on a date/time. The date format is the standard XML format, though other formats may be
	/// supported.
    """
    date = "date"

    """ Search parameter is a simple string, like a name part. Search is case-insensitive and accent-insensitive. May
	/// match just the start of a string. String parameters may contain spaces.
    """
    string = "string"

    """ Search parameter on a coded element or identifier. May be used to search through the text, display, code and
	/// code/codesystem (for codes) and label, system and key (for identifier). Its value is either a string or a pair
	/// of namespace and value, separated by a "|", depending on the modifier used.
    """
    token = "token"

    """ A reference to another resource (Reference or canonical).
    """
    reference = "reference"

    """ A composite search parameter that combines a search on two values together.
    """
    composite = "composite"

    """ A search parameter that searches on a quantity.
    """
    quantity = "quantity"

    """ A search parameter that searches on a URI (RFC 3986).
    """
    uri = "uri"


class SecurityRoleType(CodeSystemValue):
    """ This CodeSystem contains Additional FHIR-defined Security Role types not defined elsewhere

    URL: http://hl7.org/fhir/extra-security-role-type
    """
    URL = "http://hl7.org/fhir/extra-security-role-type"
    EXPERIMENTAL = True

    """ An entity providing authorization services to enable the electronic sharing of health-related information based
	/// on resource owner's preapproved permissions. For example, an UMA Authorization Server[UMA]
    """
    authserver = "authserver"

    """ An entity that collects information over which the data subject may have certain rights under policy or law to
	/// control that information's management and distribution by data collectors, including the right to access,
	/// retrieve, distribute, or delete that information.
    """
    datacollector = "datacollector"

    """ An entity that processes collected information over which the data subject may have certain rights under policy
	/// or law to control that information's management and distribution by data processors, including the right to
	/// access, retrieve, distribute, or delete that information.
    """
    dataprocessor = "dataprocessor"

    """ A person whose personal information is collected or processed, and who may have certain rights under policy or
	/// law to control that information's management and distribution by data collectors or processors, including the
	/// right to access, retrieve, distribute, or delete that information.
    """
    datasubject = "datasubject"

    """ The human user that has participated.
    """
    humanuser = "humanuser"


class SequenceStatus(CodeSystemValue):
    """ Codes providing the status of the variant test result

    URL: http://hl7.org/fhir/variant-state
    ValueSet: http://hl7.org/fhir/ValueSet/variant-state
    """
    URL = "http://hl7.org/fhir/variant-state"
    EXPERIMENTAL = False

    """ the variant is detected
    """
    positive = "positive"

    """ no variant is detected
    """
    negative = "negative"

    """ result of the variant is missing
    """
    absent = "absent"


class SequenceType(CodeSystemValue):
    """ Type if a sequence -- DNA, RNA, or amino acid sequence

    URL: http://hl7.org/fhir/sequence-type
    ValueSet: http://hl7.org/fhir/ValueSet/sequence-type
    """
    URL = "http://hl7.org/fhir/sequence-type"
    EXPERIMENTAL = False

    """ Amino acid sequence
    """
    aa = "aa"

    """ DNA Sequence
    """
    dna = "dna"

    """ RNA Sequence
    """
    rna = "rna"


class ServiceProvisionConditions(CodeSystemValue):
    """ The code(s) that detail the conditions under which the healthcare service is available/offered.

    URL: http://hl7.org/fhir/service-provision-conditions
    ValueSet: http://hl7.org/fhir/ValueSet/service-provision-conditions
    """
    URL = "http://hl7.org/fhir/service-provision-conditions"
    EXPERIMENTAL = False

    """ This service is available for no patient cost.
    """
    free = "free"

    """ There are discounts available on this service for qualifying patients.
    """
    disc = "disc"

    """ Fees apply for this service.
    """
    cost = "cost"


class SlicingRules(CodeSystemValue):
    """ How slices are interpreted when evaluating an instance.

    URL: http://hl7.org/fhir/resource-slicing-rules
    ValueSet: http://hl7.org/fhir/ValueSet/resource-slicing-rules
    """
    URL = "http://hl7.org/fhir/resource-slicing-rules"
    EXPERIMENTAL = False

    """ No additional content is allowed other than that described by the slices in this profile.
    """
    closed = "closed"

    """ Additional content is allowed anywhere in the list.
    """
    open = "open"

    """ Additional content is allowed, but only at the end of the list. Note that using this requires that the slices be
	/// ordered, which makes it hard to share uses. This should only be done where absolutely required.
    """
    openAtEnd = "openAtEnd"


class SlotStatus(CodeSystemValue):
    """ The free/busy status of the slot.

    URL: http://hl7.org/fhir/slotstatus
    ValueSet: http://hl7.org/fhir/ValueSet/slotstatus
    """
    URL = "http://hl7.org/fhir/slotstatus"
    EXPERIMENTAL = False

    """ Indicates that the time interval is busy because one  or more events have been scheduled for that interval.
    """
    busy = "busy"

    """ Indicates that the time interval is free for scheduling.
    """
    free = "free"

    """ Indicates that the time interval is busy and that the interval cannot be scheduled.
    """
    busyUnavailable = "busy-unavailable"

    """ Indicates that the time interval is busy because one or more events have been tentatively scheduled for that
	/// interval.
    """
    busyTentative = "busy-tentative"

    """ This instance should not have been part of this patient's medical record.
    """
    enteredInError = "entered-in-error"


class SmartCapabilities(CodeSystemValue):
    """ Codes that define what the server is capable of

    URL: http://hl7.org/fhir/smart-capabilities
    ValueSet: http://hl7.org/fhir/ValueSet/smart-capabilities
    """
    URL = "http://hl7.org/fhir/smart-capabilities"
    EXPERIMENTAL = False

    """ support for SMART’s EHR Launch mode
    """
    launchEhr = "launch-ehr"

    """ support for SMART’s Standalone Launch mode
    """
    launchStandalone = "launch-standalone"

    """ support for SMART’s public client profile (no client authentication)
    """
    clientPublic = "client-public"

    """ support for SMART’s confidential client profile (symmetric client secret authentication)
    """
    clientConfidentialSymmetric = "client-confidential-symmetric"

    """ support for SMART’s OpenID Connect profile
    """
    ssoOpenidConnect = "sso-openid-connect"

    """ support for “need patient banner” launch context (conveyed via need_patient_banner token parameter)
    """
    contextPassthroughBanner = "context-passthrough-banner"

    """ support for “SMART style URL” launch context (conveyed via smart_style_url token parameter)
    """
    contextPassthroughStyle = "context-passthrough-style"

    """ support for patient-level launch context (requested by launch/patient scope, conveyed via patient token
	/// parameter)
    """
    contextEhrPatient = "context-ehr-patient"

    """ support for encounter-level launch context (requested by launch/encounter scope, conveyed via encounter token
	/// parameter)
    """
    contextEhrEncounter = "context-ehr-encounter"

    """ support for patient-level launch context (requested by launch/patient scope, conveyed via patient token
	/// parameter)
    """
    contextStandalonePatient = "context-standalone-patient"

    """ support for encounter-level launch context (requested by launch/encounter scope, conveyed via encounter token
	/// parameter)
    """
    contextStandaloneEncounter = "context-standalone-encounter"

    """ support for refresh tokens (requested by offline_access scope)
    """
    permissionOffline = "permission-offline"

    """ support for patient-level scopes (e.g. patient/Observation.read)
    """
    permissionPatient = "permission-patient"

    """ support for user-level scopes (e.g. user/Appointment.read)
    """
    permissionUser = "permission-user"


class SortDirection(CodeSystemValue):
    """ The possible sort directions, ascending or descending

    URL: http://hl7.org/fhir/sort-direction
    ValueSet: http://hl7.org/fhir/ValueSet/sort-direction
    """
    URL = "http://hl7.org/fhir/sort-direction"
    EXPERIMENTAL = False

    """ Sort by the value ascending, so that lower values appear first
    """
    ascending = "ascending"

    """ Sort by the value descending, so that lower values appear last
    """
    descending = "descending"


class SpecialArrangements(CodeSystemValue):
    """ This value set defines a set of codes that can be used to indicate the kinds of special arrangements in place for a
patients visit.

    URL: http://hl7.org/fhir/encounter-special-arrangements
    ValueSet: http://hl7.org/fhir/ValueSet/encounter-special-arrangements
    """
    URL = "http://hl7.org/fhir/encounter-special-arrangements"
    EXPERIMENTAL = True

    """ The patient requires a wheelchair to be made available for the encounter.
    """
    wheel = "wheel"

    """ An additional bed made available for a person accompanying the patient, for example a parent accompanying a
	/// child.
    """
    addBed = "add-bed"

    """ The patient is not fluent in the local language and requires an interpreter to be available. Refer to the
	/// Patient.Language property for the type of interpreter required.
    """
    int = "int"

    """ A person who accompanies a patient to provide assistive services necessary for the patient's care during the
	/// encounter.
    """
    att = "att"

    """ The patient has a guide-dog and the location used for the encounter should be able to support the presence of
	/// the service animal.
    """
    dog = "dog"


class SpecialValues(CodeSystemValue):
    """ A set of generally useful codes defined so they can be included in value sets.

    URL: http://hl7.org/fhir/special-values
    ValueSet: http://hl7.org/fhir/ValueSet/special-values
    """
    URL = "http://hl7.org/fhir/special-values"
    EXPERIMENTAL = False

    """ Boolean true.
    """
    true = "true"

    """ Boolean false.
    """
    false = "false"

    """ The content is greater than zero, but too small to be quantified.
    """
    trace = "trace"

    """ The specific quantity is not known, but is known to be non-zero and is not specified because it makes up the
	/// bulk of the material.
    """
    sufficient = "sufficient"

    """ The value is no longer available.
    """
    withdrawn = "withdrawn"

    """ The are no known applicable values in this context.
    """
    nilKnown = "nil-known"


class SpecimenContainedPreference(CodeSystemValue):
    """ Degree of preference of a type of conditioned specimen

    URL: http://hl7.org/fhir/specimen-contained-preference
    ValueSet: http://hl7.org/fhir/ValueSet/specimen-contained-preference
    """
    URL = "http://hl7.org/fhir/specimen-contained-preference"
    EXPERIMENTAL = False

    """ This type of contained specimen is preferred to collect this kind of specimen
    """
    preferred = "preferred"

    """ This type of conditioned specimen is an alternate
    """
    alternate = "alternate"


class SpecimenStatus(CodeSystemValue):
    """ Codes providing the status/availability of a specimen.

    URL: http://hl7.org/fhir/specimen-status
    ValueSet: http://hl7.org/fhir/ValueSet/specimen-status
    """
    URL = "http://hl7.org/fhir/specimen-status"
    EXPERIMENTAL = False

    """ The physical specimen is present and in good condition.
    """
    available = "available"

    """ There is no physical specimen because it is either lost, destroyed or consumed.
    """
    unavailable = "unavailable"

    """ The specimen cannot be used because of a quality issue such as a broken container, contamination, or too old.
    """
    unsatisfactory = "unsatisfactory"

    """ The specimen was entered in error and therefore nullified.
    """
    enteredInError = "entered-in-error"


class Status(CodeSystemValue):
    """ The validation status of the target

    URL: http://hl7.org/fhir/status
    ValueSet: http://hl7.org/fhir/ValueSet/status
    """
    URL = "http://hl7.org/fhir/status"
    EXPERIMENTAL = False

    """ attested
    """
    attested = "attested"

    """ validated
    """
    validated = "validated"

    """ inProcess
    """
    inProcess = "in-process"

    """ reqRevalid
    """
    reqRevalid = "req-revalid"

    """ valFail
    """
    valFail = "val-fail"

    """ revalFail
    """
    revalFail = "reval-fail"


class StrandType(CodeSystemValue):
    """ Type for strand

    URL: http://hl7.org/fhir/strand-type
    ValueSet: http://hl7.org/fhir/ValueSet/strand-type
    """
    URL = "http://hl7.org/fhir/strand-type"
    EXPERIMENTAL = False

    """ Watson strand of reference sequence
    """
    watson = "watson"

    """ Crick strand of reference sequence
    """
    crick = "crick"


class StrengthOfRecommendationRating(CodeSystemValue):
    """ A rating system that describes the strength of the recommendation, such as the GRADE, DynaMed, or HGPS systems

    URL: http://hl7.org/fhir/recommendation-strength
    ValueSet: http://hl7.org/fhir/ValueSet/recommendation-strength
    """
    URL = "http://hl7.org/fhir/recommendation-strength"
    EXPERIMENTAL = False

    """ Strong recommendation
    """
    strong = "strong"

    """ Weak recommendation
    """
    weak = "weak"


class StructureDefinitionKind(CodeSystemValue):
    """ Defines the type of structure that a definition is describing.

    URL: http://hl7.org/fhir/structure-definition-kind
    ValueSet: http://hl7.org/fhir/ValueSet/structure-definition-kind
    """
    URL = "http://hl7.org/fhir/structure-definition-kind"
    EXPERIMENTAL = False

    """ A primitive type that has a value and an extension. These can be used throughout Resource and extension
	/// definitions. Only the base specification can define primitive types.
    """
    primitiveType = "primitive-type"

    """ A  complex structure that defines a set of data elements. These can be used throughout Resource and extension
	/// definitions, and in logical models.
    """
    complexType = "complex-type"

    """ A resource defined by the FHIR specification.
    """
    resource = "resource"

    """ A conceptual package of data that will be mapped to resources for implementation.
    """
    logical = "logical"


class StructureMapContextType(CodeSystemValue):
    """ How to interpret the context

    URL: http://hl7.org/fhir/map-context-type
    ValueSet: http://hl7.org/fhir/ValueSet/map-context-type
    """
    URL = "http://hl7.org/fhir/map-context-type"
    EXPERIMENTAL = False

    """ The context specifies a type
    """
    type = "type"

    """ The context specifies a variable
    """
    variable = "variable"


class StructureMapGroupTypeMode(CodeSystemValue):
    """ If this is the default rule set to apply for the source type, or this combination of types

    URL: http://hl7.org/fhir/map-group-type-mode
    ValueSet: http://hl7.org/fhir/ValueSet/map-group-type-mode
    """
    URL = "http://hl7.org/fhir/map-group-type-mode"
    EXPERIMENTAL = False

    """ This group is not a default group for the types
    """
    none = "none"

    """ This group is a default mapping group for the specified types and for the primary source type
    """
    types = "types"

    """ This group is a default mapping group for the specified types
    """
    typeAndTypes = "type-and-types"


class StructureMapInputMode(CodeSystemValue):
    """ Mode for this instance of data

    URL: http://hl7.org/fhir/map-input-mode
    ValueSet: http://hl7.org/fhir/ValueSet/map-input-mode
    """
    URL = "http://hl7.org/fhir/map-input-mode"
    EXPERIMENTAL = False

    """ Names an input instance used a source for mapping
    """
    source = "source"

    """ Names an instance that is being populated
    """
    target = "target"


class StructureMapModelMode(CodeSystemValue):
    """ How the referenced structure is used in this mapping

    URL: http://hl7.org/fhir/map-model-mode
    ValueSet: http://hl7.org/fhir/ValueSet/map-model-mode
    """
    URL = "http://hl7.org/fhir/map-model-mode"
    EXPERIMENTAL = False

    """ This structure describes an instance passed to the mapping engine that is used a source of data
    """
    source = "source"

    """ This structure describes an instance that the mapping engine may ask for that is used a source of data
    """
    queried = "queried"

    """ This structure describes an instance passed to the mapping engine that is used a target of data
    """
    target = "target"

    """ This structure describes an instance that the mapping engine may ask to create that is used a target of data
    """
    produced = "produced"


class StructureMapSourceListMode(CodeSystemValue):
    """ If field is a list, how to manage the source

    URL: http://hl7.org/fhir/map-source-list-mode
    ValueSet: http://hl7.org/fhir/ValueSet/map-source-list-mode
    """
    URL = "http://hl7.org/fhir/map-source-list-mode"
    EXPERIMENTAL = False

    """ Only process this rule for the first in the list
    """
    first = "first"

    """ Process this rule for all but the first
    """
    not_first = "not_first"

    """ Only process this rule for the last in the list
    """
    last = "last"

    """ Process this rule for all but the last
    """
    not_last = "not_last"

    """ Only process this rule is there is only item
    """
    only_one = "only_one"


class StructureMapTargetListMode(CodeSystemValue):
    """ If field is a list, how to manage the production

    URL: http://hl7.org/fhir/map-target-list-mode
    ValueSet: http://hl7.org/fhir/ValueSet/map-target-list-mode
    """
    URL = "http://hl7.org/fhir/map-target-list-mode"
    EXPERIMENTAL = False

    """ when the target list is being assembled, the items for this rule go first. If more than one rule defines a first
	/// item (for a given instance of mapping) then this is an error
    """
    first = "first"

    """ the target instance is shared with the target instances generated by another rule (up to the first common n
	/// items, then create new ones)
    """
    share = "share"

    """ when the target list is being assembled, the items for this rule go last. If more than one rule defines a last
	/// item (for a given instance of mapping) then this is an error
    """
    last = "last"

    """ re-use the first item in the list, and keep adding content to it
    """
    collate = "collate"


class StructureMapTransform(CodeSystemValue):
    """ How data is copied/created

    URL: http://hl7.org/fhir/map-transform
    ValueSet: http://hl7.org/fhir/ValueSet/map-transform
    """
    URL = "http://hl7.org/fhir/map-transform"
    EXPERIMENTAL = False

    """ create(type : string) - type is passed through to the application on the standard API, and must be known by it
    """
    create = "create"

    """ copy(source)
    """
    copy = "copy"

    """ truncate(source, length) - source must be stringy type
    """
    truncate = "truncate"

    """ escape(source, fmt1, fmt2) - change source from one kind of escaping to another (plain, java, xml, json). note
	/// that this is for when the string itself is escaped
    """
    escape = "escape"

    """ cast(source, type?) - case source from one type to another. target type can be left as implicit if there is one
	/// and only one target type known
    """
    cast = "cast"

    """ append(source...) - source is element or string
    """
    append = "append"

    """ translate(source, uri_of_map) - use the translate operation
    """
    translate = "translate"

    """ reference(source : object) - return a string that references the provided tree properly
    """
    reference = "reference"

    """ Perform a date operation. *Parameters to be documented*
    """
    dateOp = "dateOp"

    """ Generate a random UUID (in lowercase). No Parameters
    """
    uuid = "uuid"

    """ Return the appropriate string to put in a reference that refers to the resource provided as a parameter
    """
    pointer = "pointer"

    """ Execute the supplied FHIRPath expression and use the value returned by that
    """
    evaluate = "evaluate"

    """ Create a CodeableConcept. Parameters = (text) or (system. Code[, display])
    """
    cc = "cc"

    """ Create a Coding. Parameters = (system. Code[, display])
    """
    C = "c"

    """ Create a quantity. Parameters = (text) or (value, unit, [system, code]) where text is the natural representation
	/// e.g. [comparator]value[space]unit
    """
    qty = "qty"

    """ Create an identifier. Parameters = (system, value[, type]) where type is a code from the identifier type value
	/// set
    """
    id = "id"

    """ Create a contact details. Parameters = (value) or (system, value). If no system is provided, the system should
	/// be inferred from the content of the value
    """
    cp = "cp"


class SubscriptionChannelType(CodeSystemValue):
    """ The type of method used to execute a subscription.

    URL: http://hl7.org/fhir/subscription-channel-type
    ValueSet: http://hl7.org/fhir/ValueSet/subscription-channel-type
    """
    URL = "http://hl7.org/fhir/subscription-channel-type"
    EXPERIMENTAL = False

    """ The channel is executed by making a post to the URI. If a payload is included, the URL is interpreted as the
	/// service base, and an update (PUT) is made.
    """
    restHook = "rest-hook"

    """ The channel is executed by sending a packet across a web socket connection maintained by the client. The URL
	/// identifies the websocket, and the client binds to this URL.
    """
    websocket = "websocket"

    """ The channel is executed by sending an email to the email addressed in the URI (which must be a mailto:).
    """
    email = "email"

    """ The channel is executed by sending an SMS message to the phone number identified in the URL (tel:).
    """
    sms = "sms"

    """ The channel is executed by sending a message (e.g. a Bundle with a MessageHeader resource etc.) to the
	/// application identified in the URI.
    """
    message = "message"


class SubscriptionStatus(CodeSystemValue):
    """ The status of a subscription.

    URL: http://hl7.org/fhir/subscription-status
    ValueSet: http://hl7.org/fhir/ValueSet/subscription-status
    """
    URL = "http://hl7.org/fhir/subscription-status"
    EXPERIMENTAL = False

    """ The client has requested the subscription, and the server has not yet set it up.
    """
    requested = "requested"

    """ The subscription is active.
    """
    active = "active"

    """ The server has an error executing the notification.
    """
    error = "error"

    """ Too many errors have occurred or the subscription has expired.
    """
    off = "off"


class SubscriptionTag(CodeSystemValue):
    """ Tags to put on a resource after subscriptions have been sent.

    URL: http://hl7.org/fhir/subscription-tag
    ValueSet: http://hl7.org/fhir/ValueSet/subscription-tag
    """
    URL = "http://hl7.org/fhir/subscription-tag"
    EXPERIMENTAL = False

    """ The message has been queued for processing on a destination systems.
    """
    queued = "queued"

    """ The message has been delivered to its intended recipient.
    """
    delivered = "delivered"


class SubstanceCategoryCodes(CodeSystemValue):
    """ Substance category codes

    URL: http://hl7.org/fhir/substance-category
    ValueSet: http://hl7.org/fhir/ValueSet/substance-category
    """
    URL = "http://hl7.org/fhir/substance-category"
    EXPERIMENTAL = True

    """ A substance that causes an allergic reaction.
    """
    allergen = "allergen"

    """ A substance that is produced by or extracted from a biological source.
    """
    biological = "biological"

    """ A substance that comes directly from a human or an animal (e.g. blood, urine, feces, tears, etc.).
    """
    body = "body"

    """ Any organic or inorganic substance of a particular molecular identity, including -- (i) any combination of such
	/// substances occurring in whole or in part as a result of a chemical reaction or occurring in nature and (ii) any
	/// element or uncombined radical (http://www.epa.gov/opptintr/import-export/pubs/importguide.pdf).
    """
    chemical = "chemical"

    """ A food, dietary ingredient, or dietary supplement for human or animal.
    """
    food = "food"

    """ A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease in man or
	/// other animals (Federal Food Drug and Cosmetic Act).
    """
    drug = "drug"

    """ A finished product which is not normally ingested, absorbed or injected (e.g. steel, iron, wood, plastic and
	/// paper).
    """
    material = "material"


class SupplyDeliveryStatus(CodeSystemValue):
    """ Status of the supply delivery.

    URL: http://hl7.org/fhir/supplydelivery-status
    ValueSet: http://hl7.org/fhir/ValueSet/supplydelivery-status
    """
    URL = "http://hl7.org/fhir/supplydelivery-status"
    EXPERIMENTAL = False

    """ Supply has been requested, but not delivered.
    """
    inProgress = "in-progress"

    """ Supply has been delivered ("completed").
    """
    completed = "completed"

    """ Delivery was not completed.
    """
    abandoned = "abandoned"

    """ This electronic record should never have existed, though it is possible that real-world decisions were based on
	/// it. (If real-world activity has occurred, the status should be "cancelled" rather than "entered-in-error".)
    """
    enteredInError = "entered-in-error"


class SupplyItemType(CodeSystemValue):
    """ This value sets refers to a specific supply item.

    URL: http://hl7.org/fhir/supply-item-type
    ValueSet: http://hl7.org/fhir/ValueSet/supplydelivery-type
    """
    URL = "http://hl7.org/fhir/supply-item-type"
    EXPERIMENTAL = True

    """ Supply is a kind of medication.
    """
    medication = "medication"

    """ What is supplied (or requested) is a device.
    """
    device = "device"


class SupplyRequestReason(CodeSystemValue):
    """ The reason why the supply item was requested

    URL: http://hl7.org/fhir/supplyrequest-reason
    ValueSet: http://hl7.org/fhir/ValueSet/supplyrequest-reason
    """
    URL = "http://hl7.org/fhir/supplyrequest-reason"
    EXPERIMENTAL = False

    """ The supply has been requested for use in direct patient care.
    """
    patientCare = "patient-care"

    """ The supply has been requested for creating or replenishing ward stock.
    """
    wardStock = "ward-stock"


class SupplyRequestStatus(CodeSystemValue):
    """ Status of the supply request

    URL: http://hl7.org/fhir/supplyrequest-status
    ValueSet: http://hl7.org/fhir/ValueSet/supplyrequest-status
    """
    URL = "http://hl7.org/fhir/supplyrequest-status"
    EXPERIMENTAL = False

    """ The request has been created but is not yet complete or ready for action
    """
    draft = "draft"

    """ The request is ready to be acted upon
    """
    active = "active"

    """ The authorization/request to act has been temporarily withdrawn but is expected to resume in the future
    """
    suspended = "suspended"

    """ The authorization/request to act has been terminated prior to the full completion of the intended actions.  No
	/// further activity should occur.
    """
    cancelled = "cancelled"

    """ Activity against the request has been sufficiently completed to the satisfaction of the requester
    """
    completed = "completed"

    """ This electronic record should never have existed, though it is possible that real-world decisions were based on
	/// it.  (If real-world activity has occurred, the status should be "cancelled" rather than "entered-in-error".)
    """
    enteredInError = "entered-in-error"

    """ The authoring system does not know which of the status values currently applies for this request.  Note: This
	/// concept is not to be used for "other" - one of the listed statuses is presumed to apply, it's just not known
	/// which one.
    """
    unknown = "unknown"


class SupplyType(CodeSystemValue):
    """ This value sets refers to a Category of supply.

    URL: http://hl7.org/fhir/supply-kind
    ValueSet: http://hl7.org/fhir/ValueSet/supplyrequest-kind
    """
    URL = "http://hl7.org/fhir/supply-kind"
    EXPERIMENTAL = True

    """ Supply is stored and requested from central supply.
    """
    central = "central"

    """ Supply is not onsite and must be requested from an outside vendor using a non-stock requisition.
    """
    nonstock = "nonstock"


class SurfaceCodes(CodeSystemValue):
    """ This value set includes a smattering of FDI tooth surface codes.

    URL: http://hl7.org/fhir/FDI-surface
    ValueSet: http://hl7.org/fhir/ValueSet/surface
    """
    URL = "http://hl7.org/fhir/FDI-surface"
    EXPERIMENTAL = True

    """ The surface of a tooth that is closest to the midline (middle) of the face.
    """
    M = "M"

    """ The chewing surface of posterior teeth.
    """
    O = "O"

    """ The biting edge of anterior teeth.
    """
    I = "I"

    """ The surface of a tooth that faces away from the midline of the face.
    """
    D = "D"

    """ The surface of a posterior tooth facing the cheeks.
    """
    B = "B"

    """ The surface of a tooth facing the lips.
    """
    V = "V"

    """ The surface of a tooth facing the tongue.
    """
    L = "L"

    """ The Mesioclusal surfaces of a tooth.
    """
    MO = "MO"

    """ The Distoclusal surfaces of a tooth.
    """
    DO = "DO"

    """ The Distoincisal surfaces of a tooth.
    """
    DI = "DI"

    """ The Mesioclusodistal surfaces of a tooth.
    """
    MOD = "MOD"


class SystemVersionProcessingMode(CodeSystemValue):
    """ How to manage the intersection between a fixed version in a value set, and a fixed version of the system in the
expansion profile

    URL: http://hl7.org/fhir/system-version-processing-mode
    ValueSet: http://hl7.org/fhir/ValueSet/system-version-processing-mode
    """
    URL = "http://hl7.org/fhir/system-version-processing-mode"
    EXPERIMENTAL = False

    """ Use this version of the code system if a value set doesn't specify a version
    """
    default = "default"

    """ Use this version of the code system. If a value set specifies a different version, the expansion operation
	/// should fail
    """
    check = "check"

    """ Use this version of the code system irrespective of which version is specified by a value set. Note that this
	/// has obvious safety issues, in that it may result in a value set expansion giving a different list of codes that
	/// is both wrong and unsafe, and implementers should only use this capability reluctantly. It primarily exists to
	/// deal with situations where specifications have fallen into decay as time passes. If the value is override, the
	/// version used SHALL explicitly be represented in the expansion parameters
    """
    override = "override"


class TaskPerformerType(CodeSystemValue):
    """ The type(s) of task performers allowed

    URL: http://hl7.org/fhir/task-performer-type
    ValueSet: http://hl7.org/fhir/ValueSet/task-performer-type
    """
    URL = "http://hl7.org/fhir/task-performer-type"
    EXPERIMENTAL = False

    """ A workflow participant that requests services.
    """
    requester = "requester"

    """ A workflow participant that dispatches services (assigns another task to a participant).
    """
    dispatcher = "dispatcher"

    """ A workflow participant that schedules (dispatches and sets the time or date for performance of) services.
    """
    scheduler = "scheduler"

    """ A workflow participant that performs services.
    """
    performer = "performer"

    """ A workflow participant that monitors task activity.
    """
    monitor = "monitor"

    """ A workflow participant that manages task activity.
    """
    manager = "manager"

    """ A workflow participant that acquires resources (specimens, images, etc.) necessary to perform the task.
    """
    acquirer = "acquirer"

    """ A workflow participant that reviews task inputs or outputs.
    """
    reviewer = "reviewer"


class TaskStatus(CodeSystemValue):
    """ The current status of the task.

    URL: http://hl7.org/fhir/task-status
    ValueSet: http://hl7.org/fhir/ValueSet/task-status
    """
    URL = "http://hl7.org/fhir/task-status"
    EXPERIMENTAL = False

    """ The task is not yet ready to be acted upon.
    """
    draft = "draft"

    """ The task is ready to be acted upon and action is sought.
    """
    requested = "requested"

    """ A potential performer has claimed ownership of the task and is evaluating whether to perform it.
    """
    received = "received"

    """ The potential performer has agreed to execute the task but has not yet started work.
    """
    accepted = "accepted"

    """ The potential performer who claimed ownership of the task has decided not to execute it prior to performing any
	/// action.
    """
    rejected = "rejected"

    """ The task is ready to be performed, but no action has yet been taken.  Used in place of
	/// requested/received/accepted/rejected when request assignment and acceptance is a given.
    """
    ready = "ready"

    """ The task was not completed.
    """
    cancelled = "cancelled"

    """ The task has been started but is not yet complete.
    """
    inProgress = "in-progress"

    """ The task has been started but work has been paused.
    """
    onHold = "on-hold"

    """ The task was attempted but could not be completed due to some error.
    """
    failed = "failed"

    """ The task has been completed.
    """
    completed = "completed"

    """ The task should never have existed and is retained only because of the possibility it may have used.
    """
    enteredInError = "entered-in-error"


class TestReportActionResult(CodeSystemValue):
    """ The results of executing an action.

    URL: http://hl7.org/fhir/report-action-result-codes
    ValueSet: http://hl7.org/fhir/ValueSet/report-action-result-codes
    """
    URL = "http://hl7.org/fhir/report-action-result-codes"
    EXPERIMENTAL = False

    """ The action was successful.
    """
    _pass = "pass"

    """ The action was skipped.
    """
    skip = "skip"

    """ The action failed.
    """
    fail = "fail"

    """ The action passed but with warnings.
    """
    warning = "warning"

    """ The action encountered a fatal error and the engine was unable to process.
    """
    error = "error"


class TestReportParticipantType(CodeSystemValue):
    """ The type of participant.

    URL: http://hl7.org/fhir/report-participant-type
    ValueSet: http://hl7.org/fhir/ValueSet/report-participant-type
    """
    URL = "http://hl7.org/fhir/report-participant-type"
    EXPERIMENTAL = False

    """ The test execution engine.
    """
    testEngine = "test-engine"

    """ A FHIR Client
    """
    client = "client"

    """ A FHIR Server
    """
    server = "server"


class TestReportResult(CodeSystemValue):
    """ The reported execution result.

    URL: http://hl7.org/fhir/report-result-codes
    ValueSet: http://hl7.org/fhir/ValueSet/report-result-codes
    """
    URL = "http://hl7.org/fhir/report-result-codes"
    EXPERIMENTAL = False

    """ All test operations successfully passed all asserts
    """
    _pass = "pass"

    """ One or more test operations failed one or more asserts
    """
    fail = "fail"

    """ One or more test operations is pending execution completion
    """
    pending = "pending"


class TestReportStatus(CodeSystemValue):
    """ The current status of the test report.

    URL: http://hl7.org/fhir/report-status-codes
    ValueSet: http://hl7.org/fhir/ValueSet/report-status-codes
    """
    URL = "http://hl7.org/fhir/report-status-codes"
    EXPERIMENTAL = False

    """ All test operations have completed
    """
    completed = "completed"

    """ A test operations is currently executing
    """
    inProgress = "in-progress"

    """ A test operation is waiting for an external client request
    """
    waiting = "waiting"

    """ The test script execution was manually stopped
    """
    stopped = "stopped"

    """ This test report was entered or created in error
    """
    enteredInError = "entered-in-error"


class TestScriptOperationCode(CodeSystemValue):
    """ This value set defines a set of codes that are used to indicate the supported operations of a testing engine or tool.

    URL: http://hl7.org/fhir/testscript-operation-codes
    ValueSet: http://hl7.org/fhir/ValueSet/testscript-operation-codes
    """
    URL = "http://hl7.org/fhir/testscript-operation-codes"
    EXPERIMENTAL = True

    """ Read the current state of the resource.
    """
    read = "read"

    """ Read the state of a specific version of the resource.
    """
    vread = "vread"

    """ Update an existing resource by its id.
    """
    update = "update"

    """ Update an existing resource by its id (or create it if it is new).
    """
    updateCreate = "updateCreate"

    """ Patch an existing resource by its id.
    """
    patch = "patch"

    """ Delete a resource.
    """
    delete = "delete"

    """ Conditionally delete a single resource based on search parameters.
    """
    deleteCondSingle = "deleteCondSingle"

    """ Conditionally delete one or more resources based on search parameters.
    """
    deleteCondMultiple = "deleteCondMultiple"

    """ Retrieve the change history for a particular resource or resource type.
    """
    history = "history"

    """ Create a new resource with a server assigned id.
    """
    create = "create"

    """ Search based on some filter criteria.
    """
    search = "search"

    """ Update, create or delete a set of resources as independent actions.
    """
    batch = "batch"

    """ Update, create or delete a set of resources as a single transaction.
    """
    transaction = "transaction"

    """ Get a capability statement for the system.
    """
    capabilities = "capabilities"

    """ Realizes an ActivityDefinition in a specific context
    """
    apply = "apply"

    """ Closure Table Maintenance
    """
    closure = "closure"

    """ Code Composition based on supplied properties
    """
    compose = "compose"

    """ Compare two systems CapabilityStatements
    """
    conforms = "conforms"

    """ Aggregates and returns the parameters and data requirements for a resource and all its dependencies as a single
	/// module definition
    """
    dataRequirements = "data-requirements"

    """ Generate a Document
    """
    document = "document"

    """ Request clinical decision support guidance based on a specific decision support module
    """
    evaluate = "evaluate"

    """ Invoke an eMeasure and obtain the results
    """
    evaluateMeasure = "evaluate-measure"

    """ Return all the related information as described in the Encounter or Patient
    """
    everything = "everything"

    """ Value Set Expansion
    """
    expand = "expand"

    """ Find a functional list
    """
    find = "find"

    """ Invoke a GraphQL query
    """
    graphql = "graphql"

    """ Test if a server implements a client's required operations
    """
    implements = "implements"

    """ Last N Observations Query
    """
    lastn = "lastn"

    """ Concept Look Up and Decomposition
    """
    lookup = "lookup"

    """ Find patient matches using MPI based logic
    """
    match = "match"

    """ Access a list of profiles, tags, and security labels
    """
    meta = "meta"

    """ Add profiles, tags, and security labels to a resource
    """
    metaAdd = "meta-add"

    """ Delete profiles, tags, and security labels for a resource
    """
    metaDelete = "meta-delete"

    """ Populate Questionnaire
    """
    populate = "populate"

    """ Generate HTML for Questionnaire
    """
    populatehtml = "populatehtml"

    """ Generate a link to a Questionnaire completion webpage
    """
    populatelink = "populatelink"

    """ Process a message according to the defined event
    """
    processMessage = "process-message"

    """ Build Questionnaire
    """
    questionnaire = "questionnaire"

    """ Observation Statistics
    """
    stats = "stats"

    """ Fetch a subset of the CapabilityStatement resource
    """
    subset = "subset"

    """ CodeSystem Subsumption Testing
    """
    subsumes = "subsumes"

    """ Model Instance Transformation
    """
    transform = "transform"

    """ Concept Translation
    """
    translate = "translate"

    """ Validate a resource
    """
    validate = "validate"

    """ ValueSet based Validation
    """
    validateCode = "validate-code"


class TestScriptProfileDestinationType(CodeSystemValue):
    """ This value set defines a set of codes that are used to indicate the profile type of a test system when acting as the
destination within a TestScript.

    URL: http://hl7.org/fhir/testscript-profile-destination-types
    ValueSet: http://hl7.org/fhir/ValueSet/testscript-profile-destination-types
    """
    URL = "http://hl7.org/fhir/testscript-profile-destination-types"
    EXPERIMENTAL = True

    """ General FHIR server used to respond to operations sent from a FHIR client.
    """
    fHIRServer = "FHIR-Server"

    """ A FHIR server acting as a Structured Data Capture Form Manager.
    """
    fHIRSDCFormManager = "FHIR-SDC-FormManager"

    """ A FHIR server acting as a Structured Data Capture Form Processor.
    """
    fHIRSDCFormProcessor = "FHIR-SDC-FormProcessor"

    """ A FHIR server acting as a Structured Data Capture Form Receiver.
    """
    fHIRSDCFormReceiver = "FHIR-SDC-FormReceiver"


class TestScriptProfileOriginType(CodeSystemValue):
    """ This value set defines a set of codes that are used to indicate the profile type of a test system when acting as the
origin within a TestScript.

    URL: http://hl7.org/fhir/testscript-profile-origin-types
    ValueSet: http://hl7.org/fhir/ValueSet/testscript-profile-origin-types
    """
    URL = "http://hl7.org/fhir/testscript-profile-origin-types"
    EXPERIMENTAL = True

    """ General FHIR client used to initiate operations against a FHIR server.
    """
    fHIRClient = "FHIR-Client"

    """ A FHIR client acting as a Structured Data Capture Form Filler.
    """
    fHIRSDCFormFiller = "FHIR-SDC-FormFiller"


class TestScriptRequestMethodCode(CodeSystemValue):
    """ The allowable request method or HTTP operation codes.

    URL: http://hl7.org/fhir/http-operations
    ValueSet: http://hl7.org/fhir/ValueSet/http-operations
    """
    URL = "http://hl7.org/fhir/http-operations"
    EXPERIMENTAL = False

    """ HTTP DELETE operation
    """
    delete = "delete"

    """ HTTP GET operation
    """
    get = "get"

    """ HTTP OPTIONS operation
    """
    options = "options"

    """ HTTP PATCH operation
    """
    patch = "patch"

    """ HTTP POST operation
    """
    post = "post"

    """ HTTP PUT operation
    """
    put = "put"


class TransactionMode(CodeSystemValue):
    """ A code that indicates how transactions are supported.

    URL: http://hl7.org/fhir/transaction-mode
    ValueSet: http://hl7.org/fhir/ValueSet/transaction-mode
    """
    URL = "http://hl7.org/fhir/transaction-mode"
    EXPERIMENTAL = False

    """ Neither batch or transaction is supported.
    """
    notSupported = "not-supported"

    """ Batches are  supported.
    """
    batch = "batch"

    """ Transactions are supported.
    """
    transaction = "transaction"

    """ Both batches and transactions are supported.
    """
    both = "both"


class TriggerType(CodeSystemValue):
    """ The type of trigger

    URL: http://hl7.org/fhir/trigger-type
    ValueSet: http://hl7.org/fhir/ValueSet/trigger-type
    """
    URL = "http://hl7.org/fhir/trigger-type"
    EXPERIMENTAL = False

    """ The trigger occurs in response to a specific named event, and no other information about the trigger is
	/// specified. Named events are completely pre-coordinated, and the formal semantics of the trigger are not provided
    """
    namedEvent = "named-event"

    """ The trigger occurs at a specific time or periodically as described by a timing or schedule. A periodic event
	/// cannot have any data elements, but may have a name assigned as a shorthand for the event
    """
    periodic = "periodic"

    """ The trigger occurs whenever data of a particular type is changed in any way, either added, modified, or removed
    """
    dataChanged = "data-changed"

    """ The trigger occurs whenever data of a particular type is added
    """
    dataAdded = "data-added"

    """ The trigger occurs whenever data of a particular type is modified
    """
    dataModified = "data-modified"

    """ The trigger occurs whenever data of a particular type is removed
    """
    dataRemoved = "data-removed"

    """ The trigger occurs whenever data of a particular type is accessed
    """
    dataAccessed = "data-accessed"

    """ The trigger occurs whenever access to data of a particular type is completed
    """
    dataAccessEnded = "data-access-ended"


class TypeDerivationRule(CodeSystemValue):
    """ How a type relates to its baseDefinition.

    URL: http://hl7.org/fhir/type-derivation-rule
    ValueSet: http://hl7.org/fhir/ValueSet/type-derivation-rule
    """
    URL = "http://hl7.org/fhir/type-derivation-rule"
    EXPERIMENTAL = False

    """ This definition defines a new type that adds additional elements to the base type
    """
    specialization = "specialization"

    """ This definition adds additional rules to an existing concrete type
    """
    constraint = "constraint"


class UDICodes(CodeSystemValue):
    """ This value set includes sample UDI codes.

    URL: http://hl7.org/fhir/ex-udi
    ValueSet: http://hl7.org/fhir/ValueSet/udi
    """
    URL = "http://hl7.org/fhir/ex-udi"
    EXPERIMENTAL = True

    """ GUDID (FDA) US Repository
    """
    gudid = "gudid"


class UDIEntryType(CodeSystemValue):
    """ Codes to identify how UDI data was entered

    URL: http://hl7.org/fhir/udi-entry-type
    ValueSet: http://hl7.org/fhir/ValueSet/udi-entry-type
    """
    URL = "http://hl7.org/fhir/udi-entry-type"
    EXPERIMENTAL = False

    """ a barcodescanner captured the data from the device label
    """
    barcode = "barcode"

    """ An RFID chip reader captured the data from the device label
    """
    rfid = "rfid"

    """ The data was read from the label by a person and manually entered. (e.g.  via a keyboard)
    """
    manual = "manual"

    """ The data originated from a patient's implant card and was read by an operator.
    """
    card = "card"

    """ The data originated from a patient source and was not directly scanned or read from a label or card.
    """
    selfReported = "self-reported"

    """ The method of data capture has not been determined
    """
    unknown = "unknown"


class UnitTypeCodes(CodeSystemValue):
    """ This value set includes a smattering of Unit type codes.

    URL: http://hl7.org/fhir/benefit-unit
    ValueSet: http://hl7.org/fhir/ValueSet/benefit-unit
    """
    URL = "http://hl7.org/fhir/benefit-unit"
    EXPERIMENTAL = True

    """ A single individual
    """
    individual = "individual"

    """ A family, typically includes self, spouse(s) and children to a defined age
    """
    family = "family"


class UnknownContentCode(CodeSystemValue):
    """ A code that indicates whether an application accepts unknown elements or extensions when reading resources.

    URL: http://hl7.org/fhir/unknown-content-code
    ValueSet: http://hl7.org/fhir/ValueSet/unknown-content-code
    """
    URL = "http://hl7.org/fhir/unknown-content-code"
    EXPERIMENTAL = False

    """ The application does not accept either unknown elements or extensions.
    """
    no = "no"

    """ The application accepts unknown extensions, but not unknown elements.
    """
    extensions = "extensions"

    """ The application accepts unknown elements, but not unknown extensions.
    """
    elements = "elements"

    """ The application accepts unknown elements and extensions.
    """
    both = "both"


class UsageContextType(CodeSystemValue):
    """ A code that specifies a type of context being specified by a usage context

    URL: http://hl7.org/fhir/usage-context-type
    ValueSet: http://hl7.org/fhir/ValueSet/usage-context-type
    """
    URL = "http://hl7.org/fhir/usage-context-type"
    EXPERIMENTAL = False

    """ The gender of the patient. For this context type, appropriate values can be found in the
	/// http://hl7.org/fhir/ValueSet/administrative-gender value set
    """
    gender = "gender"

    """ The age of the patient. For this context type, the value could be a range that specifies the applicable ages or
	/// a code from an appropriate value set such as the MeSH value set
	/// http://hl7.org/fhir/ValueSet/v3-AgeGroupObservationValue
    """
    age = "age"

    """ The clinical concept(s) addressed by the artifact. For example, disease, diagnostic test interpretation,
	/// medication ordering as in http://hl7.org/fhir/ValueSet/condition-code
    """
    focus = "focus"

    """ The clinical specialty of the context in which the patient is being treated - For example, PCP, Patient,
	/// Cardiologist, Behavioral Professional, Oral Health Professional, Prescriber, etc... taken from a specialty value
	/// set such as the NUCC Health Care provider taxonomy value set http://hl7.org/fhir/ValueSet/provider-taxonomy
    """
    user = "user"

    """ The settings in which the artifact is intended for use. For example, admission, pre-op, etc. For example, the
	/// ActEncounterCode value set http://hl7.org/fhir/ValueSet/v3-ActEncounterCode
    """
    workflow = "workflow"

    """ The context for the clinical task(s) represented by this artifact. For example, this could be any task context
	/// represented by the HL7 ActTaskCode value set http://hl7.org/fhir/ValueSet/v3-ActTaskCode. General categories
	/// include: order entry, patient documentation and patient information review
    """
    task = "task"

    """ The venue in which an artifact could be used. For example, Outpatient, Inpatient, Home, Nursing home. The code
	/// value may originate from the HL7 ServiceDeliveryLocationRoleType value set
	/// (http://hl7.org/fhir/ValueSet/v3-ServiceDeliveryLocationRoleType)
    """
    venue = "venue"

    """ The species to which an artifact applies. For example, SNOMED - 387961004 | Kingdom Animalia (organism)
    """
    species = "species"


class Use(CodeSystemValue):
    """ Complete, proposed, exploratory, other

    URL: http://hl7.org/fhir/claim-use
    ValueSet: http://hl7.org/fhir/ValueSet/claim-use
    """
    URL = "http://hl7.org/fhir/claim-use"
    EXPERIMENTAL = False

    """ The treatment is complete and this represents a Claim for the services.
    """
    complete = "complete"

    """ The treatment is proposed and this represents a Pre-authorization for the services.
    """
    proposed = "proposed"

    """ The treatment is proposed and this represents a Pre-determination for the services.
    """
    exploratory = "exploratory"

    """ A locally defined or otherwise resolved status.
    """
    other = "other"


class UserSessionStatus(CodeSystemValue):
    """ The status of the user session

    URL: http://hl7.org/fhir/usersession-status
    ValueSet: http://hl7.org/fhir/ValueSet/usersession-status
    """
    URL = "http://hl7.org/fhir/usersession-status"
    EXPERIMENTAL = False

    """ The user session is activating
    """
    activating = "activating"

    """ The user session is active
    """
    active = "active"

    """ The user session is suspended
    """
    suspended = "suspended"

    """ The user session is closing
    """
    closing = "closing"

    """ The user session is closed
    """
    closed = "closed"


class UserSessionStatusSource(CodeSystemValue):
    """ The source of the status of the user session

    URL: http://hl7.org/fhir/usersession-status-source
    ValueSet: http://hl7.org/fhir/ValueSet/usersession-status-source
    """
    URL = "http://hl7.org/fhir/usersession-status-source"
    EXPERIMENTAL = False

    """ The status was reported by the user
    """
    user = "user"

    """ The status was reported by the system
    """
    system = "system"


class ValidationProcess(CodeSystemValue):
    """ The primary process by which the target is validated

    URL: http://hl7.org/fhir/validation-process
    ValueSet: http://hl7.org/fhir/ValueSet/validation-process
    """
    URL = "http://hl7.org/fhir/validation-process"
    EXPERIMENTAL = False

    """ editCheck
    """
    editCheck = "edit-check"

    """ valueset
    """
    valueset = "valueset"

    """ primary
    """
    primary = "primary"

    """ multi
    """
    multi = "multi"

    """ standalone
    """
    standalone = "standalone"

    """ inContext
    """
    inContext = "in-context"


class ValidationStatus(CodeSystemValue):
    """ Status of the validation of the target against the primary source

    URL: http://hl7.org/fhir/validation-status
    ValueSet: http://hl7.org/fhir/ValueSet/validation-status
    """
    URL = "http://hl7.org/fhir/validation-status"
    EXPERIMENTAL = False

    """ successful
    """
    successful = "successful"

    """ failed
    """
    failed = "failed"

    """ The validations status has not been determined yet
    """
    unknown = "unknown"


class ValidationType(CodeSystemValue):
    """ What the target is validated against

    URL: http://hl7.org/fhir/validation-type
    ValueSet: http://hl7.org/fhir/ValueSet/validation-type
    """
    URL = "http://hl7.org/fhir/validation-type"
    EXPERIMENTAL = False

    """ nothing
    """
    nothing = "nothing"

    """ primary
    """
    primary = "primary"

    """ multiple
    """
    multiple = "multiple"


class VisionBase(CodeSystemValue):
    """ A coded concept listing the base codes.

    URL: http://hl7.org/fhir/vision-base-codes
    ValueSet: http://hl7.org/fhir/ValueSet/vision-base-codes
    """
    URL = "http://hl7.org/fhir/vision-base-codes"
    EXPERIMENTAL = False

    """ top
    """
    up = "up"

    """ bottom
    """
    down = "down"

    """ inner edge
    """
    _in = "in"

    """ outer edge
    """
    out = "out"


class VisionEyes(CodeSystemValue):
    """ A coded concept listing the eye codes.

    URL: http://hl7.org/fhir/vision-eye-codes
    ValueSet: http://hl7.org/fhir/ValueSet/vision-eye-codes
    """
    URL = "http://hl7.org/fhir/vision-eye-codes"
    EXPERIMENTAL = False

    """ Right Eye
    """
    right = "right"

    """ Left Eye
    """
    left = "left"


class W3cProvenanceActivityType(CodeSystemValue):
    """ This value set includes W3C PROV Data Model Activity concepts, which are treated as codes in this valueset.  Some
adaptations were made to make these concepts suitable values for the Provenance.activity element. Coded concepts are
from PROV-DM and the display names are their counterparts in PROV-N (human readable notation syntax specification).[code
system OID: http://www.w3.org/TR/2013/REC-prov-dm-20130430/ and http://www.w3.org/TR/2013/REC-prov-n-20130430/]

    URL: http://hl7.org/fhir/w3c-provenance-activity-type
    """
    URL = "http://hl7.org/fhir/w3c-provenance-activity-type"
    EXPERIMENTAL = True

    """ The completion of production of a new entity by an activity. This entity did not exist before generation and
	/// becomes available for usage after this generation. Given that a generation is the completion of production of an
	/// entity, it is instantaneous.
    """
    generation = "Generation"

    """ the beginning of utilizing an entity by an activity. Before usage, the activity had not begun to utilize this
	/// entity and could not have been affected by the entity.  (Note: This definition is formulated for a given usage;
	/// it is permitted for an activity to have used a same entity multiple times.) Given that a usage is the beginning
	/// of utilizing an entity, it is instantaneous.
    """
    usage = "Usage"

    """ The exchange of some unspecified entity by two activities, one activity using some entity generated by the
	/// other. A communication implies that activity a2 is dependent on another activity, a1, by way of some unspecified
	/// entity that is generated by a1 and used by a2.
    """
    communication = "Communication"

    """ When an activity is deemed to have been started by an entity, known as trigger. The activity did not exist
	/// before its start. Any usage, generation, or invalidation involving an activity follows the activity's start. A
	/// start may refer to a trigger entity that set off the activity, or to an activity, known as starter, that
	/// generated the trigger. Given that a start is when an activity is deemed to have started, it is instantaneous.
    """
    start = "Start"

    """ When an activity is deemed to have been ended by an entity, known as trigger. The activity no longer exists
	/// after its end. Any usage, generation, or invalidation involving an activity precedes the activity's end. An end
	/// may refer to a trigger entity that terminated the activity, or to an activity, known as ender that generated the
	/// trigger.
    """
    end = "End"

    """ The start of the destruction, cessation, or expiry of an existing entity by an activity. The entity is no longer
	/// available for use (or further invalidation) after invalidation. Any generation or usage of an entity precedes
	/// its invalidation. Given that an invalidation is the start of destruction, cessation, or expiry, it is
	/// instantaneous.
    """
    invalidation = "Invalidation"

    """ A transformation of an entity into another, an update of an entity resulting in a new one, or the construction
	/// of a new entity based on a pre-existing entity. For an entity to be transformed from, created from, or resulting
	/// from an update to another, there must be some underpinning activity or activities performing the necessary
	/// action(s) resulting in such a derivation. A derivation can be described at various levels of precision. In its
	/// simplest form, derivation relates two entities. Optionally, attributes can be added to represent further
	/// information about the derivation. If the derivation is the result of a single known activity, then this activity
	/// can also be optionally expressed. To provide a completely accurate description of the derivation, the generation
	/// and usage of the generated and used entities, respectively, can be provided, so as to make the derivation path,
	/// through usage, activity, and generation, explicit. Optional information such as activity, generation, and usage
	/// can be linked to derivations to aid analysis of provenance and to facilitate provenance-based reproducibility.
    """
    derivation = "Derivation"

    """ A derivation for which the resulting entity is a revised version of some original. The implication here is that
	/// the resulting entity contains substantial content from the original. A revision relation is a kind of derivation
	/// relation from a revised entity to a preceding entity.
    """
    revision = "Revision"

    """ The repeat of (some or all of) an entity, such as text or image, by someone who might or might not be its
	/// original author. A quotation relation is a kind of derivation relation, for which an entity was derived from a
	/// preceding entity by copying, or 'quoting', some or all of it.
    """
    quotation = "Quotation"

    """ Refers to something produced by some agent with direct experience and knowledge about the topic, at the time of
	/// the topic's study, without benefit from hindsight. Because of the directness of primary sources, they 'speak for
	/// themselves' in ways that cannot be captured through the filter of secondary sources. As such, it is important
	/// for secondary sources to reference those primary sources from which they were derived, so that their reliability
	/// can be investigated. It is also important to note that a given entity might be a primary source for one entity
	/// but not another. It is the reason why Primary Source is defined as a relation as opposed to a subtype of Entity.
    """
    primarySource = "Primary-Source"

    """ Ascribing of an entity (object/document) to an agent.
    """
    attribution = "Attribution"

    """  An aggregating activity that results in composition of an entity, which provides a structure to some
	/// constituents that must themselves be entities. These constituents are said to be member of the collections.
    """
    collection = "Collection"


class XPathUsageType(CodeSystemValue):
    """ How a search parameter relates to the set of elements returned by evaluating its xpath query.

    URL: http://hl7.org/fhir/search-xpath-usage
    ValueSet: http://hl7.org/fhir/ValueSet/search-xpath-usage
    """
    URL = "http://hl7.org/fhir/search-xpath-usage"
    EXPERIMENTAL = False

    """ The search parameter is derived directly from the selected nodes based on the type definitions.
    """
    normal = "normal"

    """ The search parameter is derived by a phonetic transform from the selected nodes.
    """
    phonetic = "phonetic"

    """ The search parameter is based on a spatial transform of the selected nodes.
    """
    nearby = "nearby"

    """ The search parameter is based on a spatial transform of the selected nodes, using physical distance from the
	/// middle.
    """
    distance = "distance"

    """ The interpretation of the xpath statement is unknown (and can't be automated).
    """
    other = "other"