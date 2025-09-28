from pydantic import BaseModel, EmailStr, field_validator
from typing import List
from datetime import datetime
from app.core.enums import UserRole
from .types import name_type, description_type, phone_type, skill_type


class UserBase(BaseModel):
    email: EmailStr
    phone: str
    name: name_type
    bio: description_type
    role: UserRole = UserRole.user
    skills: List[str] = []


class UserCreate(BaseModel):
    email: str
    phone: phone_type
    name: name_type
    bio: description_type
    role: UserRole = UserRole.user
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


class UserInDB(BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
