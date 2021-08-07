from math import sqrt, ceil


def prime_sieve(n):
    if n < 2:
        return []

    primes = [True] * n

    primes[0], primes[1] = False, False

    for i in range(2, ceil(sqrt(n))):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False

    return [num for num, val in enumerate(primes) if val]
