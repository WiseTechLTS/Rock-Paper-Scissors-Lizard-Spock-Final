#(10 points): As a developer, I want to store all of the gesture options/choices in a list. I want to find
#a way to utilize the list of gestures within my code(display gesture options, assign player a gesture, etc).
# We will need a list of chosen gestures and a list of which gesture defeats which. Taken from the rules.
class Gesture:

    def __init__(self, gestureType):
        self.gestureType = gestureType
        self.defeats = []
        self.populateDefeats()

    def populateDefeats(self):
        if self.gestureType == "rock":
            self.defeats.append("scissors")
            self.defeats.append("lizard")

        elif self.gestureType == 'paper':
            self.defeats.append('rock')
            self.defeats.append('spock')

        elif self.gestureType == 'scissors':
            self.defeats.append('paper')
            self.defeats.append('lizard')

        elif self.gestureType == 'lizard':
            self.defeats.append('paper')
            self.defeats.append('spock')

        elif self.gestureType == 'spock':
            self.defeats.append('scissors')
            self.defeats.append('rock')
