import pytest
from httpx import AsyncClient

import app.main
from tests import conftest

@pytest.mark.asyncio
async def test_get_cities(ac: AsyncClient):
    params = {"id": 2, "name": "Москва"}
    response = await ac.get("/cities")
    assert response.status_code == 200
