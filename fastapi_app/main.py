from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.v1 import endpoints
from app.core.database import engine, Base

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

Base.metadata.create_all(bind=engine)

app.include_router(endpoints.router)
