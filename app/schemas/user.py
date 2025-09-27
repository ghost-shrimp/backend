from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from app.enums import UserRole


class UserBase(BaseModel):
    email: str
    phone: str
    name: str
    bio: Optional[str] = None
    location_id: Optional[int] = None
    role: UserRole = UserRole.user


class UserCreate(UserBase):
    password: str
    skills: Optional[List[str]] = []


class UserUpdate(BaseModel):
    email: Optional[str] = None
    phone: Optional[str] = None
    name: Optional[str] = None
    bio: Optional[str] = None
    location_id: Optional[int] = None
    role: Optional[UserRole] = None
    skills: Optional[List[str]] = None


class UserResponse(UserBase):
    id: str
    created_at: datetime
    updated_at: datetime
    skills: List[str] = []

    model_config = {
        "from_attributes": True
    }
