#!/usr/bin/python3
"""
Define isWinner function
"""


def isWinner(x, nums):
    """Determines the winner of a prime game by playing `x` rounds.
    """
    if x < 1 or not nums:
        return None
    maria_win, ben_win = 0, 0
    n = max(nums)
    prime_number = [True for _ in range(1, n + 1)]
    prime_number[0] = False
    for i, is_prime in enumerate(prime_number, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            prime_number[j - 1] = False

    for _, n in zip(range(x), nums):
        prime_count = len(list(filter(lambda x: x, prime_number[0: n])))
        ben_win += prime_count % 2 == 0
        maria_win += prime_count % 2 == 1
    if maria_win == ben_win:
        return None
    return 'Maria' if maria_win > ben_win else 'Ben'
