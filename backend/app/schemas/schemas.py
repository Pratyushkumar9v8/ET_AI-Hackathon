from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, EmailStr, Field

# User Schemas
class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    role: str = "SOC Analyst"

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: str
    is_active: bool
    created_at: datetime
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse

# Asset Schemas
class AssetResponse(BaseModel):
    id: str
    hostname: str
    ip_address: str
    mac_address: Optional[str] = None
    asset_type: str
    environment: str
    operating_system: Optional[str] = None
    criticality_score: int
    status: str
    owner: Optional[str] = None
    last_seen: datetime
    class Config:
        from_attributes = True

# Event Schemas
class EventCreate(BaseModel):
    source_type: str
    host_id: Optional[str] = None
    source_ip: Optional[str] = None
    destination_ip: Optional[str] = None
    source_port: Optional[int] = None
    destination_port: Optional[int] = None
    user_name: Optional[str] = None
    process_name: Optional[str] = None
    process_command_line: Optional[str] = None
    event_code: Optional[str] = None
    raw_payload: Dict[str, Any]

class EventResponse(EventCreate):
    id: str
    timestamp: datetime
    anomaly_score: float
    is_anomaly: bool
    class Config:
        from_attributes = True

# Incident & MITRE Schemas
class MitreMappingResponse(BaseModel):
    id: str
    tactic: str
    technique_id: str
    technique_name: str
    confidence: float
    observed_at: datetime
    class Config:
        from_attributes = True

class ResponseActionResponse(BaseModel):
    id: str
    action_type: str
    target: str
    status: str
    executed_by: str
    executed_at: datetime
    output_log: Optional[str] = None
    class Config:
        from_attributes = True

class IncidentResponse(BaseModel):
    id: str
    title: str
    summary: Optional[str] = None
    severity: str
    status: str
    risk_score: int
    assigned_to: Optional[str] = None
    root_cause_asset_id: Optional[str] = None
    ai_explanation: Optional[str] = None
    predicted_next_step: Optional[str] = None
    prediction_confidence: float
    created_at: datetime
    updated_at: datetime
    mitre_mappings: List[MitreMappingResponse] = []
    responses: List[ResponseActionResponse] = []
    class Config:
        from_attributes = True

# Attack Graph Schemas
class GraphNode(BaseModel):
    id: str
    label: str
    type: str  # User, Device, IP, Process
    risk_level: str
    metadata: Optional[Dict[str, Any]] = None

class GraphEdge(BaseModel):
    id: str
    source: str
    target: str
    relationship: str

class AttackGraphResponse(BaseModel):
    nodes: List[GraphNode]
    edges: List[GraphEdge]

# SOC Copilot Schemas
class CopilotMessage(BaseModel):
    message: str
    incident_id: Optional[str] = None

class CopilotResponse(BaseModel):
    response: str
    sources: List[str] = []
    suggested_actions: List[str] = []
    mitre_techniques: List[str] = []

# Dashboard Schemas
class DashboardMetrics(BaseModel):
    threat_score: int
    live_attacks_count: int
    open_incidents_count: int
    critical_assets_count: int
    active_users_count: int
    compromised_hosts_count: int
    mttd_minutes: float
    mttr_minutes: float
