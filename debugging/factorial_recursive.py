#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be calculated.
             The function assumes n is a valid non-negative integer, as negative
             integers do not have a factorial.

    Returns:
    int: The factorial of the input integer n.
         If n is 0, the function returns 1, since 0! is defined as 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
