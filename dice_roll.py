import random


def d20roll():
    """
    Input: None
    Output:
        [0] Dice roll value
        [1] Roll outcome
    """
    roll = random.randint(1, 20)
    if roll == 1:
        outcome = "Catasrophe"
    elif 2 <= roll <= 5:
        outcome = "Failure"
    elif 6 <= roll <= 10:
        outcome = "Tough Choice"
    elif 11 <= roll <= 19:
        outcome = "Success"
    elif roll == 20:
        outcome = "Triumph"
    return roll, outcome
