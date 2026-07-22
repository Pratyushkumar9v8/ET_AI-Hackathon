"use client";

import { useState } from "react";
import { Sidebar } from "@/components/layout/Sidebar";
import { Header } from "@/components/layout/Header";
import { Eye, Search, ShieldAlert, Globe, Server, Hash, AlertTriangle, CheckCircle2 } from "lucide-react";

const KNOWN_IOCS = [
  { value: "198.51.100.42", type: "IP", actor: "APT29 (Cozy Bear)", malware: "Cobalt Strike C2", confidence: 95, country: "RU", origin: "Russia" },
  { value: "203.0.113.15", type: "IP", actor: "VOLT TYPHOON", malware: "Web Shell Proxy", confidence: 90, country: "CN", origin: "China" },
  { value: "bad-domain-exfil.com", type: "Domain", actor: "Lazarus Group", malware: "DNS Tunneling", confidence: 88, country: "KP", origin: "North Korea" },
  { value: "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", type: "SHA256", actor: "LockBit 3.0", malware: "Ransomware Encryptor", confidence: 99, country: "Global", origin: "Distributed" }
];

export default function ThreatIntelPage() {
  const [searchQuery, setSearchQuery] = useState("");
  const [lookupResult, setLookupResult] = useState<any>(null);

  const handleLookup = (e: React.FormEvent) => {
    e.preventDefault();
    const hit = KNOWN_IOCS.find(i => i.value.toLowerCase() === searchQuery.trim().toLowerCase());
    if (hit) {
      setLookupResult({ status: "MALICIOUS", data: hit });
    } else {
      setLookupResult({ status: "CLEAN", query: searchQuery });
    }
  };

  return (
    <div className="min-h-screen bg-[#090D16] text-slate-100 flex">
      <Sidebar />
      <Header />

      <main className="flex-1 ml-64 pt-20 p-6 space-y-6">
        <div>
          <h2 className="text-xl font-bold tracking-tight text-white flex items-center gap-2">
            <Eye className="w-5 h-5 text-cyan-400" /> Threat Intelligence Repository
          </h2>
          <p className="text-xs text-slate-400 mt-0.5 font-mono">Global Malicious IPs, Domains, Hashes & CVE Correlation</p>
        </div>

        {/* Search IOC Form */}
        <div className="glass-panel p-5 rounded-xl">
          <form onSubmit={handleLookup} className="flex gap-3">
            <div className="relative flex-1">
              <Search className="w-4 h-4 absolute left-3 top-3 text-slate-400" />
              <input
                type="text"
                placeholder="Search IP, Domain, File Hash (e.g. 198.51.100.42)..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full pl-9 pr-4 py-2 bg-slate-900 border border-slate-800 rounded-lg text-xs font-mono text-white focus:outline-none focus:border-cyan-500"
              />
            </div>
            <button type="submit" className="px-5 py-2 bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold text-xs rounded-lg transition-all">
              Lookup IOC
            </button>
          </form>

          {lookupResult && (
            <div className="mt-4 p-4 rounded-lg bg-slate-900 border border-slate-800 text-xs font-mono">
              {lookupResult.status === "MALICIOUS" ? (
                <div className="text-rose-400 space-y-1">
                  <p className="font-bold flex items-center gap-2 text-sm">
                    <ShieldAlert className="w-4 h-4 text-rose-500" /> KNOWN MALICIOUS IOC MATCH FOUND
                  </p>
                  <p>Actor: <strong>{lookupResult.data.actor}</strong> | Malware: <strong>{lookupResult.data.malware}</strong> | Confidence: <strong>{lookupResult.data.confidence}%</strong></p>
                </div>
              ) : (
                <div className="text-emerald-400 flex items-center gap-2">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400" /> No malicious matches found for indicator: {lookupResult.query}
                </div>
              )}
            </div>
          )}
        </div>

        {/* IOC Table */}
        <div className="glass-panel rounded-xl overflow-hidden">
          <div className="p-4 border-b border-slate-800">
            <h3 className="text-sm font-semibold text-white">Active Threat Feed Indicators</h3>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs font-mono">
              <thead className="bg-slate-900/80 text-slate-400 uppercase text-[10px] border-b border-slate-800">
                <tr>
                  <th className="p-3.5">Indicator Value</th>
                  <th className="p-3.5">Type</th>
                  <th className="p-3.5">Threat Actor</th>
                  <th className="p-3.5">Malware Family</th>
                  <th className="p-3.5">Geo Origin</th>
                  <th className="p-3.5">Confidence</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800/60">
                {KNOWN_IOCS.map((ioc, i) => (
                  <tr key={i} className="hover:bg-slate-800/30">
                    <td className="p-3.5 font-bold text-rose-300">{ioc.value}</td>
                    <td className="p-3.5"><span className="px-2 py-0.5 rounded bg-slate-800 border border-slate-700 text-slate-300">{ioc.type}</span></td>
                    <td className="p-3.5 text-cyan-300">{ioc.actor}</td>
                    <td className="p-3.5 text-slate-300">{ioc.malware}</td>
                    <td className="p-3.5 text-slate-400">{ioc.origin} ({ioc.country})</td>
                    <td className="p-3.5 text-rose-400 font-bold">{ioc.confidence}%</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </main>
    </div>
  );
}
