from pydantic import BaseModel


class CountryBase(BaseModel):
    name: str
    code: str


class CountryResponse(CountryBase):
    id: int

    model_config = {
        "from_attributes": True
    }
