# SentinelAI 🛡️⚡
> **Autonomous Cyber Resilience Platform for Critical National Infrastructure (CNI)**  
> *Inspired by ET AI Hackathon 2026 Problem Statement #7*

---

![SentinelAI Banner](https://img.shields.io/badge/SentinelAI-v1.0.0-06B6D4?style=for-the-badge&logo=shield&logoColor=white)
![ET AI Hackathon](https://img.shields.io/badge/ET_AI_Hackathon_2026-Problem_Statement_%237-10B981?style=for-the-badge)
![Next.js 15](https://img.shields.io/badge/Next.js-15.2-black?style=for-the-badge&logo=next.js)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-009688?style=for-the-badge&logo=fastapi)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-8B5CF6?style=for-the-badge)

---

## 🌟 Executive Summary

**SentinelAI** is an agentic AI-driven Cyber Resilience Platform designed for hybrid IT and OT environments across Critical National Infrastructure (Power Grids, Water Treatment Plants, Defense, and Transportation networks).

It continuously monitors heterogeneous security telemetry, detects statistical anomalies using unsupervised Machine Learning, correlates weak signals across IT/OT boundaries into unified attack campaigns, maps techniques to the **MITRE ATT&CK Framework**, predicts future attacker steps, and orchestrates automated **SOAR playbooks**.

Think of SentinelAI as a unified miniature **Microsoft Defender + CrowdStrike Falcon + Splunk + Palo Alto Cortex XSOAR** powered by autonomous Agentic AI.

---

## 🔥 Key Capabilities

- 🤖 **LangGraph Multi-Agent Mesh**: 8 stateful specialized agents (`Behavior`, `ThreatIntel`, `MITRE`, `Correlation`, `RiskScoring`, `Prediction`, `Response`, `Report`) collaborating in real time.
- ⚡ **Heterogeneous Telemetry Pipeline**: Standardized Elastic Common Schema (ECS) ingestion for Windows Sysmon, Linux auditd, NetFlow, Firewall, VPN, DNS, and SCADA/OT Modbus events.
- 🧠 **Dual ML Anomaly Engine**: Unsupervised **Isolation Forest** & **Autoencoder** feature scoring for zero-day behavioral outlier detection.
- 🕸️ **Interactive Attack Path Graph**: React Flow directed topology visualizer mapping host-to-host lateral movement, process trees, and credential usage.
- 📊 **Interactive MITRE ATT&CK Matrix**: 14-tactic matrix grid with live technique detection overlays and risk heat intensity.
- 💬 **Explainable RAG SOC Copilot**: Conversational AI assistant backed by vector embeddings over MITRE ATT&CK Enterprise Matrix v14 datasets.
- 🚀 **10,000+ Synthetic Event Simulator**: Multi-stage APT attack scenario playouts (Ransomware Outbreak, VPN Cloud Exfiltration, Insider OT SCADA Sabotage).

---

## 🏗️ System Architecture

```
                                  [ Heterogeneous Log Sources ]
                (Sysmon, Auditd, NetFlow, Firewall, VPN, DNS, Cloud, OT/SCADA)
                                                │
                                                ▼
                                    [ Ingestion Engine ]
                              (FastAPI / Redis Event Stream)
                                                │
                                                ▼
                                   [ Normalization & ELS ]
                             (ECS Normalizer + Feature Extractor)
                                                │
                 ┌──────────────────────────────┴──────────────────────────────┐
                 ▼                                                             ▼
       [ Machine Learning Pipeline ]                                [ Agentic AI Mesh (LangGraph) ]
  (Isolation Forest, DBSCAN, Autoencoder)                    (Behavior, ThreatIntel, MITRE, Correlator,
                 │                                            Risk Scoring, Predictor, Response, SOC Copilot)
                 │                                                             │
                 └──────────────────────────────┬──────────────────────────────┘
                                                ▼
                                     [ PostgreSQL / FAISS ]
                               (Relational Data + Vector Index)
                                                │
                                                ▼
                                     [ Real-Time Stream ]
                                     (WebSockets Hub)
                                                │
                                                ▼
                                   [ Modern SOC UI (Next.js 15) ]
                (Dashboard, Incident Center, Attack Graph, MITRE Matrix, SOC Copilot)
```

---

## 💻 Application Modules

| Module | URL Path | Description |
| :--- | :--- | :--- |
| **Landing Page** | `/` | Cyber grid hero banner, Hackathon problem breakdown, and feature launcher. |
| **Command Dashboard** | `/dashboard` | System Threat Score meter (0-100), 24h anomaly timeline chart, live WebSocket log ticker, and risk heatmap. |
| **Incident Center** | `/incidents` | Master-detail incident viewer, AI explanation drawer, predicted next step, MITRE badges, and SOAR response buttons. |
| **Threat Intelligence** | `/threat-intel` | Known malicious IPs, domains, hashes, threat actor profiles (APT29, Volt Typhoon, Lazarus Group), and live IOC lookup tool. |
| **ATT&CK Matrix** | `/mitre` | Interactive 14-tactic grid with detection heat overlays. |
| **Attack Path Graph** | `/attack-graph` | React Flow topology canvas visualizing lateral movement, process spawning, and host-to-host links. |
| **User Behavior (UBA)**| `/uba` | UEBA baseline profiles highlighting Impossible Travel (Washington → Moscow in 12m), abnormal encoded PowerShell, and off-hours SCADA register writes. |
| **Asset Inventory** | `/assets` | Hardware profiling (IT / OT / Cloud) with criticality scores and CVE vulnerability badges. |
| **Response SOAR** | `/soar` | One-click containment playbooks (Endpoint Host Isolation, Firewall C2 Drop Rules, Account Token Revocation, Executive PDF Report generator). |
| **SOC Copilot** | `/copilot` | RAG-powered chat interface with streaming responses and context prompt chips. |
| **Analytics** | `/analytics` | MTTD (2.4m), MTTR (8.5m), 96.8% Detection Accuracy benchmark, and top attack vectors. |

---

## 🚀 Quick Start Guide

### Prerequisites
- **Python**: 3.10 or higher
- **Node.js**: v18.0 or higher
- **Docker**: (Optional, for containerized run)

---

### Option 1: Local Development Run (Fastest)

#### 1. Setup & Start Backend
```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install email-validator

# Start FastAPI Dev Server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
*Backend API will run at `http://localhost:8000`* (Interactive Docs: `http://localhost:8000/docs`)

#### 2. Setup & Start Frontend
```bash
# Install dependencies (run in the root directory)
npm install --legacy-peer-deps

# Start Next.js Dev Server
npm run dev
```
*Frontend interface will run at `http://localhost:3000`*

---

### Option 2: Docker Compose Run (One Command)

To run the full stack (Frontend, Backend, PostgreSQL, Redis) via Docker:

```bash
docker compose up --build
```
Access the platform at **`http://localhost:3000`**.

---

## 🎮 Simulation & Attack Scenarios

SentinelAI includes a built-in simulation engine. You can trigger synthetic multi-stage APT attack playouts directly from the Header bar or API:

1. **APT Ransomware Outbreak**:
   - `Initial Access` (Spearphishing Word Macro) → `Execution` (PowerShell Encoded Payload) → `Credential Access` (Mimikatz LSASS Dump) → `Impact` (VSSadmin Shadow Copy Deletion & Encryption).
2. **VPN Cloud Exfiltration**:
   - `Initial Access` (Compromised VPN credentials from Russia) → `Exfiltration` (High-frequency DNS TXT query tunneling to `bad-domain-exfil.com`).
3. **SCADA OT Sabotage**:
   - `Initial Access` (Rogue insider on HMI workstation) → `Impair Process Control` (Direct Modbus function `0x06` register override on chemical dosing pumps).

---

## 🧰 Tech Stack Summary

| Domain | Technologies |
| :--- | :--- |
| **Frontend** | Next.js 15 (App Router), TypeScript, TailwindCSS, Shadcn UI, Framer Motion, Recharts, React Flow (`@xyflow/react`), Lucide Icons |
| **Backend** | FastAPI, Python 3.14, SQLAlchemy, Pydantic v2, Uvicorn, WebSockets, Celery |
| **AI Mesh** | LangGraph, LangChain, SentenceTransformers, FAISS Vector Search, RAG Architecture |
| **Machine Learning** | Isolation Forest, Autoencoder, DBSCAN, NetworkX Graph Analytics |
| **Database & Cache** | PostgreSQL 16, Redis 7 |
| **Containerization** | Docker, Docker Compose |

---

## 📄 License & Attribution

Built for the **ET AI Hackathon 2026 Problem Statement #7**.

---

## 🏆 Hackathon Judging Criteria Alignment

Our solution is tailored to maximize the score across all judging criteria:

| Criteria | Weight | SentinelAI Alignment |
| :--- | :--- | :--- |
| **Innovation** | 25% | First-of-its-kind multi-agent AI mesh natively integrating IT/OT signals with MITRE ATT&CK. |
| **Business Impact** | 25% | Automates incident response, compressing containment from weeks to hours for critical infrastructure. |
| **Technical Excellence** | 20% | Real-time dual ML pipeline (Unsupervised + Vector Search) built on a scalable, typed Next.js/FastAPI stack. |
| **Scalability** | 15% | Containerized and optimized to ingest thousands of events via high-throughput WebSockets. |
| **User Experience** | 15% | Intuitive SOC dashboard with interactive Attack Path Graphs and conversational AI Copilot. |