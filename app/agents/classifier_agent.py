from langchain_ollama import ChatOllama

llm=ChatOllama(
    model="phi3"
)
def classify_email(state):
    email=state["email"]

    prompt=f"""

Classify the customer support email into one catrgory 

Categories:
-biling
-refud
-technical
-general

Email:
{email}

Return ONLY category name
"""
    response=llm.invoke(prompt)

    category=response.content.strip()

    state["category"]=category

    return state