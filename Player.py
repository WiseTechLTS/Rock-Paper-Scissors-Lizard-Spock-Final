#(15 points): As a developer, I want to find a way to properly incorporate inheritance into my game.
class Player:
    def __init__(self, name):
        self.name = name 
        self.listed_gestures = ["rock", "paper", "scissors", "lizard", "spock"]
        self.player_choice = ''
        self.current_score = 0


    def player_choice(self):
        self.player_choice = ''

    def current_score(self):
        self.current_score = +1
# (10 points): As a developer, I want to store all of the gesture options/choices in a list. I want to find
# a way to utilize the list of gestures within my code(display gesture options, assign player a gesture, etc).

        