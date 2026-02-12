#!/usr/bin/env python3

from checkmate import checkmate

def main():

    print("---- Test 1 : Rook check ----")
    board1 = """\
R...
....
K...
...."""
    checkmate(board1)

    print("---- Test 2 : Bishop check ----")
    board2 = """\
B...
.K..
....
...."""
    checkmate(board2)

    print("---- Test 3 : Queen check ----")
    board3 = """\
Q...
.K..
....
...."""
    checkmate(board3)

    print("---- Test 4 : Pawn check ----")
    board4 = """\
....
.P..
..K.
...."""
    checkmate(board4)

    print("---- Test 5 : Not in check ----")
    board5 = """\
R...
.K..
..P.
...."""
    checkmate(board5)


if __name__ == "__main__":
    main()