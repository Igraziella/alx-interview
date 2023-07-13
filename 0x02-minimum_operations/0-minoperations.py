#!/usr/bin/python3
"""method that calculates minimum operations"""
import math


def minOperations(n):
    """calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    if n == 1:
        return 0
    
    # Find the divisors of n
    divisors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            divisors.append(i)
            n //= i
    if n > 1:
        divisors.append(n)
    
    if not divisors:
        return 0
    
    # Calculate the minimum number of operations
    min_ops = sum(divisors)
    return min_ops
