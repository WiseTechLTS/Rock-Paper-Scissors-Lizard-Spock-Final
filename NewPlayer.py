from Gestures import Gesture

class Player:

    def __init__(self,name):
        self.readyGestures = [Gesture('rock'), Gesture('paper'), Gesture('scissors'), Gesture('lizard'), Gesture('spock')]
        self.chosenGesture = Gesture('NONE')
        self.name = name 
        self.score = 0 
    
    # Tool to increase score
    def winPoint(self):
        self.score +=1 