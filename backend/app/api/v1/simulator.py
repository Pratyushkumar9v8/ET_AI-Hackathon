from fastapi import APIRouter
from app.services.simulator_engine import simulator_engine
from app.agents.graph import run_agent_pipeline

router = APIRouter()

@router.post("/run-scenario")
async def trigger_simulation_scenario(scenario: str = "ransomware", count: int = 1000):
    events = simulator_engine.generate_synthetic_events(count=count, scenario=scenario)
    anom_events = [e for e in events if e.get("is_anomaly")]
    
    # Run events through LangGraph Agent Mesh
    pipeline_result = run_agent_pipeline(anom_events)
    
    return {
        "status": "success",
        "scenario": scenario,
        "total_generated_events": len(events),
        "anomalous_events_detected": len(anom_events),
        "composite_risk_score": pipeline_result.get("composite_risk_score"),
        "predicted_next_step": pipeline_result.get("predicted_next_step"),
        "agent_logs": pipeline_result.get("agent_logs")
    }
