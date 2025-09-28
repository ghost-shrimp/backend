from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.schemas.response import FieldError, ErrorResponse
from starlette import status
from app.core.error.exceptions import DuplicateFieldError


def add_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        errors = []
        for e in exc.errors():
            ctx = e.get("ctx")
            if ctx and "error" in ctx:
                ctx = {**ctx, "error": str(ctx["error"])}
            errors.append(FieldError(
                field=".".join(map(str, e["loc"][1:])),
                type=e["type"],
                context=ctx
            ))

        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=ErrorResponse(code=422, errors=errors).model_dump()
        )

    @app.exception_handler(DuplicateFieldError)
    async def duplicate_field_exception_handler(request: Request, exc: DuplicateFieldError):
        errors = [
            FieldError(
                field=exc.field,
                type="duplicate",
                context={"error": exc.message}
            )
        ]
        return JSONResponse(
            status_code=400,
            content=ErrorResponse(code=400, errors=errors).model_dump()
        )
