from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Sequence, select
from typing import Any, Type


from typing import Any, Type, Optional, Dict
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


async def get_all(
    db: AsyncSession,
    model: Type[Any],
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    filters: Optional[Dict[str, Any]] = None,
):
    query = select(model)

    if filters:
        for field, value in filters.items():
            if hasattr(model, field):
                query = query.where(getattr(model, field) == value)

    if offset:
        query = query.offset(offset)
    if limit:
        query = query.limit(limit)

    result = await db.execute(query)
    return result.scalars().all()


async def get_one(
    db: AsyncSession,
    model: Type[Any],
    id_value: str,
    options: Sequence[Any] = None
):
    query = select(model).where(model.id == id_value)

    if options:
        query = query.options(*options)

    result = await db.execute(query)
    return result.scalar_one_or_none()


async def get_filtered(db: AsyncSession, model: Type[Any], **filters):
    query = select(model)
    for attr, value in filters.items():
        query = query.where(getattr(model, attr) == value)
    result = await db.execute(query)
    return result.scalars().all()
