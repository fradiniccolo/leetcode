class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        unique_i = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[unique_i] = nums[i]
                unique_i += 1

        return unique_i
