"""
Problem: Even Fibonacci numbers


Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.

"""

import numpy as np
from helpers import fibonacci as fb
from helpers import genMath as gm

if __name__ == '__main__':
    fibs = fb.all_fibs_up_to(4000000)
    fibs = gm.find_evens(fibs)
    print(np.sum(fibs))
