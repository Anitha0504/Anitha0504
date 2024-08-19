import random

def roll_dice():
    return random.randint(2, 6)

# Rolling the dice
result = roll_dice()
print(f"The dice roll result is: {result}")
