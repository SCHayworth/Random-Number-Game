# Random-Number-Game
 User tries to guess a randomly generated integer between 1 - 100.

## Scope
 Write a program that generates a random number between 1 and 100 and asks the user to guess what the number is. If the user's guess is higher than the random number, the program should display, "Too high. Try again." If the user's guess is lower than the random number, the program should display, "Too low. Try again." The program should use a loop that repeats until the user correctly guesses the random number. Then, the program should display, "Congratulations! You figured out the number!"

 You will need the following module import and sample statement:

    import random
    x = random.randint(1, 100)

### Sample Run
    I am thinking of a number between 1 and 100.
    Can you guess what it is? Enter your guess. 50

    50 is too high. Try a smaller number:  25
    25 is too high. Try a smaller number:  12
    12 is too low. Try a larger number:  19
    19 is too high. Try a smaller number:  15
    15 is too high. Try a smaller number:  13

    Boom!! You got it! My number was 13.

## Pseudocode
### Main Program Logic
    START
      IMPORT random module
      SET target number to a random integer between 1 - 100
      SET guess accumulator to 0
      SET game over flag to false
      PRINT "I am thinking of a number between 1 and 100."
      PRINT "Can you guess what it is? Enter your guess:"
      INPUT guess
      WHILE game over flag is false
        INCREMENT guess accumulator by 1
        IF guess is equal to target Number
          IF guess accumulator is equal to 1
            PRINT "Yes, my number is {target number}! You got it on the first try!!"
            SET game over flag to true
          ELSE
            PRINT "Boom!! You got it in {guess accumulator} guesses! My number was {target number}."
            SET game over flag to true
        ELSE IF guess is less than target number
          PRINT "{guess} is too low. Try a larger number: "
          INPUT guess
        ELSE
          PRINT "{guess} is too high. Try a smaller number: "
          INPUT guess
        ENDIF      
    END
