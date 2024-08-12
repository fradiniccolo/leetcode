fibonacci_cache = {}


class Solution:
    def climbStairs(self, n: int) -> int:

        def fibonacci(n):
            global fibonacci_cache
            if n is None:
                return None
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            if n > 2:
                if n in fibonacci_cache.keys():
                    return fibonacci_cache[n]
                else:
                    nth_fibonacci = fibonacci(n-1) + fibonacci(n-2)
                    fibonacci_cache[n] = nth_fibonacci
                    return nth_fibonacci

        return fibonacci(n+1)
