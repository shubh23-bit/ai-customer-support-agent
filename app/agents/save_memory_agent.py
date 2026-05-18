from app.db.memory_store import (
    load_memory,
    save_memory
)


def save_conversation(state):

    customer_id = state["customer_id"]

    memory_db = load_memory()

    if customer_id not in memory_db:
        memory_db[customer_id] = []

    new_memory = f"""
    EMAIL: {state['email']}
    CATEGORY: {state['category']}
    SENTIMENT: {state['sentiment']}
    """

    memory_db[customer_id].append(new_memory)

    print("\nSAVING MEMORY:\n")
    print(new_memory)

    save_memory(memory_db)

    return state