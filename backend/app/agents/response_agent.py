from app.agents.state import AgentState

def response_agent_node(state: AgentState) -> AgentState:
    """
    Response Agent: Recommends dynamic SOAR playbook actions based on incident type and risk score.
    """
    incidents = state.get("correlated_incidents", [])
    risk = state.get("composite_risk_score", 50)
    logs = list(state.get("agent_logs", []))

    actions = [
        {"action": "Isolate Endpoint Host", "target": "SRV-DC-01", "recommended": True},
        {"action": "Block External Malicious IP", "target": "198.51.100.42", "recommended": True},
        {"action": "Revoke Compromised User Token", "target": "administrator@cni.gov", "recommended": True},
        {"action": "Kill Suspicious Process Tree", "target": "PID 4820 (powershell.exe)", "recommended": True},
        {"action": "Enforce OT SCADA Read-Only Interlock", "target": "PLC-WATER-PUMP-01", "recommended": risk > 80}
    ]

    playbook = {
        "playbook_name": "SOAR Automated Containment & Threat Isolation",
        "risk_threshold": 75,
        "actions": actions,
        "auto_executable": risk >= 85
    }

    logs.append(f"[ResponseAgent] Formulated containment playbook with {len(actions)} recommended actions.")
    state["recommended_playbook"] = playbook
    state["agent_logs"] = logs
    return state
