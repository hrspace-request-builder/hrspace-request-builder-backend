from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.admin import admin
from app.api.routers import main_router
from app.core.config import settings
from app.core.dependencies import engine
from app.data.load_data import load_models_data
from app.models.models import Base


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, Any]:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    await load_models_data()
    yield


app = FastAPI(
    title=settings.app_title, description=settings.app_description, lifespan=lifespan
)

app.include_router(main_router)
admin.mount_to(app)

origins = [
    "http://185.221.162.231",
    "http://185.221.162.231:81",
    "http://localhost",
    "http://localhost:81",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
