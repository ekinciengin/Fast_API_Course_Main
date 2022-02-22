from fastapi import FastAPI
from . import models
from .database import engine
from .routers import authentication, audioRecord, userAccount

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(audioRecord.router)
app.include_router(userAccount.router)
