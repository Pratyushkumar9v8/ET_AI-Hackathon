"use client";

import Link from "next/link";
import { ShieldAlert, Cpu, GitMerge, Bot, ShieldCheck, ArrowRight, Activity, Terminal, Server } from "lucide-react";

export default function LandingPage() {
  return (
    <div className="min-h-screen bg-[#090D16] text-slate-100 selection:bg-cyan-500 selection:text-slate-950 flex flex-col">
      {/* Top Navbar */}
      <header className="h-20 border-b border-slate-800/80 bg-[#0B0F19]/80 backdrop-blur-md px-8 flex items-center justify-between sticky top-0 z-50">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-lg bg-gradient-to-tr from-cyan-500 to-emerald-500 p-[2px]">
            <div className="w-full h-full bg-[#090D16] rounded-[6px] flex items-center justify-center">
              <ShieldAlert className="w-6 h-6 text-cyan-400" />
            </div>
          </div>
          <div>
            <h1 className="font-bold text-xl tracking-wider bg-gradient-to-r from-cyan-400 via-emerald-400 to-blue-500 bg-clip-text text-transparent">
              SENTINEL<span className="text-rose-500">.AI</span>
            </h1>
            <p className="text-[10px] text-slate-400 tracking-widest uppercase">CNI Autonomous Cyber Resilience Platform</p>
          </div>
        </div>

        <div className="flex items-center gap-4">
          <Link
            href="/dashboard"
            className="px-5 py-2.5 rounded-lg bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-400 hover:to-blue-400 text-slate-950 font-bold text-xs shadow-[0_0_20px_rgba(6,182,212,0.3)] transition-all flex items-center gap-2"
          >
            Launch Command Center <ArrowRight className="w-4 h-4" />
          </Link>
        </div>
      </header>

      {/* Hero Section */}
      <section className="py-24 px-6 relative overflow-hidden flex-1 flex flex-col items-center justify-center text-center">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(6,182,212,0.1)_0,transparent_70%)] pointer-events-none" />

        <div className="max-w-4xl space-y-6 relative z-10">
          <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-xs font-mono">
            <span className="w-2 h-2 rounded-full bg-cyan-400 animate-ping" />
            ET AI Hackathon 2026 Problem Statement #7 Solution
          </div>

          <h1 className="text-4xl sm:text-6xl font-black tracking-tight text-white leading-tight">
            Autonomous Cyber Resilience for <br />
            <span className="bg-gradient-to-r from-cyan-400 via-emerald-400 to-rose-500 bg-clip-text text-transparent">
              Critical National Infrastructure
            </span>
          </h1>

          <p className="text-sm sm:text-base text-slate-300 max-w-2xl mx-auto leading-relaxed">
            Unified agentic AI mesh continuously monitoring IT/OT telemetry, detecting behavioral anomalies, predicting multi-stage attacker progression, and orchestrating automated SOAR playbooks.
          </p>

          <div className="pt-4 flex flex-wrap items-center justify-center gap-4">
            <Link
              href="/dashboard"
              className="px-8 py-3.5 rounded-xl bg-gradient-to-r from-cyan-500 to-emerald-400 text-slate-950 font-extrabold text-sm shadow-[0_0_25px_rgba(6,182,212,0.4)] transition-all transform hover:scale-105"
            >
              Open Live SOC Dashboard
            </Link>
            <Link
              href="/copilot"
              className="px-8 py-3.5 rounded-xl bg-slate-900 border border-slate-800 hover:border-cyan-500/50 text-cyan-300 font-bold text-sm transition-all"
            >
              Try SOC Copilot Chat
            </Link>
          </div>
        </div>

        {/* Feature Cards Grid */}
        <div className="max-w-6xl w-full grid grid-cols-1 md:grid-cols-3 gap-6 mt-16 text-left relative z-10">
          <div className="glass-panel p-6 rounded-2xl border border-cyan-500/20">
            <Cpu className="w-8 h-8 text-cyan-400 mb-4" />
            <h3 className="text-base font-bold text-white mb-2">LangGraph Multi-Agent Mesh</h3>
            <p className="text-xs text-slate-400 leading-relaxed">
              8 independent AI agents collaborating statefully across Behavior, ThreatIntel, MITRE, Correlation, Risk Scoring, Prediction, and SOAR response tasks.
            </p>
          </div>

          <div className="glass-panel p-6 rounded-2xl border border-rose-500/20">
            <GitMerge className="w-8 h-8 text-rose-500 mb-4" />
            <h3 className="text-base font-bold text-white mb-2">Interactive Attack Path Graph</h3>
            <p className="text-xs text-slate-400 leading-relaxed">
              Real-time React Flow directed topology map visualizing host-to-host lateral movement, process spawning, and compromised credential usage.
            </p>
          </div>

          <div className="glass-panel p-6 rounded-2xl border border-emerald-500/20">
            <Bot className="w-8 h-8 text-emerald-400 mb-4" />
            <h3 className="text-base font-bold text-white mb-2">RAG-Powered SOC Copilot</h3>
            <p className="text-xs text-slate-400 leading-relaxed">
              Conversational assistant powered by vector store retrieval over MITRE ATT&CK enterprise datasets and live incident evidence.
            </p>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-slate-800 py-6 text-center text-xs text-slate-500 font-mono">
        SentinelAI Cyber Resilience Engine • Designed for ET AI Hackathon 2026
      </footer>
    </div>
  );
}
