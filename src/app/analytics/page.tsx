"use client";

import { Sidebar } from "@/components/layout/Sidebar";
import { Header } from "@/components/layout/Header";
import { BarChart3, Activity, Clock, CheckCircle2 } from "lucide-react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

const DAILY_ATTACKS = [
  { date: "Jul 16", count: 140 },
  { date: "Jul 17", count: 185 },
  { date: "Jul 18", count: 210 },
  { date: "Jul 19", count: 190 },
  { date: "Jul 20", count: 310 },
  { date: "Jul 21", count: 450 },
  { date: "Jul 22", count: 520 }
];

export default function AnalyticsPage() {
  return (
    <div className="min-h-screen bg-[#090D16] text-slate-100 flex">
      <Sidebar />
      <Header />

      <main className="flex-1 ml-64 pt-20 p-6 space-y-6">
        <div>
          <h2 className="text-xl font-bold tracking-tight text-white flex items-center gap-2">
            <BarChart3 className="w-5 h-5 text-cyan-400" /> Platform Security Analytics
          </h2>
          <p className="text-xs text-slate-400 mt-0.5 font-mono">Detection Accuracy, Mean Time To Detect (MTTD), & Response Benchmarks</p>
        </div>

        {/* Metrics Row */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <div className="glass-panel p-4 rounded-xl">
            <span className="text-xs text-slate-400 font-mono uppercase">Detection Accuracy</span>
            <p className="text-3xl font-black text-emerald-400 font-mono mt-2">96.8%</p>
            <p className="text-[11px] text-slate-400 mt-1">Isolation Forest + Autoencoder</p>
          </div>

          <div className="glass-panel p-4 rounded-xl">
            <span className="text-xs text-slate-400 font-mono uppercase">Mean Time To Detect (MTTD)</span>
            <p className="text-3xl font-black text-cyan-400 font-mono mt-2">2.4 min</p>
            <p className="text-[11px] text-slate-400 mt-1">Real-time Redis Stream</p>
          </div>

          <div className="glass-panel p-4 rounded-xl">
            <span className="text-xs text-slate-400 font-mono uppercase">Mean Time To Respond (MTTR)</span>
            <p className="text-3xl font-black text-purple-400 font-mono mt-2">8.5 min</p>
            <p className="text-[11px] text-slate-400 mt-1">Automated SOAR Orchestration</p>
          </div>

          <div className="glass-panel p-4 rounded-xl">
            <span className="text-xs text-slate-400 font-mono uppercase">False Positive Rate</span>
            <p className="text-3xl font-black text-amber-400 font-mono mt-2">2.1%</p>
            <p className="text-[11px] text-slate-400 mt-1">Multi-Agent Correlation Filtering</p>
          </div>
        </div>

        {/* Bar Chart */}
        <div className="glass-panel p-5 rounded-xl">
          <h3 className="text-sm font-semibold text-white mb-4">7-Day Attacks & Threat Ingestion Volume</h3>
          <div className="h-64 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={DAILY_ATTACKS}>
                <XAxis dataKey="date" stroke="#64748B" fontSize={11} />
                <YAxis stroke="#64748B" fontSize={11} />
                <Tooltip contentStyle={{ backgroundColor: "#0F172A", borderColor: "#1E293B", borderRadius: "8px", fontSize: "12px" }} />
                <Bar dataKey="count" fill="#06B6D4" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </main>
    </div>
  );
}
