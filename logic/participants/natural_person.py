from datetime import datetime
from uuid import uuid4, UUID

from sqlalchemy import select
from typing_extensions import Literal

from pydantic import BaseModel

from enums import IdentificationType, ParticipantType
from logic.participants.common import RetrievedParticipantBase
from models import Participant as ParticipantModel, NaturalPerson as NaturalPersonModel, \
    Identification as IdentificationModel


class Identification(BaseModel):
    value: str
    type: IdentificationType


class IdentificationUpdate(BaseModel):
    value: str | None
    type: IdentificationType | None


class UpdateNaturalPersonParticipant(BaseModel):
    first_name: str | None
    last_name: str | None
    identification: IdentificationUpdate | None
    type: Literal[ParticipantType.NATURAL_PERSON] = ParticipantType.NATURAL_PERSON

    async def update_to_persistance(self, participant_id: UUID, persistance):
        values = self.dict(exclude={"identification"}, exclude_none=True)
        query = select(IdentificationModel, NaturalPersonModel).select_from(IdentificationModel).join(NaturalPersonModel, isouter=False).filter(NaturalPersonModel.participant_id == participant_id)
        res = await persistance.execute(query)

        identification, person = res.all()[0]
        for field, value in values.items():
            setattr(person, field, value)

        if self.identification:
            for field, value in self.identification.dict(exclude_none=True).items():
                setattr(identification, field, value)


class NaturalPersonParticipant(BaseModel):
    first_name: str
    last_name: str
    type: Literal[ParticipantType.NATURAL_PERSON] = ParticipantType.NATURAL_PERSON
    identification: Identification

    async def persist_to(self, persistence):
        participant = ParticipantModel(id=uuid4(), is_verified=False, type=self.type)
        person = NaturalPersonModel(first_name=self.first_name, last_name=self.last_name, participant_id=participant.id,
                                    id=uuid4())
        identification = IdentificationModel(type=self.identification.type, value=self.identification.value,
                                             person_id=person.id)
        persistence.add(participant)
        persistence.add(person)
        persistence.add(identification)
        return participant.id


class RetrievedNaturalPerson(NaturalPersonParticipant, RetrievedParticipantBase):

    def is_named(self, first_name, last_name):
        return self.first_name == first_name and self.last_name == last_name

    def has_dni(self, dni):
        return self.identification.type == IdentificationType.DNI and self.identification.value == dni

    @staticmethod
    def add_columns_to_query(query):
        query = query.add_columns(NaturalPersonModel, IdentificationModel)
        return query

    @staticmethod
    def add_joins_to_query(query):
        query = query.join(NaturalPersonModel,isouter=True).join(IdentificationModel, isouter=True)
        return query

    @staticmethod
    def from_row(row):
        participant, natural_person, identification = row
        parseable = dict(created_at=participant.created_at, is_verified=participant.is_verified, id=participant.id, first_name=natural_person.first_name, last_name=natural_person.last_name, identification=dict(type=identification.type, value=identification.value))
        return RetrievedNaturalPerson.parse_obj(parseable)
