#import random
#import Player
## 
###
#### Rock Paper Scissors Lizard Spock
####            Final
###          Inheritance 
## 
##   Before you begin coding, write an algorithm that represents the steps necessary to #   play a game of rock, paper, scissors, lizard, Spock in a best-of-three format. By #   writing out the steps, it will make you think about every piece needed to bring the #   game to life. Please submit to your instructor Slack channel once completed for  #   approval to start coding. Below is an example of how to get started:

##  Step one: Display the rules of the game.
##   Step Two: Ask for number of human users. 
##    Step Three: Users select gesture
##     Step Four: Compare and decide winner of round.
##    Step Five: Decide winner one user reaches 2 rounds won. 
##   Step Six: Display winner. 
##  Step Seven: Restart / Exit program 

## We want to write a function that equate our string variables to integers. Whole numbers will work just fine.
#Rpsls_gesture = [
#0 == 'Rock',
#1 == 'Spock',
#2 == 'Paper',
#3 == 'Lizard', 
#4 == 'Scissors',
#]
## We will write functions below this comment.
## The first thing we want to create is the numbers to name function. 
#def integer_to_name(num):
#    if num ==1:
#        result = "Rock"
#    elif num ==2:
#        result = "Spock"
#    elif num ==3:
#        result = "Paper"
#    elif num ==4:
#        result = "Lizard"
#    elif num ==5:
#        result = "Scissors"
#        return result

#########   Now Reverse
#########       it
#def name_to_integer(name):
#    if name == "Rock":
#        result = 1
#    elif name == "Spock":
#        result = 2
#    elif name == "Paper":
#        result = 3
#    elif name == "Lizard":
#        result = 4  
#    elif name == "Scissors":
#        result = 5
#        return result
##
## This next function will converts name to player_number using name to number.
## WE will need to create a random guess for ai_player using random.randrange()
##
#def rpsls(name):
#    player_number = input("Type gesture:   Enter for auto:  ")
#    while input == 'n':
#        name = input  
    
    
#    rnd = 0
#    num = random.randrange(1, 5)
#    print(f'{"Player 1 chooses", name }')
#    print('Computer chooses', num)

#    if (num +1) % 5 == player_number:
#        print("Player Wins!")
#        rnd +=1
#    elif (num +2) % 5 == player_number:
#        print("Player Wins!")
#    elif num == player_number:
#        print("Tie Round!")
#    else:
#        print("Computer Wins!")
        


#rpsls("Rock")
#rpsls("Spock")
#rpsls("Paper")
#rpsls("Lizard")
#rpsls("Scissors")
