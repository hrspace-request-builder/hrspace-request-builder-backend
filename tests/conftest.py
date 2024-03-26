from typing import Any, AsyncGenerator

from app.core.dependencies import get_async_session
from app.main import app

from .fixtures.db import TestingSessionLocal

pytest_plugins = [
    "tests.fixtures.fixtures",
]


async def override_get_async_session() -> AsyncGenerator[Any, None]:
    async with TestingSessionLocal() as session:
        yield session


app.dependency_overrides[get_async_session] = override_get_async_session
