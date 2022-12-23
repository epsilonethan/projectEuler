import numpy as np


def find_multiples_of(multiple, max_value):
    return np.arange(0, max_value, multiple)


def find_factors(num):
    # Find all factors of num

    factors = []

    i = 2
    while True:
        if num % i == 0:
            factors.append(i)
            num /= i

        else:
            i += 1

        if i > num:
            break

    return list(factors)
