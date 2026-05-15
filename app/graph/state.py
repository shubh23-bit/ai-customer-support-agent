from typing import TypedDict

class EmailState(TypedDict):
    email:str
    category:str
    sentiment:str
    response:str
    next_step:str
    
