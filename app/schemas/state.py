from pydantic import BaseModel
from typing import Optional


class StateBase(BaseModel):
    name: str
    country_id: Optional[int] = None


class StateCreate(StateBase):
    pass


class StateUpdate(BaseModel):
    name: Optional[str] = None
    country_id: Optional[int] = None


class StateResponse(StateBase):
    id: int

    model_config = {
        "from_attributes": True
    }
