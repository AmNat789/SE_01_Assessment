import copy

initial_board = [[1, 2, 0],
                 [4, 5, 3],
                 [7, 8, 6]]

board = copy.deepcopy(initial_board)


def display_board():
    for row in board:
        print(row)


def find_gap():
    for row_index in range(len(board)):
        for col_index in range(len(board[0])):
            if board[row_index][col_index] == 0:
                return row_index, col_index


def check_move(row, col, gap_row, gap_col):
    if row < 0 or row > len(board) or col < 0 or col > len(board[0]):
        return False

    row_adjacency = (row == gap_row - 1) or (row == gap_row + 1)
    col_adjacency = (col == gap_col - 1) or (col == gap_col + 1)

    return row_adjacency ^ col_adjacency


def do_move(row, col, gap_row, gap_col):
    global board
    temp_board = copy.deepcopy(board)

    temp_board[row][col] = board[gap_row][gap_col]
    temp_board[gap_row][gap_col] = board[row][col]

    board = temp_board


def check_win():
    current_num = 0

    for i in board:
        for value in i:
            if value == 0:
                continue
            if value == current_num + 1:
                current_num = value
            else:
                return True
    return False


if __name__ == '__main__':
    attempts = 3
    moves_record = []
    moves = 0

    while attempts > 0:

        while check_win():
            display_board()

            gap_row, gap_col = find_gap()

            pos = input("Type the position of the tile you want to move.")
            pos_row, pos_col = pos.split(",")
            row = int(pos_row)
            col = int(pos_col)

            if check_move(row, col, gap_row, gap_col):
                do_move(row, col, gap_row, gap_col)
            else:
                print("This move won't work... please choose another tile to move")

            moves += 1

        attempts -= 1
        print("You won in ", moves, " moves. You have ", attempts, "attempts remaining")
        moves_record.append(moves)
        moves = 0
        board = copy.deepcopy(initial_board)

    moves_record.sort()
    print("Congrats! Your high-score was ", moves_record[0], " moves")
