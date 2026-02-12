import sys


def read_board(filename):
    try:
        with open(filename, "r") as file:
            lines = file.read().splitlines()
    except:
        return None

    if len(lines) != 8:
        return None

    board = []

    for line in lines:
        if len(line) != 8:
            return None

        row = []
        for char in line:
            if char not in [".", "K", "R", "B", "Q", "P"]:
                return None
            row.append(char)

        board.append(row)

    return board


def find_king(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == "K":
                return (i, j)
    return None


def is_path_clear(board, start_row, start_col, end_row, end_col):
    if start_row == end_row:
        step = 1 if end_col > start_col else -1
        for col in range(start_col + step, end_col, step):
            if board[start_row][col] != ".":
                return False

    elif start_col == end_col:
        step = 1 if end_row > start_row else -1
        for row in range(start_row + step, end_row, step):
            if board[row][start_col] != ".":
                return False

    return True


def is_rook_attacking(board, rook_pos, king_pos):
    r_row, r_col = rook_pos
    k_row, k_col = king_pos

    if r_row == k_row or r_col == k_col:
        return is_path_clear(board, r_row, r_col, k_row, k_col)

    return False


def is_bishop_attacking(board, bishop_pos, king_pos):
    b_row, b_col = bishop_pos
    k_row, k_col = king_pos

    if abs(b_row - k_row) == abs(b_col - k_col):
        step_row = 1 if k_row > b_row else -1
        step_col = 1 if k_col > b_col else -1

        row = b_row + step_row
        col = b_col + step_col

        while row != k_row and col != k_col:
            if board[row][col] != ".":
                return False
            row += step_row
            col += step_col

        return True

    return False


def is_queen_attacking(board, queen_pos, king_pos):
    return (
        is_rook_attacking(board, queen_pos, king_pos)
        or is_bishop_attacking(board, queen_pos, king_pos)
    )


def is_pawn_attacking(pawn_pos, king_pos):
    p_row, p_col = pawn_pos
    k_row, k_col = king_pos

    if (p_row + 1 == k_row) and (abs(p_col - k_col) == 1):
        return True

    return False


def is_king_in_check(board):
    king_pos = find_king(board)
    if not king_pos:
        return False

    for i in range(8):
        for j in range(8):
            piece = board[i][j]

            if piece == "R":
                if is_rook_attacking(board, (i, j), king_pos):
                    return True

            elif piece == "B":
                if is_bishop_attacking(board, (i, j), king_pos):
                    return True

            elif piece == "Q":
                if is_queen_attacking(board, (i, j), king_pos):
                    return True

            elif piece == "P":
                if is_pawn_attacking((i, j), king_pos):
                    return True

    return False


def main():
    if len(sys.argv) != 2:
        print("Error")
        return

    board = read_board(sys.argv[1])

    if not board:
        print("Error")
        return

    if is_king_in_check(board):
        print("Success")
    else:
        print("Success")


if __name__ == "__main__":
    main()