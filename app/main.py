from fastapi import FastAPI
from app.routers.task import router as task_router
from app.routers.status import router as status_router
from app.routers.location import router as location_router
from app.routers.user import router as user_router
from app.core.database import close_db

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    await close_db()

app = FastAPI(
    title="Shrimp API",
    description="Shrimp API",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(user_router)
app.include_router(task_router)
app.include_router(location_router)
app.include_router(status_router)
