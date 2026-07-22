from fastapi import APIRouter
from app.agents.threat_intel_agent import KNOWN_MALICIOUS_IOCS

router = APIRouter()

@router.get("/iocs")
async def get_threat_intel_list():
    iocs = []
    for val, meta in KNOWN_MALICIOUS_IOCS.items():
        iocs.append({
            "ioc_value": val,
            "ioc_type": meta["type"],
            "threat_actor": meta["actor"],
            "malware_family": meta["malware"],
            "confidence_score": meta["confidence"],
            "source": "Sentinel Global Threat Feed",
            "last_updated": "2026-07-22T08:00:00"
        })
    return iocs

@router.get("/lookup/{ioc_value}")
async def lookup_ioc(ioc_value: str):
    if ioc_value in KNOWN_MALICIOUS_IOCS:
        return {"status": "MALICIOUS", "details": KNOWN_MALICIOUS_IOCS[ioc_value]}
    return {"status": "CLEAN", "ioc_value": ioc_value, "details": "No known threat intelligence match found."}
