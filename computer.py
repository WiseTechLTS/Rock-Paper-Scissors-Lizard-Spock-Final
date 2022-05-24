# Import Player class and random
import Player 
from random import choice 

class Computer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.listed_gestures = ["rock", "paper", "scissors", "lizard", "spock"]

    def computer_choice(self):
        self.computer_choice = choice(self.listed_gestures)

    def current_score(self):
        self.current_score += 1