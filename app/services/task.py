from sqlalchemy.ext.asyncio import AsyncSession
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskInDB, TaskMinimalResponse, TaskResponse
from app.core.helper.service import get_all, get_one
from app.services.location import get_full_location


async def get_tasks(db: AsyncSession):
    tasks = await get_all(db, Task)
    responses = []
    for task in tasks:
        location = await get_full_location(db, task.city_id)
        if location:
            responses.append(TaskMinimalResponse(
                id=task.id,
                title=task.title,
                price=task.price,
                negotiable=task.negotiable,
                status=task.status,
                location=location,
                created_at=task.created_at,
                updated_at=task.updated_at
            ))

    return responses


async def get_task(db: AsyncSession, task_id: str):
    task = await get_one(
        db,
        Task,
        task_id,
    )

    location = await get_full_location(db, task.city_id)
    task_data = TaskInDB.model_validate(task).model_dump()

    return TaskResponse(
        **task_data,
        location=location
    )


async def create_task(db: AsyncSession, task_data: TaskCreate):
    task_dict = task_data.model_dump()
    task = Task(**task_dict)
    db.add(task)
    await db.commit()
    await db.refresh(task)

    location = await get_full_location(db, task.city_id)

    return TaskResponse(
        **task_dict,
        id=task.id,
        location=location,
        created_at=task.created_at,
        updated_at=task.updated_at
    )
