from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Review

router = APIRouter(prefix="/reviews")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def list_reviews(db: Session = Depends(get_db)):
    return db.query(Review).all()

@router.post("/{review_id}/approve")
def approve_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(Review).get(review_id)
    review.status = "APPROVED"
    db.commit()
    return {"status": "approved"}

@router.post("/{review_id}/reject")
def reject_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(Review).get(review_id)
    review.status = "REJECTED"
    db.commit()
    return {"status": "rejected"}

@router.get("/{review_id}")
def get_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(Review).get(review_id)
    return review
