from typing import Optional, Dict
from pydantic import BaseModel


class StatusModel(BaseModel):
    code: int
    description: str


class ErrorResponse(BaseModel):
    status: StatusModel
    data: Optional[Dict] = None


class TokenResponse(BaseModel):
    refresh_token: str
