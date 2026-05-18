from langgraph.graph import StateGraph, END

from app.graph.state import EmailState
from app.agents.classifier_agent import classify_email
from app.agents.sentiment_agent import analyze_sentiment
from app.agents.response_agent import generate_response
from app.agents.supervisior_agent import supervisor_agent
from app.agents.escalation_agent import escalate_issue
from app.agents.memory_agent import retrieve_memory
from app.agents.save_memory_agent import save_conversation


workflow = StateGraph(EmailState)

# Add Nodes
workflow.add_node("classifier_agent", classify_email)
workflow.add_node("sentiment_agent", analyze_sentiment)
workflow.add_node("supervisor_agent", supervisor_agent)
workflow.add_node("response_agent", generate_response)
workflow.add_node("escalation_agent", escalate_issue)
workflow.add_node("memory_agent", retrieve_memory)
workflow.add_node("save_memory_agent", save_conversation)

# Entry Point
workflow.set_entry_point("memory_agent")

# Flow Edges
workflow.add_edge("memory_agent", "classifier_agent")
workflow.add_edge("classifier_agent", "sentiment_agent")
workflow.add_edge("sentiment_agent", "supervisor_agent")

# Conditional Routing
def route_decision(state):
    return state["next_step"]


workflow.add_conditional_edges(
    "supervisor_agent",
    route_decision,
    {
        "reply": "response_agent",
        "escalate": "escalation_agent"
    }
)

# End Edges
workflow.add_edge("response_agent", "save_memory_agent")
workflow.add_edge("save_memory_agent", END)

workflow.add_edge("escalation_agent", END)

# Compile Graph
app = workflow.compile()