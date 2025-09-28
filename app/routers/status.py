from fastapi import APIRouter
from app.core.helper.response import success

router = APIRouter(tags=["Status"])


@router.get("/health")
async def healthcheck():
    return success("ok")
