#!/usr/bin/python3
""" 0 prime game """


def sieve_of_eratosthenes(max_n):
    """ Generates a boolen array where is_prime[i] is true
    only if i is a prime number

    Args:
        max_n (int): The number to generate from

    Returns:
        _type_: is_prime
    """
    is_prime = [True] * (max_n + 1)
    is_prime[0], is_prime[1] = False, False
    p = 2
    while p * p <= max_n:
        if is_prime[p]:
            for multiple in range(p * p, max_n + 1, p):
                is_prime[multiple] = False
        p += 1
    return is_prime


def prime_counts_up_to(n, is_prime):
    """ Generates a array of prime_count
    where prime_count[i] gives the prime from 1 to i

    Args:
        n (_type_): The number to generate the prime from
        is_prime (bool): Checks if the each number is a prime

    Returns:
        _type_: The count of the prime numbers
    """
    prime_count = [0] * (n + 1)
    count = 0
    for i in range(n + 1):
        if is_prime[i]:
            count += 1
        prime_count[i] = count
    return prime_count


def isWinner(x, nums):
    """ determines the winner by countings each winner

    Args:
        x (_type_): number of rounds and
        nums (_type_): An array of n numbers

    Returns:
        _type_: Either maria or ben
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)
    prime_counts = prime_counts_up_to(max_n, is_prime)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
