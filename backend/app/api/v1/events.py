from fastapi import APIRouter
from app.services.simulator_engine import simulator_engine

router = APIRouter()

@router.get("")
async def get_events(limit: int = 50, anomaly_only: bool = False):
    events = simulator_engine.generate_synthetic_events(count=limit, scenario="ransomware")
    if anomaly_only:
        events = [e for e in events if e.get("is_anomaly")]
    return events
