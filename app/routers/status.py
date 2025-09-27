from fastapi import APIRouter, status

router = APIRouter(tags=["Status"])


@router.get("/health")
async def healthcheck():
    return {"status": status.HTTP_200_OK}
