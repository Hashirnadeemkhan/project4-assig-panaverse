import random  # Required for random.random()

DONE_LIKELIHOOD = 0.2  # Define the probability constant (20% chance)

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return
        print(curr_num, end=" ")  # Print with space instead of newline

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.", end=" ")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()