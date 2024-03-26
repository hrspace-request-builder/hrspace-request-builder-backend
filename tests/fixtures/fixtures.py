from typing import Any, AsyncGenerator

import pytest_asyncio
from httpx import AsyncClient

from app.main import app
from app.models.base import Base

from .db import TestingSessionLocal, test_engine
from .load_csv_data import DATA, load_csv


@pytest_asyncio.fixture(autouse=True, scope="session")
async def init_db() -> AsyncGenerator[None, Any]:
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture
async def get_test_session() -> AsyncGenerator[None, Any]:
    async with TestingSessionLocal() as session:
        yield session


@pytest_asyncio.fixture(scope="session")
async def async_client() -> AsyncGenerator[AsyncClient, Any]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest_asyncio.fixture(scope="session")
async def load_csv_data() -> None:
    for model, scv_file in DATA:
        await load_csv(model, scv_file)
