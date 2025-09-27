from datetime import datetime, timezone
from app.models.base import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncAttrs


class Rating(Base, AsyncAttrs):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    rater_id = Column(String, ForeignKey("users.id"), nullable=False)
    rated_id = Column(String, ForeignKey("users.id"), nullable=False)
    score = Column(Integer, nullable=False)
    comment = Column(Text)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    rater = relationship("User", foreign_keys=[
                         rater_id], back_populates="ratings_given")
    rated = relationship("User", foreign_keys=[
                         rated_id], back_populates="ratings_received")
