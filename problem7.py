"""
Problem: 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

if __name__ == "__main__":
    primes = [2, 3, 5, 7, 11, 13]
    num = 13
    while len(primes) != 10001:
        num += 2
        prime_flag = True
        for prime in primes[1:]:
            if num % prime == 0:
                prime_flag = False
                break

        if prime_flag:
            primes.append(num)

    print(primes[-1])