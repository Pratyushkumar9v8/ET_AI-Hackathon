from fastapi import APIRouter
from app.ml.graph_analyzer import graph_analyzer
from app.services.simulator_engine import simulator_engine

router = APIRouter()

@router.get("/{incident_id}")
async def get_attack_graph(incident_id: str):
    events = simulator_engine.generate_synthetic_events(count=10, scenario="ransomware")
    graph_data = graph_analyzer.build_attack_graph_for_incident(events)
    return graph_data
