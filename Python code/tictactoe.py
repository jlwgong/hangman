# Tic Tac Toe, 2 Player
# NIS Karaganda
# January 2018
# Justin Gong, jlwgong@mit.edu



# -----------------------------------------------------
# -----------------  HELPER FUNCTIONS  ----------------
# -----------------------------------------------------

def get_board(moves):
    line1 = [moves["A1"], "|", moves["A2"], "|", moves["A3"]]
    line2 = ["-", "-", "-", "-", "-"]
    line3 = [moves["B1"], "|", moves["B2"], "|", moves["B3"]]
    line4 = ["-", "-", "-", "-", "-"]
    line5 = [moves["C1"], "|", moves["C2"], "|", moves["C3"]]
    board = [line1, line2, line3, line4, line5]
    return board

def print_board(moves):
    board = get_board(moves)
    for line in board:
        print_line = ""
        for i in line:
            print_line += i
        print(print_line)
    return None

def get_player_move(moves, letter):

    valid_moves = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    
    # Player 1 Move
    invalid_move = True
    while invalid_move:
        message = "Enter " + letter + " Move: "
        player_move = raw_input(message)
        
        #check if a valid move
        if player_move in valid_moves:
            
            # check if spot has already been played
            if moves[player_move] != " ":
                print("Invalid move, try again!")
            else:
                invalid_move = False
                moves[player_move] = letter
                print_board(moves)
        else:
            print("Invalid move, try again!")

def check_win(moves):
    win = False
    board = get_board(moves)

    # to check:
    #   across  x3
    #   down    x3
    #   diag    x2
    
    for i in range(0,5,2):
        across = []
        for j in range(0,5,2):
            across.append(board[i][j])
        
        # check for horizontal win
        if (across[0] == across[1]) and (across[1] == across[2]) and (across[2] != ' '):
            win = True
            print("Horizontal win detected!")
            print(across[0], "wins!")
            return win

        # check for vertical win
        if (board[0][i] == board[2][i]) and (board[2][i] == board[4][i]) and (board[2][i] != ' '):
            win = True
            print("Vertical win detected!")
            print(board[0][i], "wins!")
            return win

    #check for diagonal win
    if (board[0][0] == board[2][2]) and (board[2][2] == board[4][4]) and (board[2][2] != ' '):
        win = True
        print("Diagonal win detected!")
        print(board[2][2], "wins!")
        return win
    elif (board[4][0] == board[2][2]) and (board[2][2] == board[0][4]) and (board[2][2] != ' '):
        win = True
        print("Diagonal win detected!")
        print(board[2][2], "wins!")
        return win

    return win



# --------------------------------------------------------
# ------------------   MAIN GAMEPLAY   -------------------
# --------------------------------------------------------


# Initialize Board, print moves for user
print(" ")
line1 = ["A1", "|", "A2", "|", "A3"]
line2 = ["-", "-", "-", "-", "-"]
line3 = ["B1", "|", "B2", "|", "B3"]
line4 = ["-", "-", "-", "-", "-"]
line5 = ["AC", "|", "C2", "|", "C3"]
board = [line1, line2, line3, line4, line5]
for line in board:
    print_line = ""
    for i in line:
        print_line += i
    print(print_line)
print(" ")


# Initialize Game

positions = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
moves = {}
for i in range(0,9):
    moves[positions[i]] = " "

print_board(moves)

game_done = False


# Start Game

letter_count = 0
while game_done != True:

    if letter_count % 2 == 0:
        get_player_move(moves, "X")
    else:
        get_player_move(moves, "O")

    game_done = check_win(moves)
    
    null_count = 0
    for i in moves.values():
        if i == " ":
            null_count += 1
    if null_count == 0:
        game_done = True

    letter_count += 1

