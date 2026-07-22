from app.agents.state import AgentState

def report_agent_node(state: AgentState) -> AgentState:
    """
    Report Agent: Auto-generates markdown/executive report summarizing incident findings.
    """
    incidents = state.get("correlated_incidents", [])
    risk = state.get("composite_risk_score", 50)
    mitre = state.get("mitre_mappings", [])
    next_step = state.get("predicted_next_step", {})
    logs = list(state.get("agent_logs", []))

    report = f"""# SENTINEL-AI EXECUTIVE INCIDENT BRIEFING
**Security Operations Center (SOC) Automated Intelligence Report**

---

### Executive Summary
- **Overall Threat Index**: {risk}/100
- **Total Correlated Incidents**: {len(incidents)}
- **Highest Severity Level**: Critical
- **Primary Attack Stage**: {next_step.get('current_phase', 'Lateral Movement')}

---

### Observed MITRE ATT&CK Techniques
"""
    for m in mitre:
        report += f"- **[{m.get('tactic')}]** `{m.get('technique_id')}` - {m.get('technique_name')} (Confidence: {int(m.get('confidence', 0.9)*100)}%)\n"

    report += f"""
---

### Predictive Threat Analysis
- **Attacker Next Expected Action**: {next_step.get('predicted_next_step', 'Unknown')}
- **Prediction Confidence**: {int(next_step.get('confidence', 0.85)*100)}%

---

### Recommended Containment Actions
1. **Host Isolation**: Quarantine affected endpoints from internal networks.
2. **Credential Invalidation**: Force password reset & revoke session tokens for compromised domain accounts.
3. **Firewall Drop Rules**: Block external C2 IPs at perimeter router.

*Generated automatically by SentinelAI Autonomous Agentic Mesh.*
"""

    logs.append(f"[ReportAgent] Successfully compiled Executive Incident Report.")
    state["generated_report"] = report
    state["agent_logs"] = logs
    return state
