import uuid
from sqlalchemy import Column, Enum, Float, String, Integer, ForeignKey, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship
from app.core.enums import UserRole
from app.models.base import BaseModel
from app.core.constants import MAX_DESCRIPTION, MAX_NAME


class User(BaseModel):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True,
                default=lambda: str(uuid.uuid4()))
    identification = Column(String, unique=True, nullable=False)
    city_id = Column(Integer, ForeignKey("cities.id"))
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    name = Column(String(MAX_NAME), nullable=False)
    bio = Column(String(MAX_DESCRIPTION))
    role = Column(Enum(UserRole), default=UserRole.user, nullable=False)
    skills = Column(ARRAY(String), default=list)
    average_rating = Column(Float, default=0.0)
    rating_count = Column(Integer, default=0)

    city = relationship("City")
    tasks_created = relationship(
        "Task", back_populates="creator", cascade="all, delete-orphan")
    applications = relationship(
        "Application", back_populates="applicant", cascade="all, delete-orphan")
    promotion = relationship(
        "Promotion", back_populates="user", uselist=False, cascade="all, delete-orphan")
    ratings_given = relationship("Rating", foreign_keys="Rating.rater_id",
                                 back_populates="rater", cascade="all, delete-orphan")
    ratings_received = relationship(
        "Rating", foreign_keys="Rating.rated_id", back_populates="rated", cascade="all, delete-orphan")
    subscription = relationship("Subscription", back_populates="user",
                                uselist=False, cascade="all, delete-orphan")
    sessions = relationship(
        "Session", back_populates="user", cascade="all, delete-orphan")
