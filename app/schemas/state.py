from pydantic import BaseModel
from typing import Optional


class StateBase(BaseModel):
    name: str
    country_id: Optional[int] = None


class StateResponse(StateBase):
    id: int

    model_config = {
        "from_attributes": True
    }
