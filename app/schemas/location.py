from pydantic import BaseModel
from typing import Optional


class LocationBase(BaseModel):
    lat: float
    lng: float
    city_id: Optional[int] = None


class LocationCreate(LocationBase):
    pass


class LocationUpdate(BaseModel):
    lat: Optional[float] = None
    lng: Optional[float] = None
    city_id: Optional[int] = None


class LocationResponse(LocationBase):
    id: int

    model_config = {
        "from_attributes": True
    }


class FullLocation(BaseModel):
    city_id: int
    state_id: int
    country_id: int

    model_config = {
        "from_attributes": True
    }
