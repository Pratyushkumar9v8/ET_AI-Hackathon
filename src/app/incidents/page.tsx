"use client";

import { useState } from "react";
import { Sidebar } from "@/components/layout/Sidebar";
import { Header } from "@/components/layout/Header";
import { AlertTriangle, ShieldCheck, Cpu, Bot, CheckCircle2, ChevronRight, Play, Terminal, ShieldAlert } from "lucide-react";

const MOCK_INCIDENTS = [
  {
    id: "inc_ransomware_001",
    title: "Multi-Stage APT Ransomware Outbreak on Domain Controller",
    summary: "Correlated Mimikatz LSASS memory dumping, PowerShell obfuscated payload execution, and volume shadow copy deletion across host SRV-DC-01.",
    severity: "Critical",
    status: "In Progress",
    risk_score: 98,
    assigned_to: "analyst@sentinel.cni.gov",
    root_cause: "SRV-DC-01 (192.168.1.10)",
    ai_explanation: "Attacker gained initial foothold via spearphishing link on WKSTN-FIN-08, dumped LSASS credentials, moved laterally via WMI to SRV-DC-01, and attempted shadow copy wiping prior to mass encryption.",
    predicted_next_step: "Lateral movement to OT SCADA gateway subnets & Data Encrypted for Impact (T1486)",
    prediction_confidence: 0.94,
    created_at: "2026-07-22 10:15:00",
    mitre_mappings: [
      { tactic: "Initial Access", id: "T1078", name: "Valid Accounts" },
      { tactic: "Execution", id: "T1059.001", name: "PowerShell" },
      { tactic: "Credential Access", id: "T1003.001", name: "LSASS Memory Credential Dumping" },
      { tactic: "Impact", id: "T1490", name: "Inhibit System Recovery" }
    ],
    responses: [
      { action: "Isolate Endpoint", target: "SRV-DC-01", status: "Success", time: "10:26:00" },
      { action: "Block IP", target: "198.51.100.42", status: "Success", time: "10:26:30" }
    ]
  },
  {
    id: "inc_scada_002",
    title: "Unauthorized SCADA PLC Register Overwrite in Water Dosing Station",
    summary: "Rogue insider attempted direct Modbus write register commands to alter chemical dosing parameters.",
    severity: "Critical",
    status: "Open",
    risk_score: 92,
    assigned_to: "Unassigned",
    root_cause: "HMI-WATER-PUMP-01 (10.0.4.12)",
    ai_explanation: "Direct connection established from HMI-WATER-PUMP-01 sending unauthorized Modbus function code 0x06 write commands to PLC registers 40001.",
    predicted_next_step: "Safety Instrumented System (SIS) override to bypass physical pressure reliefs",
    prediction_confidence: 0.96,
    created_at: "2026-07-22 11:05:00",
    mitre_mappings: [
      { tactic: "Impair Process Control", id: "T0855", name: "Unauthorized Command Message in SCADA" }
    ],
    responses: []
  },
  {
    id: "inc_vpn_003",
    title: "Suspicious VPN Login from Anomaly Location & DNS Tunneling",
    summary: "User account m.taylor authenticated via VPN from Russian IP, followed by high-frequency TXT DNS queries.",
    severity: "High",
    status: "Open",
    risk_score: 78,
    assigned_to: "analyst@sentinel.cni.gov",
    root_cause: "VPN-GW-01 (203.0.113.15)",
    ai_explanation: "Impossible travel anomaly combined with DNS exfiltration signature to bad-domain-exfil.com.",
    predicted_next_step: "Staging sensitive database files for cloud upload",
    prediction_confidence: 0.88,
    created_at: "2026-07-22 09:40:00",
    mitre_mappings: [
      { tactic: "Exfiltration", id: "T1071.004", name: "DNS Data Exfiltration" }
    ],
    responses: []
  }
];

export default function IncidentsPage() {
  const [selectedIncident, setSelectedIncident] = useState(MOCK_INCIDENTS[0]);
  const [actionSuccessMessage, setActionSuccessMessage] = useState("");

  const triggerSOARAction = (actionName: string, targetName: string) => {
    const newResp = {
      action: actionName,
      target: targetName,
      status: "Success",
      time: new Date().toLocaleTimeString()
    };
    setSelectedIncident({
      ...selectedIncident,
      responses: [...selectedIncident.responses, newResp],
      status: "Contained"
    });
    setActionSuccessMessage(`Successfully executed SOAR action: ${actionName} on ${targetName}`);
    setTimeout(() => setActionSuccessMessage(""), 4000);
  };

  return (
    <div className="min-h-screen bg-[#090D16] text-slate-100 flex">
      <Sidebar />
      <Header />

      <main className="flex-1 ml-64 pt-20 p-6 space-y-6">
        <div>
          <h2 className="text-xl font-bold tracking-tight text-white flex items-center gap-2">
            <AlertTriangle className="w-5 h-5 text-rose-500" /> Incident Response Center
          </h2>
          <p className="text-xs text-slate-400 mt-0.5 font-mono">Autonomous Correlation, Attacker Progression & SOAR Playbooks</p>
        </div>

        {actionSuccessMessage && (
          <div className="p-3 bg-emerald-500/20 border border-emerald-500/40 text-emerald-300 text-xs rounded-lg flex items-center gap-2">
            <CheckCircle2 className="w-4 h-4 text-emerald-400" /> {actionSuccessMessage}
          </div>
        )}

        {/* Master-Detail Layout */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
          {/* Left Incident List (4 cols) */}
          <div className="lg:col-span-4 space-y-3">
            {MOCK_INCIDENTS.map((inc) => {
              const isSelected = selectedIncident.id === inc.id;
              return (
                <div
                  key={inc.id}
                  onClick={() => setSelectedIncident(inc)}
                  className={`p-4 rounded-xl border cursor-pointer transition-all ${
                    isSelected
                      ? "bg-[#162238] border-cyan-500 shadow-[0_0_20px_rgba(6,182,212,0.15)]"
                      : "bg-[#111827] border-slate-800 hover:border-slate-700"
                  }`}
                >
                  <div className="flex items-center justify-between">
                    <span className={`text-[10px] font-bold px-2 py-0.5 rounded font-mono uppercase ${
                      inc.severity === "Critical" ? "bg-rose-500/20 text-rose-400 border border-rose-500/30" : "bg-amber-500/20 text-amber-400"
                    }`}>
                      {inc.severity}
                    </span>
                    <span className="text-xs text-slate-400 font-mono">Risk {inc.risk_score}/100</span>
                  </div>

                  <h4 className="text-xs font-semibold text-white mt-2 line-clamp-2">{inc.title}</h4>
                  <p className="text-[11px] text-slate-400 mt-1 line-clamp-2">{inc.summary}</p>

                  <div className="flex items-center justify-between mt-3 pt-2 border-t border-slate-800/80 text-[10px] text-slate-400 font-mono">
                    <span>{inc.created_at}</span>
                    <span className="text-cyan-400 flex items-center gap-1">Detail <ChevronRight className="w-3 h-3" /></span>
                  </div>
                </div>
              );
            })}
          </div>

          {/* Right Detailed Incident Inspection View (8 cols) */}
          <div className="lg:col-span-8 glass-panel p-6 rounded-xl space-y-6">
            <div className="flex items-start justify-between pb-4 border-b border-slate-800">
              <div>
                <span className="text-[11px] font-mono text-cyan-400 uppercase">INCIDENT ID: {selectedIncident.id}</span>
                <h3 className="text-lg font-bold text-white mt-1">{selectedIncident.title}</h3>
                <p className="text-xs text-slate-400 mt-1 font-mono">Root Cause Asset: <span className="text-rose-400 font-semibold">{selectedIncident.root_cause}</span></p>
              </div>
              <div className="text-right">
                <span className="text-2xl font-black text-rose-400 font-mono">{selectedIncident.risk_score}</span>
                <p className="text-[10px] text-slate-400 uppercase font-mono">Composite Risk Score</p>
              </div>
            </div>

            {/* AI Explanation Box */}
            <div className="p-4 rounded-xl bg-gradient-to-r from-cyan-950/40 to-blue-950/30 border border-cyan-500/30">
              <div className="flex items-center gap-2 text-xs font-semibold text-cyan-300 mb-2">
                <Bot className="w-4 h-4 text-cyan-400" /> AI Agent Explanatory Reasoning & Cause Analysis
              </div>
              <p className="text-xs text-slate-300 leading-relaxed">{selectedIncident.ai_explanation}</p>
            </div>

            {/* Predictive Attacker Progression Box */}
            <div className="p-4 rounded-xl bg-slate-900/60 border border-amber-500/30">
              <div className="flex items-center justify-between text-xs mb-1">
                <span className="font-semibold text-amber-400 flex items-center gap-2">
                  <Cpu className="w-4 h-4 text-amber-400" /> Attacker Next Step Prediction
                </span>
                <span className="font-mono text-amber-300 text-[11px]">Confidence: {int(selectedIncident.prediction_confidence * 100)}%</span>
              </div>
              <p className="text-xs text-slate-200 font-mono mt-1">{selectedIncident.predicted_next_step}</p>
            </div>

            {/* MITRE Mapping Badges */}
            <div>
              <h4 className="text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2">Mapped MITRE ATT&CK Techniques</h4>
              <div className="flex flex-wrap gap-2">
                {selectedIncident.mitre_mappings.map((m, i) => (
                  <span key={i} className="px-2.5 py-1 rounded bg-slate-800 border border-slate-700 text-[11px] text-cyan-300 font-mono">
                    [{m.tactic}] <strong>{m.id}</strong> - {m.name}
                  </span>
                ))}
              </div>
            </div>

            {/* Recommended SOAR Action Playbook Controls */}
            <div className="pt-4 border-t border-slate-800 space-y-3">
              <h4 className="text-xs font-semibold text-slate-300 uppercase tracking-wider flex items-center gap-2">
                <ShieldCheck className="w-4 h-4 text-emerald-400" /> Recommended SOAR Automated Responses
              </h4>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                <button
                  onClick={() => triggerSOARAction("Isolate Host Endpoint", selectedIncident.root_cause)}
                  className="p-3 rounded-lg bg-rose-500/15 hover:bg-rose-500/25 border border-rose-500/40 text-rose-300 text-xs font-medium transition-all flex items-center justify-between"
                >
                  <span>Isolate Host ({selectedIncident.root_cause})</span>
                  <Play className="w-3.5 h-3.5 text-rose-400" />
                </button>

                <button
                  onClick={() => triggerSOARAction("Block External Malicious IP", "198.51.100.42")}
                  className="p-3 rounded-lg bg-amber-500/15 hover:bg-amber-500/25 border border-amber-500/40 text-amber-300 text-xs font-medium transition-all flex items-center justify-between"
                >
                  <span>Block External C2 IP (198.51.100.42)</span>
                  <Play className="w-3.5 h-3.5 text-amber-400" />
                </button>

                <button
                  onClick={() => triggerSOARAction("Kill Process Tree", "PID 4820 powershell.exe")}
                  className="p-3 rounded-lg bg-cyan-500/15 hover:bg-cyan-500/25 border border-cyan-500/40 text-cyan-300 text-xs font-medium transition-all flex items-center justify-between"
                >
                  <span>Kill Suspicious Process Tree</span>
                  <Play className="w-3.5 h-3.5 text-cyan-400" />
                </button>

                <button
                  onClick={() => triggerSOARAction("Disable User Credentials", "administrator")}
                  className="p-3 rounded-lg bg-purple-500/15 hover:bg-purple-500/25 border border-purple-500/40 text-purple-300 text-xs font-medium transition-all flex items-center justify-between"
                >
                  <span>Revoke Account Tokens</span>
                  <Play className="w-3.5 h-3.5 text-purple-400" />
                </button>
              </div>

              {/* Execution Audit History */}
              {selectedIncident.responses.length > 0 && (
                <div className="mt-4 p-3 rounded-lg bg-slate-900 border border-slate-800 space-y-2">
                  <h5 className="text-[11px] font-mono text-slate-400 uppercase">Action Execution Audit Trail</h5>
                  {selectedIncident.responses.map((r, i) => (
                    <div key={i} className="flex items-center justify-between text-xs font-mono text-emerald-400">
                      <span>✓ {r.action} on {r.target}</span>
                      <span className="text-slate-500">{r.time}</span>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

function int(val: number) {
  return Math.round(val);
}
