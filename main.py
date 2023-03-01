class Color: 
    def __init__(self, name, hex, rgb) -> None:
        self.name = name
        self.hex = hex
        self.rgb = rgb

    def to_string(self): 
        return f"name: {self.name}\nhex: {self.hex}, rgb: {self.rgb}\n---\n"

class Algo: 
    def __init__(self, name) -> None:
        self.name = name
    def to_string(self):
        return self.name + '\n---'
    
class Scheme: 
    def __init__(self, algo, colors) -> None:
        self.algo = algo
        self.colors = colors
        
    def to_string(self): 
        target = ""
        for i in self.colors: 
            target += i.to_string()
        target += f"\nvia {self.algo}"

def main():
    a = [Color(i, i, i) for i in range(10)]
    for i in a:
        print(i.to_string())

if __name__ == "__main__":
    main()