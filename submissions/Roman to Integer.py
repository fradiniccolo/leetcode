class Solution:
    def romanToInt(self, s: str) -> int:

        str_to_int = {
            'III': 3,
            'II': 2,
            'I': 1,
            'XXX': 30,
            'XX': 20,
            'X': 10,
            'CCC': 300,
            'CC': 200,
            'C': 100,
            'MMM': 3000,
            'MM': 2000,
            'M': 1000,
            'V': 5,
            'L': 50,
            'D': 500,
        }

        chars = [s[0]]
        for char in s[1:]:
            if char == chars[-1][-1]:
                chars[-1] += char
            else:
                chars.append(char)

        nums = [str_to_int.get(item) for item in chars]

        nums_sum = 0
        for curr_num, next_num in zip(nums, nums[1:]+[0]):
            if curr_num > next_num:
                nums_sum += curr_num
            else:
                nums_sum -= curr_num

        return nums_sum
