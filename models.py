from pydantic import BaseModel

class MenuItem(BaseModel):
    id:int
    name:str
    price:float
    category:str
    description:str
    available:bool

class Menuresponse(BaseModel):
    status:str="success"
    count:int
    items:list[MenuItem]