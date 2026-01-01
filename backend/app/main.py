from fastapi import FastAPI
from .database import Base, engine
from .webhook import router as webhook_router
from .reviews import router as reviews_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(webhook_router)
app.include_router(reviews_router)
