#!/usr/bin/python3
"""
factorial_recursive.py

This script calculates the factorial of a number using recursion.
The number is provided as a command-line argument.
"""

import sys  # Provides access to command-line arguments

def factorial(n):
    """
    Recursively calculates the factorial of a non-negative integer n.

    Args:
        n (int): The number whose factorial is to be calculated

    Returns:
        int: The factorial of n
    """
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)

# Convert the first command-line argument to an integer
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
