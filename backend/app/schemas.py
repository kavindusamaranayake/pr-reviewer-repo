from pydantic import BaseModel

class ReviewResponse(BaseModel):
    id: int
    pr_title: str
    branch: str
    review_data: dict
    status: str
