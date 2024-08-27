from time import time
from functools import cache


class Solution:
    def countPrimes(self, n: int) -> int:

        @cache
        def is_prime(n):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            i = 2
            while i*i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True

        count = 0
        for i in range(1,n,2):
            if is_prime(i):
                count += 2
        return count

test = Solution()
time_start = time()
print(f"{test.countPrimes(5000000):,}")
time_end = time()
print(f"runtime: {time_end-time_start:.6f}")