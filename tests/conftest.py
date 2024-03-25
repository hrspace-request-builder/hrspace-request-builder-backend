import asyncio
from typing import AsyncGenerator

import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker

from app.core.dependencies import get_async_session
from app.data.load_data import load_models_data
from app.models.models import Base
from app.core.config import settings
from app.main import app

engine_test = create_async_engine(settings.database_url, echo=True)
TestingSessionLocal = async_sessionmaker(engine_test, expire_on_commit=False)

async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with TestingSessionLocal() as session:
        yield session

app.dependency_overrides[get_async_session] = override_get_async_session

@pytest_asyncio.fixture(autouse=True)
async def prepare_database():
   async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
   yield
   async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

# SETUP
@pytest_asyncio.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

#client = TestClient(app)

@pytest_asyncio.fixture(scope="session")
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(
        app=app,
        base_url="http://localhost/api/v1/hrspace"
    ) as client:
        yield client
