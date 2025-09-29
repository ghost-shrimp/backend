from sqlalchemy.ext.asyncio import AsyncSession
from app.models.category import Category
from app.schemas.category import CategoryInDB
from app.core.helper.service import get_all


async def get_categories(db: AsyncSession, amount: int | None = None) -> list[CategoryInDB]:
    return await get_all(db, Category, limit=amount)
