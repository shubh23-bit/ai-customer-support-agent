from langchain_ollama import ChatOllama
llm=ChatOllama(model="phi3")

def generate_response(state):
    category=state["category"]
    sentiment=state["sentiment"]
    email=state["email"]

    prompt=f"""

you are profrssionl customer supoort agent

customer Email:
{email}

cateogry:
{category}

sentiment:
{sentiment}

Genratw a professional response email.
"""
    response=llm.invoke(prompt)
    state["response"]=response.content
    return state
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 