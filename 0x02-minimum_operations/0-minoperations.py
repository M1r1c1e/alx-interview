#!/usr/bin/python3
"""`minOperations(n) function`"""


def minOperations(n):
    """ calculates the fewest number of operations (copy, paste)
        needed to result in exactly n H characters
    """
    length_H = 1
    len_copied_H = 0
    total_operations = 0

    while length_H < n:
        if n % length_H == 0:
            total_operations += 2
            len_copied_H = length_H
            length_H *= 2
        else:
            total_operations += 1
            length_H += len_copied_H
    return total_operations
