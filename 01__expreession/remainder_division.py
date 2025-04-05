def main():
    num1:int = int(input("Enter the first value: "))
    num2:int = int(input("Enter the second value: "))
    quotient = (num1 /num2)
    remainder = num1%num2
    print(f"the quotient is {quotient}")
    print(f"the remainder is {remainder}")



if __name__ == '__main__':
    main()