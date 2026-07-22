"use client";

import { useState } from "react";
import { Play, Activity, Bell, Radio, Sparkles } from "lucide-react";
import { API_BASE_URL } from "@/services/api";

export function Header() {
  const [isSimulating, setIsSimulating] = useState(false);

  const triggerSimulation = async (scenario: string) => {
    setIsSimulating(true);
    try {
      await fetch(`${API_BASE_URL}/api/v1/simulator/run-scenario?scenario=${scenario}&count=1000`, { method: "POST" });
    } catch (e) {
      console.error(e);
    } finally {
      setTimeout(() => setIsSimulating(false), 1500);
    }
  };

  return (
    <header className="h-16 bg-[#0B0F19]/90 backdrop-blur-md border-b border-[#1E293B] fixed top-0 left-64 right-0 z-30 flex items-center justify-between px-6">
      {/* Live Threat Indicator */}
      <div className="flex items-center gap-6">
        <div className="flex items-center gap-3 bg-[#111827] border border-rose-500/30 px-3.5 py-1.5 rounded-lg">
          <Activity className="w-4 h-4 text-rose-500 animate-pulse" />
          <div className="flex items-baseline gap-2">
            <span className="text-xs text-slate-400 font-medium">THREAT INDEX</span>
            <span className="text-sm font-bold text-rose-400 font-mono">87 / 100</span>
          </div>
        </div>

        <div className="flex items-center gap-2 text-xs text-slate-400">
          <Radio className="w-3.5 h-3.5 text-emerald-400 animate-ping" />
          <span className="font-mono">STREAM: <span className="text-emerald-400 font-semibold">ACTIVE</span></span>
        </div>
      </div>

      {/* Simulator Action Triggers & Controls */}
      <div className="flex items-center gap-3">
        <div className="flex items-center gap-2 bg-[#141C2E] p-1 rounded-lg border border-slate-800">
          <span className="text-[11px] text-slate-400 px-2 font-mono uppercase">Simulate APT:</span>
          <button
            onClick={() => triggerSimulation("ransomware")}
            disabled={isSimulating}
            className="px-2.5 py-1 text-[11px] font-medium bg-rose-500/20 hover:bg-rose-500/30 text-rose-300 rounded border border-rose-500/40 transition-all flex items-center gap-1"
          >
            <Play className="w-3 h-3" /> Ransomware
          </button>
          <button
            onClick={() => triggerSimulation("exfiltration")}
            disabled={isSimulating}
            className="px-2.5 py-1 text-[11px] font-medium bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 rounded border border-amber-500/40 transition-all flex items-center gap-1"
          >
            <Play className="w-3 h-3" /> VPN Tunnel
          </button>
          <button
            onClick={() => triggerSimulation("insider_ot")}
            disabled={isSimulating}
            className="px-2.5 py-1 text-[11px] font-medium bg-cyan-500/20 hover:bg-cyan-500/30 text-cyan-300 rounded border border-cyan-500/40 transition-all flex items-center gap-1"
          >
            <Sparkles className="w-3 h-3" /> SCADA OT
          </button>
        </div>

        {/* User Badge */}
        <div className="flex items-center gap-3 pl-3 border-l border-slate-800">
          <button className="relative p-2 text-slate-400 hover:text-slate-200 rounded-lg hover:bg-slate-800/50">
            <Bell className="w-4 h-4" />
            <span className="absolute top-1.5 right-1.5 w-2 h-2 rounded-full bg-rose-500" />
          </button>
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-full bg-slate-800 border border-cyan-500/40 flex items-center justify-center text-cyan-400 font-bold text-xs">
              SA
            </div>
            <div className="text-left hidden lg:block">
              <p className="text-xs font-semibold text-slate-200">Senior SOC Lead</p>
              <p className="text-[10px] text-slate-400 font-mono">SOC Analyst Role</p>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}
