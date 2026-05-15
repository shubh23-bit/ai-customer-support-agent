from app.graph.workflow import app
intial_state={
    "email":"Hi,i am extremely angry with u.but i like u r  services.",
    "category":"",
    "sentiment":"",
    "response":"",
    "next-step":""
}
result =app.invoke(intial_state)

print("\nFINAL RESULT\n")
print(result)