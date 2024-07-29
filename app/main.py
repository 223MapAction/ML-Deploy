from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.apis import main_router
from .database import database
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_router.router, prefix="/api1", tags=["api1"])
