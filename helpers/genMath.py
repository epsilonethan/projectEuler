import numpy as np


def find_multiples_of(multiple, max_value):
    if not type(multiple) is int:
        raise TypeError("Only integers are allowed")

    if not type(max_value) is int:
        raise TypeError("Only integers are allowed")

    return np.arange(0, max_value, multiple)


def find_evens(array):
    if not type(array) is np.ndarray:
        raise TypeError("Only np.ndarray is allowed")

    even_count = 0
    for i in range(len(array)):
        if array[i] % 2 == 0:
            even_count += 1

    even_array = np.empty(even_count)
    j = 0
    for i in range(len(array)):
        if array[i] % 2 == 0:
            even_array[j] = array[i]
            j += 1

    return even_array


def find_factors(num):
    if not type(num) is int:
        raise TypeError("Only integers are allowed")

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
