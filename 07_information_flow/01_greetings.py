def main():
    name: str = input("Enter your name: ")
    print(greet(name))
def greet(name):
    return f"Greeting {name}"


if __name__ == '__main__':
    main()