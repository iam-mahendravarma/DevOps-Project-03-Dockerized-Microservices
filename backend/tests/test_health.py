import pytest
from httpx import AsyncClient
from main import app


@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.get("/")
    assert resp.status_code == 200
    assert "Welcome" in resp.json().get("message", "")


