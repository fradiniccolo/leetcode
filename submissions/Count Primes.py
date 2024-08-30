class Solution:
    def countPrimes(self, n: int) -> int:

        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False

        # sieve of eratosthenes
        current = 2
        while (current * current < n):
            if is_prime[current]:
                # prime's multiples are not primes
                for mult_index in range(current * current, n, current):
                    is_prime[mult_index] = False
            current += 1

        prime_count = sum(is_prime)
        return prime_count
