import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2  # Returns a tuple with two values

# Main program
print("Simulating rolling two dice, three times:")
for roll in range(1, 4):
    result1, result2 = roll_dice()  # Unpacks the two values
    print(f"Roll {roll}:")
    print(f"  Die 1: {result1}")
    print(f"  Die 2: {result2}")
    print(f"  Total: {result1 + result2}")
    print()
    