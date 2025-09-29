from app.models.base import BaseModel
from sqlalchemy import Column, Integer, ForeignKey, Enum, String, UniqueConstraint
from sqlalchemy.orm import relationship
from app.core.enums import ApplicationStatus


class Application(BaseModel):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    task_id = Column(String, ForeignKey("tasks.id"), nullable=False)
    applicant_id = Column(String, ForeignKey("users.id"), nullable=False)
    status = Column(Enum(ApplicationStatus),
                    default=ApplicationStatus.waiting)

    task = relationship("Task", back_populates="applicants")
    applicant = relationship("User", back_populates="applications")

    __table_args__ = (
        UniqueConstraint("task_id", "applicant_id", name="uq_task_applicant"),
    )
