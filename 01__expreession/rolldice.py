import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

# Simulate one roll of two dice
print("Rolling two dice...")
result1, result2 = roll_dice()
total = result1 + result2

# Print the results
print(f"Die 1: {result1}")
print(f"Die 2: {result2}")
print(f"Total: {total}")