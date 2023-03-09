from pydantic import BaseModel


class AlgoBase: 
    def __init__(self, name) -> None:
        self.name = name
    def to_string(self):
        return self.name + '\n---'
    

class AlgoModel(BaseModel): 
    id: int | None = None
    name: str
