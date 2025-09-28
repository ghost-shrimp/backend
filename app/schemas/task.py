from pydantic import BaseModel, Field
from app.core.enums import TaskStatus
from datetime import datetime
from app.schemas.location import FullLocation, LocationCreate
from .types import title_type, description_type, price_type


class TaskBase(BaseModel):
    title: title_type
    price: price_type
    negotiable: bool


class TaskCreate(TaskBase):
    created_by: str
    description: description_type
    status: TaskStatus = TaskStatus.open
    location: LocationCreate


class TaskListItemResponse(TaskBase):
    id: str

    class Config:
        from_attributes = True


class TaskResponse(TaskBase):
    id: str
    description: description_type
    status: TaskStatus
    location: FullLocation
    created_by: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class TaskInDB(TaskBase):
    id: str
    description: description_type
    status: TaskStatus
    location_id: int
    created_by: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
