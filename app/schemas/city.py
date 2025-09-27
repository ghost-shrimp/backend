from pydantic import BaseModel
from typing import Optional


class CityBase(BaseModel):
    name: str
    state_id: Optional[int] = None


class CityCreate(CityBase):
    pass


class CityUpdate(BaseModel):
    name: Optional[str] = None
    state_id: Optional[int] = None


class CityResponse(CityBase):
    id: int

    model_config = {
        "from_attributes": True
    }
