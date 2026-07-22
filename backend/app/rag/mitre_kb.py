MITRE_ATTACK_KNOWLEDGE_BASE = [
    {
        "technique_id": "T1078",
        "technique_name": "Valid Accounts",
        "tactic": "Initial Access",
        "description": "Adversaries may obtain and use credentials of existing accounts to gain initial access, privilege escalation, or lateral movement.",
        "mitigation": "Enforce Multi-Factor Authentication (MFA), restrict default account usage, implement strict password policies."
    },
    {
        "technique_id": "T1059.001",
        "technique_name": "PowerShell Execution",
        "tactic": "Execution",
        "description": "Adversaries may abuse PowerShell commands and scripts to execute malicious payloads, bypass script execution policies, and download remote code.",
        "mitigation": "Enable Script Block Logging, constrain language mode, block unapproved PowerShell invocation via AppLocker."
    },
    {
        "technique_id": "T1003.001",
        "technique_name": "LSASS Memory Credential Dumping",
        "tactic": "Credential Access",
        "description": "Adversaries may attempt to access credentials by dumping memory from the Local Security Authority Subsystem Service (LSASS) process.",
        "mitigation": "Enable LSA Protection (RunAsPPL), configure Credential Guard, restrict Administrator privileges."
    },
    {
        "technique_id": "T1021.002",
        "technique_name": "SMB / Windows Admin Shares",
        "tactic": "Lateral Movement",
        "description": "Adversaries may use valid credentials to interact with remote SMB administrative shares (C$, ADMIN$) to move laterally and execute commands.",
        "mitigation": "Disable SMBv1, restrict remote admin share access, block inbound port 445 across internal segments."
    },
    {
        "technique_id": "T1486",
        "technique_name": "Data Encrypted for Impact",
        "tactic": "Impact",
        "description": "Adversaries may encrypt data on target systems to interrupt availability and demand ransom payments.",
        "mitigation": "Maintain immutable offsite backups, implement automated endpoint host isolation, deploy behavior-based anti-ransomware agents."
    },
    {
        "technique_id": "T1071.004",
        "technique_name": "DNS Data Exfiltration",
        "tactic": "Exfiltration",
        "description": "Adversaries may communicate over DNS protocols to exfiltrate sensitive data or command and control beaconing.",
        "mitigation": "Deploy DNS Sinkholing, inspect DNS query length and subdomains, restrict egress port 53 to trusted resolvers."
    },
    {
        "technique_id": "T0855",
        "technique_name": "Unauthorized Command Message in SCADA / Industrial Systems",
        "tactic": "Impair Process Control",
        "description": "Adversaries may send unauthorized commands directly to Programmable Logic Controllers (PLCs) or HMIs over Modbus/DNP3 protocols.",
        "mitigation": "Implement OT network microsegmentation, deploy industrial deep packet inspection (DPI), enforce read-only PLC register controls."
    }
]

def search_mitre_kb(query: str) -> list[dict]:
    query_lower = query.lower()
    results = []
    for item in MITRE_ATTACK_KNOWLEDGE_BASE:
        if (query_lower in item["technique_id"].lower() or 
            query_lower in item["technique_name"].lower() or 
            query_lower in item["tactic"].lower() or
            query_lower in item["description"].lower()):
            results.append(item)
    return results if results else MITRE_ATTACK_KNOWLEDGE_BASE[:3]
