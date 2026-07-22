from fastapi import APIRouter

router = APIRouter()

@router.get("/summary")
async def get_analytics_summary():
    return {
        "daily_attacks": [
            {"date": "2026-07-16", "count": 140},
            {"date": "2026-07-17", "count": 185},
            {"date": "2026-07-18", "count": 210},
            {"date": "2026-07-19", "count": 190},
            {"date": "2026-07-20", "count": 310},
            {"date": "2026-07-21", "count": 450},
            {"date": "2026-07-22", "count": 520}
        ],
        "detection_accuracy": 96.8,
        "mttd_minutes": 2.4,
        "mttr_minutes": 8.5,
        "false_positive_rate": 2.1,
        "top_attack_vectors": [
            {"vector": "Spearphishing & Malicious Attachments", "percentage": 38},
            {"vector": "Compromised VPN & Remote Desktop", "percentage": 27},
            {"vector": "SCADA / OT Protocol Abuse", "percentage": 18},
            {"vector": "DNS Data Exfiltration", "percentage": 17}
        ]
    }
