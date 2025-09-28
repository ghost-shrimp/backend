from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskInDB, TaskListItemResponse, TaskResponse
from app.core.helper.service import get_one
from app.models.location import Location
from app.services.location import get_full_location
from sqlalchemy.orm import selectinload


async def get_tasks(db: AsyncSession):
    result = await db.execute(
        select(
            Task.id,
            Task.title,
            Task.price,
            Task.negotiable
        )
    )
    rows = result.mappings().all()
    return [
        TaskListItemResponse.model_validate(row)
        for row in rows
    ]


async def get_task(db: AsyncSession, task_id: str):
    task = await get_one(
        db,
        Task,
        task_id,
        options=[selectinload(Task.location)]
    )

    city_id = task.location.city_id
    full_location = await get_full_location(db, city_id)
    task_data = TaskInDB.model_validate(
        task).model_dump(exclude={'location_id'})

    return TaskResponse(
        **task_data,
        location=full_location
    )


async def create_task(db: AsyncSession, task_data: TaskCreate):
    location_id = None
    if task_data.location:
        location = Location(**task_data.location.model_dump())
        db.add(location)
        await db.commit()
        await db.refresh(location)
        location_id = location.id

    task_dict = task_data.model_dump(exclude={"location"})
    task_dict["location_id"] = location_id
    task = Task(**task_dict)
    db.add(task)
    await db.commit()
    await db.refresh(task)

    location = await get_full_location(db, task_data.location.city_id)

    return TaskResponse(
        **task_dict,
        id=task.id,
        location=location,
        created_at=task.created_at,
        updated_at=task.updated_at
    )
