


from tkinter.tix import InputOnly


class Game:

    def__init__(self):
    self.menu = ["One Player Game", "Two Player Game",
    "Setup Game", "Rules / HELP!", "Exit/Endgame"]
    self.player1 = Player|'Tom'|
    self.player2 = Player|'Jeff'|
    self.roundsToWin = 2
    self.bestInThree = 3
    self.mode = 'RPSLS'
    self.gameChoice = ["Play vs Ai","Play vs Human"]
    self.pVsAi = False 

# We need tools for the game to run
def scoreUpdate(self, player):
    print(player.name+ "Won the round!")

def showGestures():
    print("Press any Key to show each players gesture and compare: ")
    input()
    print('Player One chose: ' 'Player Two chose: ')

def compareGestures(self):
    playerOneWin = False
    if self.player1.chosenGesture.chosenType == self.player2.chosenGesture.chosenType:
        print("Tie Round! no score")
        return
    for gesture in self.player1.chosenGesture.defeats:
        if self.player2.chosenGesture.gestureType == gesture:
            self.ScoreUpdate(self.player1)
            playerOneWin = True
            break 
        
        if playerOneWin == False:
            self.ScoreUpdate(self.player2)


def showScores(self):
    print(f"Score: {self.player1, self.player1.score} and {self.player2, self.player2.score}")
    print('Any key press to continue')

def displayWinner(self):
    if (self.player1.score > self.player2.score):
        print(f"Game-Over: Player One Wins! {self.player1.score} - {self.player2.score}")
    else:
        print(f"Game-Over: Player Two Wins! {self.player1.score} - {self.player2.score}")


def endGame(self):
    self.player1.score = 0
    self.player2.score = 0

    userInput = input("Would you like to play again? -Y for yes, N or other key-press - main")
    if userInput == 'Y' or userInput == 'y':
        self.mainMenu()
    else:
        self.endGame()


def exitGame(self):
    # Clear choice restart
    self.mainMenu()


def startGame(self):
    print("Welcome to Rock Paper Scissors Lizard Spock!!" "Press any Key to continue.")
    input()
    mainMenu()


def mainMenu(self):
    userKey = input("Press 1 for Human vs. Ai & Press 2 for Human vs. Human: ")
    if userKey !='1' and userKey != '2':
        self.mainMenu()
    
    if userKey == '1':
        self.player1 = Human("Player One")
        self.player2 = Ai("Cortana", random)
        self.play()
    
    else:
        self.player1 = Human("Player One")
        self.player2 = Human("Player Two")
        self.play()