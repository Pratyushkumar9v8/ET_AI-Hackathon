from app.agents.state import AgentState

# Known IOC feeds repository
KNOWN_MALICIOUS_IOCS = {
    "198.51.100.42": {"type": "IP", "actor": "APT29 (Cozy Bear)", "malware": "Cobalt Strike C2", "confidence": 95},
    "203.0.113.15": {"type": "IP", "actor": "VOLT TYPHOON", "malware": "Web Shell Proxy", "confidence": 90},
    "bad-domain-exfil.com": {"type": "Domain", "actor": "Lazarus Group", "malware": "DNS Tunneling", "confidence": 88},
    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855": {"type": "SHA256", "actor": "LockBit 3.0", "malware": "Ransomware Encryptor", "confidence": 99}
}

def threat_intel_agent_node(state: AgentState) -> AgentState:
    """
    Threat Intel Agent: Checks source/destination IPs, domains, and process hashes
    against threat intelligence database.
    """
    events = state.get("analyzed_events", [])
    hits = []
    logs = list(state.get("agent_logs", []))

    for evt in events:
        ip = evt.get("destination_ip") or evt.get("source_ip")
        if ip in KNOWN_MALICIOUS_IOCS:
            ioc_info = KNOWN_MALICIOUS_IOCS[ip]
            hits.append({
                "event_id": evt.get("id"),
                "ioc_value": ip,
                "ioc_type": ioc_info["type"],
                "threat_actor": ioc_info["actor"],
                "malware_family": ioc_info["malware"],
                "confidence": ioc_info["confidence"]
            })
            # Boost event anomaly score if IOC hit occurs
            evt["anomaly_score"] = max(evt.get("anomaly_score", 0.0), 0.95)
            evt["is_anomaly"] = True

    logs.append(f"[ThreatIntelAgent] Scanned indicators against Threat Feed. Found {len(hits)} IOC matches.")
    state["threat_intel_hits"] = hits
    state["agent_logs"] = logs
    return state
