from random import randint, choice
from inspect import getmembers, isfunction
import hints

# Class which returns a random hint from hints.py
class HintReturner:
    def __init__(self):
        self.hints = [ func[1] for func in getmembers(hints, isfunction) ]

    def get_hint(self, guess, chosen_number):
        return choice(self.hints)(guess, chosen_number)

# Function which loops until user enters a valid number
def choose_lower_bound():
    bound = None
    while bound == None or bound < 1:
        try:
            bound = int(input("Please input the lower bound for choosing a number:\n"))
        except ValueError:
            print("Please enter a valid number\n")
        else:
            if bound < 1:
                print("Must be a positive integer\n")
    return bound

# Function which loops until user enters a valid number
# Valid number must be larger than lower bound
def choose_upper_bound(lower_bound):
    upper_bound = None
    while upper_bound == None or upper_bound < 1 or upper_bound <= lower_bound:
        try:
            upper_bound = int(input("Please input the upper bound for choosing a number:\n"))
        except ValueError:
            print("Please enter a valid number\n")
        else: 
            if upper_bound < 1:
                print("Must be a positive integer\n")
            elif upper_bound <= lower_bound:
                print(f"Must be larger than the lower bound ({lower_bound})\n")
    return upper_bound

if __name__ == "__main__":

    print("Welcome to the guessing game!")
    name = input("Please input your name:\n")
    print(f"Hello {name}\n")

    lower_bound = choose_lower_bound()
    upper_bound = choose_upper_bound(lower_bound)

    chosen_number = randint(lower_bound, upper_bound)
    print("I have chosen a number within the range you specified :)\n")

    hint_gen = HintReturner()

    num_of_guesses = 0

    while True:
        print(f"Number of guesses: {num_of_guesses}")
        
        guess = int(input(f"Please guess the number ({lower_bound}-{upper_bound}):\n"))
        
        if guess == chosen_number:
            break
        
        print(hint_gen.get_hint(guess, chosen_number), end="\n\n")
        
        num_of_guesses += 1

    print(f"Congratulations!! You guessed it!!\nThe number I chose was {chosen_number}!")
    