from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, authentication, audioRecord, userAccount

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(audioRecord.router)
app.include_router(userAccount.router)
app.include_router(blog.router)
app.include_router(user.router)
