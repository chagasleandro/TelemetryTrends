from fastapi import FastAPI
from pydantic import BaseModel
from .simulator import start_simulator
from .storage import InMemoryStorage
import os

app = FastAPI(title="TelemetryTrends (TTE) - Demo")
storage = InMemoryStorage()

class Telemetry(BaseModel):
    device_id: str
    metric: str
    value: float
    ts: float

@app.post("/telemetry", status_code=201)
async def ingest(t: Telemetry):
    storage.save(t.dict())
    return {"status": "ok"}

@app.get("/metrics/{device_id}")
async def get_metrics(device_id: str, limit: int = 100):
    data = storage.query(device_id)
    return data[-limit:]

if __name__ == "__main__":
    import uvicorn
    if os.getenv("TTE_START_SIMULATOR", "false").lower() in ("1","true","yes"):
        start_simulator(storage, count=3)
    uvicorn.run("telemetrytrends.main:app", host="0.0.0.0", port=8000, reload=True)
