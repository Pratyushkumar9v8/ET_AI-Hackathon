import asyncio
import random
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.api.websockets.manager import ws_manager

router = APIRouter()

@router.websocket("/ws/live-stream")
async def websocket_endpoint(websocket: WebSocket):
    await ws_manager.connect(websocket)
    try:
        while True:
            # Simulate real-time streaming telemetry ping every 3 seconds
            await asyncio.sleep(3)
            live_event = {
                "type": "LIVE_TELEMETRY",
                "timestamp": "2026-07-22T12:00:00",
                "source_type": random.choice(["Sysmon", "Firewall", "OT_Modbus", "DNS"]),
                "hostname": random.choice(["SRV-DC-01", "WKSTN-FIN-08", "HMI-WATER-PUMP-01"]),
                "anomaly_score": round(random.uniform(0.1, 0.95), 2),
                "is_anomaly": random.choice([True, False, False])
            }
            await ws_manager.broadcast(live_event)
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)
