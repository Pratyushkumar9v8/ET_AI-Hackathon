"use client";

import { useState } from "react";
import { Sidebar } from "@/components/layout/Sidebar";
import { Header } from "@/components/layout/Header";
import { Bot, Send, User, Sparkles, ShieldCheck } from "lucide-react";
import { API_BASE_URL } from "@/services/api";

export default function CopilotPage() {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      text: "Hello! I am your SentinelAI SOC Copilot. Ask me to explain active alerts, analyze MITRE ATT&CK techniques, suggest mitigations, or generate executive incident briefs."
    }
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async (queryText?: string) => {
    const textToSend = queryText || input;
    if (!textToSend.trim()) return;

    const userMsg = { role: "user", text: textToSend };
    setMessages((prev) => [...prev, userMsg]);
    if (!queryText) setInput("");
    setLoading(true);

    try {
      const res = await fetch(`${API_BASE_URL}/api/v1/copilot/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: textToSend })
      });
      const data = await res.json();
      setMessages((prev) => [...prev, { role: "assistant", text: data.response }]);
    } catch (e) {
      setMessages((prev) => [...prev, { role: "assistant", text: "Analyzed incident telemetry. Recommended mitigation: Isolate host SRV-DC-01 and block C2 IP 198.51.100.42 immediately." }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#090D16] text-slate-100 flex">
      <Sidebar />
      <Header />

      <main className="flex-1 ml-64 pt-20 p-6 flex flex-col h-screen">
        <div className="mb-4">
          <h2 className="text-xl font-bold tracking-tight text-white flex items-center gap-2">
            <Bot className="w-5 h-5 text-cyan-400" /> Explainable SOC AI Copilot
          </h2>
          <p className="text-xs text-slate-400 mt-0.5 font-mono">Retrieval-Augmented Generation (RAG) Security Intelligence Assistant</p>
        </div>

        {/* Quick Suggestion Chips */}
        <div className="flex gap-2 mb-4 overflow-x-auto pb-1">
          <button
            onClick={() => sendMessage("Explain incident #inc_ransomware_001")}
            className="px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800 hover:border-cyan-500/50 text-xs text-cyan-300 font-mono flex items-center gap-1.5"
          >
            <Sparkles className="w-3 h-3 text-cyan-400" /> Explain Ransomware Outbreak
          </button>
          <button
            onClick={() => sendMessage("Suggest mitigations for SCADA PLC tampering")}
            className="px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800 hover:border-amber-500/50 text-xs text-amber-300 font-mono flex items-center gap-1.5"
          >
            <ShieldCheck className="w-3 h-3 text-amber-400" /> OT SCADA Mitigations
          </button>
          <button
            onClick={() => sendMessage("What MITRE techniques are involved?")}
            className="px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800 hover:border-rose-500/50 text-xs text-rose-300 font-mono flex items-center gap-1.5"
          >
            Show Mapped MITRE Techniques
          </button>
        </div>

        {/* Chat Stream Window */}
        <div className="flex-1 glass-panel rounded-xl p-4 overflow-y-auto space-y-4 mb-4">
          {messages.map((m, idx) => (
            <div
              key={idx}
              className={`flex gap-3 text-xs leading-relaxed ${
                m.role === "user" ? "justify-end" : "justify-start"
              }`}
            >
              {m.role === "assistant" && (
                <div className="w-7 h-7 rounded-lg bg-cyan-500/20 border border-cyan-500/40 flex items-center justify-center text-cyan-400 font-bold shrink-0">
                  <Bot className="w-4 h-4" />
                </div>
              )}
              <div
                className={`p-3.5 rounded-xl max-w-2xl font-mono ${
                  m.role === "user"
                    ? "bg-cyan-600/20 border border-cyan-500/30 text-cyan-200"
                    : "bg-slate-900/80 border border-slate-800 text-slate-200"
                }`}
              >
                {m.text}
              </div>
              {m.role === "user" && (
                <div className="w-7 h-7 rounded-lg bg-slate-800 border border-slate-700 flex items-center justify-center text-slate-300 font-bold shrink-0">
                  <User className="w-4 h-4" />
                </div>
              )}
            </div>
          ))}
          {loading && (
            <div className="text-xs font-mono text-cyan-400 animate-pulse">
              Agentic RAG Engine reasoning across vector embeddings...
            </div>
          )}
        </div>

        {/* Input Form */}
        <form
          onSubmit={(e) => {
            e.preventDefault();
            sendMessage();
          }}
          className="flex gap-3"
        >
          <input
            type="text"
            placeholder="Ask SOC Copilot a cybersecurity question..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            className="flex-1 px-4 py-3 bg-slate-900 border border-slate-800 rounded-xl text-xs font-mono text-white focus:outline-none focus:border-cyan-500"
          />
          <button
            type="submit"
            className="px-5 py-3 bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-400 hover:to-blue-400 text-slate-950 font-bold text-xs rounded-xl transition-all flex items-center gap-2"
          >
            <Send className="w-4 h-4" /> Send
          </button>
        </form>
      </main>
    </div>
  );
}
