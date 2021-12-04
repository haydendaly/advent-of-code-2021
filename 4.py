def format_input(raw):
    rows = raw.split("\n\n")
    input_stream = [int(num) for num in rows[0].split(",")]
    boards = []
    for raw_board in rows[1:]:
        # beefy list comprehension
        board = [[int(num) for num in line.split(" ") if num != ""] for line in raw_board.split("\n")]
        boards.append(board)
    return input_stream, boards


def get_board_sum(board):
    board_sum = 0
    for row in board:
        for col in row:
            if col < 100:
                board_sum += col
    return board_sum


def has_bingo(board, num):
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if board[i][j] == num:
                board[i][j] += 100 # mark columns by incrementing by 100
    
    # check rows for bingo
    for row in board:
        row_sum = 0
        for col in row:
            if col >= 100:
                row_sum += 1
        if row_sum == 5:
            return True

    # check columns for bingo
    l = len(board)
    for j in range(l):
        col_sum = 0
        for i in range(l):
            if board[i][j] >= 100:
                col_sum += 1
        if col_sum == 5:
            return True

    # check diagonals - apparently not necessary
    # diag_sum_1 = 0
    # diag_sum_2 = 0
    # for i in range(l):
    #     if board[i][i] >= 100:
    #         diag_sum_1 += 1
    #     if board[l - i - 1][i] >= 100:
    #         diag_sum_2 += 1
    # return diag_sum_1 == 5 or diag_sum_2 == 5

def part1(input_stream, boards):
    winner_sum = 0
    for num in input_stream:
        for board in boards:
            if has_bingo(board, num):
                board_sum = get_board_sum(board)
                return board_sum * num
    return 0


def part2(input_stream, boards):
    for num in input_stream:
        new_boards = []
        for board in boards:
            if not has_bingo(board, num):
                new_boards.append(board)
        if len(new_boards) == 0:
            board_sum = get_board_sum(boards[0])
            return board_sum * num
        boards = new_boards
    return 0


if __name__ == "__main__":
    raw = open("data/4.txt", "r").read()
    input_stream, boards = format_input(raw)
    result = part1(input_stream, boards)
    print(result)

    raw = open("data/4.txt", "r").read()
    input_stream, boards = format_input(raw)
    result = part2(input_stream, boards)
    print(result)
