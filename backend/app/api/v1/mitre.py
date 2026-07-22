from fastapi import APIRouter
from app.rag.mitre_kb import MITRE_ATTACK_KNOWLEDGE_BASE

router = APIRouter()

TACTICS = [
    "Initial Access", "Execution", "Persistence", "Privilege Escalation", 
    "Credential Access", "Discovery", "Lateral Movement", "Collection", 
    "Exfiltration", "Impact", "Impair Process Control"
]

@router.get("/matrix")
async def get_mitre_matrix():
    # Build full matrix grid structure
    matrix = {}
    for tactic in TACTICS:
        matrix[tactic] = [
            item for item in MITRE_ATTACK_KNOWLEDGE_BASE if item["tactic"] == tactic
        ]
        # Add extra fallback techniques for rich visualization
        if not matrix[tactic]:
            matrix[tactic] = [{
                "technique_id": "T1000",
                "technique_name": f"Generic {tactic} Pattern",
                "tactic": tactic,
                "description": "Monitored tactic category",
                "mitigation": "Standard policy control."
            }]
    return {"tactics": TACTICS, "matrix": matrix}

@router.get("/stats")
async def get_mitre_stats():
    return [
        {"tactic": "Credential Access", "active_count": 8, "risk_impact": "High"},
        {"tactic": "Lateral Movement", "active_count": 6, "risk_impact": "Critical"},
        {"tactic": "Impact", "active_count": 4, "risk_impact": "Critical"},
        {"tactic": "Exfiltration", "active_count": 3, "risk_impact": "Medium"}
    ]
