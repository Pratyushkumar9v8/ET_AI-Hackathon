from fastapi import APIRouter

router = APIRouter()

@router.get("/anomalies")
async def get_uba_anomalies():
    return [
        {
            "user_name": "m.taylor",
            "anomaly_type": "Impossible Travel",
            "normal_baseline": "Login from Washington, USA (192.168.1.50)",
            "current_activity": "Login from Moscow, RU (203.0.113.15)",
            "risk_score": 88,
            "detected_at": "2026-07-22T09:40:00"
        },
        {
            "user_name": "administrator",
            "anomaly_type": "Abnormal PowerShell Execution",
            "normal_baseline": "Standard GUI administrative tooling",
            "current_activity": "Base64 encoded string invocation in background session",
            "risk_score": 95,
            "detected_at": "2026-07-22T10:16:00"
        },
        {
            "user_name": "r.insider",
            "anomaly_type": "Off-Hours SCADA Register Tampering",
            "normal_baseline": "Read-only HMI telemetry monitoring",
            "current_activity": "Modbus function 0x06 single register override",
            "risk_score": 98,
            "detected_at": "2026-07-22T11:05:00"
        }
    ]
