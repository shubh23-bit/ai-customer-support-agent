from langgraph.graph import StateGraph,END

from app.graph.state import EmailState
from app.agents.classifier_agent import classify_email
from app.agents.sentiment_agent import analyze_sentiment
from app.agents.response_agent import generate_response
from app.agents.supervisior_agent import supervisor_agent
from app.agents.escalation_agent import escalate_issue


workflow=StateGraph(EmailState)

#Add Node

workflow.add_node("classifier",classify_email)
workflow.add_node("sentiment",analyze_sentiment)
workflow.add_node("supervisor",supervisor_agent)
workflow.add_node("response",generate_response)
workflow.add_node("escalate",escalate_issue)

#Entry Point
workflow.set_entry_point("classifier")

#flow edge
workflow.add_edge("classifier","sentiment")
workflow.add_edge("sentiment","supervisor")

#conditional routing
def route_decision(state):
    return state["next_step"]

workflow.add_conditional_edges(
    "supervisor",
    route_decision,
    {
        "reply":"response",
        "escalate":"escalate"
    }
)
#End Edge
workflow.add_edge("classifier",END)
workflow.add_edge("escalate",END)

#compile graph
app=workflow.compile()
