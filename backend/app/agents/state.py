from typing import TypedDict, List, Dict, Any, Optional

class AgentState(TypedDict):
    raw_events: List[Dict[str, Any]]
    analyzed_events: List[Dict[str, Any]]
    threat_intel_hits: List[Dict[str, Any]]
    mitre_mappings: List[Dict[str, Any]]
    correlated_incidents: List[Dict[str, Any]]
    composite_risk_score: int
    predicted_next_step: Dict[str, Any]
    recommended_playbook: Dict[str, Any]
    generated_report: Optional[str]
    agent_logs: List[str]
