from datetime import datetime, timezone
from app.models.base import Base
from sqlalchemy import Column,  Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncAttrs


class Subscription(Base, AsyncAttrs):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    start_date = Column(DateTime(timezone=True),
                        default=datetime.now(timezone.utc))
    end_date = Column(DateTime(timezone=True))

    user = relationship("User", back_populates="subscription")
