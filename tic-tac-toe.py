import random

# Initialize the board with empty cells
board = [" " for i in range(9)]

# Function to draw the board
def draw_board():
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("-------------")

# Function to check if the board is full
def is_board_full():
    if " " in board:
        return False
    else:
        return True

# Function to check for a win
def check_for_win(player):
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    elif board[3] == player and board[4] == player and board[5] == player:
        return True
    elif board[6] == player and board[7] == player and board[8] == player:
        return True
    elif board[0] == player and board[3] == player and board[6] == player:
        return True
    elif board[1] == player and board[4] == player and board[7] == player:
        return True
    elif board[2] == player and board[5] == player and board[8] == player:
        return True
    elif board[0] == player and board[4] == player and board[8] == player:
        return True
    elif board[2] == player and board[4] == player and board[6] == player:
        return True
    else:
        return False

# Function for the computer's move
def computer_move():
    possible_moves = [i for i in range(9) if board[i] == " "]
    move = 0
    
    for player in ["O", "X"]:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = player
            if check_for_win(player):
                move = i
                return move
    
    corners = []
    for i in possible_moves:
        if i in [0, 2, 6, 8]:
            corners.append(i)
    if len(corners) > 0:
        move = random.choice(corners)
        return move
    
    if 4 in possible_moves:
        move = 4
        return move
    
    edges = []
    for i in possible_moves:
        if i in [1, 3, 5, 7]:
            edges.append(i)
    if len(edges) > 0:
        move = random.choice(edges)
    
    return move

# Main game loop
while True:
    draw_board()
    if is_board_full():
        print("Tie game!")
        break
    
    # Player's move
    player_move = int(input("Enter your move (0-8): "))
    if board[player_move] != " ":
        print("That space is already taken. Try again.")
        continue
    
    board[player_move] = "X"
    
    if check_for_win("X"):
        draw_board()
        print("You win!")
        break
    
    # Computer's move
