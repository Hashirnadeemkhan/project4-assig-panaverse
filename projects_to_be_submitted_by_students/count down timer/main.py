import time

# Ask user for the countdown time in seconds
seconds = input("Enter time in seconds: ")

# Check if input is a number and positive
if seconds.isdigit() and int(seconds) > 0:
    seconds = int(seconds)
    print("Countdown started!")
    
    # Count down from the input time to 0
    while seconds > 0:
        print(f"{seconds} seconds left")
        time.sleep(1)  # Wait for 1 second
        seconds -= 1
    
    # When timer reaches 0
    print("Time's up!")
else:
    print("Please enter a positive number.")