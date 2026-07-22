"use client";

import { Sidebar } from "@/components/layout/Sidebar";
import { Header } from "@/components/layout/Header";
import { Grid, ShieldAlert } from "lucide-react";

const TACTICS_DATA = [
  {
    tactic: "Initial Access",
    techniques: [
      { id: "T1078", name: "Valid Accounts", active: true, risk: "High" },
      { id: "T1566", name: "Phishing Attachment", active: true, risk: "Critical" },
      { id: "T1190", name: "Exploit Public Application", active: false, risk: "Low" }
    ]
  },
  {
    tactic: "Execution",
    techniques: [
      { id: "T1059.001", name: "PowerShell", active: true, risk: "Critical" },
      { id: "T1059.003", name: "Windows Command Shell", active: true, risk: "Medium" }
    ]
  },
  {
    tactic: "Credential Access",
    techniques: [
      { id: "T1003.001", name: "LSASS Memory Dump", active: true, risk: "Critical" },
      { id: "T1555", name: "Credentials from Password Stores", active: false, risk: "Low" }
    ]
  },
  {
    tactic: "Lateral Movement",
    techniques: [
      { id: "T1021.002", name: "SMB / Admin Shares", active: true, risk: "Critical" },
      { id: "T1047", name: "WMI Execution", active: true, risk: "High" }
    ]
  },
  {
    tactic: "Exfiltration",
    techniques: [
      { id: "T1071.004", name: "DNS Exfiltration", active: true, risk: "High" },
      { id: "T1048", name: "Exfiltration Over Alternative Protocol", active: false, risk: "Low" }
    ]
  },
  {
    tactic: "Impact",
    techniques: [
      { id: "T1490", name: "Inhibit System Recovery", active: true, risk: "Critical" },
      { id: "T1486", name: "Data Encrypted for Impact", active: true, risk: "Critical" }
    ]
  },
  {
    tactic: "Impair Process Control (OT)",
    techniques: [
      { id: "T0855", name: "Unauthorized Command Message in SCADA", active: true, risk: "Critical" }
    ]
  }
];

export default function MitrePage() {
  return (
    <div className="min-h-screen bg-[#090D16] text-slate-100 flex">
      <Sidebar />
      <Header />

      <main className="flex-1 ml-64 pt-20 p-6 space-y-6">
        <div>
          <h2 className="text-xl font-bold tracking-tight text-white flex items-center gap-2">
            <Grid className="w-5 h-5 text-cyan-400" /> MITRE ATT&CK Enterprise & OT Matrix
          </h2>
          <p className="text-xs text-slate-400 mt-0.5 font-mono">Real-Time Technique Detection Overlays & Progression Heatmap</p>
        </div>

        {/* ATT&CK Matrix Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 xl:grid-cols-7 gap-3">
          {TACTICS_DATA.map((tGroup, i) => (
            <div key={i} className="glass-panel rounded-xl overflow-hidden flex flex-col">
              <div className="p-3 bg-slate-900/90 border-b border-slate-800 text-center">
                <h4 className="text-[11px] font-bold text-cyan-300 uppercase tracking-wider line-clamp-1">{tGroup.tactic}</h4>
              </div>

              <div className="p-2 space-y-2 flex-1">
                {tGroup.techniques.map((tech, j) => (
                  <div
                    key={j}
                    className={`p-2.5 rounded-lg border text-xs font-mono transition-all ${
                      tech.active
                        ? "bg-rose-500/20 border-rose-500/40 text-rose-200 shadow-[0_0_12px_rgba(244,63,94,0.15)]"
                        : "bg-slate-900/40 border-slate-800 text-slate-400 opacity-60"
                    }`}
                  >
                    <div className="flex items-center justify-between text-[10px] mb-1">
                      <span className="font-bold">{tech.id}</span>
                      {tech.active && (
                        <span className="px-1.5 py-0.2 rounded bg-rose-500/30 text-rose-300 font-semibold text-[9px]">
                          OBSERVED
                        </span>
                      )}
                    </div>
                    <p className="font-sans text-[11px] font-medium leading-tight">{tech.name}</p>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
}
