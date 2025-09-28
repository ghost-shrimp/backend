from pydantic import BaseModel


class FullLocation(BaseModel):
    city_id: int
    state_id: int
    country_id: int

    model_config = {
        "from_attributes": True
    }
