from fastapi import APIRouter
from app.schemas.schemas import DashboardMetrics

router = APIRouter()

@router.get("/metrics", response_model=DashboardMetrics)
async def get_dashboard_metrics():
    return DashboardMetrics(
        threat_score=87,
        live_attacks_count=3,
        open_incidents_count=5,
        critical_assets_count=7,
        active_users_count=42,
        compromised_hosts_count=2,
        mttd_minutes=2.4,
        mttr_minutes=8.5
    )

@router.get("/timeline")
async def get_dashboard_timeline():
    return [
        {"time": "08:00", "anomalies": 12, "critical": 0},
        {"time": "10:00", "anomalies": 18, "critical": 1},
        {"time": "12:00", "anomalies": 45, "critical": 2},
        {"time": "14:00", "anomalies": 89, "critical": 5},
        {"time": "16:00", "anomalies": 62, "critical": 3},
        {"time": "18:00", "anomalies": 24, "critical": 1}
    ]

@router.get("/heatmap")
async def get_risk_heatmap():
    return [
        {"zone": "IT Domain Controllers", "risk": 95, "status": "Critical"},
        {"zone": "OT Water Treatment PLCs", "risk": 90, "status": "Critical"},
        {"zone": "Corporate Endpoints", "risk": 65, "status": "Medium"},
        {"zone": "DMZ Firewalls", "risk": 40, "status": "Low"},
        {"zone": "Cloud VPC Subnets", "risk": 30, "status": "Low"}
    ]
