import pytest
from httpx import AsyncClient


from backend.main import app


@pytest.mark.asyncio
async def test_departments_list():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.get("/departments")
    assert r.status_code == 200
    data = r.json()
    assert "count" in data
    assert "results" in data
    assert data["count"] >= 8
