from app.db.memory_store import load_memory

def retrieve_memory(state):

    customer_id=state["customer_id"]

    memory_db=load_memory()
    customer_memory=memory_db.get(customer_id,[])

    print("\nFetched memeory:\n")
    print(customer_memory)

    state["memory"]=customer_memory
    return state

# read customer_id 
# find previous conversastions
#update state["memory"]
