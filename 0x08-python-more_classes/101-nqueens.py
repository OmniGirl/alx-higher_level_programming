#!/usr/bin/python3
"""
Solution to the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard
"""
from sys import argv
if __name__ == "__main__":
    ab = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    h = int(argv[1])
    if h < 4:
        print("N must be at least 4")
        exit(1)
    # initialize the answer list
    for z in range(h):
        ab.append([z, None])

    def already_exists(q):
        """check that a queen does not already exist in that f value"""
        for f in range(h):
            if q == ab[f][1]:
                return True
        return False

    def reject(f, q):
        """determines whether or not to reject the solution"""
        if (already_exists(q)):
            return False
        z = 0
        while(z < f):
            if abs(ab[z][1] - q) == abs(z - f):
                return False
            z += 1
        return True

    def clear_a(f):
        """clears the answers from the point of failure on"""
        for z in range(f, h):
            ab[z][1] = None

    def nqueens(f):
        """recursive backtracking function to find the solution"""
        for q in range(h):
            clear_a(f)
            if reject(f, q):
                ab[f][1] = q
                if (f == h - 1):  # accepts the solution
                    print(ab)
                else:
                    nqueens(f + 1)  # moves on to next f value to continue
    # start the recursive process at f = 0
    nqueens(0)
