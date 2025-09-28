from app.models.base import BaseModel
from sqlalchemy import Column, String, Integer,  Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship


class Promotion(BaseModel):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    title = Column(String)
    description = Column(Text)
    visible = Column(Boolean, default=True)

    user = relationship("User", back_populates="promotion")
