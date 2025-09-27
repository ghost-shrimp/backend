from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import Country, State, City
from app.schemas.location import FullLocation


async def get_countries(db: AsyncSession):
    result = await db.execute(select(Country))
    return result.scalars().all()


async def get_states(db: AsyncSession, country_id: int):
    result = await db.execute(select(State).where(State.country_id == country_id))
    return result.scalars().all()


async def get_cities(db: AsyncSession, state_id: int):
    result = await db.execute(select(City).where(City.state_id == state_id))
    return result.scalars().all()


async def get_full_location(db: AsyncSession, city_id: int):
    result = await db.execute(select(City).where(City.id == city_id))
    city = result.scalar_one_or_none()
    if not city or not city.state or not city.state.country:
        return None
    return FullLocation(
        city_id=city.id,
        state_id=city.state.id,
        country_id=city.state.country.id,
    )
