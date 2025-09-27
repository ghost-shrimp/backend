from pydantic import BaseModel
from typing import Optional


class CountryBase(BaseModel):
    name: str
    code: str
    currency: str
    currency_symbol: str


class CountryCreate(CountryBase):
    pass


class CountryUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None


class CountryResponse(CountryBase):
    id: int

    model_config = {
        "from_attributes": True
    }
