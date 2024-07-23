#!/usr/bin/python3
""" Minimum operations """

def minOperations(n):
    """ Minimum operations

    Args:
        n (_type_): the number of characters to be printed

    Returns:
        _type_: the minimum number of operations needed to 
        result in exactly n H characters in the file
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations