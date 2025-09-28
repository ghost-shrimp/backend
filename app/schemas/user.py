from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Optional
from app.core.enums import UserRole
from app.schemas.base import BaseSchema
from app.schemas.location import FullLocation
from .types import name_type, description_type, phone_type, skill_type


class UserResponseBase(BaseSchema):
    identification: str
    email: EmailStr
    phone: phone_type
    name: name_type
    bio: description_type
    role: UserRole = UserRole.user


class UserCreate(BaseModel):
    identification: str
    email: EmailStr
    phone: phone_type
    name: name_type
    bio: description_type
    role: UserRole = UserRole.user
    city_id: int
    skills: skill_type

    @field_validator('skills', mode='before')
    def validate_skills(cls, skills):
        if not isinstance(skills, list):
            raise TypeError("Skills must be a list")
        for skill in skills:
            if ' ' in skill:
                raise ValueError("Skill must not contain spaces")
            if len(skill) > 50:
                raise ValueError("Skill must be no more than 50 characters")
        return skills


class UserResponse(UserResponseBase):
    id: str
    location: FullLocation
    skills: List[str] = []
    average_rating: Optional[float] = 0.0
    rating_count: Optional[int] = 0

    class Config:
        from_attributes = True


class UserInDB(UserResponseBase):
    id: str
    city_id: int
    skills: List[str] = []
    average_rating: float
    rating_count: int

    class Config:
        from_attributes = True
