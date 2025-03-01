from random import randrange

def display_board(board):
    print("+-------+-------+-------+".center(25))
    for row in board:
        print("|       |       |       |".center(25))
        row_display = "|".join(f"   {cell}   " for cell in row)
        print(f"|{row_display}|".center(25))
        print("|       |       |       |".center(25))
        print("+-------+-------+-------+".center(25))

def enter_move(board):
    free_fields = make_list_of_free_fields(board)
    move = None
    while move is None:
        try:
            user_input = int(input("Enter your move: "))
            if user_input < 1 or user_input > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
            else:
                move = [(i, row.index(user_input)) for i, row in enumerate(board) if user_input in row]
                if not move or move[0] not in free_fields:
                    print("Field already occupied or invalid. Try again.")
                    move = None
                else:
                    move = move[0]
                    board[move[0]][move[1]] = "0"
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 9.")

def make_list_of_free_fields(board):
    return [(i, j) for i in range(3) for j in range(3) if isinstance(board[i][j], int)]

def victory_for(board, sign):
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
    for condition in win_conditions:
        if all(board[row][col] == sign for row, col in condition):
            return True
    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        move = free_fields[randrange(len(free_fields))]
        board[move[0]][move[1]] = "X"

def tic_tac_toe_game():
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
