import asyncio
from typing import Any, AsyncGenerator

from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession


async def test_provided_loop_is_running_loop(
    event_loop: asyncio.AbstractEventLoop,
) -> None:
    assert event_loop is asyncio.get_running_loop()


def test_async_client(async_client: AsyncGenerator[AsyncClient, Any]) -> None:
    assert isinstance(async_client, AsyncClient)


def test_init_db_fixture(init_db: AsyncGenerator) -> None:
    assert init_db is None


def test_get_test_session(get_test_session: AsyncSession) -> None:
    assert isinstance(get_test_session, AsyncSession)
