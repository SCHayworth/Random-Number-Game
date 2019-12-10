# Random Number Guessing Game
# Shaun Hayworth
# CIS 2
# 12-10-2019
# Source code and revision history are available at
# https://github.com/SCHayworth/Random-Number-Game

# This program generates a random integer between 1 and 100, and asks the user
# to guess what it is, prompting the player for a higher or lower number if their
# guess is incorrect.

# Import the random module and generate a random integer between 1 and 100.
import random
target_number = random.randint(1, 100)


def main():
    '''This is the mainline program logic.'''
    # Initialize accumulator for the total guesses, and a loop condition.
    guess_number = 0
    correct_guess = false

    # Introduce the game and prompt the user for their first guess.
    print("I'm thinking of a number between 1 and 100.")
    guess = int(input('Can you guess what it is? Enter your guess: '))

    # Main gameplay loop.
    while correct_guess == false:
        # Increment the guess_number accumulator and check for a correct guess.
        # If the guess is wrong, prompt user for a new number.
        guess_number +=1
        if guess == target_number:
            if guess_number == 1:
                print(f"Yes, my number is {target_number}! You got it on the first try!")
                correct_guess = true
            else:
                print(f"Boom!! You got it in {guess_number} guesses! My number was {target_number}.")
                correct_guess = true
        elif guess < target_number:
            guess = int(input(f"{guess} is too low. Try a larger number: "))
        else:
            guess = int(input(f"{guess} is too hihgh. Try a smaller number: "))
