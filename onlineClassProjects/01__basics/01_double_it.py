def main():
    try:
        curr_value = float(input("Enter a number: "))  # Valid number input
        while curr_value < 100:
            curr_value = curr_value * 2
            print(int(curr_value) if curr_value.is_integer() else curr_value, end=" ")
    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main()