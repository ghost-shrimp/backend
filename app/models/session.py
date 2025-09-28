from datetime import datetime, timezone
from app.models.base import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Session(BaseModel):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    refresh_token = Column(String, unique=True, nullable=False)
    ip_address = Column(String, nullable=True)
    user_agent = Column(String, nullable=True)
    expires_at = Column(DateTime(timezone=True), nullable=False)
    last_active = Column(DateTime(timezone=True),
                         default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="sessions")
