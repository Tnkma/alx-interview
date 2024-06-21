#!/usr/bin/python3
""" Change making algorithm """


def makeChange(coins, total):
    """
    Determine the number of coins to meet a given total
    """
    if total <= 0:
        return 0

    coin_index = 0
    count = 0
    sorted_coins = sorted(coins, reverse=True)
    coin_len = len(coins)

    while total > 0:
        if coin_index >= coin_len:
            return -1

        if total - sorted_coins[coin_index] >= 0:
            total -= sorted_coins[coin_index]
            count += 1

        else:
            coin_index += 1

    return count
