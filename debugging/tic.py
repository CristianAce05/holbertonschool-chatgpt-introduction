#!/usr/bin/python3

def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * (len(row) * 4 - 1))


def check_winner(board):
    """Checks if there is a winner on the board."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def is_board_full(board):
    """Checks if the board is full (tie)."""
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    """Main game loop for Tic-Tac-Toe."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Input loop with validation
        while True:
            try:
                row = int(input(f"Enter row (0, 1, 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, 2) for player {player}: "))
                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print("Coordinates out of bounds! Try again.")
                    continue
                if board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter integers 0, 1, or 2.")

        # Place the player's mark
        board[row][col] = player

        # Check for winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check for tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
