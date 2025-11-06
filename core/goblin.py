from .player import Players
import random

class Goblin(Players):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.hp = 20
        self.type = "goblin"
        self.speed =  random.randint(5, 10) 
        self.power =  random.randint(5, 10) 
        self.armor_rating = 1
        self.weapon = random.choice(["sword", "ax", "knife"]) 

        

    def run_away(self):
        pass

