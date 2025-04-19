import random

# List of simple words
words = ['cat', 'dog', 'bird', 'fish', 'lion']

# Pick a random word and make it uppercase
word = random.choice(words).upper()
guessed_letters = set()  # Track guessed letters
lives = 6  # Start with 6 lives

print("Welcome to Hangman! Guess the word by picking letters.")
print(f"You have {lives} lives.")

# Keep playing until you win or lose
while lives > 0:
    # Show the word with underscores for unguessed letters
    word_display = ' '.join(letter if letter in guessed_letters else '_' for letter in word)
    print(f"\nWord: {word_display}")
    print(f"Lives left: {lives}")
    
    # Get a letter from the user
    guess = input("Guess a letter: ").upper()
    
    # Check if input is a single letter
    if len(guess) == 1 and guess.isalpha():
        if guess in guessed_letters:
            print("You already guessed that letter!")
        else:
            guessed_letters.add(guess)
            if guess in word:
                print("Good guess!")
                # Check if all letters are guessed
                if all(letter in guessed_letters for letter in word):
                    print(f"\nYou win! The word was: {word}")
                    break
            else:
                lives -= 1
                print("Wrong guess!")
    else:
        print("Please enter one letter (A-Z).")
    
    # Check if out of lives
    if lives == 0:
        print(f"\nGame over! The word was: {word}")

print("Thanks for playing!")