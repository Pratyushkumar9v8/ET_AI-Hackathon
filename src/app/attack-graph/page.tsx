"use client";

import { Sidebar } from "@/components/layout/Sidebar";
import { Header } from "@/components/layout/Header";
import { GitMerge, ShieldAlert } from "lucide-react";
import { ReactFlow, Background, Controls } from "@xyflow/react";
import "@xyflow/react/dist/style.css";

const initialNodes = [
  { id: '1', position: { x: 50, y: 150 }, data: { label: 'User: j.smith (Phished)' }, style: { background: '#1E293B', color: '#38BDF8', border: '1px solid #38BDF8', borderRadius: '8px', padding: '10px' } },
  { id: '2', position: { x: 300, y: 150 }, data: { label: 'WKSTN-FIN-08 (192.168.1.50)' }, style: { background: '#881337', color: '#FDA4AF', border: '1px solid #F43F5E', borderRadius: '8px', padding: '10px' } },
  { id: '3', position: { x: 600, y: 80 }, data: { label: 'Process: mimikatz.exe (LSASS)' }, style: { background: '#881337', color: '#FDA4AF', border: '1px solid #F43F5E', borderRadius: '8px', padding: '10px' } },
  { id: '4', position: { x: 600, y: 220 }, data: { label: 'Process: powershell -enc...' }, style: { background: '#881337', color: '#FDA4AF', border: '1px solid #F43F5E', borderRadius: '8px', padding: '10px' } },
  { id: '5', position: { x: 900, y: 150 }, data: { label: 'SRV-DC-01 (192.168.1.10) [COMPROMISED]' }, style: { background: '#991B1B', color: '#FCA5A5', border: '2px solid #EF4444', borderRadius: '8px', padding: '12px', fontWeight: 'bold' } },
  { id: '6', position: { x: 1200, y: 150 }, data: { label: 'PLC-WATER-PUMP-01 (10.0.4.20) [TARGETED]' }, style: { background: '#78350F', color: '#FDE68A', border: '1px solid #F59E0B', borderRadius: '8px', padding: '10px' } }
];

const initialEdges = [
  { id: 'e1-2', source: '1', target: '2', label: 'AUTHENTICATED_TO', animated: true, style: { stroke: '#38BDF8' } },
  { id: 'e2-3', source: '2', target: '3', label: 'SPAWNED_PROCESS', animated: true, style: { stroke: '#F43F5E' } },
  { id: 'e2-4', source: '2', target: '4', label: 'SPAWNED_PROCESS', animated: true, style: { stroke: '#F43F5E' } },
  { id: 'e3-5', source: '3', target: '5', label: 'WMI LATERAL MOVEMENT', animated: true, style: { stroke: '#EF4444', strokeWidth: 2 } },
  { id: 'e5-6', source: '5', target: '6', label: 'PREDICTED NEXT STEP (Modbus)', animated: true, style: { stroke: '#F59E0B', strokeDasharray: '5,5' } }
];

export default function AttackGraphPage() {
  return (
    <div className="min-h-screen bg-[#090D16] text-slate-100 flex">
      <Sidebar />
      <Header />

      <main className="flex-1 ml-64 pt-20 p-6 space-y-6 flex flex-col h-screen">
        <div>
          <h2 className="text-xl font-bold tracking-tight text-white flex items-center gap-2">
            <GitMerge className="w-5 h-5 text-cyan-400" /> Interactive Attack Path Topology Graph
          </h2>
          <p className="text-xs text-slate-400 mt-0.5 font-mono">Multi-Hop Entity Linkage & Lateral Movement Visualizer</p>
        </div>

        {/* Graph Canvas */}
        <div className="flex-1 glass-panel rounded-xl overflow-hidden relative">
          <ReactFlow nodes={initialNodes} edges={initialEdges} fitView>
            <Background color="#1E293B" gap={16} />
            <Controls />
          </ReactFlow>
        </div>
      </main>
    </div>
  );
}
