from pydantic import BaseModel
from models.algo import AlgoBase, AlgoModel
from models.color import ColorModel


class SchemeBase: 
    def __init__(self, algo: AlgoBase, colors, id = None) -> None:
        self.id = id
        self.algo = algo
        self.colors = colors

    def to_string(self): 
        target = ""
        for i in self.colors: 
            target += i.to_string()
        target += f"\nvia {self.algo}"


class SchemeModel(BaseModel):
    id: int | None = None
    algo: AlgoModel
    colors: list[ColorModel]


    
