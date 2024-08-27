from copy import copy
from random import shuffle


class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums

    def reset(self) -> List[int]:
        return self.array

    def shuffle(self) -> List[int]:
        array_copy = copy(self.array)
        shuffle(array_copy)
        return array_copy


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
