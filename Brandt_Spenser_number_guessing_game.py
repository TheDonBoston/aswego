# Program to guess a random number between 0 - 100
import random

# Creating the function for the number counting game
# No arguments in the parenthesis
def guessing_game(): 

# Pick the lucky number
# The programmer doesn't know this number, only the program
    lucky_num = random.randint(0, 100)
    """The program picks the number using random.randint."""
    
    while True:
        guess = input("Guess a number between 0 and 100: ")

# Guess input will be an integer
        guess = int(guess)

# This informs the user they they did not input within the given parameters       
        if guess < 0 or guess > 100:
            print("Not in the given range. Enter a number BETWEEN 0 - 100.")
            continue

        if guess < lucky_num:
            print("Too low.")
        elif guess > lucky_num:
            print("Too high.")
        else:
            """If the number guessed isn't <, or > than lucky_num
            then the program tells you the guess is correct and ends."""
            print("Just right!")
            break

# This calls the guessing game function defined in line 6       
def main():
    guessing_game()

if __name__ == "__main__":
    main()       