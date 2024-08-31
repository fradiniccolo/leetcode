class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_len = len(nums)
        sum_of_first_n_nums = nums_len*(nums_len+1)//2
        return sum_of_first_n_nums - sum(nums)
