"""
Problem: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import numpy as np
from helpers import genMath as gm

if __name__ == "__main__":

    all_factors = []

    for i in range(2, 20 + 1, 1):
        factors = gm.find_factors(i)

        for factor in factors:
            all_factors.pop

    print(19*17*13*11*7*5*3*3*2*2*2*2)
