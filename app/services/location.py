from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Country, State, City
from app.schemas.location import FullLocation
from app.core.helper.service import get_all, get_one, get_filtered


async def get_countries(db: AsyncSession):
    return await get_all(db, Country)


async def get_states(db: AsyncSession, country_id: int):
    return await get_filtered(db, State, country_id=country_id)


async def get_cities(db: AsyncSession, state_id: int):
    return await get_filtered(db, City, state_id=state_id)


async def get_full_location(db: AsyncSession, city_id: int):
    city = await get_one(db, City, city_id)
    if not city or not city.state or not city.state.country:
        return None
    return FullLocation(
        city_id=city.id,
        state_id=city.state.id,
        country_id=city.state.country.id,
    )
