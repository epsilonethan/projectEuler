"""
Problem: Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

import numpy as np
from helpers import genMath as gm

if __name__ == '__main__':
    mult3 = gm.find_multiples_of(3, 1000)
    mult5 = gm.find_multiples_of(5, 1000)

    mult3_5 = np.concatenate((mult3, mult5))
    print(np.sum(np.unique(mult3_5)))