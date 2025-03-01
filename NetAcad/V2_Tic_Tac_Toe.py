from random import randrange


def display_board(board):
    # Display the board in a centered format
    print("+-------+-------+-------+".center(25))
    for row in board:
        print("|       |       |       |".center(25))
        row_display = "|".join(f"   {cell}   " for cell in row)
        print(f"|{row_display}|".center(25))
        print("|       |       |       |".center(25))
        print("+-------+-------+-------+".center(25))


def enter_move(board):
    # Prompt user for a valid move and update the board
    free_fields = make_list_of_free_fields(board)
    while True:
        try:
            move = int(input("Enter your move: "))
            if 1 <= move <= 9:
                row, col = [(i, row.index(move)) for i, row in enumerate(board) if move in row][0]
                if (row, col) in free_fields:
                    board[row][col] = "0"
                    break
                else:
                    print("Field already occupied. Try again.")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid move.")


def make_list_of_free_fields(board):
    # Create a list of available fields
    return [(i, j) for i in range(3) for j in range(3) if isinstance(board[i][j], int)]


def victory_for(board, sign):
    # Check for a winning condition
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    return any(all(board[row][col] == sign for row, col in condition) for condition in win_conditions)


def draw_move(board):
    # Randomly select a free field for the computer's move
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = free_fields[randrange(len(free_fields))]
        board[row][col] = "X"


def tic_tac_toe_game():
    # Initialize and play the game
    board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
    display_board(board)

    while True:
        enter_move(board)
        display_board(board)
        if victory_for(board, "0"):
            print("You Won!!")
            break
        if not make_list_of_free_fields(board):
            print("It's a Tie!")
            break

        draw_move(board)
        display_board(board)
        if victory_for(board, "X"):
            print("Computer Wins!")
            break
        if not make_list_of_free_fields(board):
            print("It's a Tie!")
            break


tic_tac_toe_game()
