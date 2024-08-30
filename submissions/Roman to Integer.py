class Solution:
    def romanToInt(self, s: str) -> int:

        str_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        s = [str_to_int[i] for i in s]

        total = 0
        for curr_int, next_int in zip(s, s[1:]+[0]):
            if curr_int >= next_int or next_int == 0:
                total += curr_int
            else:
                total -= curr_int

        return total


tests = [
    ("III", 3),
    ("VIII", 8),
    ("IV", 4),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
]

for test, expected in tests:
    solution = Solution()
    print(f"{test}: {expected}/{solution.romanToInt(test)}")
