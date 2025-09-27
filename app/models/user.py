from datetime import datetime, timezone
from sqlalchemy import Column, Enum, String, Integer, ForeignKey, DateTime, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncAttrs
from app.enums import UserRole
from app.models.base import Base


class User(Base, AsyncAttrs):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    name = Column(String, nullable=False)
    bio = Column(Text)
    location_id = Column(Integer, ForeignKey("locations.id"))
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc),
                        onupdate=datetime.now(timezone.utc))
    role = Column(Enum(UserRole), default=UserRole.user, nullable=False)
    skills = Column(ARRAY(String), default=[])

    location = relationship("Location", back_populates="users")
    tasks_created = relationship(
        "Task", back_populates="creator", cascade="all, delete-orphan")
    applications = relationship(
        "Application", back_populates="applicant", cascade="all, delete-orphan")
    promotions = relationship(
        "Promotion", back_populates="user", uselist=False, cascade="all, delete-orphan")
    ratings_given = relationship("Rating", foreign_keys="Rating.rater_id",
                                 back_populates="rater", cascade="all, delete-orphan")
    ratings_received = relationship(
        "Rating", foreign_keys="Rating.rated_id", back_populates="rated", cascade="all, delete-orphan")
    subscription = relationship("Subscription", back_populates="user",
                                uselist=False, cascade="all, delete-orphan")
    sessions = relationship(
        "Session", back_populates="user", cascade="all, delete-orphan")
