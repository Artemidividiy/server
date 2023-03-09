
from pydantic import BaseModel


class ColorBase: 
    def __init__(self, name, hex, rgb) -> None:
        self.name = name
        self.hex = hex
        self.rgb = rgb

    def to_string(self): 
        return f"name: {self.name}\nhex: {self.hex}, rgb: {self.rgb}\n---\n"

class ColorModel(BaseModel):
    id: int | None = None
    name: str
    hex: str
    rgb: list[int]