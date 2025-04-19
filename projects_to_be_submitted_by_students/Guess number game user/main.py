import random
from typing import Optional

def guess_the_number(min_num: int = 1, max_num: int = 100) -> None:
    """Play a single round of Guess the Number game.
    
    Args:
        min_num: The minimum number in the range (default: 1)
        max_num: The maximum number in the range (default: 100)
    """
    # Generate a random number
    secret_number = random.randint(min_num, max_num)
    attempts = 0
    
    print(f"\nI'm thinking of a number between {min_num} and {max_num}!")
    
    while True:
        # Get user guess with error handling
        try:
            guess = input("Enter your guess: ").strip()
            if not guess:
                print("Please enter a number.")
                continue
            guess_num = int(guess)  # Convert to integer
            attempts += 1
            
            # Check if guess is within range
            if guess_num < min_num or guess_num > max_num:
                print(f"Please guess a number between {min_num} and {max_num}.")
                continue
            
            # Check if guess is correct
            if guess_num == secret_number:
                print(f"\nCongratulations! You guessed the number {secret_number} in {attempts} attempts!")
                break
            elif guess_num < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nGame cancelled by user.")
            return

def main() -> None:
    """Main function to run the Guess the Number game with a menu."""
    print("Welcome to Guess the Number!")
    
    while True:
        print("\n=== Menu ===")
        print("1. Play Game (1-100)")
        print("2. Play Game (Custom Range)")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        try:
            if choice == "1":
                guess_the_number()  # Play with default range (1-100)
            elif choice == "2":
                # Get custom range from user
                while True:
                    try:
                        min_num = int(input("Enter the minimum number: "))
                        max_num = int(input("Enter the maximum number: "))
                        if min_num >= max_num:
                            print("Minimum number must be less than maximum number.")
                            continue
                        guess_the_number(min_num, max_num)
                        break
                    except ValueError:
                        print("Please enter valid numbers.")
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