from app.agents.state import AgentState

def correlation_agent_node(state: AgentState) -> AgentState:
    """
    Correlation Agent: Correlates disparate event anomalies (PowerShell + LSASS dump + Lateral movement)
    into a unified high-level Incident object.
    """
    events = state.get("analyzed_events", [])
    anom_events = [e for e in events if e.get("is_anomaly")]
    logs = list(state.get("agent_logs", []))

    correlated = []
    if len(anom_events) >= 1:
        primary_host = anom_events[0].get("hostname", "SRV-DC-01")
        primary_user = anom_events[0].get("user_name", "administrator")
        
        # Determine incident title and severity based on events
        has_ransomware = any("vssadmin" in str(e.get("process_command_line")).lower() for e in anom_events)
        has_ot = any("OT" in str(e.get("source_type")) for e in anom_events)

        if has_ransomware:
            title = f"Multi-Stage APT Ransomware Outbreak on {primary_host}"
            severity = "Critical"
        elif has_ot:
            title = f"Unauthorized SCADA PLC Tampering Detected in Water Treatment Zone"
            severity = "Critical"
        else:
            title = f"Suspicious Privilege Escalation & Lateral Movement from {primary_user}"
            severity = "High"

        summary = f"Correlated {len(anom_events)} anomalous events across host {primary_host} involving user {primary_user}."
        
        correlated.append({
            "title": title,
            "summary": summary,
            "severity": severity,
            "events_count": len(anom_events),
            "primary_host": primary_host,
            "primary_user": primary_user
        })

    logs.append(f"[CorrelationAgent] Aggregated {len(anom_events)} alerts into {len(correlated)} correlated incident(s).")
    state["correlated_incidents"] = correlated
    state["agent_logs"] = logs
    return state
