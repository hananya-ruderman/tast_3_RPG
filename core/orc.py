from .player import Players
import random


class Orc(Players):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.hp = 50
        self.type = "orc"
        self.speed =  random.randint(0, 5) 
        self.power =  random.randint(10, 15) 
        self.armor_rating =  random.randint(2, 8) 
        self.weapon =  random.choice(["sword", "ax", "knife"]) 

   