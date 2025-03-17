def initialize_board():
    """Creates an empty 3x3 Tic Tac Toe board."""
    return [["-" for _ in range(3)] for _ in range(3)]

def print_board(board):
    """Prints the game board."""
    print("Current game board")
    for row in board:
        print(" | ".join(row))  # Fixed to use " | " as separators
    print()