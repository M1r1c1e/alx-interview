#!/usr/bin/python3
"""This module contains a function called `makeChange`"""


def makeChange(coins, total):
    """ Determines the fewest number of coins needed to meet the
        total of a given amount
    """
    coins.sort(reverse=True)
    coin_num = 0
    remainder = 0

    if total <= 0:
        return 0
    for coin in coins:
        if total == 0:
            break
        elif coin <= total:
            remainder = total % coin
            coin_num += total // coin
            total = remainder

    return coin_num if total == 0 else -1
