from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from fastapi import FastAPI

from app.admin import admin
from app.api.routers import main_router
from app.core.config import settings
from app.core.dependencies import engine
from app.models.base import Base


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, Any]:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title=settings.app_title, description=settings.app_description, lifespan=lifespan
)

app.include_router(main_router)
admin.mount_to(app)
