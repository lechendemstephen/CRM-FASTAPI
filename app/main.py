from fastapi import FastAPI 
from .routers import customer_record, users
from .database import Base, engine
from . import models


app = FastAPI()

Base = models.Base.metadata.create_all(bind=engine)


app.include_router(customer_record.router)
app.include_router(users.router)

