import random

class Ai(Human):
    def __init__(self):
        self.name = "AI"
        self.gesture = int or ' '

    gesture_choice = random.randrange(1,5)
    print("Ai chooses", gesture_choice)