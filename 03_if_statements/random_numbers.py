import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    """
    Prints 10 random numbers between 1 and 100 (inclusive) on a single line.
    """
    for i in range(N_NUMBERS):
        value = random.randint(MIN_VALUE, MAX_VALUE)
        # Print with a space after each number instead of a newline
        print(value, end=" ")
    # Add a final newline after all numbers are printed
    print()

if __name__ == '__main__':
    main()