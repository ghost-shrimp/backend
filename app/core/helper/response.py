from fastapi import status
from app.schemas.response import StandardResponse


def success(data, code: int = status.HTTP_200_OK):
    return StandardResponse(code=code, data=data)
