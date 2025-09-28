from sqlalchemy import Column, Integer, String
from app.models.base import Base
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)

    tasks = relationship("Task", back_populates="category")
