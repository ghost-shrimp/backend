from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db
from app.schemas.user import UserInDB, UserCreate
from app.services import user as user_service
from app.core.helper.response import success
from app.schemas.response import StandardResponse

router = APIRouter(prefix="/user", tags=["Users"])


@router.get("/", response_model=StandardResponse[List[UserInDB]])
async def list_users(db: AsyncSession = Depends(get_db)):
    users = await user_service.get_users(db)
    return success(users)


@router.post("/", response_model=StandardResponse[UserInDB])
async def create_user(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    user = await user_service.create_user(db, user_in)
    return success(user)


@router.get("/{user_id}", response_model=StandardResponse[UserInDB])
async def get_user(user_id: str, db: AsyncSession = Depends(get_db)):
    user = await user_service.get_user(db, user_id)
    return success(user)
