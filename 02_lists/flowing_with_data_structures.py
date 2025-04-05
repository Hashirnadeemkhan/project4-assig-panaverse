def add_three_copies(some_lists ,data):
    for i in range(3):
        some_lists.append(data)


def main():
    my_lists=[]
    message = input("Enter a message to copy: ")
    print(f"list before: ",my_lists)

    add_three_copies(my_lists,message)
    print(f"list after: ",my_lists)

if __name__ == '__main__':
    main()
