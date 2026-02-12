#!/usr/bin/env python3

def checkmate(board):
        rows = board.strip().split("\n")
        size = len(rows)

        # ตรวจว่ากระดานเป็นสี่เหลี่ยมจัตุรัส
        for row in rows:
            if len(row) != size:
                print("Fail")
                return

        grid = [list(row) for row in rows]

        # หา King
        king_row = -1
        king_col = -1

        for i in range(size):
            for j in range(size):
                if grid[i][j] == "K":
                    king_row = i
                    king_col = j

        if king_row == -1:
            print("Fail")
            return

        # ---------------- Pawn ----------------
        for i in range(size):
            for j in range(size):
                if grid[i][j] == "P":
                    if (i + 1 == king_row and j - 1 == king_col) or \
                       (i + 1 == king_row and j + 1 == king_col):
                        print("Success")
                        return

        # ---------------- Rook ----------------
        directions_straight = [(-1,0),(1,0),(0,-1),(0,1)]

        for i in range(size):
            for j in range(size):
                if grid[i][j] == "R":
                    for dr, dc in directions_straight:
                        r, c = i, j
                        while True:
                            r += dr
                            c += dc
                            if r < 0 or r >= size or c < 0 or c >= size:
                                break
                            if grid[r][c] != ".":
                                if grid[r][c] == "K":
                                    print("Success")
                                    return
                                break

        # ---------------- Bishop ----------------
        directions_diag = [(-1,-1),(-1,1),(1,-1),(1,1)]

        for i in range(size):
            for j in range(size):
                if grid[i][j] == "B":
                    for dr, dc in directions_diag:
                        r, c = i, j
                        while True:
                            r += dr
                            c += dc
                            if r < 0 or r >= size or c < 0 or c >= size:
                                break
                            if grid[r][c] != ".":
                                if grid[r][c] == "K":
                                    print("Success")
                                    return
                                break

        # ---------------- Queen ----------------
        directions_all = [
            (-1,0),(1,0),(0,-1),(0,1),
            (-1,-1),(-1,1),(1,-1),(1,1)
        ]

        for i in range(size):
            for j in range(size):
                if grid[i][j] == "Q":
                    for dr, dc in directions_all:
                        r, c = i, j
                        while True:
                            r += dr
                            c += dc
                            if r < 0 or r >= size or c < 0 or c >= size:
                                break
                            if grid[r][c] != ".":
                                if grid[r][c] == "K":
                                    print("Success")
                                    return
                                break

        print("Fail")