def get_first_element(lst):
    print(lst[0])


# Provided code (no need to edit)
def main():
    my_list = []
    while True:
        element = input("Enter an element (or 'done' to finish): ")
        if element == 'done':
            break
        my_list.append(element)
    get_first_element(my_list)

if __name__ == '__main__':
    main()    