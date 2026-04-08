import random

DICE_ART = {1:"⚀", 2:"⚁", 3:"⚂", 4:"⚃", 5:"⚄", 6:"⚅"}

def roll():
    return random.randint(1, 6)

def get_face(n):
    return DICE_ART[n]