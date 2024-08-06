import random

def get_level():
    """
    Prompt the user for a level and validate the input.
    Returns a positive integer representing the level.
    """
    while True:
        level = input("Level: ")
        try:
            level = int(level)
            if level <= 0:
                raise ValueError
            return level
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def get_guess():
    """
    Prompt the user for a guess and validate the input.
    Returns a positive integer representing the guess.
    """
    while True:
        guess = input("Guess: ")
        try:
            guess = int(guess)
            if guess <= 0:
                raise ValueError
            return guess
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def main():
    # Get the level from the user
    level = get_level()

    # Generate a random number between 1 and the chosen level
    answer = random.randint(1, level)

    while True:
        # Get the guess from the user
        guess = get_guess()

        # Compare the guess with the answer and provide feedback
        if guess < answer:
            print("Too small!")
        elif guess > answer:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
