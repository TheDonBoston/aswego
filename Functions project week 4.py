"""Random word guessing game using functions"""
import random

# Function for choosing a random word from 
def choose_random_word(words):
    return random.choice(words)

# Give the user a hint of what the word is they will be guessing
def show_hint(random_word, hints):
    if random_word in hints:
        print(f"Here's a hint: {hints[random_word]}")

# Function that asks the user to guess one letter
def get_guess():
    return input("Your guess: ")

# Shows the user their guesses
def show_guesses(letters_guessed, input_string):
    letters_guessed.add(input_string)

# Function for the game itself
def start_game(words, hints, max_lives):
    random_word = choose_random_word(words)
    letters_guessed = set()
    lives = max_lives
    show_hint(random_word, hints)

    while lives > 0:
        print("The secret word has 6 letters! Guess one letter at a time.")
        secret_word ="".join(char if char in letters_guessed else "_" for char in random_word) 
        print("Secret word: ", secret_word)
        input_string = get_guess()
        
        if input_string not in random_word:
            lives -= 1
            print(f"({input}) is not a letter in the word. Lives left: {lives}")
        """Tells the user they have n amount of lives left."""

        if lives == 0:
            print("You've run out of guesses. The word was: ")

        if secret_word == random_word:
            print("You win!!")
            break

    else:
        show_guesses(letters_guessed, input)
        print(f"{input} is a letter in the word.")

 # Set variables for the game
def main():
    words = ["bladee", "coffee", "orange", "python", "potato", "zombie"]
    hints = {
        "bladee": "A popular music artist from Sweden, a drainer, one might say.",
        "coffee": "A popular drink thatr stimulates the mind, and is dark in color.",
        "orange": "A color, a fruit, and only Eminem can use it to rhyme.",
        "python": "A programming language that you may be familiar with.",
        "potato": "A yummy starch that grows in the ground.",
        "zombie": "A non-vampire undead creature that bites humans."
    }       
    max_lives = 6

    start_game(words, hints, max_lives)

if __name__ == "__main__":
    main()   



        

    









