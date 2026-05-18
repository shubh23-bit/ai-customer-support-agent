from typing import TypedDict,List

class EmailState(TypedDict):
    customer_id:str
    email:str
    category:str
    sentiment:str
    response:str
    next_step:str
    context:str
    memory:List[str]
    
