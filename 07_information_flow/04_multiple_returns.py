def get_user_data():
    first_name= input("Enter first name: ")
    last_name= input("Enter last name: ")
    email = input("Enter email address: ")
    return first_name,last_name,email

def main():
    print(get_user_data())


if __name__ == "__main__":
     main()    