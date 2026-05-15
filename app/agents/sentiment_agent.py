from langchain_ollama import ChatOllama

llm=ChatOllama(model="phi3")

def analyze_sentiment(state):
    email=state["email"]

    prompt=f"""

options:
- angry
- neutral
- happy


Email:
{email}

Return ONLY one word.
"""
    response=llm.invoke(prompt)
    sentiment=response.content.strip().lower()
    state["sentiment"]=sentiment
    return state