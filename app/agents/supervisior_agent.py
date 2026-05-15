def supervisor_agent(state):
    sentiment=state["sentiment"]

    if sentiment=="angry":
        state["next_step"]="escalate"
    else:
        state["next_step"]="reply"
    return state