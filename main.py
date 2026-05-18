from app.graph.workflow import app
intial_state={
    "customer_id":"cust_101",
    "email":"Why is my refund still pending?",
    "category":"",
    "sentiment":"",
    "context":"",
    "memory":[],
    "response":"",
    "next-step":""
}
result =app.invoke(intial_state)

print("\nFINAL RESULT\n")
print(result["response"])