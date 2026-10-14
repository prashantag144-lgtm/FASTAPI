from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_tables()
    print("database tables created")
    yield
    # Shutdown: cleanup here
    print("Shutting down the app")
    

app=FastAPI(
    title="Rangmanch Review API",
    description="Theatre reviews API for pune rangmanch",
    lifespan=lifespan
)

@app.get("/")
def root():
    return {"message":"Welcome to rungmanch review api"}


