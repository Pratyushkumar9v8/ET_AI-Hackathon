"use client";

import { useState } from "react";
import { Sidebar } from "@/components/layout/Sidebar";
import { Header } from "@/components/layout/Header";
import { ShieldCheck, Play, CheckCircle2, FileText } from "lucide-react";

export default function SoarPage() {
  const [reportGenerated, setReportGenerated] = useState(false);

  return (
    <div className="min-h-screen bg-[#090D16] text-slate-100 flex">
      <Sidebar />
      <Header />

      <main className="flex-1 ml-64 pt-20 p-6 space-y-6">
        <div>
          <h2 className="text-xl font-bold tracking-tight text-white flex items-center gap-2">
            <ShieldCheck className="w-5 h-5 text-emerald-400" /> SOAR Orchestration & Playbook Center
          </h2>
          <p className="text-xs text-slate-400 mt-0.5 font-mono">Automated Containment, Host Isolation & Executive PDF Reports</p>
        </div>

        {/* Action Controls */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="glass-panel p-5 rounded-xl flex flex-col justify-between">
            <div>
              <h4 className="text-sm font-semibold text-white">Endpoint Host Isolation Playbook</h4>
              <p className="text-xs text-slate-400 mt-1">Disables network interfaces at perimeter switch for compromised asset.</p>
            </div>
            <button className="mt-4 w-full py-2 bg-rose-500 hover:bg-rose-600 text-white font-bold text-xs rounded-lg transition-all flex items-center justify-center gap-2">
              <Play className="w-3.5 h-3.5" /> Execute Host Isolation
            </button>
          </div>

          <div className="glass-panel p-5 rounded-xl flex flex-col justify-between">
            <div>
              <h4 className="text-sm font-semibold text-white">Firewall Perimeter Drop Rule</h4>
              <p className="text-xs text-slate-400 mt-1">Adds automated drop ACL for external C2 IP addresses.</p>
            </div>
            <button className="mt-4 w-full py-2 bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold text-xs rounded-lg transition-all flex items-center justify-center gap-2">
              <Play className="w-3.5 h-3.5" /> Push Firewall Rule
            </button>
          </div>

          <div className="glass-panel p-5 rounded-xl flex flex-col justify-between">
            <div>
              <h4 className="text-sm font-semibold text-white">Executive PDF Report Engine</h4>
              <p className="text-xs text-slate-400 mt-1">Compiles complete CNI executive incident summary report.</p>
            </div>
            <button 
              onClick={() => setReportGenerated(true)}
              className="mt-4 w-full py-2 bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold text-xs rounded-lg transition-all flex items-center justify-center gap-2"
            >
              <FileText className="w-3.5 h-3.5" /> Generate Incident Report
            </button>
          </div>
        </div>

        {/* Executive Report Preview Modal/Card */}
        {reportGenerated && (
          <div className="glass-panel p-6 rounded-xl border border-cyan-500/40 space-y-4 font-mono text-xs text-slate-200">
            <div className="flex items-center justify-between pb-3 border-b border-slate-800">
              <span className="text-cyan-400 font-bold text-sm">SENTINEL-AI EXECUTIVE INCIDENT REPORT</span>
              <span className="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">PDF GENERATED</span>
            </div>
            <div className="space-y-2">
              <p><strong>Incident ID:</strong> INC-2026-CNI-001</p>
              <p><strong>Threat Index:</strong> 98/100 (CRITICAL)</p>
              <p><strong>Targeted CNI Sector:</strong> Municipal Water Treatment Plant #04</p>
              <p><strong>Root Cause:</strong> Malicious Macro Execution & Mimikatz Credential Theft on WKSTN-FIN-08</p>
              <p><strong>Containment Status:</strong> SRV-DC-01 Isolated at 10:26:00 UTC. C2 IP 198.51.100.42 Blocked.</p>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
