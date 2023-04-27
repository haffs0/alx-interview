#!/usr/bin/env python3
"""N queens puzzle
"""
import sys


N = int(sys.argv[1])

board = [[0]*N for _ in range(N)]


def get_input():
    """Retrieves size of board"""
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueen N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def n_queen(n, i=0, a=[], b=[], c=[]):
    """ find possible positions """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from n_queen(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solution(n):
    """ solution for n queens puzzle """
    k = []
    i = 0
    for solution in n_queen(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


if __name__ == '__main__':
    n = get_input()
    solution(n)