import pytest
from httpx import AsyncClient

import app.main
from app.repositories import crud
from tests import conftest

pytest_mark_anyio = pytest.mark.asyncio

@pytest_mark_anyio
async def test_get_cities(client: AsyncClient):
    response = await client.get("/cities")
    assert response.status_code == 200

@pytest_mark_anyio
async def test_get_vacancy_names(client: AsyncClient):
    response = await client.get("/vacancy_names")
    assert response.status_code == 200

@pytest_mark_anyio
async def test_get_categories(client: AsyncClient):
    response = await client.get("/categories")
    assert response.status_code == 200

@pytest_mark_anyio
async def test_get_specialization(client: AsyncClient):
    specialization = await crud.create_specialization(
        conftest.override_get_async_session(), vacancy_name_id=1)
    response = await client.get(f"/specializations/{specialization.id}")
    assert response.status_code == 200
    assert response.json()["id"] == specialization.id
