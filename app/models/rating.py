
from app.models.base import BaseModel
from sqlalchemy import Column, Integer, ForeignKey, String, Text
from sqlalchemy.orm import relationship


class Rating(BaseModel):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    rater_id = Column(String, ForeignKey("users.id"), nullable=False)
    rated_id = Column(String, ForeignKey("users.id"), nullable=False)
    score = Column(Integer, nullable=False)
    comment = Column(Text)

    rater = relationship("User", foreign_keys=[
                         rater_id], back_populates="ratings_given")
    rated = relationship("User", foreign_keys=[
                         rated_id], back_populates="ratings_received")
