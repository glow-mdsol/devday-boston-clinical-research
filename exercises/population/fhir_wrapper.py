# -*- coding: utf-8 -*-

from fhirclient import client
import fhirclient.models.patient as p
import fhirclient.models.medicationstatement as cm
import fhirclient.models.observation as ob


class FHIRConnection(object):

    def __init__(self, base_url):
        # reuse the client-py library
        self.smart = client.FHIRClient(settings=dict(api_base=base_url, app_id='tornado-id'))

    @property
    def patients(self):
        """
        Get the Patients resources
        :return:
        """
        search = p.Patient.where(struct=dict())
        patients = []
        for patient in search.perform_resources(self.smart.server):
            patients.append(patient.as_json())
        return patients

    def get_patient(self, patient_id):
        """
        Get a Patient resources
        :arg str patient_id: the id for the patient resource
        :return:
        """
        patient = p.Patient.read(patient_id, self.smart.server)
        return patient.as_json()

    def get_patient_medications(self, patient_id):
        """
        Get MedicationStatement for a Patient
        :param str patient_id: Patient Identifier
        :return:
        """
        search_meds = cm.MedicationStatement.where(struct=dict(patient=patient_id))
        meds = []
        for meds in search_meds.perform_resources(self.smart.server):
           meds.append(meds.as_json())
        return meds

    def get_medication(self, medication_id):
        """
        Get an individual MedicationStatement Resource
        :param str medication_id: Medication Statement resource ID
        :return:
        """
        medication = cm.MedicationStatement.read(medication_id, self.smart.server)
        return medication.as_json()

    def get_obs(self, patient_id, loinc_code):
        search_obs = ob.Observation.where(struct=dict(patient=patient_id, code=loinc_code))
        obs = ""
        if len(search_obs.perform_resources(self.smart.server)) > 0:
            sysbp = search_obs.perform_resources(self.smart.server).pop().as_json()
        return obs

    def get_vitals_sysbp(self, patient_id):
        """
        Get the Systolic BP for the Patient
        :param patient_id:
        :return:
        """
        return self.get_obs(patient_id, "8480-6")

    def get_vitals_diabp(self, patient_id):
        """
        Get the Diastolic BP for the Patient
        :param patient_id:
        :return:
        """
        return self.get_obs(patient_id, "55284-4")

    def get_vitals_bmi(self, patient_id):
        """
        Get the BMI for the Patient
        :param patient_id:
        :return:
        """
        return self.get_obs(patient_id, "39156-5")

    def get_vitals_hr(self, patient_id):
        """
        Get the HR for the Patient
        :param patient_id:
        :return:
        """
        return self.get_obs(patient_id, "8867-4")

    def get_vitals_temp(self, patient_id):
        """
        Get the Temp for the Patient
        :param patient_id:
        :return:
        """
        return self.get_obs(patient_id, "8310-5")

    def get_vitals_weight(self, patient_id):
        """
        Get the Weight for the Patient
        :param patient_id:
        :return:
        """
        return self.get_obs(patient_id, "3141-9")

    def get_vitals_height(self, patient_id):
        """
        Get the Height for the Patient
        :param patient_id:
        :return:
        """
        return self.get_obs(patient_id, "8302-2")

    def get_labs_wbc(self, patient_id):
        """
        Get the White Blood Count for the Patient
        :param patient_id:
        :return:
        """
        return self.get_obs(patient_id, "6690-2")

    def get_labs_rbc(self, patient_id):
        """
        Get the Red Blood Count for the Patient
        :param patient_id:
        :return:
        """
        return self.get_obs(patient_id, "789-8")

    def get_labs_creat(self, patient_id):
        """
        Get the Creatinine for the Patient
        :param patient_id:
        :return:
        """
        return self.get_obs(patient_id, "14682-9")

    def labs_alb(self, patient_id):
        """
        Get the Albumin for the Patient
        :param patient_id:
        :return:
        """
        return self.get_obs(patient_id, "1751-7")

