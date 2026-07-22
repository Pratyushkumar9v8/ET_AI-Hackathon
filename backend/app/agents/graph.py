from langgraph.graph import StateGraph, END
from app.agents.state import AgentState
from app.agents.behavior_agent import behavior_agent_node
from app.agents.threat_intel_agent import threat_intel_agent_node
from app.agents.mitre_agent import mitre_agent_node
from app.agents.correlation_agent import correlation_agent_node
from app.agents.risk_agent import risk_agent_node
from app.agents.prediction_agent import prediction_agent_node
from app.agents.response_agent import response_agent_node
from app.agents.report_agent import report_agent_node

def build_sentinel_agent_graph():
    """
    Constructs the LangGraph multi-agent execution pipeline.
    Behavior -> ThreatIntel -> MITRE -> Correlation -> Risk -> Prediction -> Response -> Report -> END
    """
    workflow = StateGraph(AgentState)

    workflow.add_node("behavior", behavior_agent_node)
    workflow.add_node("threat_intel", threat_intel_agent_node)
    workflow.add_node("mitre", mitre_agent_node)
    workflow.add_node("correlation", correlation_agent_node)
    workflow.add_node("risk", risk_agent_node)
    workflow.add_node("prediction", prediction_agent_node)
    workflow.add_node("response", response_agent_node)
    workflow.add_node("report", report_agent_node)

    # Set entry point
    workflow.set_entry_point("behavior")

    # Define edges
    workflow.add_edge("behavior", "threat_intel")
    workflow.add_edge("threat_intel", "mitre")
    workflow.add_edge("mitre", "correlation")
    workflow.add_edge("correlation", "risk")
    workflow.add_edge("risk", "prediction")
    workflow.add_edge("prediction", "response")
    workflow.add_edge("response", "report")
    workflow.add_edge("report", END)

    return workflow.compile()

sentinel_agent_mesh = build_sentinel_agent_graph()

def run_agent_pipeline(raw_events: list[dict]) -> AgentState:
    initial_state: AgentState = {
        "raw_events": raw_events,
        "analyzed_events": [],
        "threat_intel_hits": [],
        "mitre_mappings": [],
        "correlated_incidents": [],
        "composite_risk_score": 0,
        "predicted_next_step": {},
        "recommended_playbook": {},
        "generated_report": "",
        "agent_logs": []
    }
    return sentinel_agent_mesh.invoke(initial_state)
