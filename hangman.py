# Hangman script without modularization


# Have the player enter his/her name
name = input("Please enter your name: ")

print("Hello", name, ", let's play hangman!")
print("")

# Establish the secret word
secret_word = "secret"

# Establish how many turns the player has to win the game
TURNS_LEFT = 6

# Create a list version of the secret word with the letters we have already guessed
secret_word_list = []
for letter in secret_word:
    secret_word_list.append("_")

# Print the guessed version of the secret word
secret_word_revealed = ""
for letter in secret_word_list:
    secret_word_revealed += letter
print("Secret word: ", secret_word_revealed)

# Variable to indicate that the player has won or lost
game_done = False
guesses = ''

# Main loop of the game: run until player has won or lost
while game_done == False:

    # Print game information for the player
    print("Guesses remaining:", TURNS_LEFT)
    print("Letters already guessed: ", guesses)

    letter_found = False

    # Get the guessed letter from the player
    guess = input("Guess a letter: ")

    # Tell the player what they have already guessed
    if guess not in guesses:
        guesses += guess

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
        TURNS_LEFT -= 1

    # Print a version of the word that has been revealed by the player's guesses
    secret_word_revealed = ""
    for letter in secret_word_list:
        secret_word_revealed += letter
    print("Secret word: ", secret_word_revealed)

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