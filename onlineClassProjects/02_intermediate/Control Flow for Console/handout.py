import random

def main():
    rounds = int(input("Kitne rounds khelna chahte ho? "))  # User se rounds ki sankhya
    player_score = 0  # Player ke points track karne ke liye

    for round_num in range(1, rounds+1 ):  #+1 islye kia ek agr 3 rounds khelna chahtay tu 3 hi hon ,agr nh laagayeingay tu 2 hongay,becuase last exclude hota ha range mae
        print(f"\nRound {round_num}:")
        
        # Random numbers generate karo
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        # Player ko uska number dikhao
        print(f"Tumhara number hai: {player_number}")
        
        # Player se guess lo
        guess = input("Kya tumhara number computer ke number se higher hai ya lower? (higher/lower): ").strip().lower()
        
        # Validate guess
        if guess not in ["higher", "lower"]:
            print("Galat input! Sirf 'higher' ya 'lower' likho. Is round mein point nahi mila.")
            continue
        
        # Check kya guess sahi hai
        if (guess == "higher" and player_number > computer_number) or  (guess == "lower" and player_number < computer_number):
            player_score += 1
            print(f"Sahi guess! Computer ka number tha {computer_number}. Tumhein 1 point mila!")
        else:
            print(f"Galat guess. Computer ka number tha {computer_number}. Koi point nahi.")
        
        # Round ka status dikhao
        print(f"Ab tak tumhara score: {player_score}")

    # Game khatam hone ke baad final score
    print(f"\nGame khatam! Tumhara final score hai: {player_score}/{rounds}")

if __name__ == "__main__":
    main()