def askplayertomove():
    """Prompts the current player to enter their move (row and column)."""
    row = int(input("Enter the row number (0 to 2): "))
    col = int(input("Enter the column number (0 to 2): "))
    return row, col

def is_valid_move(board, row, col):
    """Returns True if the move is valid (within the board and on an empty spot)."""
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '-'

def update_game_board(board, row, col, player_mark):
    """Places the player's mark on the board."""
    board[row][col] = player_mark