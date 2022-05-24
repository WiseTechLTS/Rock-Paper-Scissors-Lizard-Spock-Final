from human import Human
from computer import Computer
from player import Player
from random import choice 

class Game:
    def __init__(self):
        self.player_one = Human('player_one')
        self.player_two = Player('player_two')
        self.listed_gestures = ["rock", "paper", "scissors", "lizard", "spock"]
        # This is all the players needed We will assign computer as player_two if chosen
    
    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.select_opponent()
        self.play()
        self.display_winner()

     # (5 points): As a developer, I want to make at least 10 commits with descriptive messages.
    GesturesList = ["rock","paper","scissors","lizard","spock"]
    
     # Display welcome message
    def display_welcome(self):
        print('Welcome to Rock Paper Scissors Lizard Spock Final! ')
     # Print Rules
    def display_rules(self):
        print('// Rock crushes Scissors //')
        print('// Scissors cuts Paper //') 
        print('// Paper covers Rock //')
        print('// Rock crushes Lizard //') 
        print('// Lizard poisons Spock //')
        print('//  Spock smashes Scissors //')
        print('// Scissors decapitates Lizard //')
        print('// Lizard eats Paper //') 
        print('// Paper disproves Spock //')
        print('// Spock vaporizes Rock //')
    
     # Function to select opponents
     # (10 points): As a player, I want the option of a single player (human vs AI) or a multiplayer (human vs human) game.
     # We need a tool to choose between Player vs. Ai
     # Or Player vs. Player
     # Function for game selection
    def select_opponent(self):
        response = input('Type 1 for Player vs. Ai:  or  2 for Player vs. Player:  ')
        if response == '1':
            self.player_two = Computer('player_two')
            print('Player vs. Ai!')
        elif response == '2':
            self.player_two = Human('player_two')
            print('Player vs. Human')
    
    
    # Main PLAY FUNCTION Best of Three 
    def play(self):
        self.player_one.player_choice
        self.player_two.player_choice
    # While loop for the main game phase
    # (10 points): As a player, I want the game of RPSLS to be at minimum a ‘best of three’ to decide a winner.
        while self.player_one.current_score < 2 and self.player_two.current_score < 2:
         # We want 
            print(" Type your selection:/ rock / paper / scissors / lizard / spock /")
            player_choice = input()
         # This is how we define our players choice
            player_choice = player_choice.lower()
         # Print our players choice desired = "Player Picked" playerChoice
            print("Player Picked", player_choice)
         # This is our random computer choice
         # We import random.choice so that we can randomly select from our 5 choices
            computer_choice = choice(self.listed_gestures)
         # Display "Computer picked:" computerChoice
            print("Computer picked:", computer_choice)
         # (10 points): As a developer, I want to store all of the gesture options/choices in a list. I want to find
            choice_dictionary = {"rock": 0, "paper": 1, "scissors": 2, "lizard": 3, "spock": 4}
       
            choice_index = choice_dictionary.get(player_choice, 5)
            computer_index = choice_dictionary.get(computer_choice)

         ##  Our matrix is numbered to represent if we will win, lose, tie or be invalid
            result_matrix = [ [0,2,1,1,2],
                              [1,0,2,2,1],
                              [2,1,0,1,2],
                              [2,1,2,0,1],
                              [1,2,1,2,0],
                              [3,3,3,3,3] ]


         #(5 points): As a developer, I want to account for and handle bad user input, ensuring that any user input is validated and reobtained if necessary.

            result_idx = result_matrix[choice_index][computer_index]
            result_note = ['Tie Round!', 'You Win!', 'Sorry, you lose', 'invalid choice, try again']
            result = result_note[result_idx]

            print(result_idx(result_note))

         # Display Winner
    def display_winner(self):
     while True:   
      if self.player_one== 2:
         False 
         print("Player One is the Winner")
      elif self.player_two== 2:
         False
         print('Player Two is the Winner!')

    
    # No If statement RPSLS
    ####  R   P   S   L   Sp 
    # R | 0 | 2 | 1 | 1 | 2 |
    # P | 1 | 0 | 2 | 2 | 1 |
    # S | 2 | 1 | 0 | 1 | 2 |
    # L | 2 | 1 | 2 | 0 | 1 |
    # S | 1 | 2 | 1 | 2 | 0 |
    # In| 5 | 5 | 5 | 5 | 5 |

    ## This approach was gleaned from multiple sources including: Youtube.com, DevCodeCamp pdfs, w3 schools. 
     # If dictionary is not allowed we have another list here
        #
        # gesture_list ['rock', 'paper', 'scissors', 'lizard', 'spock']
        # We would then choose to convert the string values into integers
        #
        #   FUNCTION TO CONVERT STRING TO INTEGER FOR IF / ELIF
        #
        # def name_to_int(name):
        #    if name == 'rock':
        #        return 0
        #    elif name == 'paper':
        #        return 1
        #    elif name == 'scissors':
        #        return 2
        #    elif name == 'lizard':
        #        return 3
        #    elif name == 'spock':
        #        return 4
        #    else:
        #        print('Invalid Input: Try Again: ')
        #
        #  FUNCTION TO CONVERT INTEGER TO STRING FOR IF / ELIF
        #
        # def number_to_name(number):
        #    if name ==0:
        #        return 'rock'
        #    elif name ==1:
        #        return 'paper'
        #    elif name ==2:
        #        return 'scissors'
        #    elif name ==3:
        #        return 'lizard'
        #    elif name ==4:
        #        return 'spock'
        #    else:
        #        print('Invalid Input: Try Again: ')
        #
        # Here we want to
