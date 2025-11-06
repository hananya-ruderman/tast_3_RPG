from game import Game
from core.orc import Orc
from core.goblin import Goblin

if __name__ == "__main__":
    monster1 = Orc("boom")
    monster2 = Goblin("trach")
    monsters = [monster1, monster2]
    game = Game(monsters)

    game.start()