"use client";

import { Sidebar } from "@/components/layout/Sidebar";
import { Header } from "@/components/layout/Header";
import { Server, ShieldAlert } from "lucide-react";

const ASSETS_DATA = [
  { hostname: "SRV-DC-01", ip: "192.168.1.10", type: "Server", env: "IT", os: "Windows Server 2022", crit: 95, status: "Compromised", cve: "CVE-2024-1709 (Critical)" },
  { hostname: "SRV-APP-02", ip: "192.168.1.15", type: "Server", env: "IT", os: "Ubuntu 22.04 LTS", crit: 80, status: "Healthy", cve: "None" },
  { hostname: "WKSTN-FIN-08", ip: "192.168.1.50", type: "Endpoint", env: "IT", os: "Windows 11 Enterprise", crit: 60, status: "Healthy", cve: "CVE-2023-36884 (High)" },
  { hostname: "FW-PERIMETER-01", ip: "192.168.1.1", type: "Firewall", env: "IT", os: "Palo Alto PAN-OS", crit: 90, status: "Healthy", cve: "None" },
  { hostname: "HMI-WATER-PUMP-01", ip: "10.0.4.12", type: "SCADA/PLC", env: "OT", os: "FreeRTOS SCADA Firmware", crit: 100, status: "Compromised", cve: "CVE-2024-1086 (Critical)" }
];

export default function AssetsPage() {
  return (
    <div className="min-h-screen bg-[#090D16] text-slate-100 flex">
      <Sidebar />
      <Header />

      <main className="flex-1 ml-64 pt-20 p-6 space-y-6">
        <div>
          <h2 className="text-xl font-bold tracking-tight text-white flex items-center gap-2">
            <Server className="w-5 h-5 text-cyan-400" /> Enterprise & OT Asset Inventory
          </h2>
          <p className="text-xs text-slate-400 mt-0.5 font-mono">Hardware Telemetry, Criticality Scoring & Vulnerability Profiling</p>
        </div>

        <div className="glass-panel rounded-xl overflow-hidden">
          <table className="w-full text-left text-xs font-mono">
            <thead className="bg-slate-900/80 text-slate-400 uppercase text-[10px] border-b border-slate-800">
              <tr>
                <th className="p-3.5">Hostname</th>
                <th className="p-3.5">IP Address</th>
                <th className="p-3.5">Asset Type</th>
                <th className="p-3.5">Environment</th>
                <th className="p-3.5">Operating System</th>
                <th className="p-3.5">Criticality</th>
                <th className="p-3.5">Status</th>
                <th className="p-3.5">CVE Vulnerabilities</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60">
              {ASSETS_DATA.map((a, i) => (
                <tr key={i} className="hover:bg-slate-800/30">
                  <td className="p-3.5 font-bold text-white">{a.hostname}</td>
                  <td className="p-3.5 text-cyan-400">{a.ip}</td>
                  <td className="p-3.5 text-slate-300">{a.type}</td>
                  <td className="p-3.5"><span className={`px-2 py-0.5 rounded font-bold ${a.env === "OT" ? "bg-amber-500/20 text-amber-300 border border-amber-500/30" : "bg-slate-800 text-slate-300"}`}>{a.env}</span></td>
                  <td className="p-3.5 text-slate-400">{a.os}</td>
                  <td className="p-3.5 font-bold text-rose-400">{a.crit}/100</td>
                  <td className="p-3.5">
                    <span className={`px-2 py-0.5 rounded font-semibold ${a.status === "Compromised" ? "bg-rose-500/20 text-rose-400 border border-rose-500/40" : "bg-emerald-500/20 text-emerald-400"}`}>
                      {a.status}
                    </span>
                  </td>
                  <td className="p-3.5 text-rose-300">{a.cve}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </main>
    </div>
  );
}
