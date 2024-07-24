class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = {}
        for num in nums:
            if num in counter.keys():
                counter.pop(num)
            else:
                counter[num] = 1
        return list(counter.keys())[0]
