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
    correct_guess = False

    # Introduce the game and prompt the user for their first guess as long as
    # the guess_number accumulator is 0.
    while guess_number < 1:
        try:
            print("I'm thinking of a number between 1 and 100.")
            guess = int(input('Can you guess what it is? Enter your guess: '))

            # Main gameplay loop.
            while correct_guess == False:
                try:
                    # Increment the guess_number accumulator and check for a correct guess.
                    # If the guess is wrong, prompt user for a new number.
                    guess_number +=1
                    if guess == target_number:
                        if guess_number == 1:
                            print(f"\nYes, my number is {target_number}! You got it on the first try!")
                            correct_guess = True
                        else:
                            print(f"\nBoom!! You got it in {guess_number} guesses! My number was {target_number}.")
                            correct_guess = True
                    elif guess < target_number and guess >= 1:
                        guess = int(input(f"{guess} is too low. Try a larger number: "))
                    elif guess > target_number and guess <= 100:
                        guess = int(input(f"{guess} is too high. Try a smaller number: "))
                    else:
                        # If the selected number is out of range, ask for a valid
                        # guess and decrement the guess_number in order to not count it.
                        guess = int(input('Please choose a number between 1 and 100: '))
                        guess_number -= 1
                except ValueError:
                    # If a the input is not an integer, prompt the user to try again and continue the game.
                    print('You must enter an integer between 1 and 100. Try again.\n')
                    continue
        except ValueError:
            # If the first guess is not an integer, prompt the user for an appropriate value.
            print('You must enter an integer between 1 and 100.\n')
            continue


# Call the main() function to execute program.
main()
