from word_doc import words
import random
import string

random_word = random.choice(words)
input_string = ""
letters = set()
lives = 6
hints = {
    "bladee": "A popular music artist from Sweden, a drainer, one might say.",
    "coffee": "A popular drink that stimulates the mind, and is dark in color.",
    "orange": "A color, a fruit, and only Eminem can use it to rhyme.",
    "python": "A programming language that you may be familiar with.",
    "potato": "A yummy startch that grows in the ground.",
    "zombie": "A non-vampire undead creature that bites humans."
}

if random_word in hints:
    print(f"Here's a hint: {hints[random_word]}")

while lives > 0:
    print("The word has six letters!")
    input_string = input("Your guess: \n")


    if input_string not in random_word:
        lives -= 1

    if input_string in random_word:
        print(f"({input_string}) is a letter in the word.")
    else:
        print(f"({input_string}) is not a letter in the word. Lives left: {lives}")

else:
    print("Out of guesses. The word was:", random_word)
