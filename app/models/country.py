from app.models.base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncAttrs


class Country(Base, AsyncAttrs):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    code = Column(String, nullable=False, unique=True)
    currency = Column(String, nullable=False)
    currency_symbol = Column(String, nullable=False)

    states = relationship("State", back_populates="country",
                          cascade="all, delete-orphan")
