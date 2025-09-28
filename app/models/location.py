from app.models.base import Base
from sqlalchemy import Column, Float, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncAttrs


class Location(Base, AsyncAttrs):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)
    city_id = Column(Integer, ForeignKey("cities.id"))

    city = relationship("City", back_populates="locations", lazy="joined")
