from datetime import datetime, timezone
import uuid
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey, DateTime, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncAttrs
from app.core.enums import TaskStatus
from app.models.base import Base


class Task(Base, AsyncAttrs):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, index=True,
                default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    description = Column(Text)
    price = Column(Float)
    negotiable = Column(Boolean, default=True)
    status = Column(Enum(TaskStatus), default=TaskStatus.open)
    location_id = Column(Integer, ForeignKey("locations.id"))
    created_by = Column(String, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True),
                        default=datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc),
                        onupdate=datetime.now(timezone.utc))

    creator = relationship("User", back_populates="tasks_created")
    location = relationship("Location")
    applicants = relationship(
        "Application", back_populates="task", cascade="all, delete-orphan")
