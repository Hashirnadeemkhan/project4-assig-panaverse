def print_ones_digit(num):
    print("The ones digit is", num % 10)

def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()