from fastapi import APIRouter
from app.agents.response_agent import response_agent_node
from app.agents.state import AgentState

router = APIRouter()

@router.get("/playbooks")
async def get_recommended_playbooks():
    dummy_state: AgentState = {
        "raw_events": [], "analyzed_events": [], "threat_intel_hits": [], "mitre_mappings": [],
        "correlated_incidents": [], "composite_risk_score": 90, "predicted_next_step": {},
        "recommended_playbook": {}, "generated_report": "", "agent_logs": []
    }
    result = response_agent_node(dummy_state)
    return result["recommended_playbook"]
