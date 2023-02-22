from fastapi import Depends, APIRouter, HTTPException, status, FastAPI
from sqlalchemy.orm import Session

from . import  models
from .routers import users, auth
from .database import engine


app = FastAPI(title="Haihuwa",
        description="A medical health system",
        version="1.0.0",)


from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["set-cookie"],
)

app.include_router(users.router)
app.include_router(auth.router)
