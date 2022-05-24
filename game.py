from random import choice 
# (5 points): As a developer, I want to make at least 10 commits with descriptive messages.
GesturesList = ["rock","paper","scissors","lizard","spock"]
# While loop for the main game phase
while True:
    # We want 
    print("Type Gesture: ")
    playerChoice = input()
    # This is how we define our players choice
    playerChoice = playerChoice.lower()
    # Print our players choice desired = "Player Picked" playerChoice
    print("Player Picked", playerChoice)
    # This is our random computer choice
    # We import random.choice so that we can randomly select from our 5 choices
    computerChoice = choice(GesturesList)
    # Display "Computer picked:" computerChoice
    print("Computer picked:", computerChoice)
    # (10 points): As a developer, I want to store all of the gesture options/choices in a list. I want to find
    choice_dictionary = {"rock": 0, "paper": 1, "scissors": 2, "lizard": 3, "spock": 4}
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
    choice_index = choice_dictionary.get(playerChoice, 5)
    computer_index = choice_dictionary.get(computerChoice)

##  Our matrix is numbered to represent if we will win, lose, tie or be invalid
    result_matrix = [ [0,2,1,1,2],
                      [1,0,2,2,1],
                      [2,1,0,1,2],
                      [2,1,2,0,1],
                      [1,2,1,2,0],
                      [5,5,5,5,5] ]
##  0 = Tie, 1 = Winner, 2 = Lose, 5 = invalid
    
    result_idx = result_matrix[choice_index][computer_index]
    result_note = ['Tie Round!', 'You Win!', 'Sorry, you lose', 'invalid choice, try again']
    result = result_note[result_idx]

    print(result_idx)
    

# No If statement RPSLS
####  R   P   S   L   Sp 
# R | 0 | 2 | 1 | 1 | 2 |
# P | 1 | 0 | 2 | 2 | 1 |
# S | 2 | 1 | 0 | 1 | 2 |
# L | 2 | 1 | 2 | 0 | 1 |
# S | 1 | 2 | 1 | 2 | 0 |
# In| 5 | 5 | 5 | 5 | 5 |

## This approach was gleaned from multiple sources including: Youtube.com, DevCodeCamp pdfs, w3 schools. 