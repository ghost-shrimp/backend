import uuid
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from app.core.enums import TaskStatus
from app.models.base import BaseModel
from app.core.constants import MAX_DESCRIPTION, MAX_TITLE


class Task(BaseModel):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, index=True,
                default=lambda: str(uuid.uuid4()))
    title = Column(String(MAX_TITLE), nullable=False)
    description = Column(String(MAX_DESCRIPTION))
    price = Column(Float, nullable=False)
    negotiable = Column(Boolean, default=True)
    status = Column(Enum(TaskStatus), index=True, default=TaskStatus.open)
    city_id = Column(Integer, ForeignKey(
        "cities.id", ondelete="SET NULL"), nullable=True)
    created_by = Column(String, ForeignKey(
        "users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey(
        "categories.id", ondelete="SET NULL"), nullable=True)

    category = relationship("Category", back_populates="tasks")
    city = relationship("City", back_populates="tasks")
    creator = relationship("User", back_populates="tasks_created")
    applicants = relationship(
        "Application", back_populates="task", cascade="all, delete-orphan")
