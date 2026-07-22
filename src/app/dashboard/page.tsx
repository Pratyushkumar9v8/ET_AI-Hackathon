"use client";

import { useEffect, useState } from "react";
import { Sidebar } from "@/components/layout/Sidebar";
import { Header } from "@/components/layout/Header";
import { ShieldAlert, AlertCircle, Server, Users, Activity, Clock, Flame, ArrowUpRight } from "lucide-react";
import { AreaChart, Area, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

export default function DashboardPage() {
  const [metrics, setMetrics] = useState({
    threat_score: 87,
    live_attacks_count: 3,
    open_incidents_count: 5,
    critical_assets_count: 7,
    active_users_count: 42,
    compromised_hosts_count: 2,
    mttd_minutes: 2.4,
    mttr_minutes: 8.5
  });

  const [timeline, setTimeline] = useState([
    { time: "08:00", anomalies: 12, critical: 0 },
    { time: "10:00", anomalies: 18, critical: 1 },
    { time: "12:00", anomalies: 45, critical: 2 },
    { time: "14:00", anomalies: 89, critical: 5 },
    { time: "16:00", anomalies: 62, critical: 3 },
    { time: "18:00", anomalies: 24, critical: 1 }
  ]);

  const [liveLogs, setLiveLogs] = useState([
    { time: "12:45:02", host: "SRV-DC-01", type: "Sysmon", score: 0.98, is_anomaly: true, desc: "Mimikatz LSASS Memory Dump (T1003.001)" },
    { time: "12:44:18", host: "HMI-WATER-01", type: "OT_Modbus", score: 0.96, is_anomaly: true, desc: "Unauthorized Register 40001 Write (T0855)" },
    { time: "12:43:55", host: "WKSTN-FIN-08", type: "PowerShell", score: 0.92, is_anomaly: true, desc: "Base64 Encoded DownloadString Command" },
    { time: "12:42:10", host: "FW-PERIM-01", type: "Firewall", score: 0.21, is_anomaly: false, desc: "Standard HTTPS Egress Connection" }
  ]);

  return (
    <div className="min-h-screen bg-[#090D16] text-slate-100 flex">
      <Sidebar />
      <Header />

      <main className="flex-1 ml-64 pt-20 p-6 space-y-6">
        {/* Top Header Banner */}
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-xl font-bold tracking-tight text-white flex items-center gap-2">
              <ShieldAlert className="w-5 h-5 text-rose-500" />
              CNI Cyber Resilience Command Center
            </h2>
            <p className="text-xs text-slate-400 mt-0.5 font-mono">Real-time Autonomous Threat Monitoring & Anomaly Detection</p>
          </div>
          <div className="flex items-center gap-2 text-xs font-mono bg-slate-900 border border-slate-800 px-3 py-1.5 rounded-lg">
            <Clock className="w-3.5 h-3.5 text-cyan-400" />
            <span>MTTD: <strong className="text-emerald-400">{metrics.mttd_minutes}m</strong></span>
            <span className="text-slate-600">|</span>
            <span>MTTR: <strong className="text-cyan-400">{metrics.mttr_minutes}m</strong></span>
          </div>
        </div>

        {/* Metric Cards Row */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="glass-panel-glow-rose p-4 rounded-xl relative overflow-hidden">
            <div className="flex items-center justify-between">
              <span className="text-xs text-rose-300 font-mono uppercase tracking-wider">System Threat Score</span>
              <Flame className="w-5 h-5 text-rose-500 animate-pulse" />
            </div>
            <div className="mt-2 flex items-baseline gap-3">
              <span className="text-3xl font-black text-rose-400 font-mono">{metrics.threat_score}</span>
              <span className="text-xs text-rose-300 font-semibold px-2 py-0.5 rounded bg-rose-500/20 border border-rose-500/30">
                CRITICAL THREAT
              </span>
            </div>
            <p className="text-[11px] text-slate-400 mt-2">Correlated Multi-stage Ransomware Active</p>
          </div>

          <div className="glass-panel p-4 rounded-xl">
            <div className="flex items-center justify-between">
              <span className="text-xs text-slate-400 font-mono uppercase">Live Active Attacks</span>
              <AlertCircle className="w-5 h-5 text-amber-500" />
            </div>
            <div className="mt-2 flex items-baseline gap-2">
              <span className="text-3xl font-black text-amber-400 font-mono">{metrics.live_attacks_count}</span>
              <span className="text-xs text-amber-300 font-mono">APT Campaigns</span>
            </div>
            <p className="text-[11px] text-slate-400 mt-2">{metrics.open_incidents_count} Open SOC Incidents Require Action</p>
          </div>

          <div className="glass-panel p-4 rounded-xl">
            <div className="flex items-center justify-between">
              <span className="text-xs text-slate-400 font-mono uppercase">Critical Assets Risk</span>
              <Server className="w-5 h-5 text-cyan-400" />
            </div>
            <div className="mt-2 flex items-baseline gap-2">
              <span className="text-3xl font-black text-cyan-400 font-mono">{metrics.compromised_hosts_count} / {metrics.critical_assets_count}</span>
              <span className="text-xs text-rose-400 font-semibold">Compromised</span>
            </div>
            <p className="text-[11px] text-slate-400 mt-2">SRV-DC-01 & HMI-WATER Isolated</p>
          </div>

          <div className="glass-panel p-4 rounded-xl">
            <div className="flex items-center justify-between">
              <span className="text-xs text-slate-400 font-mono uppercase">Monitored Users</span>
              <Users className="w-5 h-5 text-emerald-400" />
            </div>
            <div className="mt-2 flex items-baseline gap-2">
              <span className="text-3xl font-black text-emerald-400 font-mono">{metrics.active_users_count}</span>
              <span className="text-xs text-emerald-400">Normal Baseline</span>
            </div>
            <p className="text-[11px] text-slate-400 mt-2">1 Impossible Travel Anomaly flagged</p>
          </div>
        </div>

        {/* Detection Timeline Chart & Live Log Stream */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="lg:col-span-2 glass-panel p-5 rounded-xl flex flex-col justify-between">
            <div className="flex items-center justify-between mb-4">
              <div>
                <h3 className="text-sm font-semibold text-white flex items-center gap-2">
                  <Activity className="w-4 h-4 text-cyan-400" /> 24-Hour Detection Anomaly Timeline
                </h3>
                <p className="text-[11px] text-slate-400 font-mono">Aggregated Machine Learning Behavioral Outliers</p>
              </div>
            </div>

            <div className="h-64 w-full">
              <ResponsiveContainer width="100%" height="100%">
                <AreaChart data={timeline}>
                  <defs>
                    <linearGradient id="colorAnom" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="5%" stopColor="#06B6D4" stopOpacity={0.6}/>
                      <stop offset="95%" stopColor="#06B6D4" stopOpacity={0}/>
                    </linearGradient>
                    <linearGradient id="colorCrit" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="5%" stopColor="#EF4444" stopOpacity={0.8}/>
                      <stop offset="95%" stopColor="#EF4444" stopOpacity={0}/>
                    </linearGradient>
                  </defs>
                  <XAxis dataKey="time" stroke="#64748B" fontSize={11} />
                  <YAxis stroke="#64748B" fontSize={11} />
                  <Tooltip 
                    contentStyle={{ backgroundColor: "#0F172A", borderColor: "#1E293B", borderRadius: "8px", fontSize: "12px" }}
                  />
                  <Area type="monotone" dataKey="anomalies" stroke="#06B6D4" fillOpacity={1} fill="url(#colorAnom)" name="Anomalies" />
                  <Area type="monotone" dataKey="critical" stroke="#EF4444" fillOpacity={1} fill="url(#colorCrit)" name="Critical Threats" />
                </AreaChart>
              </ResponsiveContainer>
            </div>
          </div>

          {/* Live Telemetry Ticker */}
          <div className="glass-panel p-5 rounded-xl flex flex-col">
            <div className="flex items-center justify-between mb-4 pb-2 border-b border-slate-800">
              <h3 className="text-sm font-semibold text-white flex items-center gap-2">
                <span className="w-2 h-2 rounded-full bg-emerald-400 animate-ping" /> Real-Time Telemetry Stream
              </h3>
              <span className="text-[10px] text-cyan-400 font-mono uppercase">WebSocket Live</span>
            </div>

            <div className="space-y-3 flex-1 overflow-y-auto max-h-[260px] pr-1">
              {liveLogs.map((log, idx) => (
                <div key={idx} className={`p-3 rounded-lg border text-xs font-mono ${log.is_anomaly ? "bg-rose-500/10 border-rose-500/30 text-rose-200" : "bg-slate-900/50 border-slate-800 text-slate-300"}`}>
                  <div className="flex items-center justify-between text-[10px] text-slate-400 mb-1">
                    <span>{log.time} • {log.host}</span>
                    <span className={`px-1.5 py-0.2 rounded font-bold ${log.is_anomaly ? "bg-rose-500/30 text-rose-300" : "bg-slate-800 text-slate-400"}`}>
                      Score {log.score}
                    </span>
                  </div>
                  <p className="font-sans text-xs font-medium line-clamp-1">{log.desc}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
