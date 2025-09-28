from datetime import datetime, timezone
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncAttrs

Base = declarative_base()


class BaseModel(Base, AsyncAttrs):
    __abstract__ = True

    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(
        timezone.utc), nullable=False)
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc),
                        onupdate=lambda: datetime.now(timezone.utc), nullable=False)
