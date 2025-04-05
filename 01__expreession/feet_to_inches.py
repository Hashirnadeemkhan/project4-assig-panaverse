INCHES_IN_FOOT= 12
def main():
 feet:float = float(input("Enter the feet value to convert into inches: "))

 inches = feet *INCHES_IN_FOOT
 print(f"{inches} inches")
if __name__ == '__main__':
    main()