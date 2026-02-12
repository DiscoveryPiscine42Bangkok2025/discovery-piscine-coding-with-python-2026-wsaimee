#!/usr/bin/env python3

# ANSI color codes
RESET = "\033[0m"
BLACK_BG = "\033[40m"
WHITE_BG = "\033[47m"
BLACK_TEXT = "\033[30m"
WHITE_TEXT = "\033[37m"

def print_chess_board(board):
    rows = board.strip().split("\n")
    size = len(rows)

    # หัวคอลัมน์ A-H
    columns = [chr(ord('A') + i) for i in range(size)]
    print("    " + "  ".join(columns))

    for i in range(size):
        print("  +" + "---+" * size)

        row_output = str(size - i) + " |"
        for j in range(size):
            piece = rows[i][j]

            # สลับสีแบบหมากรุก
            if (i + j) % 2 == 0:
                bg = WHITE_BG
                text = BLACK_TEXT
            else:
                bg = BLACK_BG
                text = WHITE_TEXT

            cell = f"{bg}{text} {piece} {RESET}"
            row_output += cell + "|"

        print(row_output)

    print("  +" + "---+" * size)
    print("    " + "  ".join(columns))


# ตัวอย่างกระดาน
if __name__ == "__main__":
    board = """\
RNBQKBNR
PPPPPPPP
........
........
........
........
PPPPPPPP
RNBQKBNR
"""
    print_chess_board(board)