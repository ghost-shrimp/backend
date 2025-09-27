from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


async def get_tasks(db: AsyncSession):
    result = await db.execute(select(Task))
    return result.scalars().all()


async def get_task(db: AsyncSession, task_id: str):
    result = await db.execute(select(Task).where(Task.id == task_id))
    return result.scalar_one_or_none()


async def create_task(db: AsyncSession, task_in: TaskCreate):
    task = Task(**task_in.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


async def update_task(db: AsyncSession, task_id: str, task_in: TaskUpdate):
    task = await get_task(db, task_id)
    if not task:
        return None
    for key, value in task_in.dict(exclude_unset=True).items():
        setattr(task, key, value)
    await db.commit()
    await db.refresh(task)
    return task


async def delete_task(db: AsyncSession, task_id: str):
    task = await get_task(db, task_id)
    if not task:
        return None
    await db.delete(task)
    await db.commit()
    return task
