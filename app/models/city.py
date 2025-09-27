from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncAttrs
from app.models.base import Base


class City(Base, AsyncAttrs):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    state_id = Column(Integer, ForeignKey("states.id"))
    name = Column(String, nullable=False)

    state = relationship("State", back_populates="cities", lazy="joined")
    locations = relationship(
        "Location", back_populates="city", cascade="all, delete-orphan")
