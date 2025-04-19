import random
from typing import Optional, Tuple

def get_number_range() -> Tuple[int, int]:
    """Get the number range from the user with validation.
    
    Returns:
        A tuple of (min_num, max_num).
    """
    while True:
        try:
            min_num = int(input("Enter the minimum number: "))
            max_num = int(input("Enter the maximum number: "))
            if min_num >= max_num:
                print("Minimum number must be less than maximum number.")
                continue
            return min_num, max_num
        except ValueError:
            print("Please enter valid numbers.")
        except KeyboardInterrupt:
            print("\nInput cancelled by user.")
            return 1, 100  # Default range if cancelled

def computer_guess_number(min_num: int, max_num: int) -> None:
    """Play a round where the computer guesses the user's number.
    
    Args:
        min_num: The minimum number in the range.
        max_num: The maximum number in the range.
    """
    print(f"\nThink of a number between {min_num} and {max_num}.")
    print("For each guess, enter:")
    print("  'h' if my guess is too high")
    print("  'l' if my guess is too low")
    print("  'c' if my guess is correct")
    input("Press Enter when you're ready...")

    low = min_num
    high = max_num
    attempts = 0

    while True:
        # Computer guesses the middle of the current range
        guess = (low + high) // 2
        attempts += 1
        
        print(f"\nMy guess is {guess}.")
        feedback = input("Is this (h)igh, (l)ow, or (c)orrect? ").strip().lower()

        try:
            if feedback not in ['h', 'l', 'c']:
                print("Invalid input. Please enter 'h', 'l', or 'c'.")
                attempts -= 1  # Don't count invalid input as an attempt
                continue

            if feedback == 'c':
                print(f"\nI got it! Your number is {guess}!")
                print(f"It took me {attempts} attempts.")
                break
            elif feedback == 'h':
                high = guess - 1  # Adjust upper bound
            elif feedback == 'l':
                low = guess + 1  # Adjust lower bound

            # Check if the range is still valid
            if low > high:
                print("It seems like there might be an inconsistency in your feedback.")
                print("Let's start over.")
                return

        except KeyboardInterrupt:
            print("\nGame cancelled by user.")
            return

def main() -> None:
    """Main function to run the Computer Guess the Number game with a menu."""
    print("Welcome to Computer Guess the Number!")
    print("You think of a number, and I'll try to guess it.")

    while True:
        print("\n=== Menu ===")
        print("1. Play Game (1-100)")
        print("2. Play Game (Custom Range)")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        try:
            if choice == "1":
                computer_guess_number(1, 100)  # Default range
            elif choice == "2":
                min_num, max_num = get_number_range()
                computer_guess_number(min_num, max_num)
            elif choice == "3":
                print("Thanks for playing! Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()