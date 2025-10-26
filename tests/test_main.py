import time
from fastapi.testclient import TestClient
from telemetrytrends.main import app

client = TestClient(app)

def test_ingest_and_get():
    payload = {"device_id":"d1","metric":"temp","value":25.5,"ts": time.time()}
    r = client.post("/telemetry", json=payload)
    assert r.status_code == 201
    r2 = client.get("/metrics/d1")
    assert r2.status_code == 200
    assert isinstance(r2.json(), list)
    assert any(item["device_id"] == "d1" for item in r2.json())
