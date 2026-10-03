#!/usr/bin/env python3
"""
Sieve of Eratosthenes to find all primes up to 1000
"""

def sieve_of_eratosthenes(limit):
    """
    Find all prime numbers up to limit using the Sieve of Eratosthenes.
    
    Args:
        limit: The upper bound (inclusive) to search for primes
    
    Returns:
        A list of all prime numbers up to limit
    """
    # Create a boolean array "is_prime[0..limit]" and initialize
    # all entries as true. A value in is_prime[i] will finally
    # be true if i is Prime, else false.
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    
    # Start with the smallest prime number, 2
    p = 2
    while p * p <= limit:
        # If is_prime[p] is not changed, then it is a prime
        if is_prime[p]:
            # Mark all multiples of p as not prime
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    
    # Collect all prime numbers
    primes = [i for i in range(2, limit + 1) if is_prime[i]]
    return primes


def main():
    limit = 1000
    
    # Find all primes up to 1000
    primes = sieve_of_eratosthenes(limit)
    
    # Print the count of primes
    print(f"Count of primes up to {limit}: {len(primes)}")
    
    # Print the first 10 primes
    print(f"First 10 primes: {primes[:10]}")
    
    # Print the last 10 primes
    print(f"Last 10 primes: {primes[-10:]}")


if __name__ == "__main__":
    main()