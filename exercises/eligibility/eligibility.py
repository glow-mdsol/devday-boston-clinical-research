import json

import requests
from fhirclient import client
from datetime import datetime
from fhirclient.models import patient, condition, medicationstatement, \
    medication, medicationadministration, medicationrequest, medicationdispense
from fhirclient.models.bundle import BundleEntry
from six.moves.urllib.parse import quote, urljoin
import os

from exercises.common.bioportal import get_snomed_term_for_mesh_term
from exercises.common.rxnorm import get_rxnorm_code_from_name

ENDPOINT = "https://api-stu3.hspconsortium.org/clinresearch/open"

# ENDPOINT = "http://hapi.fhir.org/baseDstu3"


def yearsago(years, from_date=None):
    """
    Taken from: https://stackoverflow.com/a/765990
    :param int years: Number of years ago
    :param datetime from_date: Start date
    :rtype datetime.datetime
    :return:
    """
    if from_date is None:
        from_date = datetime.now()
    try:
        return from_date.replace(year=from_date.year - years)
    except ValueError:
        # Must be 2/29!
        assert from_date.month == 2 and from_date.day == 29  # can be removed
        return from_date.replace(month=2, day=28,
                                 year=from_date.year - years)


class Elider:

    def __init__(self):
        self.client = client.FHIRClient(settings=dict(app_id="boston-elig-cr",
                                                      api_base=ENDPOINT))

    def get_female_subjects(self):
        # Given a Eligibility Criteria
        #  get a list of female patients
        eligible = patient.Patient.where(struct=dict(gender="female"))
        results = eligible.perform(self.client.server)
        return results

    def get_male_subjects(self):
        # Given a Eligibility Criteria
        #  get a list of male patients
        eligible = patient.Patient.where(struct=dict(gender="female"))
        results = eligible.perform(self.client.server)
        return results

    def get_by_age(self, age, inclusive=True, lower=True):
        """
        Get a patient by age
        :param age:
        :param inclusive:
        :param lower:
        :return:
        """
        if lower:
            if inclusive:
                qual = "ge"
            else:
                qual = "gt"
        else:
            if inclusive:
                qual = "le"
            else:
                qual = "lt"
        diff = yearsago(age)
        eligible = patient.Patient.where(struct=dict(birthdate="{}{}".format(qual, diff.strftime("%Y-%m-%d"))))
        results = eligible.perform(self.client.server)
        return results


    def get_by_condtion_code(self, code):
        eligible = condition.Condition.where(struct=dict(code=code))
        results = eligible.perform(self.client.server)
        return results

    def get_by_medication(self, medication_code):
        # Preferred
        state = medicationstatement.MedicationStatement.where(struct=dict(code=medication_code))
        statement_results = state.perform(self.client.server)
        # administrated
        admin = medicationadministration.MedicationAdministration.where(struct=dict(code=medication_code))
        admin_results = admin.perform(self.client.server)
        # requested
        # req = medicationrequest.MedicationRequest.where(struct=dict(code=medication_code))
        # req_results = req.perform(self.client.server)
        # dispensed
        disp = medicationdispense.MedicationDispense.where(struct=dict(code=medication_code))
        disp_results = disp.perform(self.client.server)
        # vanilla
        med = medication.Medication.where(struct=dict(code=medication_code))
        med_res = med.perform(self.client.server)
        return [x for x in (statement_results, admin_results,
                            disp_results, med_res) if x.total > 0]


def gg(bundle_entry):
    resource = bundle_entry.resource
    return resource.id


if __name__ == "__main__":
    # female > 18
    p = Elider()
    female = p.get_female_subjects()
    print("Total Female Count: ", female.total)
    _females = tuple(gg(x) for x in female.entry)
    over_eighteen = p.get_by_age(18, inclusive=False)
    print("Total >= 18 Count: ", over_eighteen.total)
    _aged = (gg(x) for x in over_eighteen.entry)
    population = set(tuple(_females)).intersection(set(tuple(_aged)))
    print("Matched: ", population)
    # MeSH terms are used frequently in Trial registries
    for mesh_term in ('Diabetes Mellitus, Type 2', 'Arthritis, Rheumatoid',
                      'Leukemia, Myeloid',
                      'Leukemia, Myeloid, Acute',
                      'Asthma'):
        term_ = get_snomed_term_for_mesh_term(mesh_term)
        print("Code for ", mesh_term, "is", term_)
        conditions = p.get_by_condtion_code(term_)
        print(conditions.total)
        if conditions.total > 0:
            for entry in conditions.entry:  # type: BundleEntry
                resource = entry.resource
                print("Subject ", resource.subject.reference, "has", mesh_term)
    for rx in ('aspirin', 'metformin', "Amoxicillin 80 MG/ML Oral Suspension"):
        rxterm = get_rxnorm_code_from_name(rx)
        if rxterm:
            medications = p.get_by_medication(rxterm.get('idGroup').get('rxnormId')[0])
            if medications:
                pass


