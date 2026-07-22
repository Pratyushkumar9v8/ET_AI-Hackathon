from app.agents.state import AgentState

def prediction_agent_node(state: AgentState) -> AgentState:
    """
    Prediction Agent: Predicts attacker next phase and technique based on current tactic progression.
    """
    mitre_maps = state.get("mitre_mappings", [])
    logs = list(state.get("agent_logs", []))

    tactics = [m.get("tactic") for m in mitre_maps]

    if "Credential Access" in tactics and "Lateral Movement" not in tactics:
        predicted = {
            "current_phase": "Credential Dumping",
            "predicted_next_step": "Lateral Movement via SMB / WMI Remote Execution",
            "predicted_technique_id": "T1021.002",
            "confidence": 0.89
        }
    elif "Lateral Movement" in tactics and "Impact" not in tactics:
        predicted = {
            "current_phase": "Lateral Movement",
            "predicted_next_step": "Data Encryption for Impact / Mass Ransomware Execution",
            "predicted_technique_id": "T1486",
            "confidence": 0.94
        }
    elif "Impair Process Control" in tactics:
        predicted = {
            "current_phase": "SCADA Tampering",
            "predicted_next_step": "Safety Instrumented System (SIS) Override & Chemical Overflow",
            "predicted_technique_id": "T0826",
            "confidence": 0.96
        }
    else:
        predicted = {
            "current_phase": "Reconnaissance / Initial Access",
            "predicted_next_step": "Privilege Escalation via Local Token Manipulation",
            "predicted_technique_id": "T1134",
            "confidence": 0.78
        }

    logs.append(f"[PredictionAgent] Predicted attacker next step: {predicted['predicted_next_step']} (Confidence: {int(predicted['confidence']*100)}%).")
    state["predicted_next_step"] = predicted
    state["agent_logs"] = logs
    return state
