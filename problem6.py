"""
Problem: Sum square difference
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

import numpy as np

if __name__ == "__main__":
    # my original solution
    numbers = np.arange(1, 101, 1)
    print(np.power(np.sum(numbers), 2) - np.sum(np.power(numbers, 2)))

    # projecteuler solution
    # sum of integers from 1 to n = n(n+1)/2
    # sum of squared integers from 1 to n = (n/6)(2n+1)(n+1)
    # reduces to => n(n+1)(n^2 - (1/3)n + 2/3)/2

    n = 100
    print((n * (n + 1) * ((n ^ 2) - ((1 / 3) * n) - (2 / 3))) / 2)
