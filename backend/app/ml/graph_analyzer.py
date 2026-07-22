import networkx as nx
from typing import List, Dict, Any

class GraphAnalyzerEngine:
    def __init__(self):
        self.G = nx.DiGraph()

    def build_attack_graph_for_incident(self, events: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Builds a NetworkX directed graph connecting Users, Devices, IPs, and Processes
        from events to visualize lateral movement and attack propagation.
        """
        nodes_dict = {}
        edges_list = []

        for evt in events:
            host_name = evt.get("hostname") or "Unknown-Host"
            user_name = evt.get("user_name") or "SYSTEM"
            src_ip = evt.get("source_ip") or "192.168.1.100"
            dest_ip = evt.get("destination_ip") or "192.168.1.200"
            proc_name = evt.get("process_name") or "cmd.exe"

            # Host Node
            host_node_id = f"host_{host_name}"
            if host_node_id not in nodes_dict:
                nodes_dict[host_node_id] = {
                    "id": host_node_id,
                    "label": host_name,
                    "type": "Device",
                    "risk_level": "High" if evt.get("is_anomaly") else "Low",
                    "metadata": {"ip": src_ip}
                }

            # User Node
            user_node_id = f"user_{user_name}"
            if user_node_id not in nodes_dict:
                nodes_dict[user_node_id] = {
                    "id": user_node_id,
                    "label": user_name,
                    "type": "User",
                    "risk_level": "Critical" if "admin" in user_name.lower() else "Medium",
                    "metadata": {"role": "Domain Admin"}
                }

            # Process Node
            proc_node_id = f"proc_{proc_name}_{evt.get('id', '1')}"
            if proc_node_id not in nodes_dict:
                nodes_dict[proc_node_id] = {
                    "id": proc_node_id,
                    "label": proc_name,
                    "type": "Process",
                    "risk_level": "Critical" if evt.get("is_anomaly") else "Low",
                    "metadata": {"cmd": evt.get("process_command_line", "")}
                }

            # Edges
            edges_list.append({
                "id": f"edge_{user_node_id}_{host_node_id}",
                "source": user_node_id,
                "target": host_node_id,
                "relationship": "AUTHENTICATED_TO"
            })
            edges_list.append({
                "id": f"edge_{host_node_id}_{proc_node_id}",
                "source": host_node_id,
                "target": proc_node_id,
                "relationship": "SPAWNED_PROCESS"
            })

            if dest_ip and dest_ip != src_ip:
                target_ip_node_id = f"ip_{dest_ip}"
                if target_ip_node_id not in nodes_dict:
                    nodes_dict[target_ip_node_id] = {
                        "id": target_ip_node_id,
                        "label": dest_ip,
                        "type": "IP",
                        "risk_level": "Critical",
                        "metadata": {"external": True}
                    }
                edges_list.append({
                    "id": f"edge_{proc_node_id}_{target_ip_node_id}",
                    "source": proc_node_id,
                    "target": target_ip_node_id,
                    "relationship": "LATERAL_MOVEMENT"
                })

        return {
            "nodes": list(nodes_dict.values()),
            "edges": edges_list
        }

graph_analyzer = GraphAnalyzerEngine()
