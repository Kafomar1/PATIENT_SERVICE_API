from sqlalchemy import Column
from lib.models.model_base import ModelBase
import sqlalchemy.dialects.postgresql as pg

class Hospital(ModelBase):
    __tablename__ = "hospital"
    HospitalID = Column(
        pg.BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    Location= Column(pg.VARCHAR)
    Speciality= Column(pg.VARCHAR)
    