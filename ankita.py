#HANGMAN_GAME
# library that we use in order to choose on random words from a list of words
import random

# Here I have asked the user to enter the name first
name = input("Enter your name: ")
print("All the best !", name,"Play well and guess the word correctly")

words = [
    "house"
    "rendezvous"
    "parliament"
    "senate"
    "website",
    "hangman",
    "rainbow",
    "computer",
    "science",
    "programming",
    "python",
    "mathematics",
    "player",
    "apple",
    "reverse",
    "water",
    "blood",
    "coder",
]

# This Function will choose one random word from this list of words
word = random.choice(words)

print("\nGuess the characters")
guesses = ""

# any number of turns can be used here I am using 12
turns = 12

while turns > 0:
    # counts the number of times a user fails
    failed = 0

    # all characters from the input
    # word taking one at a time.
    for char in word:
        if char in guesses:
            print(char, "\t",end="")
        else:
            print("_\t", end="")
            # for every failure 1 will be
            # incremented in failure
            failed += 1

    if failed == 0:
        # user will win the game if failure is 0
        # and 'You Win :D' will be given as output
        print("\nYay!!", name,"You Win :D")

        # this print the correct word
        print("\nThe word is: ", word)
        break

    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    guess = input("\n\nguess the character: ").lower()

    # every input character will be stored in guesses
    guesses += guess

    # check input with the character in word
    if guess not in word:
        turns -= 1

        # if the character doesn’t match the word
        # then “Wrong” will be given as output
        print("\nWrong")

        # this will print the number of
        # turns left for the user
        print("\nYou have", +turns, "more guesses")

        if turns == 0:
            print("\n\nYou lose,", name, "the game is Over :(\n the word is", word)
