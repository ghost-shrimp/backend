from fastapi import FastAPI
from app.routers.task import router as task_router
from app.routers.status import router as status_router
from app.routers.data import router as data_router
from app.routers.user import router as user_router
from app.core.database import close_db
from contextlib import asynccontextmanager
from app.core.error.exception_handler import add_exception_handlers
from fastapi.middleware.cors import CORSMiddleware


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

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(task_router)
app.include_router(data_router)
app.include_router(status_router)
add_exception_handlers(app)
