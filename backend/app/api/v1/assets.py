from fastapi import APIRouter
from app.services.simulator_engine import simulator_engine

router = APIRouter()

@router.get("")
async def list_assets():
    assets = simulator_engine.hosts
    formatted = []
    for idx, a in enumerate(assets):
        formatted.append({
            "id": f"ast_00{idx+1}",
            "hostname": a["hostname"],
            "ip_address": a["ip"],
            "mac_address": f"00:50:56:AB:00:0{idx+1}",
            "asset_type": a["type"],
            "environment": a["env"],
            "operating_system": "Windows Server 2022" if "SRV" in a["hostname"] else ("Ubuntu 22.04 LTS" if "FW" in a["hostname"] else "FreeRTOS SCADA Firmware"),
            "criticality_score": a["crit"],
            "status": "Compromised" if idx in [0, 5] else "Healthy",
            "owner": "CNI Infrastructure Operations",
            "last_seen": "2026-07-22T12:00:00"
        })
    return formatted
