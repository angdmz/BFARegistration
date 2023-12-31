from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, func, String, Integer, ForeignKey, UniqueConstraint, Numeric
from sqlalchemy.orm import relationship, mapped_column
from . import BaseModel
from .enums import account_controller_status


class Address(BaseModel):
    __tablename__ = "ethereum_accounts"
    id = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    public_key = Column(String, nullable=False)
    controllers = relationship("AccountController", back_populates="address")
    balance = Column(Numeric, nullable=False)
    __table_args__ = (UniqueConstraint('public_key', name='public_key_uc'),)


class BalanceLimit(BaseModel):
    __tablename__ = "balance_limits"
    id = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    amount = Column(Integer, nullable=False)
    address_id = mapped_column(ForeignKey("ethereum_accounts.id"), nullable=False)
    address = relationship("Address")
    __table_args__ = (UniqueConstraint('address_id', name='address_id_uc'),)


class AccountController(BaseModel):
    __tablename__ = "account_controllers"
    id = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    address_id = mapped_column(ForeignKey("ethereum_accounts.id"), nullable=False)
    address = relationship("Address", back_populates="controllers")
    participant_id = mapped_column(ForeignKey("participants.id"), nullable=False)
    participant = relationship("Participant")
    __table_args__ = (UniqueConstraint('address_id', 'participant_id', name='address_id_participant_id_uc'),)


class AccountControllerStatus(BaseModel):
    __tablename__ = "account_controllers_status"
    id = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    status = Column(account_controller_status, nullable=False)
    account_controller_id = mapped_column(ForeignKey("account_controllers.id"), nullable=False)
    account_controller = relationship("AccountController")
    __table_args__ = (UniqueConstraint('account_controller_id', 'status', 'created_at', name='account_controller_id_status_created_at_uc'),)
