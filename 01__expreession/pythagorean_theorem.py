import math
def main():
    ab:float = float(input("Enter the length of AB: "))
    ac:float = float(input("Enter the length of AC: "))
    bc:float = math.sqrt(ac**2 + ab**2)
    print(f"The hypotenous is {bc**2}")

main()