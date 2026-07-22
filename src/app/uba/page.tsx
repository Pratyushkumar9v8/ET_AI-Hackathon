"use client";

import { Sidebar } from "@/components/layout/Sidebar";
import { Header } from "@/components/layout/Header";
import { UserCheck, ShieldAlert, AlertTriangle } from "lucide-react";

const UBA_ANOMALIES = [
  {
    user: "m.taylor",
    type: "Impossible Travel Anomaly",
    baseline: "Normal login from Washington, USA (192.168.1.50)",
    current: "Authenticated via VPN from Moscow, RU (203.0.113.15) 12 minutes later",
    risk: 88,
    time: "2026-07-22 09:40:00"
  },
  {
    user: "administrator",
    type: "Abnormal PowerShell Invocations",
    baseline: "Standard GUI administrative tooling usage",
    current: "Executed Base64 encoded scriptblock in background non-interactive session",
    risk: 95,
    time: "2026-07-22 10:16:00"
  },
  {
    user: "r.insider",
    type: "Off-Hours SCADA Register Tampering",
    baseline: "Read-only HMI telemetry monitoring",
    current: "Direct Modbus function code 0x06 write command to PLC register 40001",
    risk: 98,
    time: "2026-07-22 11:05:00"
  }
];

export default function UbaPage() {
  return (
    <div className="min-h-screen bg-[#090D16] text-slate-100 flex">
      <Sidebar />
      <Header />

      <main className="flex-1 ml-64 pt-20 p-6 space-y-6">
        <div>
          <h2 className="text-xl font-bold tracking-tight text-white flex items-center gap-2">
            <UserCheck className="w-5 h-5 text-cyan-400" /> User Behavior Analytics (UEBA)
          </h2>
          <p className="text-xs text-slate-400 mt-0.5 font-mono">Statistical Baseline Profiles & Behavioral Outliers</p>
        </div>

        <div className="grid grid-cols-1 gap-4">
          {UBA_ANOMALIES.map((anom, i) => (
            <div key={i} className="glass-panel p-5 rounded-xl border border-rose-500/30 flex items-start justify-between">
              <div className="space-y-2">
                <div className="flex items-center gap-3">
                  <span className="px-2.5 py-1 rounded bg-rose-500/20 text-rose-300 font-mono font-bold text-xs">
                    {anom.type}
                  </span>
                  <span className="text-xs font-mono text-cyan-400">User: <strong>{anom.user}</strong></span>
                </div>
                <div className="text-xs space-y-1">
                  <p className="text-slate-400">Normal Baseline: <span className="text-slate-300">{anom.baseline}</span></p>
                  <p className="text-rose-300 font-semibold">Observed Activity: {anom.current}</p>
                </div>
                <p className="text-[10px] text-slate-500 font-mono">Detected At: {anom.time}</p>
              </div>

              <div className="text-right">
                <span className="text-2xl font-black text-rose-400 font-mono">{anom.risk}</span>
                <p className="text-[10px] text-slate-400 font-mono uppercase">Anomaly Risk</p>
              </div>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
}
