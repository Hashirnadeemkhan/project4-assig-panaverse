def access_element(lst, index):
    # Check if index is valid
    if index < 0 or index >= len(lst):
        return "Index out of range"
    return lst[index]

def modify_element(lst, index, new_value):
    # Check if index is valid
    if index < 0 or index >= len(lst):
        return "Index out of range"
    # Capitalize the first letter of the new value
    lst[index] = new_value.capitalize()
    return lst

def slice_list(lst, start, end):
    # Check if indices are valid
    if start < 0 or end > len(lst) or start >= end:
        return "Invalid slice indices"
    return lst[start:end]

def main():
    # Initialize a list with 5+ elements
    my_list = ['Apple', 'Banana', 'Orange', 'Grape', 'Mango']
    
    while True:
        # Print current list
        print(f"\nCurrent list: {my_list}")
        # Prompt for operation
        operation = input("Choose an operation (access, modify, slice, exit): ").lower()
        
        if operation == "exit":
            print("Game over!")
            break
        
        elif operation == "access":
            # Get index
            try:
                index = int(input("Enter an index: "))
                # Call access function
                result = access_element(my_list, index)
                print(f"Result: {result}")
            except ValueError:
                print("Please enter a valid integer index")
        
        elif operation == "modify":
            # Get index and new value
            try:
                index = int(input("Enter an index: "))
                new_value = input("Enter a new value: ")
                # Call modify function
                result = modify_element(my_list, index, new_value)
                if result == "Index out of range":
                    print(result)
                else:
                    print(f"List updated: {result}")
            except ValueError:
                print("Please enter a valid integer index")
        
        elif operation == "slice":
            # Get start and end indices
            try:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                # Call slice function
                result = slice_list(my_list, start, end)
                print(f"Result: {result}")
            except ValueError:
                print("Please enter valid integer indices")
        
        else:
            print("Invalid operation! Choose access, modify, slice, or exit")

if __name__ == "__main__":
    main()
