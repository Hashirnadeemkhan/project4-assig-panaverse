def main():
    numbers:list[int]=[1,2,3,4,5,5,6,8]
    sum=0
    for number in numbers:
        sum += int(number)
    print(int(sum))



if __name__ == '__main__':
    main()