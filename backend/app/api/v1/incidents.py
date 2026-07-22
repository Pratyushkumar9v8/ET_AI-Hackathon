from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.schemas import IncidentResponse

router = APIRouter()

MOCK_INCIDENTS = [
    {
        "id": "inc_ransomware_001",
        "title": "Multi-Stage APT Ransomware Outbreak on Domain Controller",
        "summary": "Correlated Mimikatz LSASS memory dumping, PowerShell obfuscated payload execution, and volume shadow copy deletion across host SRV-DC-01.",
        "severity": "Critical",
        "status": "In Progress",
        "risk_score": 98,
        "assigned_to": "analyst@sentinel.cni.gov",
        "root_cause_asset_id": "ast_srv_dc_01",
        "ai_explanation": "Attacker gained initial foothold via spearphishing link on WKSTN-FIN-08, dumped LSASS credentials, moved laterally via WMI to SRV-DC-01, and attempted shadow copy wiping prior to mass encryption.",
        "predicted_next_step": "Lateral movement to OT SCADA gateway subnets & Data Encrypted for Impact (T1486)",
        "prediction_confidence": 0.94,
        "created_at": "2026-07-22T10:15:00",
        "updated_at": "2026-07-22T10:30:00",
        "mitre_mappings": [
            {"id": "m1", "tactic": "Initial Access", "technique_id": "T1078", "technique_name": "Valid Accounts", "confidence": 0.95, "observed_at": "2026-07-22T10:15:00"},
            {"id": "m2", "tactic": "Execution", "technique_id": "T1059.001", "technique_name": "PowerShell", "confidence": 0.92, "observed_at": "2026-07-22T10:16:00"},
            {"id": "m3", "tactic": "Credential Access", "technique_id": "T1003.001", "technique_name": "LSASS Memory Credential Dumping", "confidence": 0.99, "observed_at": "2026-07-22T10:20:00"},
            {"id": "m4", "tactic": "Impact", "technique_id": "T1490", "technique_name": "Inhibit System Recovery", "confidence": 0.98, "observed_at": "2026-07-22T10:25:00"}
        ],
        "responses": [
            {"id": "r1", "action_type": "Isolate Endpoint", "target": "SRV-DC-01", "status": "Success", "executed_by": "AI Response Agent", "executed_at": "2026-07-22T10:26:00", "output_log": "Host SRV-DC-01 isolated at network layer."},
            {"id": "r2", "action_type": "Block IP", "target": "198.51.100.42", "status": "Success", "executed_by": "AI Response Agent", "executed_at": "2026-07-22T10:26:30", "output_log": "Firewall ACL updated."}
        ]
    },
    {
        "id": "inc_scada_002",
        "title": "Unauthorized SCADA PLC Register Overwrite in Water Dosing Station",
        "summary": "Rogue insider attempted direct Modbus write register commands to alter chemical dosing parameters.",
        "severity": "Critical",
        "status": "Open",
        "risk_score": 92,
        "assigned_to": None,
        "root_cause_asset_id": "ast_hmi_01",
        "ai_explanation": "Direct connection established from HMI-WATER-PUMP-01 sending unauthorized Modbus function code 0x06 write commands to PLC registers 40001.",
        "predicted_next_step": "Safety Instrumented System (SIS) override to bypass physical pressure reliefs",
        "prediction_confidence": 0.96,
        "created_at": "2026-07-22T11:05:00",
        "updated_at": "2026-07-22T11:05:00",
        "mitre_mappings": [
            {"id": "m5", "tactic": "Impair Process Control", "technique_id": "T0855", "technique_name": "Unauthorized Command Message in SCADA", "confidence": 0.96, "observed_at": "2026-07-22T11:05:00"}
        ],
        "responses": []
    },
    {
        "id": "inc_vpn_003",
        "title": "Suspicious VPN Login from Anomaly Location & DNS Tunneling",
        "summary": "User account m.taylor authenticated via VPN from Russian IP, followed by high-frequency TXT DNS queries.",
        "severity": "High",
        "status": "Open",
        "risk_score": 78,
        "assigned_to": "analyst@sentinel.cni.gov",
        "root_cause_asset_id": "ast_vpn_01",
        "ai_explanation": "Impossible travel anomaly combined with DNS exfiltration signature to bad-domain-exfil.com.",
        "predicted_next_step": "Staging sensitive database files for cloud upload",
        "prediction_confidence": 0.88,
        "created_at": "2026-07-22T09:40:00",
        "updated_at": "2026-07-22T09:45:00",
        "mitre_mappings": [
            {"id": "m6", "tactic": "Exfiltration", "technique_id": "T1071.004", "technique_name": "DNS Data Exfiltration", "confidence": 0.88, "observed_at": "2026-07-22T09:40:00"}
        ],
        "responses": []
    }
]

@router.get("", response_model=List[IncidentResponse])
async def list_incidents(severity: str = None, status: str = None):
    results = MOCK_INCIDENTS
    if severity:
        results = [i for i in results if i["severity"].lower() == severity.lower()]
    if status:
        results = [i for i in results if i["status"].lower() == status.lower()]
    return results

@router.get("/{incident_id}", response_model=IncidentResponse)
async def get_incident_detail(incident_id: str):
    for inc in MOCK_INCIDENTS:
        if inc["id"] == incident_id:
            return inc
    raise HTTPException(status_code=404, detail="Incident not found")

@router.post("/{incident_id}/trigger-action")
async def trigger_incident_action(incident_id: str, action: str, target: str):
    for inc in MOCK_INCIDENTS:
        if inc["id"] == incident_id:
            new_action = {
                "id": f"r_{len(inc['responses'])+1}",
                "action_type": action,
                "target": target,
                "status": "Success",
                "executed_by": "SOC Analyst (Manual Action)",
                "executed_at": "2026-07-22T12:00:00",
                "output_log": f"Successfully executed containment action: {action} on target {target}."
            }
            inc["responses"].append(new_action)
            inc["status"] = "Contained"
            return {"status": "success", "message": f"Action {action} executed on {target}", "response": new_action}
    raise HTTPException(status_code=404, detail="Incident not found")
