from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from database import check_connection, engine, Base
# Import routers

@asynccontextmanager
async def lifespan(app: FastAPI):
    # This runs exactly when Uvicorn starts
    check_connection() 
    yield
    # Any shutdown logic would go here

app = FastAPI(lifespan=lifespan)

# Create tables
Base.metadata.create_all(bind=engine)

