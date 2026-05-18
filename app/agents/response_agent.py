from langchain_ollama import ChatOllama
llm=ChatOllama(model="phi3")

def generate_response(state):
    category=state["category"]
    sentiment=state["sentiment"]
    email=state["email"]
    context=state["context"]
    memory="\n".join(state["memory"])
    
    prompt=f"""
    you are professional  AI supoort agent.

    Previous customer history
    {memory}

    COMPANY POLICY
    {context}
    
    customer Email:
    {email}

    cateogry:
    {category}

    sentiment:
    {sentiment}

Genrate a professional support response.
"""
    response=llm.invoke(prompt)
    state["response"]=response.content
    return state
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 