from fastapi import APIRouter
from app.api.v1 import (
    auth, dashboard, incidents, events, mitre,
    threat_intel, attack_graph, assets, uba, response,
    copilot, analytics, simulator
)

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
api_router.include_router(incidents.router, prefix="/incidents", tags=["Incidents"])
api_router.include_router(events.router, prefix="/events", tags=["Events"])
api_router.include_router(mitre.router, prefix="/mitre", tags=["MITRE ATT&CK"])
api_router.include_router(threat_intel.router, prefix="/threat-intel", tags=["Threat Intelligence"])
api_router.include_router(attack_graph.router, prefix="/attack-graph", tags=["Attack Graph"])
api_router.include_router(assets.router, prefix="/assets", tags=["Assets"])
api_router.include_router(uba.router, prefix="/uba", tags=["User Behavior Analytics"])
api_router.include_router(response.router, prefix="/response", tags=["Response SOAR"])
api_router.include_router(copilot.router, prefix="/copilot", tags=["SOC Copilot"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])
api_router.include_router(simulator.router, prefix="/simulator", tags=["Simulator Engine"])
