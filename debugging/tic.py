#!/usr/bin/python3

def print_board(board):
    """
    Prints the current state of the Tic-Tac-Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there's a winner on the board.
    
    Returns:
        bool: True if there's a winner, False otherwise.
    """
    # Check rows for winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    """
    Checks if the board is full.
    
    Returns:
        bool: True if the board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to run the Tic-Tac-Toe game.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        # Get the row and column input
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        except ValueError:
            print("Please enter a valid integer between 0 and 2.")
            continue

        # Validate the move
        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Row and column must be 0, 1, or 2. Please try again.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Make the move
        board[row][col] = player

        # Check for a winner
        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break

        # Check for a tie
        if is_board_full(board):
            print_board(board)
            print("The game is a tie!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

tic_tac_toe()
