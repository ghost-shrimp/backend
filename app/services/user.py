from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.core.helper.service import get_all, get_one
from app.core.error.exceptions import DuplicateFieldError
from app.services.location import get_full_location
from app.schemas.user import UserInDB, UserResponse


async def get_users(db: AsyncSession):
    return await get_all(db, User)


async def get_user(db: AsyncSession, user_id: str):
    user = await get_one(db, User, user_id)
    location = await get_full_location(db, user.city_id)
    user_data = UserInDB.model_validate(user).model_dump()

    return UserResponse(
        **user_data,
        location=location
    )


async def create_user(db, user_data):
    result = await db.execute(
        select(User).where(
            or_(
                User.identification == user_data.identification,
                User.email == user_data.email,
                User.phone == user_data.phone
            )
        )
    )
    existing_user = result.scalar_one_or_none()
    if existing_user:
        if existing_user.identification == user_data.identification:
            raise DuplicateFieldError(
                field="identification", message="duplicate_identification")
        if existing_user.email == user_data.email:
            raise DuplicateFieldError(
                field="email", message="duplicate_email")
        if existing_user.phone == user_data.phone:
            raise DuplicateFieldError(
                field="phone", message="duplicate_phone")

    user_dict = user_data.model_dump()
    user = User(**user_dict)
    db.add(user)
    await db.commit()
    await db.refresh(user)

    location = await get_full_location(db, user.city_id)

    return UserResponse(
        **user_dict,
        id=user.id,
        location=location,
        created_at=user.created_at,
        updated_at=user.updated_at
    )
