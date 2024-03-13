import datetime
import uuid
from sqlalchemy import Column, ForeignKey
from lib.models.model_base import ModelBase
from lib.models.physician import Physician
from lib.models.patient import Patient
from sqlalchemy.orm import mapped_column, relationship
import sqlalchemy.dialects.postgresql as pg

#Build the model
class Appointment(ModelBase):
    __tablename__ = "appointment"
    AppointmentID = Column(
        pg.BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False)
    PhysicianID = mapped_column(pg.BIGINT,  ForeignKey(Physician.PhysicianID), nullable=False)
    NurseID=Column(pg.INTEGER)
    PatientRecordNumber= mapped_column(pg.BIGINT,  ForeignKey(Patient.PatientRecordNumber), nullable=False)
    StartDateTime=Column(pg.DATE)
    EndDateTime=Column(pg.DATE)
    ExamRoomID=Column(pg.BIGINT)

# Establish relationships
    physician = relationship("Physician", foreign_keys=[PhysicianID])
    patient=relationship("Patient", foreign_keys=[PatientRecordNumber])