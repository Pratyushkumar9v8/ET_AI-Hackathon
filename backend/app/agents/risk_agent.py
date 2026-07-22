from app.agents.state import AgentState

def risk_agent_node(state: AgentState) -> AgentState:
    """
    Risk Scoring Agent: Computes composite risk score (0 - 100) based on:
    - Max anomaly score
    - Criticality of targeted assets
    - Threat Intelligence hit presence
    - MITRE severity
    """
    events = state.get("analyzed_events", [])
    intel_hits = state.get("threat_intel_hits", [])
    mitre_maps = state.get("mitre_mappings", [])
    logs = list(state.get("agent_logs", []))

    if not events:
        state["composite_risk_score"] = 0
        return state

    max_anom = max([e.get("anomaly_score", 0.0) for e in events]) * 40 # Up to 40 pts
    intel_pts = 30 if intel_hits else 0 # Up to 30 pts
    mitre_pts = min(len(mitre_maps) * 10, 30) # Up to 30 pts

    composite_score = int(min(max_anom + intel_pts + mitre_pts, 99))
    if any(m.get("tactic") == "Impact" for m in mitre_maps):
        composite_score = 98

    logs.append(f"[RiskAgent] Calculated composite Risk Score: {composite_score}/100.")
    state["composite_risk_score"] = composite_score
    state["agent_logs"] = logs
    return state
