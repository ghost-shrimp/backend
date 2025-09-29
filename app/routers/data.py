from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db
from app.services import category as category_service
from app.services import location as location_service
from app.core.helper.response import success
from app.schemas.response import StandardResponse
from app.schemas.category import CategoryInDB
from app.schemas.city import CityResponse
from app.schemas.country import CountryResponse
from app.schemas.state import StateResponse


router = APIRouter(prefix="/data", tags=["Data"])


@router.get("/categories", response_model=StandardResponse[List[CategoryInDB]])
async def list_categories(amount: int | None = Query(default=None, gt=0), db: AsyncSession = Depends(get_db)):
    categories = await category_service.get_categories(db, amount=amount)
    return success(categories)


@router.get("/countries", response_model=StandardResponse[List[CountryResponse]])
async def get_countries(db: AsyncSession = Depends(get_db)):
    countries = await location_service.get_countries(db)
    return success(countries)


@router.get("/states/{country_id}", response_model=StandardResponse[List[StateResponse]])
async def get_states(country_id: int, db: AsyncSession = Depends(get_db)):
    states = await location_service.get_states(db, country_id)
    return success(states)


@router.get("/cities/{state_id}", response_model=StandardResponse[List[CityResponse]])
async def get_cities(state_id: int, db: AsyncSession = Depends(get_db)):
    cities = await location_service.get_cities(db, state_id)
    return success(cities)
