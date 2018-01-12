# This file is going to help us code the Hangman game in Python!
# Website:  github.com/jlwgong/hangman
# Email:    jlwgong@mit.edu


# Set up initial variables
#   - Player name
#   - Secret word
#   - number of turns left
#   - game finished?



# Create a list version of the secret word
#   Hint: use a for loop and a list


# Record which letters have already been guessed
guesses = ""


# Create main loop of the game
#   Hint:   use a while loop
#   Hint:   use the "is the game finished" variable
while game_done == False:

    # Print game information for the player
    # number of turns left, which letters the player has already guessed


    # Get a letter from the player


    # Has the letter already been guessed?


    # Is the letter in the secret word?
    # If the letter is in the secret word, set letter_found to True


    # If the letter is in the secret word
    if letter_found == True:
        # Tell the player their guess was correct!


    # If the letter was NOT in the secret word
    else:
        # Tell the player their guess was not correct!
        # Deduct a turn from the player



    # Print a version of the word that the player has already guessed
    #   Hint: use the list version of the word we created!



    # Check if player has won the game (secret word has been guessed)



    # Check if player has lost the game (no more turns left)




# ALL DONE!!!
# try playing the game!
