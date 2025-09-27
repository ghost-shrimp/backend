from datetime import datetime, timezone
from app.models.base import Base
from sqlalchemy import Column, String, Integer,  Boolean, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncAttrs


class Promotion(Base, AsyncAttrs):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    title = Column(String)
    description = Column(Text)
    visible = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc),
                        onupdate=datetime.now(timezone.utc))

    user = relationship("User", back_populates="promotions")
