from app.ml.anomaly_detector import anomaly_engine
from app.agents.state import AgentState

def behavior_agent_node(state: AgentState) -> AgentState:
    """
    Behavior Agent: Uses Isolation Forest & Rule Heuristics to detect anomalies
    in raw events batch.
    """
    raw_events = state.get("raw_events", [])
    analyzed = []
    logs = list(state.get("agent_logs", []))

    anomalies_found = 0
    for evt in raw_events:
        score, is_anom = anomaly_engine.predict_anomaly(evt)
        evt_copy = dict(evt)
        evt_copy["anomaly_score"] = score
        evt_copy["is_anomaly"] = is_anom
        if is_anom:
            anomalies_found += 1
        analyzed.append(evt_copy)

    logs.append(f"[BehaviorAgent] Processed {len(raw_events)} events. Identified {anomalies_found} behavioral anomalies.")
    state["analyzed_events"] = analyzed
    state["agent_logs"] = logs
    return state
