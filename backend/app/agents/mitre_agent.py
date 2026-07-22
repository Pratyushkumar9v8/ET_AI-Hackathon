from app.agents.state import AgentState

def mitre_agent_node(state: AgentState) -> AgentState:
    """
    MITRE Agent: Maps observed technical indicators to MITRE ATT&CK tactics & techniques.
    """
    events = state.get("analyzed_events", [])
    mappings = []
    logs = list(state.get("agent_logs", []))

    for evt in events:
        cmd = str(evt.get("process_command_line", "")).lower()
        src_type = str(evt.get("source_type", ""))

        if "vssadmin delete shadows" in cmd or "wbadmin delete catalog" in cmd:
            mappings.append({"tactic": "Impact", "technique_id": "T1490", "technique_name": "Inhibit System Recovery", "confidence": 0.98})
        elif "powershell" in cmd or "-enc" in cmd:
            mappings.append({"tactic": "Execution", "technique_id": "T1059.001", "technique_name": "PowerShell", "confidence": 0.92})
        elif "mimikatz" in cmd or "sekurlsa" in cmd:
            mappings.append({"tactic": "Credential Access", "technique_id": "T1003.001", "technique_name": "LSASS Memory Credential Dumping", "confidence": 0.99})
        elif "wmic" in cmd or "psexec" in cmd or "winrm" in cmd:
            mappings.append({"tactic": "Lateral Movement", "technique_id": "T1021.002", "technique_name": "SMB / Windows Admin Shares", "confidence": 0.91})
        elif "modbus" in src_type.lower() or "write_single_register" in cmd:
            mappings.append({"tactic": "Impair Process Control", "technique_id": "T0855", "technique_name": "Unauthorized Command Message in SCADA", "confidence": 0.95})
        elif evt.get("is_anomaly") and evt.get("destination_port") == 53:
            mappings.append({"tactic": "Exfiltration", "technique_id": "T1071.004", "technique_name": "DNS Data Exfiltration", "confidence": 0.88})

    logs.append(f"[MITREAgent] Mapped event indicators to {len(mappings)} MITRE ATT&CK techniques.")
    state["mitre_mappings"] = mappings
    state["agent_logs"] = logs
    return state
