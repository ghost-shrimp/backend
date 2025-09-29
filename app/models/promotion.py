from app.models.base import BaseModel
from sqlalchemy import Column, String, Integer,  Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.constants import MAX_DESCRIPTION, MAX_TITLE


class Promotion(BaseModel):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    title = Column(String(MAX_TITLE))
    description = Column(String(MAX_DESCRIPTION))
    visible = Column(Boolean, default=True)

    user = relationship("User", back_populates="promotion")
