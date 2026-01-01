from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Review
from .reviewer import generate_review

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/webhook/github")
def github_webhook(payload: dict, db: Session = Depends(get_db)):
    pr = payload["pull_request"]
    branch = pr["head"]["ref"]
    title = pr["title"]

    review = Review(
        pr_title=title,
        branch=branch,
        review_data=generate_review(branch, title)
    )

    db.add(review)
    db.commit()

    return {"status": "review created"}
