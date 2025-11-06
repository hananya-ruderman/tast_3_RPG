from core.player import Players, Player
from core.orc import Orc
from core.goblin import Goblin
import random

class Game:
    def __init__(self, monsters):
        self.monsters = monsters
   
    
    def start(self):
        player = self.create_player()
        monster = self.choose_random_monster()
        print("game started")
        while player.hp > 0 and monster.hp > 0:
            print("turn")
            self.battle(player, monster)
            player, monster = monster, player
           
        print ("game over")
        
    
    def show_menu(self):
        pass
        
    
    def create_player(self):
        player = Player()
        player.name = random.choice(["joe", "ben"])
        player.profession = random.choice(["doctor", "soldier"])
        if player.profession  == "doctor":
            player.hp += 10
        if player.profession == "soldier":
            player.power += 2
        return player
    
    
    def choose_random_monster(self):
        monster = random.choice(self.monsters)

        return monster

        
    def battle(self, player, monster):
        player_start = 0
        monster_start = 0
        monster_power = 0
        player_power = 0
        player_start += self.roll_dice(6)
        monster_start += self.roll_dice(6)
        if monster.speed + monster_start > player.speed + player_start:
           monster_power =  monster.speed + self.roll_dice(20)
           if monster.attack(monster_power, player) == "hurt":
               player.hp -= (self.roll_dice(6) * monster.power)
               print("player hurt")
           elif monster.attack(monster_power, player) == "missed":
               print("monster missed")
        elif monster.speed + monster_start <= player.speed + player_start:
            player_power = player.speed + self.roll_dice(20)
            if player.attack(player_power, monster) == "hurt":
               monster.hp -= self.roll_dice(6) 
               print("monster hurt")
            elif player.attack(player_power, monster) == "missed":
               print("player missed")

   
    def roll_dice(self, sides):
        dice_outcome = random.randint(1, sides)
        return dice_outcome
    


