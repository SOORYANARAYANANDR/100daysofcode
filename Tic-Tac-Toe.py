# Define constants for the game
EMPTY = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'

# Define the Tic-Tac-Toe board
board = [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]

# Define the winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], '|', board[i + 1], '|', board[i + 2])

# Function to check if the board is full
def is_full(board):
    return all(cell != EMPTY for cell in board)

# Function to check if a player has won
def has_won(board, player):
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to evaluate the game state (utility function)
def evaluate(board):
    if has_won(board, PLAYER_X):
        return 1  # Player X wins
    elif has_won(board, PLAYER_O):
        return -1  # Player O wins
    elif is_full(board):
        return 0  # It's a draw
    else:
        return None  # Game is ongoing

# Min-Max function with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    result = evaluate(board)

    if result is not None:
        return result

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_X
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = EMPTY
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_O
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = EMPTY
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Function to make the computer's move using Min-Max with Alpha-Beta Pruning
def computer_move(board):
    best_move = -1
    best_eval = float('-inf')
    alpha = float('-inf')
    beta = float('inf')

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = PLAYER_X
            eval = minimax(board, 0, False, alpha, beta)
            board[i] = EMPTY
            if eval > best_eval:
                best_eval = eval
                best_move = i

    return best_move

# Main game loop
while True:
    print_board(board)
    move = int(input("Enter your move (1-9): ")) - 1

    if board[move] != EMPTY or move < 0 or move > 8:
        print("Invalid move. Try again.")
        continue

    board[move] = PLAYER_O

    if has_won(board, PLAYER_O):
        print_board(board)
        print("You win!")
        break

    if is_full(board):
        print_board(board)
        print("It's a draw!")
        break

    computer_move_index = computer_move(board)
    board[computer_move_index] = PLAYER_X

    if has_won(board, PLAYER_X):
        print_board(board)
        print("Computer wins!")
        break
