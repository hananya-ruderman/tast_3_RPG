import random

class Players:
    def __init__(self):
        self.name = ""
        self.hp = 0 
        self.speed =  0
        self.power = 0
        self.armor_rating = 0

    def speak(self):
        print(f"i am {self.name}")

    def attack(self, power, enemy):
        if enemy.armor_rating < power:
            return "hurt"
        else:
            return "missed"
        

    
        

class Player(Players):
    def __init__(self):
        super().__init__()
       
        self.hp =  50
        self.speed =  random.randint(5, 10) 
        self.power = random.randint(5, 10)
        self.armor_rating = random.randint(5, 15) 
        self.profession = ""  

   