from typing import Any, Generic, List, Optional, TypeVar
from pydantic import BaseModel

T = TypeVar("T")


class StandardResponse(BaseModel, Generic[T]):
    code: int
    data: Optional[T] = None


class FieldError(BaseModel):
    field: str
    type: str
    context: Optional[Any] = None


class ErrorResponse(BaseModel):
    code: int
    errors: List[FieldError]
