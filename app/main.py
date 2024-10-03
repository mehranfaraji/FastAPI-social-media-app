from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import post, user, auth, vote
from . import models
from .database import engine
from .config import settings

## this line creates the tables if they don't already exist
## we don't need the line below, since alembic will take care of
## creatign tables and upgrade/downgrade changes into our database
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins= ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Welcome to my social media app"}

