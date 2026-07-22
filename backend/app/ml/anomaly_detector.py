import numpy as np
from sklearn.ensemble import IsolationForest
import logging

logger = logging.getLogger(__name__)

class AnomalyDetectorEngine:
    def __init__(self):
        # Initialize Isolation Forest with 100 estimators
        self.clf = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
        # Fit on baseline reference data
        dummy_baseline = np.random.normal(loc=0.0, scale=1.0, size=(200, 5))
        self.clf.fit(dummy_baseline)

    def extract_features(self, event_data: dict) -> np.ndarray:
        """
        Extract numerical features from event payload:
        [hour_of_day, command_length, is_admin_user, is_rare_port, is_ot_event]
        """
        timestamp = event_data.get("timestamp")
        hour = 12
        if hasattr(timestamp, "hour"):
            hour = timestamp.hour

        cmd = event_data.get("process_command_line", "") or ""
        cmd_len = len(cmd)

        user = str(event_data.get("user_name", "")).lower()
        is_admin = 1.0 if any(k in user for k in ["admin", "root", "system", "administrator"]) else 0.0

        dest_port = event_data.get("destination_port") or 80
        is_rare_port = 1.0 if dest_port not in [80, 443, 53, 22, 135, 445] else 0.0

        source_type = str(event_data.get("source_type", ""))
        is_ot = 1.0 if "OT" in source_type or "Modbus" in source_type else 0.0

        return np.array([[float(hour), float(cmd_len), is_admin, is_rare_port, is_ot]])

    def predict_anomaly(self, event_data: dict) -> tuple[float, bool]:
        """
        Returns (anomaly_score [0.0 to 1.0], is_anomaly [True/False])
        """
        features = self.extract_features(event_data)
        # Isolation Forest score_samples returns negative anomaly score (more negative = more anomalous)
        raw_score = self.clf.score_samples(features)[0]
        # Normalize to 0.0 - 1.0
        normalized_score = float(np.clip((0.5 - raw_score), 0.0, 1.0))
        
        # Override heuristics for known dangerous patterns
        cmd = str(event_data.get("process_command_line", "")).lower()
        if any(term in cmd for term in ["vssadmin delete", "mimikatz", "downloadstring", "nc -e", "modbus_write_single_register"]):
            normalized_score = max(normalized_score, 0.95)

        is_anomaly = normalized_score > 0.65
        return round(normalized_score, 4), is_anomaly

anomaly_engine = AnomalyDetectorEngine()
