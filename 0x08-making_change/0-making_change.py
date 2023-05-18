#!/usr/bin/python3
"""
Define makeChange func
"""


def makeChange(coins, total):
    """
    Return: fewest numbers of coins, 0, or  -1
    args:
        coins: List of coins
        total: integer
    """
    n = len(coins)
    if (total <= 0):
        return 0
    reminder = total
    count, index = 0, 0
    sorted_coins = sorted(coins, reverse=True)
    while reminder > 0:
        if index >= n:
            return -1
        if reminder - sorted_coins[index] >= 0:
            reminder -= sorted_coins[index]
            count += 1
        else:
            index += 1
    return count
