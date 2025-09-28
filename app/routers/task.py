from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db
from app.schemas.task import TaskMinimalResponse, TaskResponse, TaskCreate
from app.services import task as task_service
from app.core.helper.response import success
from app.schemas.response import StandardResponse

router = APIRouter(prefix="/task", tags=["Tasks"])


@router.get("/", response_model=StandardResponse[List[TaskMinimalResponse]])
async def list_tasks(db: AsyncSession = Depends(get_db)):
    tasks = await task_service.get_tasks(db)
    return success(tasks)


@router.post("/", response_model=StandardResponse[TaskResponse])
async def create_task(task_in: TaskCreate, db: AsyncSession = Depends(get_db)):
    task = await task_service.create_task(db, task_in)
    return success(task)


@router.get("/{task_id}", response_model=StandardResponse[TaskResponse])
async def list_tasks(task_id: str, db: AsyncSession = Depends(get_db)):
    task = await task_service.get_task(db, task_id)
    return success(task)
