from app.models.base import Base
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncAttrs


class State(Base, AsyncAttrs):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, index=True)
    country_id = Column(Integer, ForeignKey("countries.id"))
    name = Column(String, nullable=False)

    country = relationship("Country", back_populates="states", lazy="joined")
    cities = relationship("City", back_populates="state",
                          cascade="all, delete-orphan")
