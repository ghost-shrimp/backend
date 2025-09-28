from typing import Optional

from pydantic import BaseModel
from app.core.enums import TaskStatus
from app.schemas.location import FullLocation
from app.schemas.base import BaseSchema
from .types import title_type, description_type, price_type


class TaskResponseBase(BaseSchema):
    title: title_type
    price: price_type
    negotiable: bool


class TaskCreate(BaseModel):
    title: title_type
    price: price_type
    negotiable: bool
    created_by: str
    description: description_type
    status: TaskStatus = TaskStatus.open
    city_id: int
    category_id: Optional[int] = None


class TaskMinimalResponse(TaskResponseBase):
    id: str
    status: TaskStatus
    location: FullLocation

    class Config:
        from_attributes = True


class TaskResponse(TaskMinimalResponse):
    description: description_type
    category_id: Optional[int]
    selected_application_id: Optional[int] = None
    created_by: str

    class Config:
        from_attributes = True


class TaskInDB(TaskResponseBase):
    id: str
    description: description_type
    status: TaskStatus
    city_id: int
    category_id: int
    created_by: str

    class Config:
        from_attributes = True
