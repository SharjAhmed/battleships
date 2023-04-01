"""
Import random to generate random integers in game
"""
from random import randint

# Game Legend
# ▢ - blank space
# ⨀ - missed shot
# ⊗ - hit ship

HIDDEN_BOARD = [["▢"] * 8 for x in range(8)]
GUESS_BOARD = [["▢"] * 8 for x in range(8)]
letters_to_numbers = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
}

board = []


def print_board(board):
    """
    Create board for player to guess where to hit
    """
    print("    A   B   C   D   E   F   G   H")
    row_number = 1
    for row in board:
        print("%d | %s | " % (row_number, " | ".join(row)))
        row_number += 1


print_board(GUESS_BOARD)
print_board(HIDDEN_BOARD)


def create_ships(board):
    """
    Place ships randomly within board
    """
    for ship in range(5):
        (ship_row, ship_column) = (randint(0, 7), randint(0, 7))
        while board[ship_row][ship_column] == "⊗":
            (ship_row, ship_column) = (randint(0, 7), randint(0, 7))
        board[ship_row][ship_column] = "⊗"


def fire_shot():
    """
    Asking player what row and column to fire their shot
    """
    row = input("\nEnter ship row 1-8: ")
    while row not in "12345678":
        print("\nPlease enter a valid row")
        row = input("\nEnter ship row 1-8: \n")
    column = input("\nEnter ship column A-H: ").upper()
    while column not in "ABCDEFGH":
        print("\nPlease enter a valid column")
        column = input("\nEnter ship column A-H: ").upper()
    return (int(row) - 1, letters_to_numbers[column])