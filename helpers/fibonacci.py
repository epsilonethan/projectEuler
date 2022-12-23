import numpy as np
from math import sqrt, pow


def binet_formula(n):
    return round((pow((1. + sqrt(5.)), n) - pow((1. - sqrt(5.)), n)) / (pow(2., n) * sqrt(5.)))


def generate_fibs(n):
    fib_numbers = np.empty(n, dtype=int)
    fib_numbers[0] = 0
    fib_numbers[1] = 1

    for i in range(n):
        if i != 0 and i != 1:
            fib_numbers[i] = fib_numbers[i - 1] + fib_numbers[i - 2]

    return fib_numbers


def all_fibs_up_to(max):
    # find number of fibs up to and including max
    fib = [0, 1, 1]
    count = len(fib)
    new = fib[1] + fib[2]
    while new <= max:
        fib[0] = fib[1]
        fib[1] = fib[2]
        fib[2] = new
        count += 1
        new = fib[1] + fib[2]

    return generate_fibs(count)


def find_even_fibs(fib_array):
    for i in range(len(fib_array)):
        if fib_array[i] % 2 != 0:
            fib_array[i] = 0

    return fib_array
