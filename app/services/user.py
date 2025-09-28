from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.core.helper.service import get_all, get_one
from app.core.error.exceptions import DuplicateFieldError


async def get_users(db: AsyncSession):
    return await get_all(db, User)


async def get_user(db: AsyncSession, user_id: str):
    return await get_one(db, User, user_id)


async def create_user(db, user_data):
    result = await db.execute(
        select(User).where(
            or_(
                User.email == user_data.email,
                User.phone == user_data.phone
            )
        )
    )
    existing_user = result.scalar_one_or_none()
    if existing_user:
        if existing_user.email == user_data.email:
            raise DuplicateFieldError(
                field="email", message="Email already exists")
        if existing_user.phone == user_data.phone:
            raise DuplicateFieldError(
                field="phone", message="Phone already exists")

    user = User(**user_data.model_dump())
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
