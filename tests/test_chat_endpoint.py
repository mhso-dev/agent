import pytest
from fastapi.testclient import TestClient
from langchain_core.language_models.fake_chat_models import FakeListChatModel

from src.agent import build_agent
from src.app import app, get_agent


@pytest.fixture
def client(monkeypatch):
    fake = FakeListChatModel(responses=["7 곱하기 6은 42 입니다."])
    monkeypatch.setattr("src.agent.ChatOpenAI", lambda **kw: fake)
    app.dependency_overrides[get_agent] = lambda: build_agent()
    yield TestClient(app)
    app.dependency_overrides.clear()


def test_healthz(client):
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_chat_simple(client):
    r = client.post("/chat", json={"message": "7 곱하기 6"})
    assert r.status_code == 200
    body = r.json()
    assert "42" in body["answer"]
