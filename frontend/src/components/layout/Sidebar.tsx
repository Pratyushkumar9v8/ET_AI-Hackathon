"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { 
  ShieldAlert, LayoutDashboard, AlertTriangle, Eye, Crosshair, 
  GitMerge, Grid, ShieldCheck, UserCheck, Bot, BarChart3, Settings, Server
} from "lucide-react";

const NAVIGATION_ITEMS = [
  { name: "Dashboard", href: "/dashboard", icon: LayoutDashboard },
  { name: "Incident Center", href: "/incidents", icon: AlertTriangle, badge: "3" },
  { name: "Threat Intel", href: "/threat-intel", icon: Eye },
  { name: "ATT&CK Matrix", href: "/mitre", icon: Grid },
  { name: "Attack Graph", href: "/attack-graph", icon: GitMerge },
  { name: "User Behavior", href: "/uba", icon: UserCheck },
  { name: "Asset Inventory", href: "/assets", icon: Server },
  { name: "Response SOAR", href: "/soar", icon: ShieldCheck },
  { name: "SOC Copilot", href: "/copilot", icon: Bot, highlight: true },
  { name: "Analytics", href: "/analytics", icon: BarChart3 }
];

export function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="w-64 h-screen bg-[#0E1524] border-r border-[#1E293B] flex flex-col fixed left-0 top-0 z-40">
      {/* Brand Header */}
      <div className="p-5 border-b border-[#1E293B] flex items-center gap-3">
        <div className="w-10 h-10 rounded-lg bg-gradient-to-tr from-cyan-500 to-emerald-500 p-[2px]">
          <div className="w-full h-full bg-[#090D16] rounded-[6px] flex items-center justify-center">
            <ShieldAlert className="w-6 h-6 text-cyan-400" />
          </div>
        </div>
        <div>
          <h1 className="font-bold text-lg tracking-wider bg-gradient-to-r from-cyan-400 via-emerald-400 to-blue-500 bg-clip-text text-transparent">
            SENTINEL<span className="text-rose-500">.AI</span>
          </h1>
          <p className="text-[10px] text-slate-400 tracking-widest uppercase">CNI Cyber Resilience</p>
        </div>
      </div>

      {/* Navigation Items */}
      <nav className="flex-1 px-3 py-4 space-y-1 overflow-y-auto">
        {NAVIGATION_ITEMS.map((item) => {
          const isActive = pathname === item.href;
          const Icon = item.icon;

          return (
            <Link
              key={item.name}
              href={item.href}
              className={`flex items-center justify-between px-3.5 py-2.5 rounded-lg text-xs font-medium transition-all ${
                isActive
                  ? "bg-gradient-to-r from-cyan-500/20 to-blue-500/10 text-cyan-300 border border-cyan-500/30 shadow-[0_0_15px_rgba(6,182,212,0.15)]"
                  : "text-slate-400 hover:text-slate-200 hover:bg-slate-800/50"
              }`}
            >
              <div className="flex items-center gap-3">
                <Icon className={`w-4 h-4 ${isActive ? "text-cyan-400" : item.highlight ? "text-rose-400 animate-pulse" : "text-slate-400"}`} />
                <span>{item.name}</span>
              </div>
              {item.badge && (
                <span className="px-1.5 py-0.5 text-[10px] font-bold rounded-full bg-rose-500/20 text-rose-400 border border-rose-500/30">
                  {item.badge}
                </span>
              )}
            </Link>
          );
        })}
      </nav>

      {/* System Status Footer */}
      <div className="p-4 border-t border-[#1E293B] bg-[#0A0F1B]">
        <div className="flex items-center justify-between text-[11px] text-slate-400 mb-2">
          <span>Agent Mesh Status</span>
          <span className="flex items-center gap-1.5 text-emerald-400 font-mono text-[10px]">
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-ping" />
            OPERATIONAL
          </span>
        </div>
        <div className="w-full bg-slate-800 rounded-full h-1.5 overflow-hidden">
          <div className="bg-gradient-to-r from-cyan-500 to-emerald-400 h-full w-[94%]" />
        </div>
        <p className="text-[9px] text-slate-500 mt-2 font-mono">CNI Shield v2.4 • Node #01</p>
      </div>
    </aside>
  );
}
