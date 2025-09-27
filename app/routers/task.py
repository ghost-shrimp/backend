from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db
from app.schemas.task import TaskResponse, TaskCreate
from app.services import task

router = APIRouter(prefix="/task", tags=["Tasks"])


@router.get("/", response_model=List[TaskResponse])
async def list_tasks(db: AsyncSession = Depends(get_db)):
    return await task.get_tasks(db)


@router.post("/", response_model=TaskResponse)
async def create_task(task_in: TaskCreate, db: AsyncSession = Depends(get_db)):
    return await task.create_task(db, task_in)
