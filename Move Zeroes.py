class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for index, num in enumerate(nums):
            if index < len(nums)-1:
                if num != 0:
                    continue
                else:
                    next_pos = index+1
                    try:
                        while nums[next_pos] == 0:
                            next_pos += 1
                        nums[index] = nums[next_pos]
                        nums[next_pos] = 0
                    except IndexError:
                        break
        return nums
