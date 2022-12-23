import numpy as np
from math import sqrt, pow


def binet_formula(n):
    if not type(n) is int:
        raise TypeError("Only integers are allowed")

    return round((pow((1. + sqrt(5.)), n) - pow((1. - sqrt(5.)), n)) / (pow(2., n) * sqrt(5.)))


def generate_fibs(n):
    if not type(n) is int:
        raise TypeError("Only integers are allowed")

    fib_numbers = np.empty(n, dtype=int)
    fib_numbers[0] = 0
    fib_numbers[1] = 1

    for i in range(n):
        if i != 0 and i != 1:
            fib_numbers[i] = fib_numbers[i - 1] + fib_numbers[i - 2]

    return fib_numbers


def all_fibs_up_to(max_fib):
    # find number of fibs up to and including max
    if not type(max_fib) is int:
        raise TypeError("Only integers are allowed")

    fib = [0, 1, 1]
    count = len(fib)
    new = fib[1] + fib[2]
    while new <= max_fib:
        fib[0] = fib[1]
        fib[1] = fib[2]
        fib[2] = new
        count += 1
        new = fib[1] + fib[2]

    return generate_fibs(count)
