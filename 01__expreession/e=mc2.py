def main():
    C= 299792458
    mass:float = float(input("Enter the mass value in kilograms: "))
    e = mass * (C**2)
    print(f"m={mass}kg ")
    print(f"C={C} m/s")
    print(f"The equilent energy using einistein formula is: {e} joules of energy!")


if __name__ == '__main__':
    main()


