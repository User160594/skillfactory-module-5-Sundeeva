
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def print_board():
    print("  1   2   3")
    print("1 " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print(" ---|---|---")
    print("2 " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print(" ---|---|---")
    print("3 " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])


def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def check_rows(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True
    return False


def check_columns(board):
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] and board[0][column] != " ":
            return True
    return False


def check_diagonals(board):
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != " ":
        return True
    return False


def is_winner(board):
    return check_rows(board) or check_columns(board) or check_diagonals(board)


def get_move(player):
    row = int(input("Игрок {} введите номер строки (1-3): ".format(player)))
    column = int(input("Игрок {} введите номер столбца (1-3): ".format(player)))
    return row, column


def play_game():
    player = "X"

    while not is_board_full(board):
        print_board()

        row, column = get_move(player)

        if board[row - 1][column - 1] == " ":
            board[row - 1][column - 1] = player

            if is_winner(board):
                print_board()
                print("Поздравляем! Игрок " + player + " победил!")
                return

            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("Это место уже занято. Пожалуйста, выберите другой номер.")


    print_board()
    print("Ничья!")


play_game()
