class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        values_range = range(nums[0], nums[0])
        max_value = nums[0]

        for num in nums[1:]:

            if (len(values_range) == 0 and values_range.stop < 0) or \
                    (len(values_range) != 0 and values_range.stop + num < 0):
                values_range = range(num, num)

            else:
                values_range = range(values_range.start, values_range.stop+num)

            if values_range.stop > max_value:
                max_value = values_range.stop

        return max_value
