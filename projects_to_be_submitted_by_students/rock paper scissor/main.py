import random
from typing import Optional, Tuple

def get_computer_choice() -> str:
    """Generate a random choice for the computer.
    
    Returns:
        A string: 'rock', 'paper', or 'scissors'.
    """
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice() -> Optional[str]:
    """Get the user's choice with validation.
    
    Returns:
        The user's choice ('rock', 'paper', 'scissors') or None if cancelled.
    """
    while True:
        try:
            choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
            if choice in ['rock', 'paper', 'scissors']:
                return choice
            elif choice == '':
                print("Input cannot be empty.")
            else:
                print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        except KeyboardInterrupt:
            print("\nInput cancelled by user.")
            return None

def determine_winner(user_choice: str, computer_choice: str) -> Tuple[Optional[str], int, int]:
    """Determine the winner of a round and update scores.
    
    Args:
        user_choice: The user's choice.
        computer_choice: The computer's choice.
    Returns:
        A tuple of (result message, user_score_change, computer_score_change).
    """
    if user_choice == computer_choice:
        return f"It's a tie! Both chose {user_choice}.", 0, 0
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return f"You win! {user_choice.capitalize()} beats {computer_choice}.", 1, 0
    else:
        return f"Computer wins! {computer_choice.capitalize()} beats {user_choice}.", 0, 1

def play_round(user_score: int, computer_score: int) -> Tuple[int, int]:
    """Play a single round of Rock Paper Scissors.
    
    Args:
        user_score: Current user score.
        computer_score: Current computer score.
    Returns:
        Updated (user_score, computer_score).
    """
    user_choice = get_user_choice()
    if user_choice is None:  # User cancelled
        return user_score, computer_score
    
    computer_choice = get_computer_choice()
    print(f"\nComputer chose: {computer_choice}")
    
    result, user_score_change, computer_score_change = determine_winner(user_choice, computer_choice)
    print(result)
    
    return user_score + user_score_change, computer_score + computer_score_change

def main() -> None:
    """Main function to run the Rock Paper Scissors game with a menu."""
    user_score = 0
    computer_score = 0
    print("Welcome to Rock Paper Scissors!")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")

    while True:
        print("\n=== Menu ===")
        print(f"Score: You {user_score} - Computer {computer_score}")
        print("1. Play a round")
        print("2. View current score")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        try:
            if choice == "1":
                user_score, computer_score = play_round(user_score, computer_score)
            elif choice == "2":
                print(f"\nCurrent Score: You {user_score} - Computer {computer_score}")
            elif choice == "3":
                print(f"\nFinal Score: You {user_score} - Computer {computer_score}")
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