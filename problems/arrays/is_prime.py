import math
def sieve_of_eratosthenes(n):
    """Find all prime numbers up to n using the Sieve of Eratosthenes"""
    primes = [True] * (n + 1)  # True means prime, False means composite
    primes[0] = False
    primes[1] = False  # 0 and 1 are not prime
    
    for start in range(2, int(math.sqrt(n)) + 1):
        if primes[start]:
            for multiple in range(start * start, n + 1, start):
                primes[multiple] = False
    
    prime_numbers = []
    for num in range(n + 1):
        if primes[num]:
            prime_numbers.append(num)
    
    return len(prime_numbers)

print(sieve_of_eratosthenes(10000000))