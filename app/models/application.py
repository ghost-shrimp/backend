from datetime import datetime, timezone
from app.models.base import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncAttrs
from app.core.enums import ApplicationStatus


class Application(Base, AsyncAttrs):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    task_id = Column(String, ForeignKey("tasks.id"), nullable=False)
    applicant_id = Column(String, ForeignKey("users.id"), nullable=False)
    status = Column(Enum(ApplicationStatus),
                    default=ApplicationStatus.waiting)
    created_at = Column(DateTime(timezone=True),
                        default=datetime.now(timezone.utc))

    task = relationship("Task", back_populates="applicants")
    applicant = relationship("User", back_populates="applications")
