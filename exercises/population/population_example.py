from exercises.population.fhir_wrapper import FHIRConnection
from exercises.population.rave import push_demographics, push_conmeds

FHIR_ENDPOINT = ""


def publish_dataset(dataset, fhir_id, subject_uuid):
    """
    Wrapper for getting and pushing data to Rave
    :param dataset:
    :param fhir_id:
    :param subject_uuid:
    """
    fhir = FHIRConnection(FHIR_ENDPOINT)
    if dataset == 'DM':
        demog = fhir.get_patient(fhir_id)
        if not demog:
            raise ValueError("No data to push")
        result = push_demographics(subject_uuid, demog)
    elif dataset == 'CM':
        conmeds = fhir.get_patient_medications(fhir_id)
        if not conmeds:
            raise ValueError("No data to push")
        result = push_conmeds(subject_uuid, conmeds)
