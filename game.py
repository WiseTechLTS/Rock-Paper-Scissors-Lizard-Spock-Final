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
      self.display_winner()  
      self.end_game()
    # (5 points): As a developer, I want to make at least 10 commits with descriptive messages.
    # Display welcome message
   def display_welcome(self):
       print('Welcome to Rock Paper Scissors Lizard Spock Final! ')
    # Print Rules
   def display_rules(self):
       print('// Rock crushes Scissors')
       print('// Scissors cuts Paper') 
       print('// Paper covers Rock')
       print('// Rock crushes Lizard') 
       print('// Lizard poisons Spock')
       print('// Spock smashes Scissors')
       print('// Scissors decapitates Lizard')
       print('// Lizard eats Paper') 
       print('// Paper disproves Spock')
       print('// Spock vaporizes Rock')
   
    # Function to select opponents
    # (10 points): As a player, I want the option of a single player (human vs AI) or a multiplayer (human vs human) game.
    # We need a tool to choose between Player vs. Ai
    # Or Player vs. Player
    # Function for game selection
   def select_opponent(self):
       response = input('Type 1 for Player vs. Ai:  or  2 for Player vs. Player:  ')
       if response == '1':
           print('Player vs. Ai!')
           self.play()
       elif response == '2':
           print('Player vs. Human')
           self.play_human()

   def play_human(self):
       self.player_one.player_choice
       self.player_two.player_choice
       self.player_one_wins = 0
       self.player_two_wins = 0
   # While loop for the main game phase
   # (10 points): As a player, I want the game of RPSLS to be at minimum a ‘best of three’ to decide a winner.
       while self.player_one_wins < 2 and self.player_two_wins < 2:
        # We want
         print(" Type your selection:/ rock / paper / scissors / lizard / spock /")
         # Print our players choice desired = "Player Picked" playerChoice
         self.player_one.player_choice = input('P1: or type a for auto choice. ')
         if self.player_one.player_choice == 'a':
            self.player_one.player_choice = choice(self.listed_gestures)
         else:
            pass
         print("Player Picked", self.player_one.player_choice)
         if self.player_one.player_choice == self.listed_gestures:
          True
         
         # This is how we define our players choice
         print(" Type your selection:/ rock / paper / scissors / lizard / spock /")
         self.player_two.player_choice = input('P2: or type a for auto. ')
         if self.player_two.player_choice == 'a':
            self.player_two.player_choice = choice(self.listed_gestures)
         else:
            pass
         print("Player Two Picked", self.player_two.player_choice)
         # This is our random computer choice
         # We import random.choice so that we can randomly select from our 5 choices
         #computer_choice = choice(self.listed_gestures)
         # Display "Computer picked:" computerChoice
         #print("Computer picked:", computer_choice)
         # (10 points): As a developer, I want to store all of the gesture options/choices in a list. I want to find
         choice_dictionary = {"rock": 0, "paper": 1,
                              "scissors": 2, "lizard": 3, "spock": 4}

         choice_index = choice_dictionary.get(self.player_one.player_choice, 3)
         choice_index2 = choice_dictionary.get(self.player_two.player_choice, 3)

         ##  Our matrix is numbered to represent if we will win, lose, tie or be invalid
         result_matrix = [[0, 2, 1, 1, 2],
                          [1, 0, 2, 2, 1],
                          [2, 1, 0, 1, 2],
                          [2, 1, 2, 0, 1],
                          [1, 2, 1, 2, 0],
                          [3, 3, 3, 3, 3]]

         #(5 points): As a developer, I want to account for and handle bad user input, ensuring that any user input is validated and reobtained if necessary.
         result_idx = result_matrix[choice_index][choice_index2]
         result_note = {"Tie Round!": 0, "You Win!": 1,
                        'Sorry, you lose': 2, 'invalid choice, try again': 3}
         #result = result_note[result_idx]
         needed_wins = 2

         if result_idx == 0:
            print('No Score: Possible input error:')
         elif result_idx == 1:
            print('Player One Winner')
            self.player_one_wins += 1
         elif result_idx == 2:
            print('Player Two Winner!')
            self.player_two_wins += 1
         elif result_idx == 3:
            print('Invaild input. Try again: ')
            print(result_idx)
            input()
         if self.player_one_wins == needed_wins:
            self.display_winner()
         elif self.player_two_wins == needed_wins:
            self.display_winner()
            #self.display_winner()
    # Main PLAY FUNCTION Best of Three player vs ai 
   def play(self):
       self.player_one.player_choice
       self.player_two.player_choice
       self.player_one_wins = 0
       self.player_two_wins = 0
   # While loop for the main game phase
   # (10 points): As a player, I want the game of RPSLS to be at minimum a ‘best of three’ to decide a winner.
       while self.player_one_wins < 2 and self.player_two_wins < 2:
        # We want 
         print(" Type your selection:/ rock / paper / scissors / lizard / spock /")
         self.player_one.player_choice = input('P1:  or type a for auto:' )
         if self.player_one.player_choice == 'a':
            self.player_one.player_choice = choice(self.listed_gestures)
         else: pass 
         # Print our players choice desired = "Player Picked" playerChoice
         print("Player Picked", self.player_one.player_choice)
         # This is our random computer choice
         # We import random.choice so that we can randomly select from our 5 choices
         computer_choice = choice(self.listed_gestures)
         # Display "Computer picked:" computerChoice
         print("Computer picked:", computer_choice)
         # (10 points): As a developer, I want to store all of the gesture options/choices in a list. I want to find
         choice_dictionary = {"rock": 0, "paper": 1, "scissors": 2, "lizard": 3, "spock": 4}
       
         choice_index = choice_dictionary.get(self.player_one.player_choice, 3)
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
         result_note = {"Tie Round!": 0, "You Win!": 1, 'Sorry, you lose': 2, 'invalid choice, try again': 3}
         #result = result_note[result_idx]
         needed_wins =2
            
         if result_idx == 0:
            print('Tie')
         elif result_idx == 1:
            print('Player Winner')
            self.player_one_wins +=1
         elif result_idx ==2:
            print('Computer Winner!')
            self.player_two_wins +=1
         elif result_idx == 3:
            print('Invaild input. Try again: ')   
            print(result_idx)
            input()
         if self.player_one_wins == needed_wins or self.player_two_wins == needed_wins:
            break

     # Display Winner
   def display_winner(self):
      ans = input
      if self.player_one_wins > self.player_two_wins:
       print('Player One is the Winner!')
      elif self.player_one_wins < self.player_two_wins:
       print('Player Two Wins!')
      else:
       input('Invalid selection. Try again: ')
       input('Would you like to play again? y/n: ')
      if ans == 'y':
       self.play()
      elif ans == 'n':
       self.display_welcome()
      self.end_game()
          
          
   def end_game(self):
      stop = input('press enter')
      return 


    
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
