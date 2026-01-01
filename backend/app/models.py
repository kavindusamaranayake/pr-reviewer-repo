from sqlalchemy import Column, Integer, String, JSON
from .database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    pr_title = Column(String)
    branch = Column(String)
    review_data = Column(JSON)
    status = Column(String, default="PENDING")
