# We need to import our Player class
from player import Player

class Human(Player):
    def __init__(self,name):
        super().__init__(name)

    def player_choice(self):
        self.player_choice = input('What gesture would you like to play this round?  ')

    def current_score(self):
        self.current_score = +1