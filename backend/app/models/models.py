import uuid
from datetime import datetime
from sqlalchemy import (
    Column, String, Integer, Float, Boolean, DateTime, Text, ForeignKey, JSON, Numeric, Table
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

def generate_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=True)
    full_name = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False, default="SOC Analyst") # Admin, SOC Analyst, Security Engineer, Viewer
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Asset(Base):
    __tablename__ = "assets"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    hostname = Column(String(255), unique=True, nullable=False, index=True)
    ip_address = Column(String(45), nullable=False)
    mac_address = Column(String(17), nullable=True)
    asset_type = Column(String(50), nullable=False) # Server, Endpoint, Router, Switch, Firewall, SCADA/PLC
    environment = Column(String(50), nullable=False, default="IT") # IT, OT, Cloud
    operating_system = Column(String(100), nullable=True)
    criticality_score = Column(Integer, default=50) # 1-100
    status = Column(String(50), default="Healthy") # Healthy, At Risk, Compromised, Isolated
    owner = Column(String(255), nullable=True)
    last_seen = Column(DateTime, default=datetime.utcnow)

    vulnerabilities = relationship("Vulnerability", back_populates="asset", cascade="all, delete-orphan")
    events = relationship("Event", back_populates="asset")

class Vulnerability(Base):
    __tablename__ = "vulnerabilities"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    cve_id = Column(String(50), nullable=False, index=True)
    asset_id = Column(String(36), ForeignKey("assets.id", ondelete="CASCADE"), nullable=False)
    severity = Column(String(20), nullable=False) # Low, Medium, High, Critical
    cvss_score = Column(Float, default=0.0)
    description = Column(Text, nullable=True)
    patch_status = Column(String(50), default="Unpatched")
    discovered_at = Column(DateTime, default=datetime.utcnow)

    asset = relationship("Asset", back_populates="vulnerabilities")

class Event(Base):
    __tablename__ = "events"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    source_type = Column(String(50), nullable=False) # Sysmon, LinuxAudit, Firewall, DNS, VPN, OT_Modbus
    host_id = Column(String(36), ForeignKey("assets.id", ondelete="SET NULL"), nullable=True)
    source_ip = Column(String(45), nullable=True)
    destination_ip = Column(String(45), nullable=True)
    source_port = Column(Integer, nullable=True)
    destination_port = Column(Integer, nullable=True)
    user_name = Column(String(100), nullable=True)
    process_name = Column(String(255), nullable=True)
    process_command_line = Column(Text, nullable=True)
    event_code = Column(String(50), nullable=True)
    raw_payload = Column(JSON, nullable=False)
    anomaly_score = Column(Float, default=0.0)
    is_anomaly = Column(Boolean, default=False)

    asset = relationship("Asset", back_populates="events")

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    severity = Column(String(20), nullable=False) # Low, Medium, High, Critical
    confidence = Column(Float, default=0.85)
    detector_type = Column(String(50), nullable=False) # IsolationForest, Autoencoder, ThreatIntel, RuleEngine
    status = Column(String(50), default="Open")
    created_at = Column(DateTime, default=datetime.utcnow)

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    title = Column(String(255), nullable=False)
    summary = Column(Text, nullable=True)
    severity = Column(String(20), nullable=False)
    status = Column(String(50), default="Open", index=True) # Open, In Progress, Contained, Resolved
    risk_score = Column(Integer, default=50) # 0-100
    assigned_to = Column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    root_cause_asset_id = Column(String(36), ForeignKey("assets.id", ondelete="SET NULL"), nullable=True)
    ai_explanation = Column(Text, nullable=True)
    predicted_next_step = Column(Text, nullable=True)
    prediction_confidence = Column(Float, default=0.85)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    mitre_mappings = relationship("MitreMapping", back_populates="incident", cascade="all, delete-orphan")
    responses = relationship("Response", back_populates="incident", cascade="all, delete-orphan")

class MitreMapping(Base):
    __tablename__ = "mitre_mapping"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    incident_id = Column(String(36), ForeignKey("incidents.id", ondelete="CASCADE"), nullable=False)
    tactic = Column(String(100), nullable=False) # Initial Access, Execution, Persistence, etc.
    technique_id = Column(String(50), nullable=False) # e.g. T1003
    technique_name = Column(String(255), nullable=False) # e.g. OS Credential Dumping
    confidence = Column(Float, default=0.90)
    observed_at = Column(DateTime, default=datetime.utcnow)

    incident = relationship("Incident", back_populates="mitre_mappings")

class ThreatIntelligence(Base):
    __tablename__ = "threat_intelligence"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    ioc_type = Column(String(50), nullable=False) # IP, Domain, MD5, SHA256, URL
    ioc_value = Column(String(512), unique=True, nullable=False, index=True)
    threat_actor = Column(String(100), nullable=True)
    malware_family = Column(String(100), nullable=True)
    confidence_score = Column(Integer, default=80)
    source = Column(String(100), default="SentinelThreatFeed")
    last_updated = Column(DateTime, default=datetime.utcnow)

class Playbook(Base):
    __tablename__ = "playbooks"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    trigger_condition = Column(JSON, nullable=False)
    actions = Column(JSON, nullable=False)
    is_automated = Column(Boolean, default=False)

class Response(Base):
    __tablename__ = "responses"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    incident_id = Column(String(36), ForeignKey("incidents.id", ondelete="CASCADE"), nullable=False)
    playbook_id = Column(String(36), ForeignKey("playbooks.id", ondelete="SET NULL"), nullable=True)
    action_type = Column(String(100), nullable=False) # Block IP, Isolate Endpoint, Kill Process, Disable User
    target = Column(String(255), nullable=False)
    status = Column(String(50), default="Pending") # Pending, Executing, Success, Failed
    executed_by = Column(String(100), default="AI Agent")
    executed_at = Column(DateTime, default=datetime.utcnow)
    output_log = Column(Text, nullable=True)

    incident = relationship("Incident", back_populates="responses")

class AttackGraphNode(Base):
    __tablename__ = "attack_graph_nodes"

    id = Column(String(255), primary_key=True) # e.g. host_192.168.1.50 or user_admin
    incident_id = Column(String(36), ForeignKey("incidents.id", ondelete="CASCADE"), nullable=True)
    label = Column(String(255), nullable=False)
    node_type = Column(String(50), nullable=False) # User, Device, IP, Process
    risk_level = Column(String(20), default="Medium")
    node_metadata = Column(JSON, nullable=True)

class AttackGraphEdge(Base):
    __tablename__ = "attack_graph_edges"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    incident_id = Column(String(36), ForeignKey("incidents.id", ondelete="CASCADE"), nullable=True)
    source_node_id = Column(String(255), ForeignKey("attack_graph_nodes.id", ondelete="CASCADE"), nullable=False)
    target_node_id = Column(String(255), ForeignKey("attack_graph_nodes.id", ondelete="CASCADE"), nullable=False)
    relationship = Column(String(100), nullable=False) # AUTHENTICATED_TO, COMMUNICATED_WITH, SPAWNED_PROCESS
    timestamp = Column(DateTime, default=datetime.utcnow)

class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    incident_id = Column(String(36), ForeignKey("incidents.id", ondelete="SET NULL"), nullable=True)
    role = Column(String(20), nullable=False) # user, assistant
    message = Column(Text, nullable=False)
    chat_metadata = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    action = Column(String(255), nullable=False)
    details = Column(JSON, nullable=True)
    ip_address = Column(String(45), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
