def is_multiple(guess, chosen_number):
    return "The guess is a multiple of the chosen number" if chosen_number % guess == 0 else "The guess is not a multiple of the chosen number"

def higher_or_lower(guess, chosen_number):
    # Returns either higher or lower, it cannot be equal if it has been passed to this function
    return "The guess is higher than the chosen number" if guess > chosen_number else "The guess is lower than the chosen number"

