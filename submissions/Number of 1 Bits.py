class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        for digit in f"{n:b}":
            total += int(digit)
        return total
