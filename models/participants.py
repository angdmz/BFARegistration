from sqlalchemy import Column, func, Boolean, ForeignKey
from sqlalchemy.orm import relationship, mapped_column
from sqlalchemy.types import String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID

from . import BaseModel
from .enums import identification_type, academic_type, participant_type
from session.connection import Base


class Participant(BaseModel):
    __tablename__ = "participants"

    id = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    is_verified = Column(Boolean, default=False, nullable=False)
    date_of_verification = Column(TIMESTAMP(timezone=True), nullable=True)
    type = Column(participant_type, nullable=False)


class Identification(BaseModel):
    __tablename__ = "identifications"
    id = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    type = Column(identification_type, nullable=False)
    value = Column(String, nullable=False)
    person_id = mapped_column(ForeignKey("natural_persons.id"), nullable=False)
    person = relationship("NaturalPerson", back_populates="identifications")


class NaturalPerson(Base):
    __tablename__ = "natural_persons"
    id = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    identifications = relationship("Identification", back_populates="person")
    participant_id = mapped_column(ForeignKey("participants.id"), nullable=False)
    participant = relationship("Participant")


class GovernmentOrganism(Base):
    __tablename__ = "government_organisms"
    id = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    full_name = Column(String, nullable=False)
    sector = Column(String, nullable=False)
    participant_id = mapped_column(ForeignKey("participants.id"), nullable=False)
    participant = relationship("Participant")


class Company(Base):
    __tablename__ = "companies"
    id = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    full_name = Column(String, nullable=False)
    cuit = Column(String, nullable=False)
    participant_id = mapped_column(ForeignKey("participants.id"), nullable=False)
    participant = relationship("Participant")


class Academic(Base):
    __tablename__ = "academics"
    id = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    full_name = Column(String, nullable=False)
    education_level = Column(academic_type, nullable=False)
    participant_id = mapped_column(ForeignKey("participants.id"), nullable=False)
    participant = relationship("Participant")
