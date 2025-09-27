from pydantic import BaseModel
from typing import Optional
from app.enums import TaskStatus
from datetime import datetime


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    type: Optional[int] = None
    price: Optional[float] = None
    negotiable: bool = True
    status: TaskStatus = TaskStatus.open
    location_id: Optional[int] = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[int] = None
    price: Optional[float] = None
    negotiable: Optional[bool] = None
    status: Optional[TaskStatus] = None
    location_id: Optional[int] = None


class TaskResponse(TaskBase):
    id: str
    created_by: str
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }
