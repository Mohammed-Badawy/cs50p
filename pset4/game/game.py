from random import randint
from sys import exit


def main():
    # Prompt user for level
    level = get_positive_int("Level: ")

    # Generate random int
    rand = randint(1, level)

    while True:

        # Prompt user for new guess
        guess = get_positive_int("Guess: ")

        # Check guess
        if rand == guess:
            exit("Just right!")
        elif rand < guess:
            print("Too large!")
        else:
            print("Too small!")


# Get positive int
def get_positive_int(prompt):
    num = 0

    while True:
        try:
            num = int(input(prompt))

            if num > 0:
                return num
        
        except ValueError:
            pass
        
    
main()