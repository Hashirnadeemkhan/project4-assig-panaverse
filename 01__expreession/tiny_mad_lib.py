
SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

# Prompt user for inputs
adjective = input("Please type an adjective and press enter. ")
noun = input("Please type a noun and press enter. ")
verb = input("Please type a verb and press enter. ")

# Create and print the full sentence
def main():
    full_sentence = f"{SENTENCE_START} {adjective} {noun} {verb}!"
    print(full_sentence)




if __name__ == '__main__':
    main()