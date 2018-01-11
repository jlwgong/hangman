# Hangman script with modularization

# Import the random library
import random

def get_secret_word():
    # function that chooses a random secret word from a list

    words = ["light", "electric", "shock", "wire", "round", "circuit", "voltage", "white", "pieces",
             "yellow", "science", "engineering", "warm", "camera", "christmas", "crystal", "idea",
             "magical", "table", "lamp", "shadow", "computer", "fun", "school", "television"]
    random_word = words[random.randint(0, len(words))]
    print("The secret word is", len(random_word), "letters long")
    return random_word


def word_to_list(secret_word):
    # Function converts a word to a list of its letters

    secret_word_list = []
    for letter in secret_word:
        secret_word_list.append("_")
    return secret_word_list


def is_game_done(secret_word, secret_word_revealed, TURNS_LEFT, name):
    # Function checks if the game is finished or not

    game_done = False

    # Player has won the game!
    if secret_word_revealed == secret_word:
        print("")
        print(name, "wins!")
        game_done = True

    # Player has lost the game :(
    if TURNS_LEFT == 0:
        print(name, "lost!")
        print("The secret word was:", secret_word)
        game_done = True
    print("")
    return game_done


def player_turn(secret_word, guess, previous_guesses, turns_left, secret_word_list):
    # Main function to loop over
    letter_found = False
    repeat_guess = False

    # Tell the player what they have already guessed
    if guess not in previous_guesses:
        previous_guesses += guess
    else:
        print("You've already guessed this letter!")
        repeat_guess = True

    # Check if letter guessed is in the secret word
    for i in range(0, len(secret_word)):
        if guess == secret_word[i]:
            secret_word_list[i] = guess
            letter_found = True

    # Letter is in the secret word
    if letter_found == True:
        print("Your guessed letter was in the secret word!")

    # Letter is not in the secret word, deduct a turn
    else:
        print("Your guessed letter was not in the secret word!")
        if repeat_guess == False:
            turns_left -= 1

    # Print a version of the word that has been revealed by the player's guesses
    secret_word_revealed = ""
    for letter in secret_word_list:
        secret_word_revealed += letter
    print("Secret word: ", secret_word_revealed)

    return previous_guesses, turns_left, secret_word_revealed


# Game function, call to play the game!
def hangman():

    # Have the player enter his/her name
    name = input("Please enter your name: ")

    print("Hello", name, ", let's play hangman!")
    print("")

    # Establish the secret word
    secret_word = get_secret_word()

    # Establish how many turns the player has to win the game
    TURNS_LEFT = 6

    # Create list version of secret word
    secret_word_list = word_to_list(secret_word)

    # Variable to indicate that the player has won or lost
    game_done = False
    guesses = ''

    while game_done == False:

        # Print game information for the player
        print("Guesses remaining:", TURNS_LEFT)
        print("Letters already guessed: ", guesses)
        letter_found = False

        # Get the guessed letter from the player
        guess = input("Guess a letter: ")

        # main function
        guesses, TURNS_LEFT, secret_word_revealed = player_turn(secret_word, guess, guesses, TURNS_LEFT, secret_word_list)
        game_done = is_game_done(secret_word, secret_word_revealed, TURNS_LEFT, name)




hangman()