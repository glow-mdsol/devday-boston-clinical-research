#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.3.0 (http://hl7.org/fhir/StructureDefinition/OccupationalData) on 2018-05-12.
#  2018, SMART Health IT.


from . import domainresource

class OccupationalData(domainresource.DomainResource):
    """ Patient's or family member's work information (ODH).
    
    A person's work information, structured to facilitate individual,
    population, and public health use; not intended to support billing.
    """
    
    resource_type = "OccupationalData"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.combatZonePeriod = None
        """ Combat Zone Work period.
        List of `Period` items (represented as `dict` in JSON). """
        
        self.date = None
        """ Occupational Data (ODH) recording time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.employmentStatus = None
        """ Employment status.
        List of `OccupationalDataEmploymentStatus` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Unique identifier for the occupational data (ODH) record.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.informant = None
        """ Occupational Data (ODH) informant.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.pastOrPresentJob = None
        """ Past or Present Job.
        List of `OccupationalDataPastOrPresentJob` items (represented as `dict` in JSON). """
        
        self.recorder = None
        """ Occupational Data (ODH) recorder.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.retirementDate = None
        """ Retirement date.
        List of `FHIRDate` items (represented as `str` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.subject = None
        """ Who the occupational data (ODH) is collected about.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.usualWork = None
        """ Usual Work.
        Type `OccupationalDataUsualWork` (represented as `dict` in JSON). """
        
        super(OccupationalData, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OccupationalData, self).elementProperties()
        js.extend([
            ("combatZonePeriod", "combatZonePeriod", period.Period, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("employmentStatus", "employmentStatus", OccupationalDataEmploymentStatus, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("informant", "informant", fhirreference.FHIRReference, True, None, False),
            ("pastOrPresentJob", "pastOrPresentJob", OccupationalDataPastOrPresentJob, True, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, True, None, False),
            ("retirementDate", "retirementDate", fhirdate.FHIRDate, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("usualWork", "usualWork", OccupationalDataUsualWork, False, None, False),
        ])
        return js


from . import backboneelement

class OccupationalDataEmploymentStatus(backboneelement.BackboneElement):
    """ Employment status.
    
    A person's current economic relationship to a job. Employment status refers
    to whether a person is currently working for compensation, is unemployed
    (i.e., searching for work for compensation), or is not in the labor force
    (e.g. disabled, homemaker, chooses not to work, etc.). Employment status is
    not the same as classification of work.
    """
    
    resource_type = "OccupationalDataEmploymentStatus"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Employment status code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.effective = None
        """ Employment status effective time period.
        Type `Period` (represented as `dict` in JSON). """
        
        super(OccupationalDataEmploymentStatus, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OccupationalDataEmploymentStatus, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("effective", "effective", period.Period, False, None, True),
        ])
        return js


class OccupationalDataPastOrPresentJob(backboneelement.BackboneElement):
    """ Past or Present Job.
    
    The type of work done by a person during a current or past job. A job is
    defined by the sum of all the data related to the occupation. A change in
    occupation, supervisory level, industry, employer, or employer location is
    considered a new job.
    """
    
    resource_type = "OccupationalDataPastOrPresentJob"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.effective = None
        """ Past or Present Job effective time period.
        Type `Period` (represented as `dict` in JSON). """
        
        self.employer = None
        """ Past or Present Job employer.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.industry = None
        """ Past or Present Job industry.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.jobDuty = None
        """ Past or Present Job job duty.
        List of `str` items. """
        
        self.occupation = None
        """ Past or Present Job occupation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.occupationalHazard = None
        """ Past or Present Job occupational hazard.
        List of `str` items. """
        
        self.supervisoryLevel = None
        """ Past or Present Job supervisory level.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.workClassification = None
        """ Past or Present Job work classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.workSchedule = None
        """ Past or Present Job work schedule.
        Type `OccupationalDataPastOrPresentJobWorkSchedule` (represented as `dict` in JSON). """
        
        super(OccupationalDataPastOrPresentJob, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OccupationalDataPastOrPresentJob, self).elementProperties()
        js.extend([
            ("effective", "effective", period.Period, False, None, False),
            ("employer", "employer", fhirreference.FHIRReference, False, None, False),
            ("industry", "industry", codeableconcept.CodeableConcept, False, None, True),
            ("jobDuty", "jobDuty", str, True, None, False),
            ("occupation", "occupation", codeableconcept.CodeableConcept, False, None, True),
            ("occupationalHazard", "occupationalHazard", str, True, None, False),
            ("supervisoryLevel", "supervisoryLevel", codeableconcept.CodeableConcept, False, None, False),
            ("workClassification", "workClassification", codeableconcept.CodeableConcept, False, None, False),
            ("workSchedule", "workSchedule", OccupationalDataPastOrPresentJobWorkSchedule, False, None, False),
        ])
        return js


class OccupationalDataPastOrPresentJobWorkSchedule(backboneelement.BackboneElement):
    """ Past or Present Job work schedule.
    
    Describes a person's typical arrangement of working hours for one job.
    """
    
    resource_type = "OccupationalDataPastOrPresentJobWorkSchedule"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Past or Present Job work schedule code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.dailyWorkHours = None
        """ Past or Present Job work schedule daily work hours.
        Type `float`. """
        
        self.weeklyWorkDays = None
        """ Past or Present Job work schedule weekly work days.
        Type `float`. """
        
        super(OccupationalDataPastOrPresentJobWorkSchedule, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OccupationalDataPastOrPresentJobWorkSchedule, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("dailyWorkHours", "dailyWorkHours", float, False, None, False),
            ("weeklyWorkDays", "weeklyWorkDays", float, False, None, False),
        ])
        return js


class OccupationalDataUsualWork(backboneelement.BackboneElement):
    """ Usual Work.
    
    The type of work a person has held for the longest amount of time during
    his or her life, regardless of the occupation currently held and regardless
    of whether or not it has been held for a continuous time.
    """
    
    resource_type = "OccupationalDataUsualWork"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.duration = None
        """ Usual Work duration.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.industry = None
        """ Usual Work industry.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.occupation = None
        """ Usual Work occupation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.start = None
        """ Usual Work start time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(OccupationalDataUsualWork, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OccupationalDataUsualWork, self).elementProperties()
        js.extend([
            ("duration", "duration", duration.Duration, False, None, False),
            ("industry", "industry", codeableconcept.CodeableConcept, False, None, True),
            ("occupation", "occupation", codeableconcept.CodeableConcept, False, None, True),
            ("start", "start", fhirdate.FHIRDate, False, None, False),
        ])
        return js


from . import codeableconcept
from . import duration
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
