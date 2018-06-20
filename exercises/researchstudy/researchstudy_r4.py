import json

from clinical_trials.clinical_study import ClinicalStudy, Location
from models.r4 import location, address, codeableconcept, coding, researchstudy, identifier, bundle, period
from models.r4.codesystems import ResearchStudyStatus, ResearchStudyPhase
from six.moves.urllib.parse import quote


def build_location(ct_loc):
    """
    Turn a Location (ct.gov) to a Location (fhir)
    :param Location ct_loc: location from ct.gov
    """
    l = location.Location()
    if not ct_loc.facility.name:
        print("Missing facility name: ")
        name = "{}-{}".format(ct_loc.facility.address.city, ct_loc.facility.address.country)
    else:
        name = ct_loc.facility.name
    l.id = quote(name)
    l.name = ct_loc.facility.name
    a = address.Address(dict(city=ct_loc.facility.address.city,
                             country=ct_loc.facility.address.country,
                             postalCode=ct_loc.facility.address.zip,
                             type='both'))
    l.address = a
    return l


def build_focus(mesh_terms):
    """
    Build the ResearchStudy.focus
    :param conditions:
    :param interventions:
    :return:
    """
    # assuming mesh term here
    focus = []
    for study_term_type, terms in mesh_terms.items():
        print("{}: {}".format(study_term_type, terms))
        for term in terms:
            cc = codeableconcept.CodeableConcept()
            cc.text = term
            cc.coding = [coding.Coding(dict(code=term, system="https://mesh.org", display=""))]
            focus.append(cc)
    return focus


def build_keyword(study_keywords):
    """
    Build the keywords up
    :param keywords:
    :return:
    """
    keywords = []
    for term in study_keywords:
        cc = codeableconcept.CodeableConcept()
        cc.text = term
        cc.coding = [coding.Coding(dict(code=quote(term), system="https://example.org", display=term))]
        keywords.append(cc)
    return keywords


def build_identifiers(nct_id, study_id, secondary_ids):
    """
    Construct the identifiers
    :param id_info:
    :return:
    """
    ident = [identifier.Identifier(dict(use="usual", value=study_id)),
             identifier.Identifier(dict(use="official", value=nct_id,
                                        system="https://clinicaltrials.gov/ct2/show/"))]
    for _id in secondary_ids:
        ident.append(dict(use='secondary', value=_id))
    return ident


def build_status(status):
    """
    Return a standard coded status
    :param status:
    :return:
    """
    if status in ("Active, not recruiting"):
        return 'closed-to-accrual'
    elif status in ("Enrolling by invitation", "Recruiting"):
        return 'active'
    elif status in ("Completed"):
        return 'completed'
    elif status in ("Suspended"):
        return 'suspended'
    elif status in ("Terminated", "Withdrawn"):
        return 'stopped'
    else:
        return 'draft'


def build_phase(phase):
    if phase == "N/A":
        _phase = ResearchStudyPhase.NA
    elif phase == "Phase 1":
        _phase = ResearchStudyPhase.phase1
    elif phase == "Early Phase 1":
        _phase = ResearchStudyPhase.earlyPhase1
    elif phase == "Phase 1":
        _phase = ResearchStudyPhase.phase2
    elif phase == "Phase 1/Phase 2":
        _phase = ResearchStudyPhase.phase1Phase2
    elif phase == "Phase 2":
        _phase = ResearchStudyPhase.phase2
    elif phase == "Phase 2/Phase 3":
        _phase = ResearchStudyPhase.phase2Phase3
    elif phase == "Phase 3":
        _phase = ResearchStudyPhase.phase3
    elif phase == "Phase 4":
        _phase = ResearchStudyPhase.phase4
    return _phase.codeable_concept


if __name__ == "__main__":
    ct = ClinicalStudy.from_file("examples/NCT02348489.xml", local_schema=True)
    locations = [build_location(x) for x in ct.locations]
    foci = build_focus(ct.mesh_terms)
    print([x.as_json() for x in foci])
    keywords = build_keyword(ct.keywords)
    print([x.as_json() for x in keywords])
    identifiers = build_identifiers(ct.nct_id, ct.study_id, ct.secondary_id)
    print([x.as_json() for x in identifiers])
    package = bundle.Bundle()
    package.type = "document"
    package.identifier = identifier.Identifier(dict(use='official',
                                                    system="https://clinicaltrials.gov/ct2/show/",
                                                    value=ct.nct_id))
    entries = []
    for location in locations:
        be = bundle.BundleEntry()
        be.resource_type = "Location"
        be.resource = location
        entries.append(be)
    study = researchstudy.ResearchStudy()
    study.identifier = identifiers
    study.period = period.Period(dict(start=ct.trail.study_first_posted.date.strftime("%Y-%m-%d")))
    study.status = build_status(ct.status)
    study.phase = build_phase(ct.phase)
    entries.append(study)
    package.entry = entries
    print(json.dumps(package.as_json(), indent=4, separators=(',', ': ')))
