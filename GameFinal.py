#from PlayerClass import Player
#from CompAi import Ai 
#import random 


#Player
#Ai

## Rock Paper Scissors Lizard Spock
#rules = "Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock"

## We set a variable for a computer choice
#gesture_List = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
#ai_choice = ''
#player_choice = ''

## We set a variable for a computer choice
#def choosing_round(gesture_list):
#    ai_choice = random.choice(gesture_List)
#    player_choice = input("Type gesture choice:  or Type pick for random: ")
#    if input == 'Pick' or 'type':
#        player_choice=random.choice(gesture_List)
#        # Now lets print to the console our ai and player choice
#        print(f"Player chose{player_choice}, Ai chose {ai_choice}.")

## Counts 
#tie_count = int()


## We need a tool to decide a winner

#def decide_winnerPlayerAi(player_choice, ai_choice, tie_count):
#    player_round_wins = int()
#    ai_round_wins = int()
    
#    while True:

#        if player_choice == ai_choice:
#            tie_count+=1
#            print(f"You chose {player_choice} Ai chose {ai_choice} Tie round!")
#            return 0
#        if ai_choice == "Rock" and player_choice == "Scissors" or player_choice == "Lizard":
#            ai_round_wins+=1
#            print("Ai Wins!")
#            return 1    
#        elif player_choice == "Rock" and ai_choice == "Scissors" or ai_choice == "Lizard":
#            player_round_wins +=1
#            print("You Win!")
#            return 1
#        if ai_choice == "Scissors" and player_choice == "Paper" or player_choice == "Lizard":
#            ai_round_wins+=1
#            print("Ai Wins!")
#            return 1
#        elif player_choice == "Scissors" and ai_choice == "Paper" or ai_choice == "Lizard":
#            player_round_wins +=1
#            print("You Win!")
#            return 1
#        if ai_choice == "Paper" and player_choice == "Spock" or player_choice == "Rock":
#            ai_round_wins+=1
#            print("Ai Wins!")
#            return 1
#        elif player_choice == "Paper" and ai_choice == "Spock" or ai_choice == "Rock":
#            player_round_wins+=1
#            print("You Win!")
#            return 1
#        if ai_choice == "Spock" and player_choice == "Scissors" or player_choice == "Rock":
#            ai_round_wins+=1
#            print("Ai Wins!")
#            return 1
#        elif player_choice == "Spock" and ai_choice == "Scissors" or ai_choice == "Rock":
#            player_round_wins+=1
#            print("You Win!")
#            return 1 
#        if ai_choice == "Lizard" and player_choice == "Paper" or player_choice == "Spock":
#            ai_round_wins+=1
#            print("Ai Wins!")
#            return 1
#        elif player_choice == "Lizard" and ai_choice == "Paper" or ai_choice == "Spock":
#            player_round_wins+=1
#            print("You Win!")
#            return 1 
#        if player_round_wins ==2:
#            Player = False
#        elif ai_round_wins ==2:
#            Ai = False
#        print(f"Human{player_round_wins} Ai{ai_round_wins}")




#round=decide_winnerPlayerAi(player_choice, ai_choice, tie_count)




#class Game:
## Game Class
#    def __init__(self, player_choice, player2_choice, ai_choice, round_count, tie_count, player1_wins, player2_wins, ai_wins):
#        print("Rock paper scissors lizard spock. Welcome to the game.")
#        print("The rules are easy.")
#        print(" Rock crushes Scissors \ Scissors cuts Paper \ Paper covers Rock\  Rock crushes Lizard\  Lizard poisons Spock\  Spock smashes Scissors\  Scissors decapitates Lizard\  Lizard eats Paper\  Paper disproves Spock\  Spock vaporizes Rock")
#        print("Press Enter to begin.")
#        _ = input()

#        # We set a variable for users choice of gesture, round count, tie rounds and winners
#        self.player_choice = player_choice
#        self.player2_choice = player2_choice 
#        self.ai_choice = ai_choice
#        self.round_count = round_count
#        self.tie_count = tie_count
#        self.player1_wins = player1_wins
#        self.ai_wins = ai_wins
#        self.player2_wins = player2_wins


