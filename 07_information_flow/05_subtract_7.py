def main():
    num:int= 7
    num = subtract_seven(num)
    print("this should be a number depend to the users input: ", num)

def subtract_seven(num):
    num = num - int(input("enter the number to subtact from 7: "))
    return num


if __name__ == '__main__':
    main()


