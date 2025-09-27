from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db
from app.services import location
from app.schemas.city import CityResponse
from app.schemas.country import CountryResponse
from app.schemas.location import FullLocation
from app.schemas.state import StateResponse

router = APIRouter(prefix="/location", tags=["Location"])


@router.get("/countries", response_model=List[CountryResponse])
async def get_countries(db: AsyncSession = Depends(get_db)):
    return await location.get_countries(db)


@router.get("/states/{country_id}", response_model=List[StateResponse])
async def get_states(country_id: int, db: AsyncSession = Depends(get_db)):
    return await location.get_states(db, country_id)


@router.get("/cities/{state_id}", response_model=List[CityResponse])
async def get_cities(state_id: int, db: AsyncSession = Depends(get_db)):
    return await location.get_cities(db, state_id)


@router.get("/location/{city_id}", response_model=FullLocation)
async def get_full_location(city_id: int, db: AsyncSession = Depends(get_db)):
    return await location.get_full_location(db, city_id)
